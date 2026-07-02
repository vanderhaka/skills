---
name: feature-integrator
description: Integration stage for feature-orchestrator worker waves. Use after one or more feature-slice-worker reports to verify evidence, check write boundaries, reconcile shared contracts, update canonical progress.md, launch the next safe dependency wave, and prevent worker reports from being treated as complete without proof.
---

# Feature Integrator

## Purpose

Accept or reject worker outputs and advance the dependency graph. This stage is the only stage, besides the main orchestrator, that may update `progress.md`.

## Workflow

1. Read `plans/<feature-slug>/plan.md`, `progress.md`, and the relevant `agent-runs/*.md` from the same folder.
2. For each worker report, run two review passes:
   - Spec pass: assigned behavior, acceptance criteria, decisions, intentional behavior changes, and previous behavior preservation are satisfied.
   - Quality pass: changed files stayed inside write boundaries, dependencies were satisfied before work began, tests are meaningful, contracts still fit, and no unrelated work was absorbed.
3. Verify RED, GREEN, REFACTOR, and required gates have fresh evidence from this run.
4. Verify browser/boundary/migration skips have explicit accepted reasons.
5. Run integration checks when workers touched shared contracts, generated types, routes, schemas, or UI flows.
6. Update `progress.md`:
   - `DONE` only when evidence is accepted
   - `BLOCKED` with exact blocker
   - keep `IN_PROGRESS` or set `VERIFYING` when evidence is weak; a worker's `NEEDS ATTENTION` is a recommendation, not a node status
7. Add newly discovered required work as new graph nodes.
8. Recompute eligible next-wave nodes.
9. Recommend or launch the next safe parallel wave when the main orchestrator requests it.

## Rules

- Do not trust a worker's `DONE` recommendation without checking evidence.
- Do not merge outputs that collide on files or contracts without local integration proof.
- Do not advance dependent nodes until prerequisite progress is accepted.
- Do not launch the next wave before the accepted wave is committed as one orchestrator-owned checkpoint commit; reject worker reports that include their own commits or pushes.
- Do not hide failed gates behind notes.
- Do not accept a broad success claim when the evidence only proves a narrow path.
- Do not treat stale command output, expected behavior, or confidence as proof.
