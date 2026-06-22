# TDD Plan Grill

## What This Skill Does

`tdd-plan-grill` stress-tests a test-first plan before implementation. It makes sure the plan is clear, scoped, testable, and ready for the current implementation flow.

## Use It When

- A `plans/{slug}-tdd/plan.md` exists.
- You want to harden a test-first plan before coding.
- The test strategy, dependencies, or acceptance criteria may be weak.
- You need focused questions and plan edits before implementation.

## How It Works

The skill reviews the plan for completeness, ambiguity, feasibility, test quality, dependency order, and scope control. It asks focused questions when needed, records decisions in `grill-review.md`, and updates the plan so implementation can proceed.

## What You Get

- TDD plan critique.
- Missing decision list.
- Better acceptance criteria.
- Stronger RED/GREEN/REFACTOR path.
- Updated plan ready for `safe-feature-slice` or `feature-orchestrator`.

## Not For

Use `feature-plan-grill` for `feature-orchestrator` dependency graphs. Use `thin-slice-plan` when no TDD plan exists yet.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/tdd-plan-grill
```

Restart Codex after installing new skills.
