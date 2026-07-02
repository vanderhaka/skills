# Plan-Only Mode

This reference carries the planning-only discipline absorbed from the former standalone `thin-slice-plan` skill. Load it whenever the request classifies as `needs-plan` and the user wants planning output only (no implementation), or when reviewing an existing plan artifact.

For the working brief format, risk tier definitions, interview gate style, subagent reasoning budget (`gpt-5.5`, medium reasoning), hard rules, and the confidence-scoring bands, use the main `SKILL.md` — they are shared and not repeated here. This file covers what is unique to producing and maintaining the plan artifact itself.

## Purpose

Turn broad work into a concrete, progress-tracked plan made of small, safe, independently verifiable slices. In plan-only mode this skill plans only. It does not implement code, run migrations, deploy, or mark work complete without evidence. It decomposes into a dependency-ordered thin-slice plan with progress tracking, then stops.

## When To Use Plan-Only Mode

- The user explicitly asks to plan, slice, sequence, or stop before implementation.
- The user asks to review an existing plan without implementing it.
- A `needs-plan` classification applies and the user wants the plan only, not the execution loop.

Do not use plan-only mode for tiny one-file fixes where the next safe implementation step is already obvious — that is `single-slice` in the main skill.

## Required Output Artifact

Create or update:

```text
plans/<feature-slug>/slice-plan.md
```

Use a stable slug based on the feature or fix. If the repo already has a relevant `plans/<slug>/` folder, update that folder instead of creating a duplicate.

The plan must be resumable. A future agent should be able to read only this file plus the referenced source files and know: what is in scope, what is out of scope, what has been proven, what is blocked, which slice is next, and which checks are required before progress can move.

## Initial Read (Plan-Only)

Before writing or updating the plan, read only the relevant evidence needed to plan safely:

- user request, feature brief, issue, PRD, handoff, or existing plan
- nearby domain/service code and shared contracts
- schema, migrations, constraints, RLS, policies, and seed/fixture shape
- API routes, server actions, jobs, webhooks, queues, and external adapters
- auth, ownership, permission, audit, and state-transition code
- UI routes and workflow entry points
- existing tests and verification scripts

Prefer bounded reads. Do not broad-read secret-bearing files. For env or deployment facts, use redacted presence checks unless the user explicitly requests values.

If a repo has canonical planning/status files, use them as the source of truth instead of inventing a parallel plan.

If the invariant cannot be stated, pause and ask the smallest set of questions needed to make the plan safe.

## Audit-Driven Planning

A common input to plan-only mode is an audit artifact — a gap report, persona review, security scan, lighthouse pass, or any document listing many findings. Audits are not plans. Treat them as input that must be triaged before slicing. This goes beyond the main skill's per-finding reproduction step (see `Audit-Driven Slice Inputs` in `SKILL.md`) by classifying and sequencing the surviving findings into slices.

For an audit-driven plan, add a triage pass before decomposition:

1. Re-verify each finding against the current code. Audits go stale; the next commit invalidates a portion of every audit. Drop findings that no longer reproduce. Note the verification method per finding.
2. Classify what each finding needs:
   - `code-only` — implementable without product or content input; eligible to slice now.
   - `needs-product-decision` — blocked by a small set of questions for the user; surface in `Blocked decisions`.
   - `needs-content` — blocked on a human (founder, copywriter, designer) producing real content; create a parallel content brief, do not invent copy.
   - `false-alarm` — finding does not reproduce or is an artifact of the audit tool itself; record the verification and drop.
3. For audits that captured screenshots, watch for screenshot-only artifacts: `position: fixed` elements rendered mid-page in `fullPage` captures, dev-only indicators (Next.js build badge, Vercel toolbar), scroll-reveal animation pre-states, browser-extension overlays. These are not bugs real users see.
4. Slice only the verified, actionable findings. Surface the rest in the plan's `Blocked decisions` and `Out of scope` sections so future agents do not re-scope them.

A useful follow-up pattern is **lens-per-pass**: each gap-finding lens (render correctness via crawler, UX via persona review, security via deep audit, a11y via WCAG pass, scope drift via doc diff) produces its own audit. Plan one lens at a time. Do not bundle findings from different lenses into one slice plan — they have different acceptance signals, different specialist evidence, and benefit from independent triage.

## Decomposition Rules

A valid thin slice has:

- one primary actor or system trigger
- one main action or observable behavior
- one protected invariant
- explicit intentional behaviour changes, if any
- previous intended behaviours that must remain true
- one acceptance signal
- one expected verification path
- a small expected file/module surface
- clear dependencies on prior slices
- a clear stop condition

Split a slice when it combines:

- schema plus multiple behaviors
- backend rule plus unrelated UI polish
- two different actors
- two different state transitions
- sync/webhook behavior plus manual admin behavior
- migration/backfill plus user-facing flow
- refactor plus feature behavior
- setup plumbing plus domain rule
- acceptance path plus unrelated nice-to-have

Do not create slices that are only file chores unless the chore is a real enabling dependency, such as adding a shared contract, migration, fixture harness, or test helper needed by later behavior.

## Dependency Graph

Build the plan from a dependency graph before writing the sequence.

Classify each candidate step as:

- `blocking`: later work depends on it
- `parallel-safe`: can be delegated independently with disjoint files/state
- `single-threaded`: touches shared mutable state such as git, lockfiles, migrations, test databases, deploys, or shared generated files
- `decision-needed`: blocked by product/business/ops ambiguity
- `unsafe-live`: cannot be executed against live data without explicit approval

Never parallelize:

- git checkout, merge, rebase, push, or release tagging
- package-lock or dependency graph edits
- migrations against the same database
- tests sharing one mutable database
- deploys or promotions
- multiple agents writing the same files
- broad refactors across shared contracts

For every implementation slice, list the intended independent worker ownership. Default worker config is model `gpt-5.5`, medium reasoning, fastest available medium profile when the runtime exposes speed/profile controls (same default as the main skill's Subagent Orchestration Gate). For every `parallel-safe` slice, list write boundaries and evidence expected from a specialist agent.

## Plan File Template

Use this structure for `plans/<feature-slug>/slice-plan.md`:

```markdown
# [Feature/Fix Name] Thin Slice Plan

Status: PLANNING | READY | IN_PROGRESS | BLOCKED | COMPLETE | RETIRED
Last updated: YYYY-MM-DD
Owner: Codex

## Working Brief

- Feature or fix:
- Primary actors:
- Core invariant:
- Previous intended behaviours:
- Unsafe outcomes:
- Current evidence:
- Assumptions:
- Out of scope:

## Risk Classification

- Overall tier:
- Why:
- Live-data risk:
- Migration risk:
- External-contract risk:

## Dependency Graph

| Node | Depends on | Parallel? | Shared-state risk | Notes |
| --- | --- | --- | --- | --- |
| S1 | None | No | [risk] | [notes] |

## Audit Triage (omit when not audit-driven)

Source artifact: [path/URL of audit report]
Audit date: YYYY-MM-DD
Findings reviewed: N

| Finding | Verified against current code? | Disposition | Reason |
| --- | --- | --- | --- |
| F1 | yes — curled route, error string in body | sliced as S2 | code-only, no product call needed |
| F2 | no — not reproducible | dropped | already fixed in earlier commit |
| F3 | yes | blocked | needs Chris's copy for /about |
| F4 | n/a | dropped (false alarm) | screenshot artifact: dev-only indicator |

## Progress

| Slice | Status | Tier | Owner | Evidence | Next gate |
| --- | --- | --- | --- | --- | --- |
| S1 | pending | T1 | unassigned | none | failing test |

Allowed statuses: `pending`, `in_progress`, `blocked`, `done`, `skipped`.

## Slices

### S1 - [Short behavior name]

Status: pending
Tier: T1/T2/T3
Type: schema | backend | frontend | integration | verification | docs | ops
Actor/trigger:
Action:
Invariant protected:
Intentional behaviour changes:
Previous intended behaviours preserved:
Unsafe outcomes:
Dependencies:
Expected files:
Write boundaries:
Tests required:
Runtime verification:
Migration/backfill notes:
External docs needed:
Acceptance criteria:
Exit evidence:
Parallelization:
Blocked on:

## Verification Gates

- Automated checks:
- Runtime checks:
- Migration checks:
- Security/auth checks:
- Observability/audit checks:

## Update Rules

- Move only one slice to `in_progress` per worker unless the plan explicitly allows parallel work.
- Mark `done` only after exit evidence is recorded.
- Mark `blocked` with the exact missing decision, dependency, or failing check.
- Add newly discovered work as a new slice or follow-up; do not silently expand an active slice.
- Keep rejected or skipped work visible with the reason.
```

## Slice Detail Requirements

Each slice must say enough for `safe-feature-slice` build mode to execute it without re-planning the whole feature. The `S1` slice template above carries most of this; every implementation slice must also make these explicit:

- Allowed scope: the expected files/folders/modules the slice may touch
- Integration risk: what this slice could break
- Tests first: the failing or characterization test to write or locate before code
- Unsafe cases: wrong user, wrong org, stale version, duplicate request, invalid transition, etc.
- Runtime verification: browser/computer-use/manual proof required, or not required with reason
- Exit evidence: commands, screenshots, logs, DB checks, or code references required before done

## Progress Discipline

The plan is a control surface, not a static document.

When creating the plan:

- all slices start as `pending` unless evidence proves they are already done
- already-done slices must cite evidence, not memory
- blocked slices must name the blocker
- the next recommended slice must be explicit

When executing later (in build mode, outside plan-only mode):

- update the `Progress` table before starting a slice if work begins
- update it again after verification
- record exact commands or runtime evidence in `Exit evidence`
- do not mark `COMPLETE` until every required slice is `done` or explicitly `skipped`
- if tests reveal a missing prerequisite, create a new earlier slice and re-sequence

## Verification Planning

For each slice, specify the minimum proof needed:

- unit or domain tests for core rules
- regression checks for previous intended behaviours that should remain true
- integration tests for real boundaries
- RLS/policy tests for ownership and org/customer boundaries
- concurrency or idempotency tests for duplicate requests, retries, webhooks, and race conditions
- migration checks for schema changes
- browser verification for user-visible web workflows
- Computer Use verification for desktop, OS dialogs, native windows, file pickers, or cross-app flows
- current official docs or Context7 checks for third-party APIs, SDKs, frameworks, cloud services, or standards where behavior may have changed

If runtime verification is required but cannot be performed safely, mark the affected slice `blocked` or give it a `PASS WITH RISKS` execution gate for the later implementing work. The plan itself should not claim the feature is safe.

## Migrations And Data

During planning:

- identify whether migrations, backfills, seed changes, type generation, or fixture updates are required
- separate schema creation from behavior changes unless the repo pattern proves they should land together
- label migrations as destructive, non-destructive, or unknown
- mark destructive or live-data mutations as `decision-needed`
- include non-destructive migration execution as an implementation gate when project rules require it

Do not execute migrations from plan-only mode. A read-only planning-time migration check (dry run or diff) is allowed only when the user explicitly asks for it. Actual migration execution belongs to build mode or the cap/deploy flow.

## Subagent Plan

If the implementation will benefit from agents, include a `Subagent Plan` section in the plan artifact:

```markdown
## Subagent Plan

| Agent | Role | Slice(s) | Model/reasoning | Read scope | Write scope | Must not touch | Evidence required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Auth/RLS reviewer | S2 | gpt-5.5 / medium / fastest medium profile | schema + policies | none | app code | findings with file:line |
```

Rules:

- Keep the main chat on the critical path.
- Plan for each implementation slice to be handled by its own independent worker agent when agent use is available and safe.
- Continue through all required slices by default during execution; stop only for blockers, unsafe shared state, or explicit user limits.
- Delegate only independent work that reduces risk or wall-clock time.
- Give each agent a specialist role and disjoint write boundaries.
- Tell code-writing agents they are not alone in the codebase, must not revert others' work, and must adapt to nearby changes.
- Require current official docs or Context7 for third-party/framework work where current behavior matters.
- Do not delegate unresolved product decisions.

## Existing Plan Review Mode

When asked to review an existing plan:

- check whether every slice has actor, action, invariant, unsafe outcomes, dependencies, verification, and exit evidence
- check whether every implementation slice separates intentional behaviour changes from previous intended behaviours that should remain true
- identify monolithic slices that should be split
- identify missing dependency gates and shared-state risks
- identify places where progress could be marked done without proof
- recommend the smallest edits that make the plan executable

Use `PASS`, `PASS WITH RISKS`, `BLOCKED`, or `FAIL` for the plan itself:

- `PASS`: ready for slice-by-slice execution
- `PASS WITH RISKS`: usable but has non-critical gaps
- `BLOCKED`: missing decisions or prerequisites prevent safe execution
- `FAIL`: plan is unsafe, too broad, unverifiable, or likely to cause shared-state collisions

## Plan-Only Final Response

After creating or updating the plan in plan-only mode, respond with this format instead of the main skill's Final Response format:

```text
Summary:
[what plan was created/updated]

Plan artifact:
[path]

Feature invariant:
[core invariant]

Behaviour preservation approach:
[how the plan separates intentional changes from older intended behaviours that should remain true]

Slice count:
[number and brief grouping]

Next slice:
[exact recommended next slice]

Parallel opportunities:
[what can run concurrently, or none]

Blocked decisions:
[questions or none]

Progress state:
[READY / BLOCKED / etc.]

Files changed or reviewed:
[short list]

Status:
PASS / PASS WITH RISKS / BLOCKED / FAIL

Confidence:
[0-100]% absolute confidence in the plan's executability, with one sentence explaining the evidence and biggest remaining uncertainty. Use the confidence bands in the main SKILL.md.

Commit/push recommendation:
[COMMIT + PUSH / COMMIT ONLY / DO NOT COMMIT / DO NOT PUSH YET], with the reason. For planning-only changes, say whether the plan artifact itself is worth committing now or should wait for missing decisions/evidence.

Next action:
[the single best next action: commit/push the plan, answer a blocker, start the required slice execution loop in build mode, run a missing evidence read, or stop because the user asked for planning only]
```

Do not include optional follow-up implementation when the user asked for planning only. If the user asked to implement the work, hand off into the required slice execution loop (build mode) instead of stopping after the plan.

Do not recommend `COMMIT + PUSH` for a plan when high-risk decisions remain unresolved or the plan is not ready for another agent to execute. Recommend `COMMIT ONLY` when the plan is useful as a checkpoint but execution should wait. Recommend `DO NOT COMMIT` when the plan is speculative, stale, or likely to mislead future work.

## The Hard Wall

In plan-only mode this skill never implements code, never runs migrations, never deploys, and never marks a slice `done` without evidence supplied by the user or an already-completed run. It decomposes into a dependency-ordered thin-slice plan with progress tracking and stops. Handing off into execution requires an explicit user request to build, at which point control passes to the main `SKILL.md` build mode (or `feature-orchestrator` for whole-feature graph execution).
