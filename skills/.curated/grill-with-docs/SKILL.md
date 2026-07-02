---
name: grill-with-docs
description: Docs-backed decision grilling for codebase work. Use when the user says "grill with docs", or when a feature, refactor, architecture choice, or product/design plan needs material decisions clarified while updating project domain language, assumptions, ADR-worthy decisions, and plans/<feature-slug>/decisions.md as the discussion resolves. Use grill-me instead when no durable docs need updating.
---

# Grill With Docs

Interview the user about the material decisions that affect a codebase, while keeping the project's durable docs current. This is `grill-me` plus documentation discipline: ask only decisions that cannot be safely answered from repo evidence or best practice, and record the answers before downstream agents reinterpret them.

## When To Use

Use this before implementation when the work needs shared understanding and one or more of these should survive the conversation:

- domain terms, actor names, lifecycle names, or overloaded vocabulary
- glossary conflicts, ownership rules, scenarios, or code-vs-domain contradictions
- architectural or product decisions that future agents should not re-litigate
- feature assumptions, safe defaults, rejected options, and blockers
- scope, permission, money, state, migration, external-contract, or live-risk decisions

For a normal `feature-orchestrator` flow, write decisions to `plans/<feature-slug>/decisions.md`. For general repo language, update `CONTEXT.md`. For architectural choices that should constrain future work, create or update an ADR under `docs/adr/`.

## Workflow

1. Read nearby repo instructions, existing `CONTEXT.md`, `docs/adr/`, and any existing `plans/<feature-slug>/decisions.md` that applies.
2. Inspect code, docs, tests, schema, routes, and product copy before asking questions the repo can answer.
3. Use `references/domain-modeling.md` when the discussion changes domain language, actors, lifecycle states, ownership, or business rules.
4. Use the `grill-me` decision standard:
   - decide codebase-discoverable questions from repo evidence
   - choose routine best-practice defaults directly
   - ask one user-material decision at a time, with a recommended answer
   - log model defaults for review instead of interrupting for every reversible choice
5. While grilling, maintain a decision log with:
   - confirmed user decisions
   - model-defaulted decisions
   - rejected options
   - open blockers
   - downstream implications
6. Update durable docs as decisions crystallize:
   - `plans/<feature-slug>/decisions.md` for feature flow decisions
   - `CONTEXT.md` for canonical domain language and relationships
   - `docs/adr/YYYY-MM-DD-short-title.md` for load-bearing architecture or product decisions
7. End with a concise review of decisions captured, defaults chosen, docs changed, blockers, and the recommended next skill.

## Documentation Rules

- Do not create docs just to look thorough. Write only durable context that future agents or maintainers need.
- Keep domain language in user/business terms, not file names or class names, unless the code name is also the domain term.
- If the user's term conflicts with `CONTEXT.md`, call out the conflict and resolve it before recording anything.
- If a term is vague, propose a precise canonical term and ask only when the choice changes product meaning.
- If a claimed business rule contradicts code, docs, schema, or product copy, surface the contradiction before updating docs.
- If a relationship is unclear, test it with concrete scenarios rather than asking abstract taxonomy questions.
- If a decision would materially affect permissions, money, ownership, state transitions, destructive writes, migrations, external contracts, or live data, ask before defaulting it.
- If no material questions remain, stop grilling and produce the decision review.

## Output

Report:

```text
Decisions captured:
Model defaults for review:
Docs updated:
Open blockers:
Rejected options:
Recommended next skill:
```

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
