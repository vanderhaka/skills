#!/usr/bin/env python3
"""Lightweight public-safety audit for a Codex skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


RISK_PATTERNS = {
    "possible_secret": re.compile(
        r"(?i)(api[_-]?key|secret|token|password|private[_-]?key|webhook[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}"
    ),
    "env_file": re.compile(r"(^|/)\.env(\.|$|[A-Za-z0-9_-])"),
    "absolute_user_path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "github_token": re.compile(r"gh[opsu]_[A-Za-z0-9_]{20,}"),
    "stripe_key": re.compile(r"(sk|rk|pk)_(live|test)_[A-Za-z0-9]{16,}"),
}

SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "__pycache__"}
TEXT_SUFFIXES = {
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".txt",
    ".py",
    ".sh",
    ".js",
    ".ts",
    ".tsx",
    ".css",
    ".html",
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name == "SKILL.md"):
            yield path


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd()
    findings: list[tuple[Path, int, str, str]] = []

    for path in iter_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, start=1):
            for name, pattern in RISK_PATTERNS.items():
                if pattern.search(line):
                    findings.append((path, line_number, name, line.strip()[:160]))

    if not findings:
        print("OK public-safety scan found no obvious blockers")
        return 0

    print("Potential public-safety findings:")
    for path, line_number, name, snippet in findings:
        rel = path.relative_to(root)
        print(f"- {rel}:{line_number} [{name}] {snippet}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

