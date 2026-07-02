# Grill Me

## What This Skill Does

`grill-me` interviews the user about a plan, design, or decision until the important branches are resolved. It is for shared understanding, not busywork or reinventing common practice.

## Use It When

- The user asks to be grilled.
- A plan needs serious questioning before work starts.
- Product, business, data, permission, money, integration, state, or UX choices are unclear.
- The answer cannot be safely inferred from the codebase or established best practice.

## How It Works

The skill classifies each possible question before asking it. Routine technical decisions and reversible light business defaults are decided by the model, logged for review, and not turned into confirmation prompts. Material decisions are asked one at a time with a recommended answer. When used before `feature-orchestrator`, it records decisions in `plans/<feature-slug>/decisions.md`.

## What You Get

- Focused decision questions.
- Recommended answer for each question.
- Routine defaults selected by the model and logged for review.
- Recorded decisions when used in a feature flow.

## Not For

Use `grill-with-docs` when the answers should also update durable docs (`CONTEXT.md`, ADRs, decision records). Use `feature-intake-grill` when you only need the orchestrator decision gate. Use `issue-fix-strategy` when you want the agent to make the calls and ask only blocking questions.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/grill-me
```

Restart Codex after installing new skills.
