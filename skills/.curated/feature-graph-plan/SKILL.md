---
name: feature-graph-plan
description: Dependency-graph planning stage for feature-orchestrator flows. Use to create or update plans/<feature-slug>/plan.md and progress.md with thin RGR-ready graph nodes, risk tiers, dependencies, parallel groups, write boundaries, gates, and canonical progress tracking before workers launch.
---

# Feature Graph Plan

## Purpose

Convert a feature brief, explicit decisions, and strongly inferred defaults into one executable dependency graph for `feature-orchestrator`.

## Required Reads

- `plans/<feature-slug>/decisions.md` if present.
- Relevant repo docs, schema, routes/actions, services, UI entry points, tests, migrations, and external adapters.
- `feature-orchestrator/references/graph-and-progress.md` from the installed skills set.

## Workflow

1. Resolve `plans/<feature-slug>/`.
2. Create or update `plan.md` and `progress.md`; do not create competing `*-tdd` or `*-stepwise` plans for the same feature.
3. Define the working brief: feature, actors, invariant, previous intended behaviors, intentional changes, unsafe outcomes, evidence, assumptions, out of scope.
4. Before marking anything `decision-needed`, apply repo conventions, existing product patterns, framework norms, standard engineering practice, and strong UX/UI/product judgment. Record those defaults in `decisions.md` instead of asking the user.
5. Decompose into graph nodes.
6. For each node, require:
   - one primary actor/trigger
   - one behavior as `When X, then Y`, unless the node is scaffold/refactor/verification/ops
   - invariant protected
   - intentional changes and previous behaviors preserved
   - unsafe outcomes
   - expected files and write boundaries
   - dependencies
   - RED/GREEN/REFACTOR plan
   - repo, browser, boundary, and migration gates
   - worker role and exit evidence
7. Classify nodes as `blocking`, `parallel-safe`, `single-threaded`, `decision-needed`, or `unsafe-live`.
8. Build dependency waves and parallel groups.
9. Seed `progress.md` with every node and gate set to `TODO`/`PENDING`.

## Rules

- Split nodes that combine multiple actors, state transitions, boundaries, or unrelated file surfaces.
- Treat migrations, package locks, git operations, deploys, and shared mutable test DBs as single-threaded.
- Include non-destructive migration execution as a gate when project rules require it.
- Mark destructive/live-data work blocked until explicitly approved.
- Mark `decision-needed` only for material choices that repo evidence and strong senior-engineer judgment cannot answer, such as product intent, brand strategy, money, permissions, ownership, state semantics, destructive behavior, data model direction, external contracts, customer-visible records, or live operational risk.
- Do not block graph planning on routine technical, UX, UI, or product-taste choices such as retry mechanics, validation shape, notification badge treatment, empty/loading/error states, default sorting, standard affordances, or normal visual hierarchy.
- The graph is not ready until the first wave is unblocked and every blocked node names its blocker.
