# Code Review

## What This Skill Does

`code-review` reviews a diff, branch, PR, focused file set, or implementation plan for real issues. It prioritizes bugs, regressions, safety risks, missing tests, and merge-readiness problems over style nits.

## Use It When

- You ask for a code review.
- You want to know if a branch is safe to merge.
- You want current local changes audited.
- You want a strict review or a focused review of one area.
- You want review findings before deciding what to fix.

## How It Works

The skill identifies the review target, reads the relevant code and repo rules, inspects behavior and risk surfaces, then reports findings ordered by severity. It routes specialized requests to the better skill when appropriate, such as `launch-critical-sweep` for go-live blockers or `cap` for final ship verification.

## What You Get

- Findings first, ordered by severity.
- File and line references.
- Impact and fix direction.
- Open questions or assumptions.
- Brief summary only after the findings.

## Not For

Use `issue-fix-strategy` when you already have a pile of issues and want plain-English prioritization. Use `cap` when the work is already fixed and needs to be committed.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/code-review
```

Restart Codex after installing new skills.
