# Safe Feature Slice

## What This Skill Does

`safe-feature-slice` plans, builds, continues, or reviews feature slices while protecting important behavior. It is the safety-first workflow for work that can hurt users if done casually. It also has a `plan-only` mode: when the user explicitly asks to plan, slice, sequence, review an existing plan, or stop before implementation, the skill decomposes the work into a dependency-ordered thin-slice plan with progress tracking and never implements.

## Use It When

- Work touches money, permissions, data ownership, state transitions, destructive actions, migrations, webhooks, integrations, or customer-visible records.
- You need a thin-slice plan and then implementation.
- You want independent workers only when write boundaries are safe.
- Browser or runtime proof matters as much as tests.
- You explicitly want planning-only output, or want to review an existing plan without implementing it (`plan-only` mode).

## How It Works

The skill creates or updates a thin-slice plan for broad work, identifies invariants and unsafe outcomes, asks only material questions, executes eligible slices, uses Red-Green-Refactor discipline, and requires verification evidence before marking progress. In `plan-only` mode it stops after writing the plan artifact instead of executing slices — see `references/plan-only-mode.md` for the full artifact format, decomposition rules, and existing-plan review flow.

## What You Get

- Working brief.
- Thin-slice plan.
- Dependency order.
- Implementation evidence (build mode) or a plan artifact and next-slice recommendation (`plan-only` mode).
- Tests and browser or boundary proof when needed.
- Behavior preservation confidence.

## Not For

Use `feature-orchestrator` for whole-feature dependency-graph execution with canonical progress and worker waves.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/safe-feature-slice
```

Restart Codex after installing new skills.
