---
name: skill-rev
description: Review and distribution flow for vanderhaka/skills. Modes — no args runs the full pre-push review, "push" runs pre-push checks then hands to cap and syncs installed skills after the push lands, "pull" pulls (or clones) the repo on this device then syncs installed skills, "sync" mirrors the curated skills into ~/.codex/skills and ~/.claude/skills. Use when skills are about to be pushed, when pulling skill updates onto a device, when checking whether repo skills are updated, or when installed local skills should match the repo catalog.
---

# Skill Rev

## Role

Run the review and distribution flow for this skills repository. This skill
checks whether skill changes are shaped, documented, installable, and
public-safe before handoff to `cap`, and keeps the installed skill copies on
this device (`~/.codex/skills` and `~/.claude/skills`) in step with the repo.

This is intentionally smaller than `cap` for git mutation: it never stages,
commits, or pushes — `cap` does that. It does own installed-skill distribution:
Device Sync copies curated skills into the installed dirs and removes retired
ones.

## Modes

Arguments after the skill name select the flow. Treat the first argument as the
mode keyword; ignore case.

- (no args) — full review: Pre-Push Review plus the installed-skills comparison
  in the audit snapshot. Report only; no sync applied.
- `push` — Pre-Push Review, then hand the commit/push to `cap`. After the push
  lands on `main`, run Device Sync so this device's installed skills match what
  was just published.
- `pull` — Pull / Update flow: bring the repo checkout up to date on this
  device (clone it first if absent), then run Device Sync.
- `sync` — Device Sync only: mirror the curated skills into the installed dirs
  from the current checkout. Add `dry-run` to report actions without applying.

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

## Pull / Update Flow

Use this for `pull` mode, or when the user asks to bring this device's skills up
to date.

1. Locate the checkout. Default path: `~/Desktop/Development/vanderhaka-skills`.
   If it does not exist on this device, clone it there:

```bash
git clone git@github.com:vanderhaka/skills.git ~/Desktop/Development/vanderhaka-skills \
  || git clone https://github.com/vanderhaka/skills.git ~/Desktop/Development/vanderhaka-skills
```

2. Fetch remote state:

```bash
git fetch origin main
git status --short --branch
git rev-list --left-right --count HEAD...origin/main
```

3. If the repo is behind and the working tree is clean, fast-forward only:

```bash
git pull --ff-only origin main
```

If the working tree is dirty or the branch has diverged, do not pull. Report
the drift and the command the user should run instead, and skip Device Sync —
never distribute a checkout that is not cleanly on `main`.

4. Run Device Sync (below).

For an audit without applying anything, run the snapshot instead:

```bash
python3 skills/.curated/skill-rev/scripts/skill_audit_snapshot.py --fetch --installed-dir ~/.codex/skills --installed-dir ~/.claude/skills
```

## Device Sync

Mirror the curated skills into this device's installed skill dirs. Runs at the
end of `push` (after the push lands) and `pull`, or standalone as `sync`.

```bash
python3 skills/.curated/skill-rev/scripts/sync_installed_skills.py --repo-root .
```

What the script does per installed dir (`~/.codex/skills`, `~/.claude/skills`):

- Installs or updates every curated repo skill (full mirror by default; pass
  `--update-only` to touch only skills already installed there).
- Removes installed folders whose skill was retired from the repo, tracked via
  `.vanderhaka-skills-manifest.json` in each installed dir — unrelated local
  skills that never came from this repo are never touched.
- Skips an installed dir entirely when it does not exist on this device.
- `--dry-run` reports every install/update/remove without applying.

Report the per-dir counts and every installed/removed skill name. Remind the
user that new or removed skills take effect in new sessions.

## Output

Report in this compact shape:

```text
Skill rev: PASS | WARN | FAIL | BLOCKED
Mode: full | push | pull | sync
Scope: <changed skills or all skills>
Audit: <path to dated audit, or n/a>
Checks: validate=<pass/fail>, public-safety=<pass/fail>, diff-check=<pass/fail>, scripts=<pass/fail/skipped>
Sync: <per-dir installed/updated/removed counts, or not run>
Findings: <highest-signal issues only>
Next: <push with cap | fix issues | pull --ff-only | restart sessions to pick up synced skills>
```

Do not bury the result in a long narrative. If checks fail, state the failing
command and exact file path. If the repo or installed skills are stale, say what
is stale and which command updates it.
