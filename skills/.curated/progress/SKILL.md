---
name: progress
description: Strict production progress protocol for existing internal products, SaaS apps, dashboards, and tools. Use when the user wants Codex to discover the best real improvement, get one approval, create a fresh worktree, execute through a dependency graph with safe parallel worker waves, QA the result, and deliver a repeatable demo-ready package.
---

# Progress

## Purpose

Run a fixed production-progress protocol. The project changes; the workflow, artifacts, headings, tables, and stop points stay the same.

Use this skill to turn an existing product into one approved, production-ready improvement. Do not use it for greenfield apps, pure code review, one-line fixes, read-only launch audits, or chat-only planning.

## Core Rule

Do not treat the human as QA. The human approves the target once. After approval, continue until the approved work is production-ready, demo-ready, or blocked by a precise external condition.

## Fixed Artifact Set

Every run must create or update this exact folder:

```text
plans/<slug>/
  discovery-report.md
  approval-proposal.md
  decisions.md
  shared-contract.md
  plan.md
  progress.md
  verification.md
  demo.md
  final-delivery.md
  handoff.md
  agent-runs/
```

Use the bundled templates in `assets/templates/`:

- `discovery-report.md`
- `approval-proposal.md`
- `shared-contract.md`
- `execution-graph.md`
- `demo-package.md`
- `final-delivery.md`

If a section cannot be completed, write `BLOCKED`, `SKIPPED`, or `NOT APPLICABLE` in the matching field with the reason. Do not remove the section.

## Stage 0: Worktree Setup

1. Inspect current `git status --short`, current branch, and `git worktree list --porcelain`.
2. Discovery can run in the current checkout.
3. After approval, create or reuse exactly one sibling worktree for the approved target:

```text
../<repo-name>-<slug>
```

4. Use branch:

```text
codex/<slug>
```

5. Do not implement in the original checkout unless the user explicitly says to use the current worktree.
6. Record the worktree path, branch, base commit, and slug in `decisions.md`.
7. Preserve unrelated dirty files. Do not reset, clean, checkout away, or overwrite unrelated changes.

## Stage 1: Project Context Report

Inspect the repo, docs, routes, data models, API calls, database usage, tests, scripts, environment names, deployment hints, and existing conventions.

Write `plans/<slug>/discovery-report.md` from `assets/templates/discovery-report.md`.

Do not edit product code in this stage.

## Stage 2: Opportunity Discovery Matrix

Identify real progress opportunities. Each opportunity must:

- improve the product
- fit existing direction
- be testable
- be demoable
- be realistic to finish properly
- avoid cosmetic-only work
- avoid speculative architecture

Score every opportunity using the fixed scoring table in `assets/templates/approval-proposal.md`.

## Stage 3: Approval Proposal

Write `plans/<slug>/approval-proposal.md` from `assets/templates/approval-proposal.md`.

Present the numbered proposal to the user with the exact fields:

1. Problem
2. Impact
3. Proposed fix
4. Affected areas
5. Expected final behavior
6. Demo proof
7. Risks
8. Dependencies
9. Score

Recommend one option.

Stop for approval. Accept replies like `Do 1`, `Do 1 and 3`, `Everything except 4`, or `Change 2 to include X`.

## Stage 4: Shared Contract

After approval and before parallel execution, write `plans/<slug>/shared-contract.md` from `assets/templates/shared-contract.md`.

The shared contract must define:

1. Approved goal
2. User-facing behavior
3. Data shape
4. API expectations
5. Auth and permission assumptions
6. Files parallel workers must not touch
7. Test expectations
8. Demo path
9. Rollback risk
10. External dependency status

Do not launch workers until this file is complete.

## Stage 5: Execution Graph

Use `feature-orchestrator` for the canonical dependency graph and progress model. Read its `SKILL.md` and required references before creating or changing `plan.md` or `progress.md`.

Write `plans/<slug>/plan.md` using the fixed graph shape from `assets/templates/execution-graph.md` plus the `feature-orchestrator` graph contract.

Every node must include:

- node id
- title
- type
- risk tier
- status
- depends on
- parallel group
- blocking class
- actor or trigger
- observable behavior
- protected invariant
- write boundaries
- forbidden files
- acceptance criteria
- regression guards
- required tests
- repo gate
- browser gate
- boundary gate
- exit evidence

Classify each node as exactly one of:

- `Blocking`
- `Parallel-safe`
- `Dependent`
- `QA`
- `Demo/documentation`

## Stage 6: Worker Wave Plan

Create worker waves from the graph.

Parallelize only when all conditions are true:

- dependencies are satisfied
- write boundaries are disjoint
- data/API contracts are stable
- assumptions are recorded in `shared-contract.md`
- shared mutable state is absent
- integration can verify all reports

Do not parallelize:

- git operations
- dependency or lockfile edits
- migrations against the same database
- deploys or promotions
- mutable shared test databases
- broad refactors across shared contracts
- workers touching the same files

Default maximum: 4 workers per wave.

Each worker brief must follow the worker-contract format from `feature-orchestrator`. Workers write reports under `agent-runs/` and never edit `progress.md`.

## Stage 7: Implementation

Execute each node through:

```text
RED -> GREEN -> REFACTOR -> Repo Gate -> Browser Gate -> Boundary Gate -> Worker Report
```

Use `feature-slice-worker` for substantial implementation nodes. Use existing project patterns. Keep changes scoped to the approved goal.

Do not invent new architecture unless the current architecture blocks the approved work. Record that reason in `decisions.md` before making the architectural change.

## Stage 8: Integration

Use `feature-integrator` discipline to merge worker outputs into one coherent feature.

Verify:

- data contract
- API contract
- UI rendering
- loading, empty, error, and success states
- validation behavior
- auth and permission behavior
- tests
- generated files
- no temporary logs
- no dead code
- no unused mocks
- no debugging shortcuts

Update `progress.md` only after current evidence supports the status change.

## Stage 9: Production Done Gate

The work is not done until the available checks prove it.

Run, when scripts or surfaces exist:

1. targeted tests for changed areas
2. full tests
3. typecheck
4. lint
5. build
6. browser flow for user-visible work
7. fresh screenshot for UI layout claims
8. API or database boundary checks
9. migration dry run or non-destructive migration proof
10. deployment or provider smoke checks when deployment is approved

If a check cannot run, record:

- command or check attempted
- result
- reason it cannot run
- next-best evidence
- residual risk

## Stage 10: Self-QA Loop

Review the work as if it will be shown to management tomorrow.

Check:

- edge cases
- bad data
- missing data
- auth and permissions
- mobile layout
- console errors
- broken routes
- database state
- migrations
- seed data
- rollback risk
- external provider state
- stale environment variables

Fix issues found. Repeat until clean or blocked. Record each loop in `verification.md`.

## Stage 11: Demo Package

Always write `plans/<slug>/demo.md` from `assets/templates/demo-package.md`.

If no demo is possible, write `Demo status: BLOCKED` and the exact blocker.

The demo package must include:

- under-60-second demo script
- route or command
- required data
- expected result
- proof artifacts
- limitations

## Stage 12: Final Delivery

Use `feature-proof` before final delivery. Write `plans/<slug>/verification.md` and `plans/<slug>/final-delivery.md`.

The final response must use this exact numbered shape:

1. Approved goal
2. What changed
3. Why it matters
4. Files changed
5. Tests run
6. QA checks completed
7. How to demo it in under 60 seconds
8. Proof it works
9. Known limitations
10. Recommended next step

If the work is verified and uncommitted, recommend `cap`. Do not push, deploy, or promote unless the user approved that action.

## Language Rules

Use deterministic protocol language. Avoid advisory wording in artifacts. Write `WILL`, `MUST`, `DONE`, `BLOCKED`, `SKIPPED`, or `NOT APPLICABLE`.

Do not use `maybe`, `consider`, `if useful`, `optionally`, or `could` in protocol artifacts except when quoting the user.

## Handoff

At the end of any incomplete run, write `handoff.md` with:

- absolute worktree path
- branch
- current graph status
- next unblocked node
- blocker if any
- commands already run
- copyable next-session prompt

Use the `handoff` skill shape for the copyable prompt.
