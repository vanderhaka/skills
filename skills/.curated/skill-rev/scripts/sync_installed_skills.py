#!/usr/bin/env python3
"""Mirror curated repo skills into installed skill directories.

For each installed dir (default: ~/.codex/skills and ~/.claude/skills):
- copy every curated repo skill folder over the installed copy
- remove installed folders whose skill was retired from the repo,
  tracked via a manifest so unrelated local skills are never touched
- write .vanderhaka-skills-manifest.json recording what is managed

Safe by construction: only folders that exist in the repo now, or that a
previous sync recorded in the manifest, are ever created, updated, or
removed. Anything else in the installed dir is ignored.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MANIFEST_NAME = ".vanderhaka-skills-manifest.json"
DEFAULT_INSTALLED_DIRS = ["~/.codex/skills", "~/.claude/skills"]


def repo_head(repo_root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def dirs_differ(a: Path, b: Path) -> bool:
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return True
    return any(dirs_differ(a / d, b / d) for d in cmp.common_dirs)


def load_manifest(installed_dir: Path) -> dict:
    path = installed_dir / MANIFEST_NAME
    if path.is_file():
        try:
            data = json.loads(path.read_text())
            if isinstance(data, dict) and isinstance(data.get("skills"), list):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return {"skills": []}


def sync_dir(curated: Path, installed_dir: Path, update_only: bool, dry_run: bool) -> dict:
    repo_skills = sorted(p.name for p in curated.iterdir() if p.is_dir())
    manifest = load_manifest(installed_dir)
    # First run: infer managed set from folders that match repo skill names.
    managed = set(manifest["skills"]) | {
        name for name in repo_skills if (installed_dir / name).is_dir()
    }

    actions = {"installed": [], "updated": [], "unchanged": [], "removed": [], "skipped": []}

    for name in repo_skills:
        src = curated / name
        dest = installed_dir / name
        if not dest.is_dir():
            if update_only and name not in managed:
                actions["skipped"].append(name)
                continue
            actions["installed"].append(name)
        elif dirs_differ(src, dest):
            actions["updated"].append(name)
        else:
            actions["unchanged"].append(name)
            managed.add(name)
            continue
        managed.add(name)
        if not dry_run:
            if dest.is_dir():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)

    # Retired: previously managed, no longer in the repo.
    for name in sorted(managed - set(repo_skills)):
        dest = installed_dir / name
        if dest.is_dir():
            actions["removed"].append(name)
            if not dry_run:
                shutil.rmtree(dest)
        managed.discard(name)

    if not dry_run:
        manifest_out = {
            "repo": "vanderhaka/skills",
            "commit": repo_head(curated.parent.parent),
            "synced_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "skills": sorted(managed),
        }
        (installed_dir / MANIFEST_NAME).write_text(json.dumps(manifest_out, indent=2) + "\n")
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="skills repo checkout root")
    parser.add_argument("--installed-dir", action="append", default=None,
                        help="installed skills dir (repeatable); defaults to "
                             "~/.codex/skills and ~/.claude/skills")
    parser.add_argument("--update-only", action="store_true",
                        help="only update already-installed/managed skills; do not install new ones")
    parser.add_argument("--dry-run", action="store_true", help="report actions without applying")
    args = parser.parse_args()

    curated = Path(args.repo_root).expanduser().resolve() / "skills" / ".curated"
    if not curated.is_dir():
        print(f"FAIL curated skills dir not found: {curated}")
        return 1

    targets = args.installed_dir or DEFAULT_INSTALLED_DIRS
    overall_fail = False
    for raw in targets:
        installed_dir = Path(raw).expanduser()
        if not installed_dir.is_dir():
            print(f"SKIP {installed_dir} (directory does not exist on this device)")
            continue
        actions = sync_dir(curated, installed_dir, args.update_only, args.dry_run)
        prefix = "DRY-RUN" if args.dry_run else "OK"
        print(f"{prefix} {installed_dir}: "
              f"installed={len(actions['installed'])} updated={len(actions['updated'])} "
              f"unchanged={len(actions['unchanged'])} removed={len(actions['removed'])} "
              f"skipped={len(actions['skipped'])}")
        for key in ("installed", "updated", "removed", "skipped"):
            for name in actions[key]:
                print(f"  {key}: {name}")
    return 1 if overall_fail else 0


if __name__ == "__main__":
    sys.exit(main())
