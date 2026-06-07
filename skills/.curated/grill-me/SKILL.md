---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". Batch routine best-practice defaults into 3-5 quick confirmations instead of forcing needless one-by-one technical choices.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask material design, product, business, data, permission, state, money, integration, or user-experience questions one at a time.

Do not make the user reinvent the wheel on routine technical choices. When several low-thought decisions have clear best-practice defaults, batch them into 3-5 quick confirmations. For each item, state the default and only ask for confirmation or exceptions.

Low-thought decisions are things like naming conventions, standard validation shape, ordinary error handling, common accessibility defaults, test placement, logging level, formatting, framework-standard file organization, and other choices where the repo or ecosystem already has a normal answer.

Do not batch decisions that could materially change scope, UX, data model, permissions, billing, security, migration strategy, external contracts, or operational risk. Ask those one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

When this skill is used before `feature-orchestrator`, record decisions, safe defaults, rejected options, and open blockers in `plans/<feature-slug>/decisions.md` so worker agents do not rediscover or reinterpret product choices.
