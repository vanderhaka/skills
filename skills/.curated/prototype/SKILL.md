---
name: prototype
description: Build a disposable prototype to answer a design, UI, state, data-shape, or business-logic question before full implementation. Use when the user asks to prototype, mock up options, try UI variants, simulate a workflow, feel out a state model, or explore an approach without committing production code.
---

# Prototype

Use this skill when the right next step is a throwaway experiment, not a production implementation. A prototype answers one question quickly, captures the answer, and then gets deleted, isolated, or deliberately folded into real work.

This skill is intentionally lightweight. Do not turn the prototype into the production feature while it is still serving as a question-answering tool.

## Choose The Branch

Pick the branch from the question being answered:

- Use `references/logic-prototype.md` when the question is about state, workflow, business rules, data shape, or an API surface.
- Use `references/ui-prototype.md` when the question is about layout, information hierarchy, interaction, page structure, or visual direction.

If the branch is ambiguous, infer from the nearby code. Backend/module uncertainty defaults to logic. Page/component uncertainty defaults to UI. State the assumption before building.

## Rules

1. Write the question first.
2. Mark the code as prototype-only in the filename, route, comment, or README.
3. Use the project's existing runtime and task runner.
4. Keep persistence out unless persistence is the thing being tested.
5. Avoid broad abstractions, hardening, and polish.
6. Surface the important state or variant clearly so the user can judge it.
7. Capture the answer when the prototype has taught us something.
8. Delete, isolate, or intentionally promote the useful part when the decision is made.

## Workflow

1. Identify the exact question the prototype must answer.
2. Choose logic or UI branch.
3. Choose the smallest location that gives useful context.
4. Build the minimum runnable artifact.
5. Provide the command or URL.
6. Let the user or browser evidence answer the question.
7. Record the answer in the right durable place: commit message, ADR, issue, plan decision file, or a short `NOTES.md` beside the prototype.
8. Recommend cleanup or promotion.

## Output

Before building:

```text
Prototype question:
Branch: logic / UI
Location:
Run path:
Cleanup plan:
```

After building:

```text
Prototype built:
How to run:
What to inspect:
Answer captured:
Cleanup or promotion path:
```

## Hard Limits

- Do not wire prototype actions to real destructive mutations.
- Do not use live customer data.
- Do not add tests unless the prototype has become the real implementation.
- Do not leave variant switchers, scratch routes, or terminal shells in production paths without an explicit cleanup decision.
- Do not claim the production feature is done because the prototype works.

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
