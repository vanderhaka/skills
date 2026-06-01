# Feature Intake Grill

## What This Skill Does

`feature-intake-grill` clears the decisions that would make a feature graph unsafe or ambiguous. It is the decision gate before `feature-graph-plan`.

## Use It When

- A missing answer could change scope or safety.
- The feature touches permissions, ownership, money, state, migrations, live data, or external contracts.
- The codebase cannot answer a product or operational decision.
- Worker agents would be unsafe without a recorded decision.

## How It Works

The skill reads enough repo evidence to avoid wasting the user's time. It builds a decision map across actors, data ownership, money, state transitions, migrations, integrations, customer-visible records, and UX recovery paths. It asks only material questions and records safe defaults when the answer is routine.

## What You Get

- `plans/<feature-slug>/decisions.md`.
- Confirmed decisions.
- Safe defaults.
- Rejected options.
- Open questions.
- Any graph nodes blocked by missing decisions.

## Not For

Use `feature-graph-plan` when the decisions are already clear. Use `grill-me` only when the user explicitly wants a heavier interview.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-intake-grill
```

Restart Codex after installing new skills.
