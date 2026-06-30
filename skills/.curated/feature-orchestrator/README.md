# Feature Orchestrator

## What This Skill Does

`feature-orchestrator` is the front door for delivering a whole feature or broad multi-slice fix. It owns one canonical dependency graph, one progress file, worker waves, integration, and final proof.

## Use It When

- The user wants a complete feature shipped, not just a plan.
- The user has issue-fix-strategy triage, review findings, logs, UX complaints, or another messy issue source and wants the accepted fixes delivered.
- Work spans multiple slices or agents.
- Parallel execution would help, but write boundaries need control.
- TDD/Red-Green-Refactor discipline and proof gates matter.
- The request says to keep going until the feature is complete.

## How It Works

The skill creates or reuses `plans/<feature-slug>/`. If the request starts as a messy issue set, it uses `issue-fix-strategy` as chat-only intake first, then records accepted issue IDs, priorities, fix waves, decisions, graph nodes, worker waves, verification, and final proof in the canonical folder.

The stage skills are:

- `issue-fix-strategy`
- `feature-intake-grill`
- `feature-graph-plan`
- `feature-plan-grill`
- `feature-slice-worker`
- `feature-integrator`
- `feature-proof`

## What You Get

- `plan.md`.
- `progress.md`.
- `decisions.md`.
- `verification.md`.
- Worker reports under `agent-runs/`.
- Final summary with confidence and residual risk.

## Not For

Use standalone `issue-fix-strategy` when you have issues but only want a decision-ready strategy. Use `thin-slice-plan` when you explicitly want planning only.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-orchestrator
```

Restart Codex after installing new skills.
