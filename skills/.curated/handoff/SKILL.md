---
name: handoff
description: End-of-session handoff that gathers repo status, checks build health, and writes/overwrites HANDOFF.md for next-session continuity. Use when the user asks for a handoff, wrap up, session summary, or what they need for next session.
---

# Session Handoff

## Overview

Write a concise HANDOFF.md in the project root with the minimum context needed to resume work next session. Also give the user a copyable prompt and a short copyable handoff summary they can paste into a fresh chat.

## Workflow

1) Gather context
- Run `git diff --stat HEAD` and `git status` to capture uncommitted changes.
- Run `git log --oneline -1` to capture the last commit.
- Find any `STATUS-*.md` or `PLAN-*.md` files.
- Detect project type from config files, then run the most appropriate build check:
  - If TypeScript (e.g., `tsconfig.json` exists), run `npx tsc --noEmit`.
  - Otherwise run the closest equivalent for the detected stack, or note that no build check was run.

2) Write HANDOFF.md
Write a single `HANDOFF.md` file with this exact structure:

```markdown
# Handoff - {DATE}

## Last task
{One sentence: what was being worked on}

## Status
{clean build | N errors to fix | no build check}; {clean tree | uncommitted changes}

## Key files
- {5-10 files most relevant to resuming work, with 1-line descriptions}

## Next steps
- {What to do next, derived from STATUS/PLAN files or conversation}

## Active plans
- {STATUS-*.md or PLAN-*.md files that are in progress, if any}
```

3) Handle uncommitted changes
If there are uncommitted changes, ask:
"You have uncommitted changes. Want me to commit before ending?"

4) Confirm and provide copyable next-session material
- Tell the user where `HANDOFF.md` was written.
- Include a "Next-session prompt" section with a fenced plain-text code block the user can copy directly.
- The prompt must include the absolute project root and instruct the next session to read `HANDOFF.md` first before editing.
- Keep the prompt concise and standalone. Use this shape:

```text
Continue work in {ABSOLUTE_PROJECT_ROOT}. Read HANDOFF.md first, inspect the current git status, preserve unrelated changes, and resume from the listed next steps. Verify the current repo state before making claims or edits.
```
- Include a "Copyable handoff summary" section with a second fenced plain-text block.
- The summary must be short, standalone, and useful even if pasted without surrounding chat context.
- The summary must point to `HANDOFF.md` and the most important docs/plans/status files from "Key files" and "Active plans" so the next chat can open the right source documents quickly.
- Use this shape:

```text
Project: {ABSOLUTE_PROJECT_ROOT}
Read first: HANDOFF.md
Docs/plans: {repo-relative docs/plans/status paths, comma-separated}
State: {one sentence current state}
Next: {one sentence next action}
```

## Rules

- Always write to `HANDOFF.md` in the project root (overwrite if it exists).
- Use `YYYY-MM-DD` for `{DATE}`.
- Keep the file under 30 lines; brevity is the point.
- Only list files relevant to resuming, not every file touched.
- One HANDOFF.md per project; always overwritten.
- Add `HANDOFF.md` to `.gitignore` if not already there.
- Never assume project type; detect from config files.
- Always include both the copyable next-session prompt and the copyable handoff summary in the final response; do not only say `HANDOFF.md continue`.

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
