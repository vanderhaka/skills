# Feature Orchestrator

## What This Skill Does

`feature-orchestrator` is the front door for delivering a whole feature or broad multi-slice fix. It owns one canonical dependency graph, one progress file, worker waves, integration, and final proof.

## Use It When

- The user wants a complete feature shipped, not just a plan.
- Work spans multiple slices or agents.
- Parallel execution would help, but write boundaries need control.
- TDD/Red-Green-Refactor discipline and proof gates matter.
- The request says to keep going until the feature is complete.

## How It Works

The skill creates or reuses `plans/<feature-slug>/`. It records decisions, applies routine technical, UX, UI, and product-taste defaults before asking the user anything, builds a dependency graph, launches every safe unblocked worker wave, verifies worker reports, updates progress, and runs final proof before marking the feature complete.

The stage skills are:

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

Use `issue-fix-strategy` first when you have issues but have not decided what should be fixed or in what order. Use `thin-slice-plan` when you explicitly want planning only.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-orchestrator
```

Restart Codex after installing new skills.
