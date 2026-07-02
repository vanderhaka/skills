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

The six pipeline stages are packaged inside this skill as references under `references/stages/` — there is one dispatcher (`SKILL.md`) and one reference file per stage, loaded and executed in-session rather than invoked as separate skills:

- `references/stages/intake-grill.md` - clear decisions and write `decisions.md`.
- `references/stages/graph-plan.md` - create or update `plan.md` and `progress.md`.
- `references/stages/plan-grill.md` - stress-test the graph before worker launch.
- `references/worker-contract.md` - the single worker contract; assemble worker briefs from it.
- `references/stages/integrator.md` - verify worker reports, update `progress.md`, and advance waves.
- `references/stages/proof.md` - run final requirement-level proof and write `verification.md`.

`issue-fix-strategy` remains a separate skill for chat-only triage of messy issue sources before graph planning.

## What You Get

- `plan.md`.
- `progress.md`.
- `decisions.md`.
- `verification.md`.
- Worker reports under `agent-runs/`.
- Final summary with confidence and residual risk.

## Not For

Use standalone `issue-fix-strategy` when you have issues but only want a decision-ready strategy. Use `safe-feature-slice` in `plan-only` mode when you explicitly want planning only.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-orchestrator
```

Restart Codex after installing new skills.
