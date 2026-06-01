# Feature Integrator

## What This Skill Does

`feature-integrator` checks worker reports, accepts or rejects their evidence, updates canonical progress, and decides what dependency wave can run next.

## Use It When

- One or more `feature-slice-worker` reports are ready.
- Workers touched related contracts, routes, schemas, or UI flows.
- Progress needs to be updated without blindly trusting worker status.
- The next parallel wave needs to be computed safely.

## How It Works

The skill reads `plan.md`, `progress.md`, and relevant `agent-runs/*.md`. It verifies write boundaries, dependencies, RED/GREEN/REFACTOR evidence, browser or boundary gates, migration gates, and skipped-check reasons. It then updates `progress.md` only when evidence is good enough.

## What You Get

- Accepted, blocked, or needs-attention status per worker report.
- Integration check results.
- Updated canonical progress.
- Newly discovered graph nodes if needed.
- Next safe dependency wave recommendation.

## Not For

Use `feature-proof` when all graph nodes appear complete and the whole feature needs final requirement-level verification.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-integrator
```

Restart Codex after installing new skills.
