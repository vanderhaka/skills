# Feature Plan Grill

## What This Skill Does

`feature-plan-grill` stress-tests a feature graph before workers start coding. It is deliberately skeptical about missing decisions, unsafe parallelism, weak tests, and unverifiable completion.

## Use It When

- A `feature-orchestrator` plan exists but has not launched workers yet.
- The graph may be too broad, too vague, or unsafe.
- Parallel groups need a collision check.
- You want the plan challenged before implementation cost is spent.

## How It Works

The skill reads `plan.md`, `progress.md`, and `decisions.md`, then inspects the relevant codebase surface. It reviews completeness, node size, dependencies, write boundaries, risk tiers, RGR plans, gates, and final proof expectations.

It writes a `grill-review.md` and updates the plan only after safe assumptions or decisions are resolved.

## What You Get

- Verdict: `PASS`, `PASS WITH RISKS`, `BLOCKED`, or `FAIL`.
- Concrete plan corrections.
- Missing decision list.
- Unsafe parallelism or weak gate warnings.
- Better graph readiness before worker launch.

## Not For

Use `feature-intake-grill` when you already know the blocker is a user/product decision. Use `code-review` for reviewing code that already changed.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-plan-grill
```

Restart Codex after installing new skills.
