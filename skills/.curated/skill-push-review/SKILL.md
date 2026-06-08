---
name: skill-push-review
description: Lightweight review for vanderhaka/skills changes before push, plus pull/update audits for all curated skills. Use when skills are about to be pushed, when checking whether repo skills are updated, or when comparing installed local skills against the remote catalog.
---

# Skill Push Review

## Role

Run a lightweight pre-push review for this skills repository. This skill checks
whether skill changes are shaped, documented, installable, and public-safe before
handoff to `cap` or a normal git push.

This is intentionally smaller than `cap`. It does not stage, commit, push, repair
failures, publish, or install skills. It gives a focused review and a dated audit
snapshot so the next action is obvious.

## Pre-Push Review

Use this before pushing changes to `vanderhaka/skills`.

1. Inspect scope:

```bash
git status --short --branch
git diff --stat
git diff --cached --stat
```

2. Identify changed skill packages under `skills/.curated/<skill-name>/`.
3. For every changed skill, check:
   - `SKILL.md` exists and frontmatter `name` matches the folder.
   - `description` clearly names the capability and trigger situations.
   - `README.md` exists with install instructions.
   - `agents/openai.yaml` exists and matches the skill purpose.
   - scripts are deterministic, executable when needed, and syntax-checked.
   - no `LESSONS.md`, private local paths, private project context, or secrets.
   - `SKILL.md` stays lean; move long detail into `references/` when practical.
   - root `README.md` lists newly added curated skills.

4. Run the repo checks:

```bash
python3 scripts/validate_skills.py
python3 skills/.curated/skill-repo-maintainer/scripts/audit_skill_repo.py .
git diff --check
```

5. Syntax-check changed Python scripts:

```bash
python3 -m py_compile <changed-script.py>
```

6. Create a dated audit snapshot for all curated skills:

```bash
python3 skills/.curated/skill-push-review/scripts/skill_audit_snapshot.py
```

The snapshot writes to `.skill-audits/<timestamp>-skill-audit.md`, which is
ignored by git. Do not commit audit snapshots unless the user explicitly asks.

## Pull / Update Audit

Use this when the user asks whether repo skills are updated or wants a pull
check before syncing local installed skills.

1. Fetch remote state:

```bash
git fetch origin main
git status --short --branch
git rev-list --left-right --count HEAD...origin/main
```

2. If the repo is behind and the working tree is clean, fast-forward only:

```bash
git pull --ff-only origin main
```

3. Create a dated audit for every curated skill and compare against installed
local skills:

```bash
python3 skills/.curated/skill-push-review/scripts/skill_audit_snapshot.py --fetch --installed-dir ~/.codex/skills
```

The audit records repo HEAD, remote HEAD, ahead/behind counts, per-skill package
timestamps, README/agent metadata presence, and installed-vs-repo drift.

## Output

Report in this compact shape:

```text
Skill push review: PASS | WARN | FAIL | BLOCKED
Scope: <changed skills or all skills>
Audit: <path to dated audit>
Checks: validate=<pass/fail>, public-safety=<pass/fail>, diff-check=<pass/fail>, scripts=<pass/fail/skipped>
Findings: <highest-signal issues only>
Next: <push with cap | fix issues | pull --ff-only | reinstall/sync local skills>
```

Do not bury the result in a long narrative. If checks fail, state the failing
command and exact file path. If the repo or installed skills are stale, say what
is stale and which command updates it.
