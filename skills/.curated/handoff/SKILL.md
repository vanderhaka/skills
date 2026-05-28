---
name: handoff
description: Create or refresh a concise project handoff for next-session continuity, or resume from an existing handoff. Use when the user asks for a handoff, wrap-up, session summary, continuation note, next-session context, or says to continue from HANDOFF.md.
---

# Session Handoff

## Goal

Create or refresh the repo's continuity handoff with the minimum context needed to resume safely next session. If the user asks to continue from an existing handoff, read it first and use it as the starting context.

## Modes

- `write`: user asks for a handoff, wrap-up, end-of-session note, or next-session context.
- `resume`: user says `HANDOFF.md continue`, asks to continue from a handoff, or points at an existing handoff file.

## Resume Mode

1. Read the referenced handoff file, defaulting to `HANDOFF.md` in the repo root.
2. Check current repo state with `git status --short --branch` and `git log --oneline -1`.
3. Compare the handoff's last-known state to current state.
4. Tell the user the next action you infer, any stale assumptions, and any blocker before proceeding.

Do not treat the handoff as more authoritative than current files, git state, tests, or user instructions.

## Write Mode

### 1. Gather Context

Use bounded reads:

- `git status --short --branch`
- `git diff --stat HEAD`
- `git log --oneline -1`
- relevant `README`, `AGENTS.md`, `CONTRIBUTING.md`, `plans/`, `STATUS-*.md`, `PLAN-*.md`, or existing `HANDOFF.md`
- package/build/test config names needed to detect the safest check

Run the closest low-risk verification check when practical:

- prefer a repo script such as `test`, `typecheck`, `lint`, `build`, or documented check
- for TypeScript, use the repo's package script before falling back to `npx tsc --noEmit`
- if no safe check is clear, say that no build check was run and why

Do not run checks that mutate shared databases, deploy, call provider write APIs, or rewrite generated files unless the user explicitly asked for that.

### 2. Choose The Handoff File

Default to `HANDOFF.md` in the project root, but preserve existing repo conventions:

- If a repo already uses a different handoff/status file, update that file instead.
- If `HANDOFF.md` exists and is tracked, keep it tracked.
- If `HANDOFF.md` exists and is ignored, keep it ignored.
- If no convention exists, create `HANDOFF.md`.

Do not automatically add `HANDOFF.md` to `.gitignore`. Recommend ignoring it only when the handoff is purely local, machine-specific, or not meant for the team.

### 3. Write The Handoff

Keep it concise, usually under 40 lines:

```markdown
# Handoff - {DATE}

## Last task
{One sentence: what was being worked on}

## Current state
{branch, last commit, clean/dirty status, verification result}

## Key files
- {5-10 files most relevant to resuming work, with 1-line descriptions}

## Decisions and constraints
- {important user decisions, safety boundaries, or assumptions}

## Next steps
- {ordered next actions}

## Risks or blockers
- {anything not verified, failing, or waiting on user/external state}
```

### 4. Report Back

Tell the user:

- which handoff file was written or updated
- whether the repo is clean or dirty
- which verification check ran, passed, failed, or was skipped
- whether the handoff is tracked, ignored, or local-only

If uncommitted changes remain, do not assume the user wants a commit. Say what changed and ask before committing unless the user already requested a commit/cap flow.

## Skill Maintenance

Do not write to files inside the installed skill during normal use. If a run reveals a durable improvement to this workflow, mention it in the final answer as a suggested skill update instead of mutating the skill package.
