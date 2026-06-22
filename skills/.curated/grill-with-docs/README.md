# Grill With Docs

## What This Skill Does

`grill-with-docs` interviews the user about material codebase decisions and records the durable results in project docs as they resolve.

## Use It When

- A feature or refactor needs shared understanding before planning or coding.
- Domain terms, actor names, lifecycle states, or product rules need to be clarified.
- Decisions should survive into `CONTEXT.md`, `docs/adr/`, or `plans/<feature-slug>/decisions.md`.
- The work touches permissions, money, ownership, state, migrations, integrations, or customer-visible behavior.

## How It Works

The skill follows the local `grill-me` standard: inspect repo evidence first, default routine safe choices, and ask only user-material decisions one at a time with a recommended answer. As decisions land, it updates the relevant durable docs instead of leaving the knowledge trapped in chat.

## What You Get

- Confirmed user decisions.
- Model-defaulted decisions for review.
- Updated domain language or ADRs when warranted.
- Feature-flow decisions recorded for downstream planning and workers.
- A recommended next skill.

## Not For

Use `grill-me` when no docs need to be updated. Use `feature-intake-grill` when you only need the narrower orchestrator decision gate. Use `issue-fix-strategy` when the input is a messy issue list and you want priority/routing judgement before deeper discussion.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/grill-with-docs
```

Restart Codex after installing new skills.
