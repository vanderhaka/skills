# Grill Me

## What This Skill Does

`grill-me` interviews the user about a plan, design, or decision until the important branches are resolved. It is for shared understanding, not busywork or reinventing common practice. In docs mode, it also keeps durable project docs current as decisions resolve.

## Use It When

- The user asks to be grilled, or asks to "grill with docs".
- A plan needs serious questioning before work starts.
- Product, business, data, permission, money, integration, state, or UX choices are unclear.
- The answer cannot be safely inferred from the codebase or established best practice.
- A feature or refactor needs shared understanding before planning or coding.
- Domain terms, actor names, lifecycle states, or product rules need to be clarified.
- Glossary conflicts, ownership rules, or code-vs-domain contradictions need to be resolved.
- Decisions should survive into `CONTEXT.md`, `docs/adr/`, or `plans/<feature-slug>/decisions.md`.

## How It Works

The skill classifies each possible question before asking it. Routine technical decisions and reversible light business defaults are decided by the model, logged for review, and not turned into confirmation prompts. Material decisions are asked one at a time with a recommended answer. When used before `feature-orchestrator`, it records decisions in `plans/<feature-slug>/decisions.md`.

Docs mode fires when the user says "grill with docs", or when the grilled decisions must survive the chat in durable project docs; otherwise the skill stays chat-only. In docs mode it also stress-tests domain language with concrete scenarios, glossary conflicts, ownership rules, and code-vs-domain contradictions, and updates the relevant durable docs (`CONTEXT.md`, `docs/adr/`, `plans/<feature-slug>/decisions.md`) instead of leaving the knowledge trapped in chat.

## What You Get

- Focused decision questions.
- Recommended answer for each question.
- Routine defaults selected by the model and logged for review.
- Recorded decisions when used in a feature flow.
- In docs mode: updated domain language or ADRs when warranted, domain terms/scenarios/contradictions called out when relevant, and a recommended next skill.

## Not For

Use `feature-orchestrator`'s intake-grill stage (`references/stages/intake-grill.md`) when you only need the narrower orchestrator decision gate. Use `issue-fix-strategy` when the input is a messy issue list and you want priority/routing judgement before deeper discussion.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/grill-me
```

Restart Codex after installing new skills.
