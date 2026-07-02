# Feature Plan Grill

## Purpose

Challenge the canonical feature graph before code is written. This stage is adversarial about the plan, not the user.

## Workflow

1. Read `plans/<feature-slug>/plan.md`, `progress.md`, and `decisions.md`. If `plan.md` does not exist, stop and route to `feature-graph-plan` instead of reviewing from memory.
2. Inspect the relevant codebase surface; do not ask questions the repo can answer.
3. Review the plan across:
   - completeness against the feature brief
   - node size and behavior clarity
   - dependency graph correctness
   - parallel safety and write boundaries
   - risk tiers and unsafe outcomes
   - RED/GREEN/REFACTOR strength
   - repo/browser/boundary/migration gates
   - exact fresh evidence required for each gate
   - self-contained worker briefs and return evidence
   - root-cause/debugging expectations for failure nodes
   - final proof and behavior preservation confidence
4. Ask focused plan-changing questions in rounds only when needed.
5. Write `plans/<feature-slug>/grill-review.md` with the findings, required plan edits, and the verdict.
6. Update `plan.md` and `progress.md` only after decisions are resolved or safe assumptions are recorded.

## Verdicts

- `PASS`: ready for worker launch.
- `PASS WITH RISKS`: usable, with non-critical risks recorded.
- `BLOCKED`: missing decisions or prerequisites prevent safe launch.
- `FAIL`: graph is unsafe, too broad, unverifiable, or likely to cause shared-state collisions.

## Rules

- Prefer concrete plan edits over vague warnings.
- Do not let workers start on unresolved product decisions.
- Do not accept parallel groups that share write files, migrations, package locks, test DBs, deploys, or git state.
- Do not mark a plan ready if progress can be marked done without evidence.
- Do not accept vague worker prompts that depend on hidden chat context.
- Do not accept plans that let repeated failures continue as blind retries.
