---
name: feature-plan-grill
description: Pre-execution review stage for feature-orchestrator plans. Use to stress-test plans/<feature-slug>/plan.md and progress.md for missing decisions, monolithic nodes, unsafe parallelism, weak RGR tests, missing gates, shared-state collisions, and unverifiable completion before workers launch.
---

# Feature Plan Grill

## Purpose

Challenge the canonical feature graph before code is written. This stage is adversarial about the plan, not the user.

## Workflow

1. Read `plans/<feature-slug>/plan.md`, `progress.md`, and `decisions.md`.
2. Inspect the relevant codebase surface; do not ask questions the repo can answer.
3. Review the plan across:
   - completeness against the feature brief
   - node size and behavior clarity
   - dependency graph correctness
   - parallel safety and write boundaries
   - risk tiers and unsafe outcomes
   - RED/GREEN/REFACTOR strength
   - repo/browser/boundary/migration gates
   - final proof and behavior preservation confidence
4. Apply repo conventions, standard engineering defaults, and strong UX/UI/product-taste defaults before asking anything.
5. Ask focused plan-changing questions in rounds only when a user decision could change product intent, brand strategy, specific business logic, scope, safety, or launch risk.
6. After each answer, repeat the loop: infer newly clear defaults, revise the plan, then ask only the remaining material question.
7. Write `plans/<feature-slug>/grill-review.md`.
8. Update `plan.md` and `progress.md` only after decisions are resolved or safe assumptions are recorded.

## Verdicts

- `PASS`: ready for worker launch.
- `PASS WITH RISKS`: usable, with non-critical risks recorded.
- `BLOCKED`: missing decisions or prerequisites prevent safe launch.
- `FAIL`: graph is unsafe, too broad, unverifiable, or likely to cause shared-state collisions.

## Rules

- Prefer concrete plan edits over vague warnings.
- Do not ask the user to confirm routine technical, UX, UI, or product-taste defaults that the repo, framework, standard practice, or strong senior-engineer judgment can answer.
- Do not let workers start on unresolved product decisions.
- Do not accept parallel groups that share write files, migrations, package locks, test DBs, deploys, or git state.
- Do not mark a plan ready if progress can be marked done without evidence.
- In `grill-review.md`, summarize both user decisions and defaults applied so the user can quickly review what was decided for them.
