---
name: feature-intake-grill
description: Decision-intake stage for feature-orchestrator flows. Use to clarify product, UX, data, permission, money, state, migration, external-contract, and live-risk decisions before a dependency graph is finalized. Records confirmed decisions, safe defaults, rejected options, assumptions, and open blockers in plans/<feature-slug>/decisions.md without asking questions the codebase can answer.
---

# Feature Intake Grill

## Purpose

Clear the decisions that would make a feature graph unsafe or ambiguous. This stage feeds `feature-orchestrator`; it does not implement code.

## Inputs

- Feature request or existing `plans/<feature-slug>/`.
- Current repo evidence, docs, schema, routes, tests, and nearby implementation.
- Any user constraints about scope, rollout, risk, or verification.

## Workflow

1. Resolve or create `plans/<feature-slug>/decisions.md`.
2. Read enough repo evidence to avoid asking questions the code can answer.
3. Build a short decision map:
   - actors and permissions
   - data ownership and org/customer boundaries
   - money, price, status, state transitions, destructive actions
   - migration/backfill/live-data risk
   - external contracts, webhooks, retries, idempotency
   - customer-visible records, notifications, audit/manual review
   - UX states, error states, empty states, and recovery paths
4. Ask one material decision at a time when the answer could change scope or safety.
5. For vague, novel, customer-facing, or design-heavy work, state the intended behavior or design direction before implementation. Record product-changing decisions; record routine safe defaults without turning them into extra interruptions.
6. Batch routine defaults into 3-5 confirmations when repo conventions or best practice are clear.
7. Record every answer and safe default in `decisions.md`.

## Output Shape

```markdown
# Decisions: {feature-slug}

## Confirmed Decisions
- YYYY-MM-DD: ...

## Safe Defaults
- ...

## Open Questions
- ...

## Rejected Options
- ...

## Blocked Graph Nodes
- S?: blocked until ...
```

## Rules

- Do not ask questions that code, docs, tests, schema, or existing product copy can answer.
- Do not batch decisions that affect money, permissions, ownership, state, destructive writes, migrations, external contracts, or operational risk.
- Do not invent product decisions for workers.
- Finish when every mapped decision is confirmed, safely defaulted, or recorded as an open question or blocked node. Asking zero questions is a valid outcome when repo evidence answers everything.
- If the user asks not to be interrupted, record safe assumptions and mark unsafe nodes blocked for `feature-orchestrator`.
