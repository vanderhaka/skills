---
name: progress
description: Strict production progress protocol for existing internal products, SaaS apps, dashboards, and tools. Use when the user wants Codex to discover the best real improvement, coordinate concurrent worktrees, get one approval, execute through a dependency graph with safe parallel worker waves, QA the result, and deliver a repeatable demo-ready package.
---

# Progress

## Purpose

Run a fixed production-progress protocol. The project changes; the workflow, artifacts, headings, tables, and stop points stay the same.

Use this skill to turn an existing product into one approved, production-ready improvement while avoiding overlap with other active progress runs. Do not use it for greenfield apps, pure code review, one-line fixes, read-only launch audits, or chat-only planning.

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

Every run must also create or update this repo-level coordination artifact:

```text
plans/progress-registry.md
```

The registry is local coordination state by default. Do not stage, commit, push, or include `plans/progress-registry.md` or `plans/.progress-registry.lock/` in a PR unless the user explicitly approves making the registry a shared project artifact. If the registry file is untracked, add these local-only patterns to `.git/info/exclude`:

```text
plans/progress-registry.md
plans/.progress-registry.lock/
```

Use the bundled templates in `assets/templates/`:

- `progress-registry.md`
- `discovery-report.md`
- `approval-proposal.md`
- `shared-contract.md`
- `execution-graph.md`
- `demo-package.md`
- `final-delivery.md`

If a section cannot be completed, write `BLOCKED`, `SKIPPED`, or `NOT APPLICABLE` in the matching field with the reason. Do not remove the section.

## Stage -1: Active Work Registry

Before opportunity scoring, approval, worktree creation, or product-code edits, build an active-work inventory.

1. Resolve the repo root with `git rev-parse --show-toplevel`.
2. Inspect current `git status --short`, current branch, and `git worktree list --porcelain`.
3. Treat the first `worktree` entry from `git worktree list --porcelain` as the registry owner checkout unless the user explicitly names a different coordination checkout.
4. Before writing outside the current checkout, state the registry owner checkout path and why it is the owner. Do not silently mutate a different checkout.
5. Read active-work evidence from every worktree path:
   - `plans/progress-registry.md`
   - `plans/*/shared-contract.md`
   - `plans/*/plan.md`
   - `plans/*/progress.md`
   - `plans/*/handoff.md`
6. Create `plans/progress-registry.md` from `assets/templates/progress-registry.md` in the registry owner checkout when it does not exist.
7. If `plans/progress-registry.md` is untracked, keep it local-only and ensure `.git/info/exclude` contains the registry and lock patterns.
8. From the registry owner checkout, acquire a write lock before editing the registry owner copy:

```bash
mkdir -p plans
mkdir plans/.progress-registry.lock
```

9. After acquiring the lock, write `plans/.progress-registry.lock/owner.md` with the run slug, timestamp, current thread context, and intended registry edit.
10. If the lock command fails, do not edit the registry. Read the existing registry and lock evidence, then stop with the exact blocker unless the user explicitly approves clearing the stale lock.
11. Release the lock after the registry write by removing only `plans/.progress-registry.lock` that this run created.
12. Before presenting the approval proposal, add or update a `proposed` registry entry for the recommended work.
13. After approval, update the entry to `approved`, then `active` once the implementation worktree exists.
14. Update the entry after every completed graph node and at final delivery with status `blocked`, `complete`, or `abandoned`.
15. After a successful final delivery, run registry cleanup:
   - mark this run `complete`
   - move stale `complete` and `abandoned` entries into the archive section
   - mark stale `proposed` entries `abandoned` only when no matching approval, worktree, branch, `progress.md`, or `handoff.md` exists in any inspected worktree
   - record every cleanup decision in `Reconciliation Notes`

Registry status meanings:

- `proposed`: soft reservation. Do not duplicate the same proposal without telling the user a proposal already exists.
- `approved`: hard reservation. Do not propose or start overlapping work.
- `active`: hard reservation. Do not propose or start overlapping work.
- `blocked`: hard reservation until the user abandons it or the blocker is removed.
- `complete`: historical record. It does not block new work unless the new work reopens the same code path.
- `abandoned`: historical record. It does not block new work.

Hard conflicts:

- same or substantially equivalent approved goal
- same implementation worktree or branch
- overlapping write boundaries
- overlapping route, API, data model, migration, auth, billing, deployment, or external-provider surface
- shared mutable test database, seed data, generated client, lockfile, or environment contract
- any overlap that cannot be proven disjoint from the available evidence

When a hard conflict exists, do not continue to proposal. Present the conflict and ask whether to resume the existing run, sequence after it, merge scope, or abandon one run.

Boundary confidence:

- `HIGH`: exact files, routes, APIs, data models, tests, and external surfaces are identified from repository evidence.
- `MEDIUM`: primary files and surfaces are known, but secondary effects remain possible.
- `LOW`: the boundary is inferred mostly from names, broad directories, or incomplete discovery.

Do not present an approval proposal with `LOW` boundary confidence unless the proposal explicitly asks the user to choose between narrowing discovery or accepting the overlap risk.

Minimum boundary evidence:

- files or directories likely to change
- user-visible routes, screens, or commands
- APIs, server actions, jobs, or functions
- data models, migrations, seed data, generated clients, and fixtures
- auth, billing, permissions, analytics, email, or external-provider surfaces
- tests and browser flows that prove the boundary

## Existing Run Decisions

When an incoming run conflicts with an existing registry entry, offer only these choices:

1. Resume existing run: switch to the existing worktree, read `handoff.md`, `progress.md`, `plan.md`, `shared-contract.md`, and `verification.md`, then continue the next unblocked graph node.
2. Sequence after existing run: record the incoming idea as `proposed` with `Blocked by: <existing slug>` and do not start implementation.
3. Merge scope: update the existing approval proposal or shared contract, then get user approval before expanding implementation.
4. Narrow blocked reservation: keep the blocked entry, but reduce its forbidden overlap to the exact files, routes, APIs, data, or provider surfaces proven blocked.
5. Abandon existing run: require explicit user approval, mark the old entry `abandoned`, record the reason, then continue registry checks.

## Registry Failure Modes

The registry is coordination evidence, not a perfect distributed scheduler. Counter these failure modes every run:

- Stale entries: reconcile registry status against worktree paths, branches, `progress.md`, and `handoff.md` before scoring opportunities.
- Simultaneous proposals: re-read the registry immediately before writing a proposal and immediately after user approval.
- Underdeclared scope: record minimum boundary evidence and boundary confidence, not only a feature title.
- Duplicate wording: compare goals semantically, not only by slug.
- Overblocking: block only hard conflicts. If the work is likely independent but evidence is incomplete, mark the conflict `BLOCKED` and ask.
- Owner-checkout confusion: always report the current checkout and registry owner checkout before writing the registry.
- Registry noise: keep the registry local-only by default and run cleanup after successful final delivery.

## Stage 0: Worktree Setup

1. Confirm Stage -1 is complete and the registry has no hard conflict for the approved goal.
2. Inspect current `git status --short`, current branch, and `git worktree list --porcelain`.
3. Discovery can run in the current checkout.
4. After approval, create or reuse exactly one sibling worktree for the approved target:

```text
../<repo-name>-<slug>
```

5. Use branch:

```text
codex/<slug>
```

6. Do not implement in the original checkout unless the user explicitly says to use the current worktree.
7. Record the worktree path, branch, base commit, slug, and registry entry id in `decisions.md`.
8. Preserve unrelated dirty files. Do not reset, clean, checkout away, or overwrite unrelated changes.

## Stage 1: Project Context Report

Inspect the repo, docs, routes, data models, API calls, database usage, tests, scripts, environment names, deployment hints, and existing conventions.

Write `plans/<slug>/discovery-report.md` from `assets/templates/discovery-report.md`.

Include the registry snapshot and active-conflict decision in the discovery report.

Include boundary confidence and the evidence used to decide the work is non-overlapping.

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

Exclude opportunities with hard conflicts. Add a registry overlap check to every scored opportunity.

Score only opportunities with `HIGH` or `MEDIUM` boundary confidence unless the proposal asks the user for an explicit risk decision.

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
9. Registry overlap
10. Boundary confidence
11. Score

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
11. Registry reservation and forbidden overlap
12. Boundary confidence and evidence

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

- registry entry status and scope still match the implemented work
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

Before final response, update `plans/progress-registry.md` in the registry owner checkout to `complete` or `blocked` with final evidence. If the result is successful, run registry cleanup. Do not stage or commit the registry unless the user explicitly approved shared registry state.

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
