---
name: skill-rev
description: Lightweight review for vanderhaka/skills changes before push, plus pull/update audits for all curated skills. Modes — no args runs the full pre-push review, "push" runs pre-push checks only, "sync" runs the pull/update audit comparing installed skills against the repo. Use when skills are about to be pushed, when checking whether repo skills are updated, or when comparing installed local skills against the remote catalog.
---

# Skill Rev

## Role

Run a lightweight pre-push review for this skills repository. This skill checks
whether skill changes are shaped, documented, installable, and public-safe before
handoff to `cap` or a normal git push.

This is intentionally smaller than `cap`. It does not stage, commit, push, repair
failures, publish, or install skills. It gives a focused review and a dated audit
snapshot so the next action is obvious.

## Modes

Arguments after the skill name select the flow. Treat the first argument as the
mode keyword; ignore case.

- (no args) — full review: Pre-Push Review plus the installed-skills comparison
  in the audit snapshot.
- `push` — Pre-Push Review only. Skip the installed-skills comparison (run the
  snapshot without `--installed-dir`).
- `sync` — Pull / Update Audit only. Skip the pre-push checks.

Any other argument text is extra context (for example a skill name to focus on),
not a mode.

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

6. Create a dated audit snapshot for all curated skills (in full mode, include
   both installed dirs; in `push` mode, omit the `--installed-dir` flags):

```bash
python3 skills/.curated/skill-rev/scripts/skill_audit_snapshot.py --installed-dir ~/.codex/skills --installed-dir ~/.claude/skills
```

The snapshot writes to `.skill-audits/<timestamp>-skill-audit.md`, which is
ignored by git. Do not commit audit snapshots unless the user explicitly asks.

## Pull / Update Audit

Use this for `sync` mode, when the user asks whether repo skills are updated, or
wants a pull check before syncing local installed skills.

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

3. Create a dated audit for every curated skill and compare against both
   installed skill dirs:

```bash
python3 skills/.curated/skill-rev/scripts/skill_audit_snapshot.py --fetch --installed-dir ~/.codex/skills --installed-dir ~/.claude/skills
```

The audit records repo HEAD, remote HEAD, ahead/behind counts, per-skill package
timestamps, README/agent metadata presence, and installed-vs-repo drift for each
installed dir.

## Output

Report in this compact shape:

```text
Skill rev: PASS | WARN | FAIL | BLOCKED
Mode: full | push | sync
Scope: <changed skills or all skills>
Audit: <path to dated audit>
Checks: validate=<pass/fail>, public-safety=<pass/fail>, diff-check=<pass/fail>, scripts=<pass/fail/skipped>
Findings: <highest-signal issues only>
Next: <push with cap | fix issues | pull --ff-only | reinstall/sync local skills>
```

Do not bury the result in a long narrative. If checks fail, state the failing
command and exact file path. If the repo or installed skills are stale, say what
is stale and which command updates it.
