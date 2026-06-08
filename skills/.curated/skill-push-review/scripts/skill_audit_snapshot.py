#!/usr/bin/env python3
"""Write a timestamped audit snapshot for all curated skills."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import subprocess
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", "node_modules", ".skill-audits"}


def run(cmd: list[str], cwd: Path) -> str:
    result = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return (result.stdout or result.stderr).strip()


def display_path(path: Path | None) -> str:
    if path is None:
        return "not checked"
    try:
        return str(path.expanduser().resolve()).replace(str(Path.home()), "~", 1)
    except Exception:
        return str(path).replace(str(Path.home()), "~", 1)


def utc_mtime(path: Path) -> str:
    if not path.exists():
        return "-"
    stamp = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc)
    return stamp.strftime("%Y-%m-%d %H:%M:%SZ")


def files_under(root: Path) -> list[Path]:
    files: list[Path] = []
    for current, dirs, names in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in names:
            if name == ".DS_Store":
                continue
            files.append(Path(current) / name)
    return sorted(files)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def compare_installed(repo_skill: Path, installed_skill: Path) -> str:
    if not installed_skill.exists():
        return "absent"

    missing: list[str] = []
    changed: list[str] = []
    for repo_file in files_under(repo_skill):
        rel = repo_file.relative_to(repo_skill)
        installed_file = installed_skill / rel
        if not installed_file.exists():
            missing.append(str(rel))
        elif digest(repo_file) != digest(installed_file):
            changed.append(str(rel))

    if missing or changed:
        parts = []
        if missing:
            parts.append(f"missing {len(missing)}")
        if changed:
            parts.append(f"changed {len(changed)}")
        return ", ".join(parts)
    return "matches"


def repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "skills" / ".curated").is_dir() and (candidate / "scripts" / "validate_skills.py").exists():
            return candidate
    raise SystemExit("Run from the skills repo or pass a path inside it.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Skills repo path.")
    parser.add_argument("--installed-dir", default=None, help="Installed skills dir, usually ~/.codex/skills.")
    parser.add_argument("--out-dir", default=".skill-audits", help="Where to write the dated audit.")
    parser.add_argument("--fetch", action="store_true", help="Fetch origin/main before writing the audit.")
    args = parser.parse_args()

    root = repo_root(Path(args.repo))
    if args.fetch:
        run(["git", "fetch", "origin", "main"], root)

    installed_dir = Path(args.installed_dir).expanduser() if args.installed_dir else None
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    out_dir = (root / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    report = out_dir / f"{timestamp}-skill-audit.md"

    head = run(["git", "rev-parse", "--short", "HEAD"], root)
    remote = run(["git", "rev-parse", "--short", "origin/main"], root)
    ahead_behind = run(["git", "rev-list", "--left-right", "--count", "HEAD...origin/main"], root)
    status = run(["git", "status", "--short", "--branch"], root)

    rows = []
    for skill_dir in sorted((root / "skills" / ".curated").iterdir()):
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
        installed_skill = installed_dir / name if installed_dir else None
        installed_status = compare_installed(skill_dir, installed_skill) if installed_skill else "not checked"
        rows.append(
            "| {name} | {skill} | {readme} | {agent} | {installed} |".format(
                name=name,
                skill=utc_mtime(skill_dir / "SKILL.md"),
                readme="yes" if (skill_dir / "README.md").exists() else "no",
                agent="yes" if (skill_dir / "agents" / "openai.yaml").exists() else "no",
                installed=installed_status,
            )
        )

    content = [
        f"# Skill Audit {timestamp}",
        "",
        f"- Repo: `{display_path(root)}`",
        f"- HEAD: `{head}`",
        f"- origin/main: `{remote}`",
        f"- ahead/behind: `{ahead_behind}`",
        f"- installed dir: `{display_path(installed_dir)}`",
        "",
        "## Git Status",
        "",
        "```text",
        status,
        "```",
        "",
        "## Skills",
        "",
        "| Skill | SKILL.md updated | README | Agent metadata | Installed comparison |",
        "| --- | --- | --- | --- | --- |",
        *rows,
        "",
    ]
    report.write_text("\n".join(content), encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
