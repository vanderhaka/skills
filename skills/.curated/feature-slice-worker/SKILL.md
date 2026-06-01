---
name: feature-slice-worker
description: Worker stage for one feature-orchestrator graph node. Use when assigned a single node with write boundaries and gates. Executes RED -> GREEN -> REFACTOR -> repo gate -> browser gate -> boundary/migration gate, writes an agent-run report, and never edits the canonical progress.md directly.
---

# Feature Slice Worker

## Purpose

Implement one assigned graph node safely. The worker owns the node implementation and evidence; the orchestrator owns integration and `progress.md`.

## Required Reads

- Assigned node from `plans/<feature-slug>/plan.md`.
- `plans/<feature-slug>/decisions.md`.
- `feature-orchestrator/references/worker-contract.md` from the installed skills set.
- Relevant source and tests inside the assigned read/write scope.

## Workflow

1. Confirm dependencies are satisfied and write boundaries are clear.
2. If another worker owns the same files or shared mutable state, stop and report `BLOCKED`.
3. RED:
   - write or locate the failing behavior/characterization test first
   - map acceptance criteria to assertions
   - cover regression guards
   - prove failure is for the intended reason
4. GREEN:
   - make the smallest code change
   - rerun targeted tests
   - do not refactor yet
5. REFACTOR:
   - clean only touched code when low risk
   - rerun targeted tests
6. Repo Gate:
   - run targeted tests
   - run typecheck/lint/build when required by the node or repo
7. Browser Gate:
   - required for user-visible nodes via Codex in-app browser when available
8. Boundary/Migration Gate:
   - run DB/API/filesystem/third-party/auth/payment checks when required
   - run non-destructive migrations when required and safe
9. Write or return an `agent-runs/<node>-<attempt>.md` report.

## Rules

- Do not edit `progress.md`.
- Do not spawn child agents.
- Do not revert unrelated changes.
- Do not weaken assertions, mock the dangerous part, or widen scope.
- Do not mark `DONE`; recommend `DONE`, `BLOCKED`, or `NEEDS ATTENTION` with evidence.
