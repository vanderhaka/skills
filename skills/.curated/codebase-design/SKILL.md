---
name: codebase-design
description: Shared codebase-design discipline for deep modules, clean interfaces, seam placement, adapters, test surfaces, and design alternatives. Use when the user asks to design or improve architecture, refactor a module, choose a boundary, make code easier to test, reduce shallow abstractions, or when another skill needs architecture vocabulary before planning or review.
---

# Codebase Design

Use this skill to reason about architecture with one consistent vocabulary. The goal is not prettier abstraction. The goal is code that gives callers more leverage, concentrates change in fewer places, and can be tested through the same interface real callers use.

This is a support discipline. If the user asked only for design advice, answer in chat. If the user asked to implement, hand the result to the appropriate implementation skill after the design call is made.

## Core Vocabulary

Use these terms consistently:

- `Module`: any unit with an interface and implementation. This can be a function, class, package, route, service adapter, or larger feature slice.
- `Interface`: everything a caller must know to use the module correctly: inputs, outputs, invariants, ordering, errors, side effects, performance, and configuration.
- `Implementation`: the code hidden behind the interface.
- `Depth`: how much useful behavior sits behind how little caller-facing surface.
- `Seam`: the place where behavior can vary without editing the caller.
- `Adapter`: a concrete implementation that plugs into a seam.
- `Leverage`: what callers gain when one interface hides real complexity.
- `Locality`: what maintainers gain when a change or bug fix is concentrated in one place.

Prefer this vocabulary over loose words like "service", "component", "layer", or "boundary" when the design decision is really about module shape.

## Design Rules

1. Make the interface smaller before making the implementation clever.
2. Hide complexity behind the module only when callers no longer need to know it.
3. Put seams where behavior truly varies, not where a pattern says a seam should exist.
4. Treat one adapter as a hypothetical seam and two adapters as a real seam.
5. Make the interface the main test surface.
6. Prefer tests that prove observable behavior through the interface over tests that inspect internals.
7. Delete shallow wrappers when they only move complexity into callers.
8. Keep domain language aligned with `CONTEXT.md` or the relevant project docs.

## Design Pass

When reviewing or designing a module:

1. Name the caller-facing job in one sentence.
2. List what callers currently need to know.
3. Identify the complexity that should move behind the interface.
4. Identify the real variation point, if any.
5. Classify dependencies:
   - in-process
   - local-substitutable
   - remote but owned
   - true external
6. Propose the smallest useful interface.
7. State what the implementation hides.
8. State how it will be tested through the interface.
9. Run the deletion test: if this module vanished, would complexity disappear or spread across callers?
10. Decide whether the design is deep enough, too shallow, or over-abstracted.

Use `references/deepening.md` when the task is specifically about deepening shallow modules. Use `references/design-it-twice.md` when the design is important enough to compare multiple interface shapes.

## Output

Default to this structure:

```text
Design target:
Current problem:
Recommended interface:
What moves behind it:
Seam and adapters:
Dependency strategy:
Test surface:
Trade-offs:
Next skill:
```

## Red Flags

- The proposed interface has almost as many concepts as the implementation.
- Every caller still needs to understand the hidden workflow.
- Tests need to reach past the interface to prove important behavior.
- A new adapter exists only because "ports and adapters" sounded clean.
- A wrapper was added without deleting complexity elsewhere.
- Domain terms in the interface disagree with project docs or product language.

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
