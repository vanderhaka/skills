---
name: feature-intake-grill
description: Decision-intake stage for feature-orchestrator flows. Use to clarify only material product, UX, data, permission, money, state, migration, external-contract, and live-risk decisions before a dependency graph is finalized. Infers routine technical, UX, UI, and product defaults first, then records confirmed decisions, safe defaults, rejected options, assumptions, and open blockers in plans/<feature-slug>/decisions.md without asking questions the codebase or strong product judgment can answer.
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
   - external contracts and webhooks, separating business contract choices from routine retry/idempotency mechanics
   - customer-visible records, notifications, audit/manual review
   - UX states, error states, empty states, and recovery paths
4. Apply safe defaults for routine technical, UX, UI, and product-taste decisions where repo conventions, best practice, or strong senior-engineer judgment are clear.
5. Ask one material decision at a time only when the answer could change scope, safety, product intent, brand strategy, or specific business logic.
6. After each answer, repeat the loop: infer newly clear defaults, then ask only the remaining material decision.
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
- Do not ask the user to confirm routine technical, UX, UI, or product-taste defaults unless the repo or feature creates a credible exception.
- Do not silently default decisions that affect money, permissions, ownership, state, destructive writes, migrations, external contracts, or operational risk.
- Treat standard engineering mechanics, such as transient retries, idempotency mechanics, validation shape, accessibility defaults, test placement, and framework-standard organization, as safe defaults when the repo does not indicate otherwise.
- Treat strong UX/UI defaults, such as red notification badges, clear empty/loading/error states, sensible default sorting, standard affordances, and normal visual hierarchy, as safe defaults when the repo does not indicate otherwise.
- Still ask about business-facing contract choices, such as what counts as a duplicate, who is notified, which state is customer-visible, what manual review means, or whether a product behavior expresses a non-obvious strategic preference.
- Do not invent product decisions for workers.
- If the user asks not to be interrupted, record safe assumptions and mark unsafe nodes blocked for `feature-orchestrator`.
