---
name: grill-me
description: Interview the user about a plan or design until reaching shared understanding, while defaulting routine technical and reversible low-risk decisions to established best practice. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". Also use for "grill with docs" — when a feature, refactor, architecture choice, or product/design plan needs material decisions clarified while updating project domain language, assumptions, ADR-worthy decisions, and plans/<feature-slug>/decisions.md as the discussion resolves. Ask only material product, business, risk, or external-contract questions that cannot be safely decided from best practice or repo context.
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

## Docs Mode

Docs mode fires when the user says "grill with docs", or when the grilled decisions must survive the chat in durable project docs (`CONTEXT.md`, ADRs, `plans/<feature-slug>/decisions.md`); otherwise stay chat-only and skip this section.

In docs mode, this is the same interview engine above plus documentation discipline: ask only decisions that cannot be safely answered from repo evidence or best practice, and record the answers before downstream agents reinterpret them.

### When To Use Docs Mode

Use this before implementation when the work needs shared understanding and one or more of these should survive the conversation:

- domain terms, actor names, lifecycle names, or overloaded vocabulary
- glossary conflicts, ownership rules, scenarios, or code-vs-domain contradictions
- architectural or product decisions that future agents should not re-litigate
- feature assumptions, safe defaults, rejected options, and blockers
- scope, permission, money, state, migration, external-contract, or live-risk decisions

For a normal `feature-orchestrator` flow, write decisions to `plans/<feature-slug>/decisions.md`. For general repo language, update `CONTEXT.md`. For architectural choices that should constrain future work, create or update an ADR under `docs/adr/`.

### Docs Mode Workflow

1. Read nearby repo instructions, existing `CONTEXT.md`, `docs/adr/`, and any existing `plans/<feature-slug>/decisions.md` that applies.
2. Inspect code, docs, tests, schema, routes, and product copy before asking questions the repo can answer.
3. Use `references/domain-modeling.md` when the discussion changes domain language, actors, lifecycle states, ownership, or business rules.
4. Apply the interview engine above: decide codebase-discoverable questions from repo evidence, choose routine best-practice defaults directly, ask one user-material decision at a time with a recommended answer, and log model defaults for review instead of interrupting for every reversible choice.
5. While grilling, maintain a decision log with confirmed user decisions, model-defaulted decisions, rejected options, open blockers, and downstream implications.
6. Update durable docs as decisions crystallize:
   - `plans/<feature-slug>/decisions.md` for feature flow decisions
   - `CONTEXT.md` for canonical domain language and relationships
   - `docs/adr/YYYY-MM-DD-short-title.md` for load-bearing architecture or product decisions
7. End with a concise review of decisions captured, defaults chosen, docs changed, blockers, and the recommended next skill.

### Documentation Rules

- Do not create docs just to look thorough. Write only durable context that future agents or maintainers need.
- Keep domain language in user/business terms, not file names or class names, unless the code name is also the domain term.
- If the user's term conflicts with `CONTEXT.md`, call out the conflict and resolve it before recording anything.
- If a term is vague, propose a precise canonical term and ask only when the choice changes product meaning.
- If a claimed business rule contradicts code, docs, schema, or product copy, surface the contradiction before updating docs.
- If a relationship is unclear, test it with concrete scenarios rather than asking abstract taxonomy questions.
- If a decision would materially affect permissions, money, ownership, state transitions, destructive writes, migrations, external contracts, or live data, ask before defaulting it.
- If no material questions remain, stop grilling and produce the decision review.

### Docs Mode Output

Report:

```text
Decisions captured:
Model defaults for review:
Docs updated:
Open blockers:
Rejected options:
Recommended next skill:
```

When domain modeling was active, include:

```text
Domain terms clarified:
Glossary conflicts resolved:
Scenarios tested:
Code/docs contradictions:
```

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
