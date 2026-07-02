# Handoff

## What This Skill Does

`handoff` creates or refreshes a concise project handoff so the next session can resume without rediscovering everything.

## Use It When

- The user asks for a handoff, wrap-up, session summary, or continuation note.
- Work is paused and needs clear next steps.
- A future agent needs repo status, recent changes, checks, blockers, and risks.
- You want a copyable prompt that starts the next session correctly.

## How It Works

The skill gathers current git status, uncommitted changes, the last commit, active STATUS/PLAN files, and a quick build check, then writes a fixed-structure `HANDOFF.md` (one per project, always overwritten) plus a copyable next-session prompt.

## What You Get

- Concise summary of what changed.
- Current git and verification state.
- Known blockers and residual risks.
- Next actions.
- `HANDOFF.md` written to the project root (overwritten each run).
- A copyable next-session prompt that points a fresh session at the project and `HANDOFF.md`.
- A short copyable handoff summary that names `HANDOFF.md` and the key docs/plans/status files to read first.

## Not For

Use `cap` when the work should be verified, committed, and pushed. Use `feature-orchestrator`'s proof stage (`references/stages/proof.md`) when a feature needs final requirement-level proof before handoff.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/handoff
```

Restart Codex after installing new skills.
