---
name: tdd-plan-grill
description: Stress-test a TDD plan before implementation. Review a `plans/{slug}-tdd/plan.md` across completeness, scope, dependencies, feasibility, test strategy, and ambiguity; ask focused questions; record decisions in `grill-review.md`; and update the plan so it is ready for `$tdd-deep`. Use when the user wants to grill or harden a TDD plan specifically.
---

# TDD Plan Grill

## Overview

Challenge a TDD plan before code gets written. Read the plan, inspect the codebase, rank the highest-impact risks, ask focused follow-up questions, record the decisions, and then update the plan if the user agrees. This sits between `$tdd-plan-deep` and `$tdd-deep`.

Be adversarial about the plan, not the user. Surface gaps that would change issue count, sequencing, tests, or assumptions. Skip low-value nitpicks.

## Inputs

Accept any of these:

- `plans/{slug}-tdd/`
- `plans/{slug}-tdd/plan.md`
- `$tdd-plan-grill` when there is exactly one likely TDD plan in `plans/`
- Optional focus areas such as completeness, dependencies, or test strategy

## Output Files

- `plans/{slug}-tdd/grill-review.md`
- Updated `plans/{slug}-tdd/plan.md` when the user approves changes

## Codex-Only Rules

- Do not use Claude-only tools or conventions.
- Use `multi_tool_use.parallel` for read-only inspection when it helps.
- Ask the user directly in plain English when a plan-changing decision is required.
- Keep every question grounded in the actual plan and codebase.
- Do not edit `plan.md` until the user has confirmed the proposed changes.

## References

Read only when needed:

- `references/review-dimensions.md`
  Use for the six review dimensions and question-writing rules.

## Workflow

### 1. Resolve the plan folder

- If the user gives `plans/{slug}-tdd/`, use it.
- If the user gives `plans/{slug}-tdd/plan.md`, use its parent folder.
- Otherwise inspect `plans/*-tdd/plan.md`.
- If none exist, stop and tell the user to run `$tdd-plan-deep` first.
- If more than one exists and no target is obvious, ask which plan to review.

### 2. Read the real context

- Read the full `plan.md`.
- Read the project manifest and likely feature-area files to understand the stack, test runner, and current architecture.
- If `grill-review.md` already exists, read it before continuing and extend it instead of starting from scratch unless the user asks for a fresh review.

### 3. Create or refresh `grill-review.md`

If the file does not exist, create it with:

```markdown
# Grill Review: {feature name}

Plan: plans/{slug}-tdd/plan.md
Date: {YYYY-MM-DD}
Status: IN_PROGRESS

---
```

If it already exists, keep the prior audit trail and append new rounds below it.

### 4. Analyze silently before asking anything

Read `references/review-dimensions.md` and build an internal findings list across:

1. completeness
2. scope and sizing
3. dependencies and ordering
4. technical feasibility
5. test strategy
6. assumptions and ambiguity

Rank findings by impact:

- plan structure changes
- dependency or sequencing risks
- test weakness that could hide broken behavior
- lower-value clarifications

### 5. Present a short assessment

Before asking questions, summarize:

- how many issues and waves the plan has
- what is already strong
- the top 2-4 concerns, in impact order
- how many questions you want to ask first

Keep this summary brief. The point is to orient the user, not to dump the whole analysis.

### 6. Ask focused questions in rounds

- Start with the questions most likely to change the plan.
- Ask 5-10 questions in the first round.
- Offer concrete options where possible.
- Group related questions together.
- Reference issue numbers, behaviors, dependencies, or file paths directly.
- If answers are thin or create new risks, ask one more focused follow-up round.
- Cap the review at 3 rounds total. If concerns remain, document them and move on.

Prefer questions like:

- `Issue 4 assumes optimistic updates. Should failures roll back inline or refresh from the server?`
- `Issue 2 and Issue 3 both modify auth state. Should they merge into one scaffold issue or stay separate?`

Avoid generic prompts like:

- `Anything else to consider?`
- `How should this work?`

### 7. Record each round in `grill-review.md`

After every answer batch, append:

```markdown
## Round {N}: {primary dimension}

### Questions Asked
1. ...

### Answers
1. ...

### Decisions Made
- ...

### Plan Changes Required
- [ ] ...
```

Record what changed, why it changed, and which issue numbers are affected.

### 8. Propose the plan edits

When the questions are resolved, summarize the exact edits under plain headings:

- Added
- Modified
- Removed or merged
- Reordered

Then ask for confirmation before changing `plan.md`.

### 9. Apply the approved changes

Once the user confirms:

- update `plan.md`
- renumber issues if needed
- refresh dependency waves
- keep acceptance criteria, regression guards, and verification notes aligned with the new structure
- mark the applied items in `grill-review.md`

### 10. Finish with a verdict

Set `Status: COMPLETE` in `grill-review.md` and add a final section with:

- issue count
- wave count
- what changed
- unresolved concerns that do not block implementation
- next step: `$tdd-deep plans/{slug}-tdd/`

## Quality Rules

- Read the full plan before asking any questions.
- Challenge assumptions, but do not invent requirements the user did not confirm.
- Prefer plan changes over vague warnings.
- Do not ask the user questions you can answer by reading the codebase.
- Keep the review traceable: every material question, answer, and decision goes in `grill-review.md`.
- If the plan is already solid, say so plainly and keep the edits minimal.

## Self-Refining Loop

Before each run, read the last 10 entries from `LESSONS.md` beside this `SKILL.md` if it exists.
After each run, append exactly two lines to that `LESSONS.md`: `input pattern: ...` and `result: what worked or failed, plus the fix`.
If `LESSONS.md` does not exist, create it beside this `SKILL.md` before appending.
Keep entries concise and redact secrets, tokens, customer data, and private details.
After every 10-20 entries, distill repeated lessons into durable rules in this `SKILL.md`, preserving the raw `LESSONS.md`.
