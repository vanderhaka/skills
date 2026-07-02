# Feature Graph Plan

## Purpose

Convert a feature brief and decisions into one executable dependency graph for `feature-orchestrator`.

## Required Reads

- `plans/<feature-slug>/decisions.md` if present.
- Relevant repo docs, schema, routes/actions, services, UI entry points, tests, migrations, and external adapters.
- `feature-orchestrator/references/graph-and-progress.md`.

## Workflow

1. Resolve `plans/<feature-slug>/`.
2. Create or update `plan.md` and `progress.md`; do not create competing `*-tdd` or `*-stepwise` plans for the same feature.
3. Define the working brief: feature, actors, invariant, previous intended behaviors, intentional changes, unsafe outcomes, evidence, assumptions, out of scope.
4. Decompose into graph nodes.
5. For each node, require:
   - one primary actor/trigger
   - one behavior as `When X, then Y`, unless the node is scaffold/refactor/verification/ops
   - invariant protected
   - intentional changes and previous behaviors preserved
   - unsafe outcomes
   - expected files and write boundaries
   - dependencies
   - RED/GREEN/REFACTOR plan
   - repo, browser, boundary, and migration gates
   - exact evidence expected for each required gate
   - worker role and exit evidence
6. Classify nodes as `blocking`, `parallel-safe`, `single-threaded`, `decision-needed`, or `unsafe-live`.
7. Build dependency waves and parallel groups.
8. Seed `progress.md` with every node and gate set to `TODO`/`PENDING`.

## Rules

- Split nodes that combine multiple actors, state transitions, boundaries, or unrelated file surfaces.
- Treat migrations, package locks, git operations, deploys, and shared mutable test DBs as single-threaded.
- Include non-destructive migration execution as a gate when project rules require it.
- Mark destructive/live-data work blocked until explicitly approved.
- The graph is not ready until the first wave is unblocked and every blocked node names its blocker.
- Worker roles must be self-contained enough to launch: goal, context, allowed write scope, forbidden scope, dependencies, shared-state risks, required gates, and return evidence.
- For bug/failure nodes, include a root-cause/debugging expectation instead of letting the worker stack guesses.
- When the plan is seeded by `issue-fix-strategy` or `code-review` output, record the originating issue ID(s) (`I1`, `I2`, ...) on each node and ensure every accepted issue maps to at least one node.
