---
name: code-review
description: Harsh unified code review workflow for PRs, current diffs, changed files, focused repo areas, or implementation plans. Use when the user asks for code review, review this branch, audit current changes, find issues, compare reviewers, run a normal or strict review, assess merge safety, decide whether code is ready, or demand thermo-level maintainability scrutiny without invoking a separate thermo skill.
---

# Code Review

## Overview

Run a findings-first code review that combines correctness, security, data safety,
tests, behavior preservation, and extremely strict structural maintainability.
Default to read-only review unless the user explicitly asks for fixes, commits,
deploys, or shipping.

This skill replaces the need for a separate thermo-nuclear review. Every review
must include the harsh structural lens by default. The job is not to produce a
long backlog or a polite list of nits. The job is to identify the highest-value
confirmed issues, explain why they matter, and give a safe fix and verification
path.

Do not approve code merely because behavior appears correct. If the implementation
works but makes the codebase harder to reason about, call that out directly.

## Mode Selection

Infer the mode from the user request and repo evidence:

- `quick`: current diff or named files, concise findings only.
- `full`: broader repo/PR review with parallel lanes and a ranked plan.
- `one`: return only the single strongest confirmed issue.
- `strict`: normal review plus maximum structural pressure.
- `launch`: use `$launch-critical-sweep` when the real question is go-live safety.
- `refactor-safe`: use `$tdd-deep` when the task is behavior-preserving refactor.
- `ripple`: use `$bug-ripple` when one bug suggests sibling bugs.
- `ship`: use `$cap` when the user asks to verify, commit, push, or ship.

Do not route strict maintainability review to another skill. `$code-review` owns
that standard. If the user asks for a "thermo", "thermo-nuclear", "harsh",
"brutal", "code-judo", "spaghetti", or "1k-line" review, run this skill in
`strict` mode and apply the structural standards below.

## Preflight

Start from the real repo state:

1. Check `pwd`, `git status --short --branch`, and a narrow file tree.
2. Determine scope:
   - current branch diff when in a git repo and no scope is given
   - named files/directories when provided
   - current working tree when the user says current changes
   - plan/doc artifacts when reviewing an implementation plan
3. Read local instructions, relevant docs, manifests, configs, changed files,
   nearby tests, schemas/migrations, route maps, and public contracts as needed.
4. Exclude secrets, `.env*` values, generated output, dependencies, and private
   credential sections from broad reads.
5. For framework, SDK, provider, browser, payment, auth, or cloud behavior that
   may have changed, verify against current primary/official docs before treating
   the claim as confirmed.

If the workspace is not a git repo, say so and review the provided files/artifacts
directly.

## Risk Tier

Classify the review target before ranking findings:

- Tier 1: money, auth, ownership, data loss, destructive writes, accepted records,
  migrations, webhooks, state transitions, customer-visible records.
- Tier 2: external integrations, queues, background jobs, admin workflows,
  deployment/env behavior, shared domain services.
- Tier 3: low-risk UI display, copy, simple filters, simple local logic.

Tier 1 requires stronger evidence, stricter blocking calls, tests or runtime proof,
and explicit preserved-behavior reasoning. For non-destructive local/test
migrations needed to verify a Tier 1 path, run them when safe and available.

## Review Lanes

Use the smallest set of lanes that fits the scope. For non-trivial reviews, run
independent lanes in parallel when tools and active policy allow it; otherwise run
them locally as separate passes.

1. Correctness and runtime behavior
   - broken logic, edge cases, async ordering, stale state, error handling
   - API/route/server/client boundary failures
   - regression against previous intended behavior

2. Security, auth, ownership, and privacy
   - missing auth/role/tenant checks
   - trusted client input
   - insecure tokens, links, downloads, storage, or data exposure
   - secret leakage in code, logs, tests, or docs

3. Money, state, data, migrations, and integrations
   - double charge, missed charge, wrong amount, fulfillment mismatch
   - illegal state transitions, stale writes, non-atomic partial updates
   - webhook signature/idempotency/retry gaps
   - unsafe migrations, schema drift, RLS/policy mismatch, queue/cron drift

4. Tests and verification gaps
   - missing regression tests for changed behavior
   - weak mocks or snapshots that do not prove the real boundary
   - test/prod fixture gaps
   - missing browser/runtime/provider proof for user-visible or integration paths

5. Structural maintainability
   - file crossing or sprawling past 1000 lines without strong reason
   - spaghetti growth from scattered conditionals and special cases
   - feature logic leaking into shared/general paths
   - thin wrappers, identity abstractions, magic generic handling
   - casts, `any`, `unknown`, optionality, or loose ad-hoc shapes obscuring the invariant
   - duplicated canonical helpers or logic living in the wrong layer
   - missed simplification that could delete whole branches, layers, modes, or concepts

## Structural Standards

Apply these standards to every meaningful review, not only to explicitly strict
reviews.

### 1. Be ambitious about structural simplification

- Do not stop at "this could be a bit cleaner."
- Look for code-judo moves: restructurings that preserve behavior while making
  the implementation dramatically simpler, smaller, more direct, and more
  inevitable.
- Prefer deleting whole branches, helper layers, modes, flags, or concepts over
  polishing them.
- If behavior can stay the same while the structure becomes meaningfully cleaner,
  push for the cleaner version.
- Do not rubber-stamp an implementation that works but leaves the codebase messier.

### 2. Treat 1000-line file growth as a presumptive blocker

- Do not let a PR push a file from under 1000 lines to over 1000 lines without a
  very strong structural reason.
- Prefer extracting helpers, subcomponents, services, modules, or local
  abstractions before accepting file sprawl.
- If the diff crosses that threshold, explicitly ask whether the code should be
  decomposed first.
- Only waive this when the file has a compelling ownership reason and remains
  clearly organized.

### 3. Reject spaghetti growth

- Be highly suspicious of new ad-hoc conditionals, scattered special cases, or
  one-off branches inserted into unrelated flows.
- Treat "weird if statements in random places" as a design problem, not a style
  nit.
- Prefer pushing complexity into a dedicated model, helper, state machine, policy
  object, module, or boundary instead of tangling an existing path.
- Call out changes that make the surrounding code harder to reason about, even if
  they technically work.

### 4. Prefer direct, boring, maintainable code

- Treat brittle, ad-hoc, magical, or overly generic behavior as a quality problem.
- Be skeptical of generic mechanisms that hide simple data-shape assumptions.
- Flag thin abstractions, identity wrappers, pass-through helpers, or indirection
  layers that do not buy clarity.
- Prefer a direct flow over a clever abstraction when the abstraction does not
  remove real complexity.

### 5. Push hard on type and boundary cleanliness

- Question unnecessary optionality, `unknown`, `any`, cast-heavy code, and silent
  fallbacks when a clearer invariant or boundary should exist.
- Prefer explicit typed models, shared contracts, schemas, or discriminated
  shapes over loosely-shaped ad-hoc objects.
- If a branch relies on fallback behavior to paper over an unclear invariant, ask
  whether the boundary should be made explicit instead.

### 6. Keep logic in the canonical layer

- Call out feature logic leaking into shared paths, UI-specific logic leaking into
  services, or implementation details leaking through APIs.
- Prefer existing canonical utilities/helpers over bespoke one-offs.
- Push code toward the package, service, or module that already owns the concept
  instead of normalizing architectural drift.

### 7. Treat avoidable orchestration complexity as a design smell

- If independent work is serialized for no good reason, ask whether the flow can
  be parallelized or simplified.
- If related updates can leave state half-applied, push for a more atomic
  structure.
- Do not over-index on micro-optimizations, but do flag orchestration that makes
  correctness and recovery harder to reason about.

## Primary Review Questions

For every meaningful change, ask:

- Is there a code-judo move that would make this dramatically simpler?
- Can this change be reframed so fewer concepts, branches, helpers, flags, or
  layers are needed?
- Does this improve or worsen the local architecture?
- Did the diff add branching complexity where a better model or abstraction should
  exist?
- Did a previously cohesive module become more coupled, more stateful, or harder
  to scan?
- Is this logic living in the right file, package, service, and layer?
- Did this change enlarge a file or component past a healthy size boundary?
- Are repeated conditionals signaling a missing model, helper, or dispatcher?
- Is the implementation direct and legible, or does it rely on special cases and
  incidental control flow?
- Is this abstraction earning its keep, or is it just a wrapper?
- Did the diff introduce casts, optionality, ad-hoc object shapes, or silent
  fallback that obscure the real invariant?
- Is this orchestration more sequential or less atomic than it needs to be?
- Does the test coverage prove the real boundary, or only a mocked happy path?
- Could this fail for auth, ownership, money, state, migration, webhook, or
  customer-visible data reasons?

## What To Flag Aggressively

Escalate findings when you see:

- A complicated implementation where a cleaner reframing could delete whole
  categories of complexity.
- Refactors that move code around but fail to reduce the number of concepts a
  reader must hold in their head.
- A file crossing 1000 lines due to the PR, especially if the new code could be
  split out.
- New conditionals bolted onto unrelated code paths.
- One-off booleans, nullable modes, optional flags, or special cases that
  complicate existing control flow.
- Feature-specific logic leaking into general-purpose modules.
- Generic "magic" handling that hides simple structure and makes the code harder
  to reason about.
- Thin wrappers or identity abstractions that add indirection without simplifying
  anything.
- Unnecessary casts, `any`, `unknown`, or optional params that muddy the real
  contract.
- Copy-pasted logic instead of canonical helpers or focused extraction.
- Narrow edge-case handling implemented in the middle of an already busy function.
- Refactors that technically pass tests but make the code less modular or less
  readable.
- "Temporary" branching that is likely to become permanent debt.
- Bespoke helpers where the codebase already has a canonical utility for the job.
- Logic added in the wrong layer/package when there is a clear canonical home.
- Sequential async flow where obviously independent work could stay simpler with
  parallel execution.
- Partial-update logic that leaves state less atomic than necessary.
- Tests that mock away the boundary where the regression is likely to happen.

## Preferred Remedies

When you identify a problem, prefer suggestions like:

- Delete a whole layer of indirection rather than polishing it.
- Reframe the state model so conditionals disappear instead of getting
  centralized.
- Change the ownership boundary so the feature becomes a natural extension of an
  existing abstraction.
- Turn special-case logic into a simpler default flow with fewer exceptions.
- Extract a helper, pure function, component, service, or module with a real
  ownership boundary.
- Split a large file into smaller focused modules.
- Move feature-specific logic behind a dedicated abstraction.
- Replace condition chains with a typed model, explicit dispatcher, or state
  machine.
- Separate orchestration from business logic.
- Collapse duplicate branches into a single clearer flow.
- Delete wrappers that do not meaningfully clarify the API.
- Reuse the existing canonical helper instead of introducing a near-duplicate.
- Make type boundaries more explicit so control flow gets simpler.
- Move the logic to the package/module/layer that already owns the concept.
- Parallelize independent work when that also simplifies orchestration.
- Restructure related updates into a more atomic flow when partial state would be
  harder to reason about.
- Add regression tests at the real boundary rather than only asserting mocked
  internals.

Do not be satisfied with "maybe rename this" feedback when the real issue is
structural. Do not be satisfied with a merely cleaner version of the same messy
idea if there is a plausible path to a much simpler idea.

## Evidence Bar

Only report findings that are confirmed or strongly evidenced. A finding needs:

- specific file/line, hunk, runtime, test, schema, or documentation evidence
- a concrete failure mode or maintainability regression
- user, operator, data, security, money, deploy, or future-maintenance impact
- a focused fix direction
- the verification needed to prove the fix

Do not pad with low-value style nits. Do not invent a finding to satisfy the
shape. Label `Hypothesis` when the evidence is incomplete and keep hypotheses out
of blocker lists unless verification is cheap and important.

For structural findings, the concrete failure mode may be future-maintenance
impact: more branches to reason about, unclear invariants, wrong ownership,
larger blast radius, or avoidable coupling. Still ground it in specific code.

## Ranking

Rank by this order unless the user requested a specific lens:

1. P0/P1 correctness, security, money, auth, data loss, destructive action,
   migration, or launch-blocking workflow failures.
2. High-likelihood user-visible or operational regressions.
3. Missing invariant/ownership/state protections around Tier 1 behavior.
4. Structural regressions that make the codebase materially harder to reason
   about.
5. Missed opportunities for dramatic simplification where the simpler structure
   is visible and materially safer.
6. Test gaps that hide a realistic serious regression.
7. Performance, observability, DX, and maintainability concerns.

For `one` mode, return only the strongest confirmed issue. For `full` mode, keep
the list high-signal and deduplicated.

## Approval Bar

Do not approve merely because behavior seems correct. The bar for approval is:

- no confirmed correctness, security, ownership, money, data, migration, webhook,
  or launch-safety blocker
- no clear structural regression
- no obvious missed opportunity to make the implementation dramatically simpler
  when such a path is visible
- no unjustified file-size explosion
- no obvious spaghetti growth from special-case branching
- no hacky or magical abstraction that makes the code harder to reason about
- no unnecessary wrapper/cast/optionality churn obscuring the real design
- no clear architecture-boundary leak or avoidable canonical-helper duplication
- no missed opportunity for an obvious decomposition that would materially improve
  maintainability
- no missing verification for a realistic serious regression

Treat these as presumptive blockers unless the author can justify them clearly:

- the PR preserves a lot of incidental complexity when there is a plausible
  code-judo move that would delete it
- the PR pushes a file from below 1000 lines to above 1000 lines
- the PR adds ad-hoc branching that makes an existing flow more tangled
- the PR solves a local problem by scattering feature checks across shared code
- the PR adds an unnecessary abstraction, wrapper, or cast-heavy contract that
  makes the design more indirect
- the PR duplicates an existing helper or puts logic in the wrong layer when there
  is a clear canonical home
- the PR lacks tests or runtime proof for Tier 1 behavior

If those conditions are not met, leave explicit, actionable feedback and push for
a cleaner decomposition.

## Specialist Routing

Keep only genuinely different workflows standalone:

- Use `$launch-critical-sweep` for go-live, release readiness, catastrophic-risk,
  or "is this safe to launch?" questions.
- Use `$tdd-deep` when the user wants behavior-preserving refactor/cleanup with
  characterization tests and implementation.
- Use `$bug-ripple` after diagnosing one concrete bug when similar sibling bugs
  may exist.
- Use `$safe-feature-slice` as the default next step after actionable review
  findings when the user wants fixes, hardening, or implementation. It can plan
  first for broad/multi-finding work and then execute eligible slices.
- Use `$cap` when the user asks to verify, commit, push, deploy, or finish the
  branch.

Do not route to a separate thermo-nuclear skill. The harsh structural review bar
lives here.

When routing to a non-review workflow, explain the reason in one line and continue
with the specialist only if the current request clearly matches it.

## Subagent Pattern

Use subagents only when available and allowed by the active environment/user
instructions. Keep the critical path local and delegate independent lanes.

Good lanes to delegate:

- correctness/runtime
- auth/ownership/security
- money/state/webhooks/migrations
- tests/verification gaps
- structural maintainability and code-judo opportunities
- skeptical dedupe/false-positive pass

Brief each agent with role, exact scope, read/write boundary, files or artifacts
to inspect, evidence standard, and concise report format. Review is read-only by
default, so agents should not edit files unless the user explicitly requested
implementation and the write sets are disjoint.

## Output

Lead with findings. Use this shape:

```markdown
Findings

- [Severity] `path:line` Title
  Why it matters:
  Evidence:
  Fix direction:
  Verification:

Open Questions / Assumptions

Summary

Verdict: PASS | PASS WITH RISKS | FAIL | BLOCKED | NO MATERIAL FINDINGS
Suggested next step:
Behavior preservation confidence: 0-100, with a short evidence basis
Structural quality confidence: 0-100, with a short evidence basis
```

Severity labels:

- `BLOCKER`: should not merge/launch as-is.
- `MAJOR`: should fix before merge unless consciously accepted.
- `MODERATE`: real issue, but can be scheduled if risk is understood.
- `MINOR`: include only when no higher-value findings exist.

For review-only requests, do not edit files. For implementation requests, finish
the review judgment first, then move into the appropriate fix workflow.

When there are actionable findings, end with a suggested next step:

- `Use $safe-feature-slice to fix [specific issue]` for one narrow fix or
  hardening task.
- `Use $safe-feature-slice to create/update a slice plan for [scope] and execute
  the first eligible slice` when there are multiple related findings or broad
  work.
- `Use $launch-critical-sweep` when the real decision is go-live safety.
- `Use $tdd-deep` when the next move is behavior-preserving refactor with
  characterization tests.
- `Use $bug-ripple` when one confirmed bug implies likely sibling bugs.
- `Use $cap` when the code is reviewed and the user asks to verify, commit, push,
  or ship.
- `No action` when there are no material findings.

## Behavior Preservation

For any review of changed behavior, explicitly separate:

- previous intended behaviors that should remain true
- intentional behavior changes from the request
- possible accidental drift
- evidence used: tests, source, runtime/browser checks, docs, schemas, provider
  truth, or current official documentation

Do not give high confidence merely because the new path works. Confidence must
also account for unintended regressions and avoidable complexity that makes future
behavior harder to preserve.

## Review Tone

Be direct, serious, and demanding about quality. Do not be rude, but do not soften
major maintainability issues into mild suggestions. If the code is making the
codebase messier, say so clearly. If the implementation missed an opportunity for
dramatic simplification, say that clearly too.

Useful phrasing:

- `this pushes the file past 1000 lines. can we decompose this first?`
- `this adds another special-case branch into an already busy flow. can we move this behind its own abstraction?`
- `this works, but it makes the surrounding code harder to reason about. keep the behavior and restructure the implementation.`
- `this feels like feature logic leaking into a shared path. isolate it.`
- `this abstraction seems unnecessary. keep the direct flow unless the wrapper removes real complexity.`
- `why does this need a cast or optional here? make the boundary explicit instead.`
- `this looks like a bespoke helper for something the codebase already owns elsewhere. reuse the canonical one.`
- `there is a code-judo move here that makes this much simpler. reframe this so these branches disappear.`
- `this refactor moves complexity around, but does not delete it. make the model itself simpler.`
