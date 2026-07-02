# Feature Slice Worker

## What This Skill Does

`feature-slice-worker` implements one assigned graph node from a `feature-orchestrator` plan. It follows strict Red-Green-Refactor discipline and reports evidence back to the orchestrator.

## Use It When

- A single graph node has been assigned.
- Dependencies are satisfied.
- Write boundaries are clear.
- The worker needs to implement, test, and report one slice without touching canonical progress.

## How It Works

The worker reads the assigned node, decisions, worker contract, and relevant source files. It writes or locates the failing test first, proves the RED failure, makes the smallest GREEN fix, refactors only after tests pass, then runs required repo, browser, boundary, and migration gates.

## What You Get

- Implementation for one graph node.
- Targeted RED/GREEN/REFACTOR evidence.
- Required gate results.
- `plans/<feature-slug>/agent-runs/<node>-<attempt>.md` report.
- Recommendation: `DONE`, `BLOCKED`, or `NEEDS ATTENTION`.

## Not For

Do not use this as a general implementation shortcut. Use `feature-orchestrator` to own the full feature and `feature-integrator` to accept or reject worker output.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-slice-worker
```

Restart Codex after installing new skills.
