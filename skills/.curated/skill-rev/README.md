# Skill Rev

## What This Skill Does

`skill-rev` is the review and distribution flow for this skills repo. It checks
pending skill changes before they are pushed, and it keeps the installed skill
copies on each device (`~/.codex/skills` and `~/.claude/skills`) in step with
the repo — push your changes up from one machine, pull them down on another.

## Modes

- `skill-rev` — full pre-push review including installed-skills comparison
  (report only).
- `skill-rev push` — pre-push checks, hand the commit/push to `cap`, then sync
  this device's installed skills after the push lands.
- `skill-rev pull` — pull (or clone) the repo on this device, then sync the
  installed skills.
- `skill-rev sync` — mirror the curated skills into `~/.codex/skills` and
  `~/.claude/skills` from the current checkout; `sync dry-run` reports without
  applying.

## Use It When

- You are about to push skill changes to `vanderhaka/skills`.
- You are on another device and want the latest skills pulled and installed.
- You want a dated audit covering every curated skill.
- You want installed `~/.codex/skills` or `~/.claude/skills` to match the repo.

## How It Works

The review side runs the repo validators, public-safety audit, diff whitespace
check, changed script syntax checks, and a timestamped all-skill audit snapshot.

The distribution side (`scripts/sync_installed_skills.py`) mirrors every curated
skill into the installed dirs, removes skills retired from the repo, and tracks
what it manages in a per-dir manifest so local skills that never came from this
repo are never touched.

Git mutation stays with `cap`: skill-rev never stages, commits, or pushes.

## What You Get

- A compact PASS/WARN/FAIL/BLOCKED result.
- A dated `.skill-audits/<timestamp>-skill-audit.md` report.
- Changed-skill review notes.
- Installed-skill sync results per directory (installed/updated/removed).
- Clear next action.

## Not For

Use `cap` when you want the reviewed work committed and pushed. Use
`skill-repo-maintainer` when creating or restructuring a public skill package.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/skill-rev
```

Restart Codex after installing new skills.
