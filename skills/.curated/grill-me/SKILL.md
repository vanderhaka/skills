---
name: grill-me
description: Interview the user about a plan or design until reaching shared understanding, while defaulting routine technical and reversible low-risk decisions to established best practice. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". Ask only material product, business, risk, or external-contract questions that cannot be safely decided from best practice or repo context. When the answers must also update durable docs such as CONTEXT.md or ADRs, use grill-with-docs instead.
---

Interview me relentlessly about the decisions that actually require my judgment. The goal is shared understanding, not making me reinvent common practice.

Before asking any question, classify the candidate decision:

1. Codebase-discoverable: inspect the codebase or docs and follow the existing pattern. Do not ask.
2. Best-practice default: decide directly using repo conventions, ecosystem norms, accessibility defaults, ordinary validation/error-handling patterns, standard test placement, logging norms, formatting, and framework-standard file organization. Do not ask.
3. Reversible light business default: decide directly when normal category practice is enough and the downside is low, such as default copy tone, empty-state behavior, standard onboarding steps, conventional non-binding labels, default analytics event names, or MVP scope guardrails. Do not ask.
4. User-material decision: ask me one question at a time, provide your recommended answer, and explain why it cannot safely be defaulted.

Ask only user-material decisions. These include material scope or positioning choices, revenue/pricing/contracts, permissions/privacy/security boundaries, irreversible data model or migration strategy, external API contracts, legal/compliance exposure, operational risk, stakeholder commitments, brand/business choices where category best practice does not decide, and UX/state choices that materially change a core workflow.

Do not batch-confirm routine defaultable choices during the interview. Choose the default, keep a "Model defaults for review" log, and continue to the next material decision. If the user objects to a default at review time, update the decision log and revisit only dependent decisions.

When asking a user-material question, walk down the design tree and resolve dependencies one by one. After each answer, decide which downstream branch is now relevant before asking again. If the user defers a question ("you decide", "don't know"), choose the best-practice answer, log it under model defaults, and move on — do not re-ask.

If a question can be answered by exploring the codebase, explore the codebase instead.

At the end, produce a concise review containing user decisions captured, model-defaulted decisions for review, rejected material options, open blockers, and remaining risks. If no material question remains, stop asking and produce the review.

When this skill is used before `feature-orchestrator`, record decisions, safe defaults, rejected options, and open blockers in `plans/<feature-slug>/decisions.md` so worker agents do not rediscover or reinterpret product choices.
