#!/usr/bin/env python3
"""Validate Codex skill folders in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$|^[a-z0-9]$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not text.startswith("---\n"):
        return {}, ["missing opening YAML frontmatter fence"]

    try:
        _, raw_frontmatter, _ = text.split("---\n", 2)
    except ValueError:
        return {}, ["missing closing YAML frontmatter fence"]

    data: dict[str, str] = {}
    for line_number, line in enumerate(raw_frontmatter.splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"frontmatter line {line_number} is not key: value")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        raw_value = value.strip()
        if ":" in raw_value and not (
            (raw_value.startswith('"') and raw_value.endswith('"'))
            or (raw_value.startswith("'") and raw_value.endswith("'"))
        ):
            errors.append(f"frontmatter line {line_number} contains an unquoted colon")
        data[key] = raw_value.strip('"').strip("'")

    extra_keys = sorted(set(data) - {"name", "description"})
    if extra_keys:
        errors.append(f"frontmatter has unsupported keys: {', '.join(extra_keys)}")

    return data, errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    data, frontmatter_errors = parse_frontmatter(path)
    errors.extend(frontmatter_errors)

    folder_name = path.parent.name
    skill_name = data.get("name", "")
    description = data.get("description", "")
    text = path.read_text(encoding="utf-8")

    if not skill_name:
        errors.append("frontmatter is missing name")
    elif skill_name != folder_name:
        errors.append(f"name {skill_name!r} does not match folder {folder_name!r}")
    elif not SKILL_NAME_RE.fullmatch(skill_name):
        errors.append("name must use lowercase letters, digits, and hyphens")

    if not description:
        errors.append("frontmatter is missing description")
    elif len(description) < 60:
        errors.append("description is too short to trigger reliably")

    if "[TODO" in text or "TODO:" in text:
        errors.append("contains TODO placeholder text")

    return errors


def main() -> int:
    skill_files = sorted((ROOT / "skills").glob("**/SKILL.md"))
    if not skill_files:
        print("No SKILL.md files found under skills/", file=sys.stderr)
        return 1

    failed = False
    for skill_file in skill_files:
        errors = validate_skill(skill_file)
        rel = skill_file.relative_to(ROOT)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
