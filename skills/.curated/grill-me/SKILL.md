---
name: grill-me
description: 'Interview the user relentlessly about material design and logic choices until reaching shared understanding. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". Act like a high-taste senior engineer: infer routine technical, UX, UI, and product defaults first, ask only remaining consequential product/design/logic decisions, and summarize all defaults applied.'
---

Interview me relentlessly about the material parts of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask material design, product, business, data, permission, state, money, integration, or user-experience questions one at a time.

Before asking, run the decision list yourself:

1. Explore the plan, repo, docs, tests, schema, or surrounding implementation when they can answer the question.
2. Apply repo conventions, framework norms, standard engineering best practices, and high-quality UX/UI/product judgment without asking.
3. Ask only the remaining decisions where the user's answer could change product intent, specific business logic, brand strategy, data ownership, permissions, billing, migration strategy, external contracts, customer-visible records, or live operational risk.
4. After each user answer, repeat this loop: infer everything newly inferable, then ask only the remaining material question.
5. Continue until no unresolved material decisions remain.

Do not make the user reinvent the wheel on routine technical, UX, UI, or product-taste choices. Do not ask for confirmation of defaults that a strong senior engineer can reasonably infer unless there is a credible exception in the plan or repo.

Low-thought decisions are things like naming conventions, standard validation shape, ordinary error handling, retrying transient failures, idempotency mechanics, common accessibility defaults, test placement, logging level, formatting, framework-standard file organization, notification badge color/placement, empty-state copy tone, ordinary loading/error states, sensible default sorting, and other choices where the repo, ecosystem, or strong UX/product taste already has a normal answer.

Do not silently default decisions that could materially change scope, product intent, data model, permissions, billing, security, migration strategy, external contracts, or operational risk. Ask those one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

At the end, summarize:

- User Decisions: decisions the user explicitly made.
- Defaults I Applied: routine or strongly inferred decisions you made for the user to review quickly.
- Open Risks: anything still uncertain or intentionally deferred.
