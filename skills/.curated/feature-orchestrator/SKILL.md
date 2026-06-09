---
name: feature-orchestrator
description: End-to-end feature delivery orchestration through one canonical dependency graph and progress file. Use when the user wants a whole feature implemented, a broad multi-slice fix shipped, many parallel agents coordinated, strict TDD/Red-Green-Refactor coding standards enforced, or a tracked "keep going until complete" feature flow with dependency-aware parallel execution, browser/boundary verification, and final proof.
---

# Feature Orchestrator

## Purpose

Deliver a complete feature through a tracked dependency graph. The orchestrator owns the plan, launches as many independent workers as safely possible, enforces strict RED -> GREEN -> REFACTOR and verification gates for every slice, integrates evidence, and keeps going until every required graph node is `DONE`, `SKIPPED`, or `BLOCKED`.

This is the front door for broad feature implementation. Use helper skills as stage tools, but keep one canonical flow folder and one canonical `progress.md`.

## Canonical Folder

Create or reuse:

```text
plans/<feature-slug>/
```

Required artifacts:

- `plan.md` - feature brief, dependency graph, slice definitions, worker plan.
- `progress.md` - canonical live status for the whole feature.
- `decisions.md` - user decisions, safe defaults, assumptions, blockers.
- `verification.md` - final proof, skipped checks, behavior preservation confidence.
- `agent-runs/` - one report per worker attempt.

Only orchestrator-owned stages edit `progress.md`: the main orchestrator and `feature-integrator`. Workers write reports under `agent-runs/`; the orchestrator or integrator verifies the report and then updates progress.

Read `references/graph-and-progress.md` before creating or changing the canonical artifacts.

## Stage Skill Map

Use these stage skills when the stage is substantial enough to benefit from a focused pass:

- `feature-intake-grill` - clear decisions and write `decisions.md`.
- `feature-graph-plan` - create or update `plan.md` and `progress.md`.
- `feature-plan-grill` - stress-test the graph before worker launch.
- `feature-slice-worker` - execute one graph node with RGR and gates.
- `feature-integrator` - verify worker reports, update `progress.md`, and advance waves.
- `feature-proof` - run final requirement-level proof and write `verification.md`.

The main `feature-orchestrator` coordinates these stages and owns the end-to-end status.

## Helper Skill Map

- Use `grill-me` patterns for decision discovery when product, data, permission, money, state, migration, external contract, or UX decisions are unclear.
- Use `thin-slice-plan` discipline for invariants, unsafe outcomes, risk tiers, dependency graph, and progress tracking.
- Use `tdd-plan-deep` issue-writing discipline inside each graph node: one observable `When X, then Y`, concrete acceptance criteria, regression guards, and test sketches.
- `feature-slice-worker` is the canonical per-node worker loop. `tdd-deep` discipline is already embedded in it; treat `tdd-deep` as reference material, not as a competing worker loop.
- Use `tdd-review-deep` only for refactor-only nodes: `LOCK -> REVIEW -> REFACTOR`.
- Use systematic debugging discipline when a failure or unexpected behavior appears: reproduce it, find the root cause, compare against a working pattern, and test one hypothesis at a time.
- Use evidence-before-claims discipline before advancing nodes, reporting success, committing, or marking the feature complete.

Do not create a separate `plans/*-tdd/` or `plans/*-stepwise/` flow for the same feature unless the user explicitly asks for a standalone specialist plan. The orchestrator's `plans/<feature-slug>/progress.md` remains the source of truth.

## Handoffs

Inbound:

- `issue-fix-strategy` triage output and `code-review` findings are valid seed material. Carry their issue list, priorities, regression protections, and proof requirements into the working brief, `decisions.md`, and the graph, so every accepted issue maps to at least one node. Do not re-litigate priority calls the triage already made unless repo evidence contradicts them.
- A direct feature request with no prior triage enters at the intake stage as normal.

Outbound:

- When the feature is `COMPLETE`, offer `cap` to verify, commit, and push.
- When blocked on product decisions, run `feature-intake-grill` rather than guessing.
- When the user wants independent scrutiny of the delivered work, offer `code-review`.

When ending a response with a handoff, recommend exactly one next step. When another route is genuinely defensible, list it as an alternative with a one-line tradeoff; never list more than two alternatives.

## Workflow

### 1. Resolve State

1. Read nearest repo instructions and relevant memory.
2. Find or create the canonical flow folder.
3. If existing `plan.md` or `progress.md` exists, treat it as authoritative unless current source evidence contradicts it.
4. Inspect the current worktree before relying on prior context.

### 2. Intake And Decision Gate

Build or update a working brief:

```text
Feature:
Primary actors:
Core invariant:
Previous intended behaviors:
Intentional behavior changes:
Unsafe outcomes:
Evidence:
Assumptions:
Out of scope:
```

Ask only for decisions that repo evidence cannot answer and that could change permissions, ownership, money, state transitions, destructive behavior, data model, migration direction, external contracts, customer-visible records, or live-data risk.

Batch routine defaults. Do not delegate unresolved product decisions to workers.

For vague, novel, customer-facing, or design-heavy features, slow down enough to state the intended behavior or design direction before code starts. If the choice changes product direction, permissions, data, money, state, or user-visible records, get the decision recorded in `decisions.md`; otherwise record the safe default and continue.

### 3. Build The Dependency Graph

Represent the feature as graph nodes, not a loose checklist. A node is valid only when it has one primary actor/trigger, one observable behavior, one protected invariant, explicit prior behavior preservation, expected files, write boundaries, dependencies, tests, verification gates, and exit evidence.

Classify every node:

- `blocking` - later nodes depend on it.
- `parallel-safe` - can run with other nodes because dependencies are met and write scopes do not overlap.
- `single-threaded` - touches shared mutable state such as lockfiles, git, migrations, a shared test DB, deploys, or generated files.
- `decision-needed` - blocked by a missing product/business/ops decision.
- `unsafe-live` - cannot run against live data without explicit approval.

Risk tiers:

- `T1`: money, permissions, ownership, state transitions, destructive writes, webhooks, accepted/customer-facing records.
- `T2`: external adapters, background jobs, queues, sync logic, admin workflows, migrations, operational tooling.
- `T3`: UI display, copy, layout, simple filters, low-risk polish.

### 4. Plan Worker Waves

Launch every unblocked node whose dependencies are `DONE` and whose write boundaries are disjoint. Use as many workers as safely possible, not blindly as many as possible.

Launch mechanics:

- Launch a wave as concurrent subagent calls through the environment's agent mechanism (agent/task tool, team, or workflow runner) — dispatch all workers in the wave together, not one worker per turn.
- Default soft cap: 4 workers per wave. Exceed it only when the user explicitly asks for more parallelism and integration can still verify every report properly.
- Use isolated worktrees for workers when the environment supports them and write boundaries are tight or shared-state risk is non-trivial.

Never parallelize:

- git checkout, merge, rebase, push, or release tagging
- package lockfile or dependency graph edits
- migrations against the same database
- tests sharing one mutable database
- deploys or promotions
- multiple workers writing the same files
- broad refactors across shared contracts

Read `references/worker-contract.md` before launching workers.

Each worker brief must be self-contained: one goal, the relevant current context, allowed write scope, forbidden scope, dependencies already satisfied, shared-state risks, required gates, and exact evidence to return. Do not rely on hidden chat context for worker success.

### 5. Execute Nodes

Each implementation node must follow:

```text
RED -> GREEN -> REFACTOR -> Repo Gate -> Browser Gate -> Boundary/Migration Gate -> Worker Report
```

Required standards:

- Write or locate the failing behavior test first, unless the node is already implemented and can be proven.
- Confirm RED fails for the intended reason.
- Make the smallest GREEN change.
- Refactor only after tests pass.
- Cover regression guards for previous intended behaviors.
- Do not weaken assertions, mock the dangerous part, or widen scope with bonus fixes.
- Run non-destructive migrations when the node requires them and project rules allow them.
- Use current official docs or Context7 for third-party/framework behavior where current behavior matters.
- For UI/user-visible nodes, verify in a real browser before marking the node done, using whatever browser tooling the active environment provides (in-app browser, browser MCP/extension, or Playwright).
- If a bug, test failure, build failure, or unexpected behavior appears, write down the current root-cause finding or hypothesis before changing code.
- If the same error or failed fix repeats twice, stop blind retries, research current official docs or reputable current sources, choose one safe fix, and record the reasoning.
- Do not claim a node is done or move to the next node without fresh evidence from the current run.

Workers return concise evidence in `agent-runs/<node>-<attempt>.md`. They do not edit `progress.md`.

### 6. Integrate And Advance

For each worker report:

1. Run a spec pass: verify the report satisfies the node behavior, acceptance criteria, decisions, intentional changes, and previous behavior preservation.
2. Run a quality pass: verify changed files are inside the assigned write boundary, tests are meaningful, contracts still fit, and no unrelated work was absorbed.
3. Verify RED, GREEN, REFACTOR, and required gates have evidence.
4. Run integration checks when worker outputs share contracts.
5. Update `progress.md` only after evidence is accepted.
6. Commit the accepted wave as one checkpoint commit before launching the next wave. Workers never run git mutations; only the orchestrator commits. Pushing or shipping goes through `cap` and only when the user asks.
7. Recompute the dependency graph and launch the next safe wave.

If a node fails, keep it `IN_PROGRESS` or mark it `BLOCKED` with the exact failing command, missing decision, or unsafe shared-state reason. Do not quietly skip a gate and continue.

### 7. Final Proof

Before `COMPLETE`, prove every explicit requirement:

- All required nodes are `DONE` or explicitly `SKIPPED` with accepted reasons.
- No blocker remains for in-scope work.
- Targeted tests passed for changed areas.
- Full tests, typecheck, lint, and build ran when practical, or each skip has a reason.
- Browser proof ran for user-visible workflows.
- Boundary checks ran for DB/API/filesystem/third-party/payment/auth nodes, or each skip has a reason.
- Non-destructive migrations ran when required.
- `verification.md` records behavior preservation confidence from 0-100.
- Every positive completion claim is backed by fresh evidence in `verification.md`, not by memory, expectation, or a worker's recommendation.

Only mark the feature `COMPLETE` when current evidence proves the full requested scope, not merely the last node.

## Final Response

Report:

```text
Summary:
Plan artifact:
Progress artifact:
Nodes completed / blocked / skipped:
Parallel waves run:
Behavior preservation approach:
Final verification:
Skipped checks:
Residual risk:
Confidence:
Next action:
```

If work is not complete, leave the flow active and state the next unblocked graph node or blocker. If work is complete, set `Next action` using the Handoffs rules.

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
