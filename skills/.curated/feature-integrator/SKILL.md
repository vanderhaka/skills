---
name: feature-integrator
description: Integration stage for feature-orchestrator worker waves. Use after one or more feature-slice-worker reports to verify evidence, check write boundaries, reconcile shared contracts, update canonical progress.md, launch the next safe dependency wave, and prevent worker reports from being treated as complete without proof.
---

# Feature Integrator

## Purpose

Accept or reject worker outputs and advance the dependency graph. This stage is the only stage, besides the main orchestrator, that may update `progress.md`.

## Workflow

1. Read `plan.md`, `progress.md`, and the relevant `agent-runs/*.md`.
2. For each worker report, verify:
   - changed files stayed inside write boundaries
   - dependencies were satisfied before work began
   - RED, GREEN, REFACTOR, and required gates have evidence
   - browser/boundary/migration skips have explicit reasons
   - defaults applied by the worker are routine and inferable from repo conventions, existing product patterns, framework norms, standard engineering practice, or strong UX/UI/product judgment
   - no unrelated work was absorbed
3. Run integration checks when workers touched shared contracts, generated types, routes, schemas, or UI flows.
4. Update `progress.md`:
   - `DONE` only when evidence is accepted
   - `BLOCKED` with exact blocker
   - `NEEDS ATTENTION` or keep `IN_PROGRESS` when evidence is weak
5. Add newly discovered required work as new graph nodes.
6. Recompute eligible next-wave nodes.
7. Recommend or launch the next safe parallel wave when the main orchestrator requests it.

## Rules

- Do not trust a worker's `DONE` recommendation without checking evidence.
- Do not merge outputs that collide on files or contracts without local integration proof.
- Do not advance dependent nodes until prerequisite progress is accepted.
- Do not hide failed gates behind notes.
- Do not bounce routine defaults back to the user during integration; accept them when evidence and product taste support them, record them in `decisions.md` if they matter for future workers, and only block on material missing decisions.
