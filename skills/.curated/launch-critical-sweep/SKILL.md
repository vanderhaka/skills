---
name: launch-critical-sweep
description: Pre-launch catastrophic-risk audit for finding confirmed P0/P1 launch blockers across auth, ownership, payments, destructive actions, deployment/env, migrations, integrations, webhooks, data loss, and trust-breaking client workflows. Use when the user asks for critical issues before launch, go-live blockers, release readiness, catastrophic client/team risk, or a deep sweep of paths that could instantly break trust. Reports only confirmed launch blockers, not a backlog, and hands each fix to safe-feature-slice.
---

# Launch Critical Sweep

## Goal

Find confirmed launch-blocking issues before a production release or client go-live. This is the heavier sibling of `$one-major-issue`: it sweeps more surfaces, uses stricter risk framing, and may report a small set of catastrophic blockers instead of only one issue.

The output should answer: **Can this launch safely, or is there a confirmed issue that could seriously hurt customers, the client, the project owner, revenue, data, security, or operational trust?**

Use this skill when the user asks for:

- `Use $launch-critical-sweep`
- `critical issues before launch`
- `deep launch blocker sweep`
- `what could instantly break trust`
- `catastrophic client/team risk before go-live`
- `is this safe to launch?`

If the user appends extra instruction after the skill call, treat it as binding scope. Examples:

- `Use $launch-critical-sweep on checkout and billing only`
- `Use $launch-critical-sweep read-only, no DB writes`
- `Use $launch-critical-sweep before client handoff; focus data loss and permissions`

## Operating Mode

Default to read-only investigation. Do not edit code, write migrations, change data, reformat files, deploy, or mutate external services unless the user explicitly asks for fixes or launch execution.

Tests, builds, typechecks, lint, local app runs, browser checks, and local migrations are allowed only when they do not mutate shared state or violate the user's constraint. Run migrations only after the target is provably local/test-scoped, non-destructive, and relevant to launch readiness. If the target database, environment, or migration impact is unclear, report the migration check as blocked instead of running it.

Do not ask the user to restate context that can be recovered from repo docs, branch state, deployment config, or memory. If a missing answer could affect money, real customer data, destructive writes, deploy cutover, auth boundaries, or external provider behavior, ask a short blocking question or mark the finding as blocked by that decision.

## Severity Bar

Report only confirmed or very strongly evidenced P0/P1 launch blockers.

A launch blocker must plausibly cause one or more of:

- unauthorized access, tenant/client data leak, ownership bypass, or role escalation
- data loss, irreversible destructive action, duplicate mutation, or broken recovery path
- wrong charge, double charge, missed payment, invoice mismatch, or revenue-impacting checkout failure
- broken customer-critical journey at launch, such as sign-up, login, purchase, booking, submission, quote acceptance, or admin fulfillment
- webhook, queue, cron, sync, or background job behavior that silently corrupts state or leaves users misled
- production deploy/env/migration mismatch that makes the live app fail, use test providers, or write to the wrong system
- missing audit/idempotency/locking around accepted, paid, destructive, or customer-visible records
- legal, privacy, compliance, or contractual exposure that is directly evident in code/config/docs

Do not report:

- generic missing tests
- code style, refactor taste, small UX polish, copy nits, or non-blocking accessibility concerns
- hypothetical risks without a concrete path
- stale audit findings that no longer reproduce
- issues that would annoy users but not break launch trust

If no issue meets this bar, say so plainly.

## Initial Repo Pass

Start from the repo's real shape:

- Check `pwd`, `git status --short --branch`, and the top-level file tree.
- Read launch docs, handoff docs, README, package manifests, framework config, deployment config, route maps, schema/migrations, test setup, and existing plans enough to understand the launch surface.
- Use `rg`/`rg --files` for targeted discovery.
- Exclude `.env*`, secret stores, generated output, build artifacts, dependency folders, and private ops credential sections from broad searches.
- Prefer file-backed behavior evidence over README claims or naming assumptions.

Quickly infer:

```text
Launch target:
[what is being launched]

Primary users:
[customer/client/admin/operator roles]

Critical journeys:
[flows that must not fail at launch]

Trusted records:
[paid, accepted, submitted, destructive, or customer-visible records]

External systems:
[payment, email, storage, auth, CRM, CMS, webhooks, queues, deploy hosts]
```

## Sweep Lanes

For non-trivial repos, inspect these lanes. Use parallel shell reads freely when safe. Use delegated/background agents only when the environment and user instruction permit them; give each lane a specialist brief and ask for the strongest confirmed blocker with file/line evidence.

### 1. Auth, Roles, Ownership, And Tenancy

Look for:

- missing auth checks on API routes, server actions, RPCs, loaders, mutations, admin pages, storage, or downloads
- owner/client/tenant scoping gaps
- role checks that trust client input or UI hiding
- RLS/schema policies that do not match app logic
- impersonation, invite, password reset, token, or session edge cases

### 2. Money, Accepted Records, And State Transitions

Look for:

- checkout/payment/invoice paths that can double-charge, skip payment, or mismatch amounts
- accepted quotes, approved orders, bookings, contracts, or submissions that can be edited unsafely
- missing idempotency for payment/webhook/order creation
- state machines with illegal transitions, race windows, or stale-version writes
- refunds, cancellations, retries, and partial failures that leave contradictory state

### 3. Data Loss, Destructive Actions, And Recovery

Look for:

- delete/archive/bulk actions without ownership, confirmation, soft-delete, audit, or recovery
- migrations that drop/rename/backfill unsafely for existing data
- import/sync jobs that overwrite canonical records
- storage cleanup paths that can delete shared/customer assets
- backup/restore assumptions that are missing from launch docs when destructive changes exist

### 4. Deployment, Environment, And Provider Drift

Look for:

- env vars missing from production, preview, worker, or cron contexts
- test keys, localhost URLs, dev callbacks, disabled auth, or mock providers reachable in production
- build/runtime mismatches, edge/node incompatibility, missing generated clients, stale migrations
- route protection differences between local and deployed hosts
- cron/queue/worker processes not deployed or pointing at wrong URLs

### 5. External Integrations, Webhooks, Queues, And Email

Look for:

- webhook signature verification gaps
- retry/idempotency failures
- queue jobs that can run twice or out of order
- emails that leak data, go to wrong recipients, or falsely confirm failed actions
- provider API behavior where current docs matter; verify against Context7 or current official docs before finalizing

### 6. Critical User Journeys And Trust-Breaking Runtime Paths

Look for launch flows that fail in a way a real user or client would immediately notice:

- login/sign-up/onboarding
- purchase/checkout/payment confirmation
- booking/submission/quote acceptance
- admin fulfillment/reconciliation
- file upload/download or document generation
- client-visible dashboards, status, or notifications

Use browser or end-to-end checks when tests cannot prove the journey.

### 7. Fixture, Mock, And Test-Vs-Production Gaps

Look for:

- tests passing only because of fixtures, mocks, seeded admin users, bypassed auth, fake provider responses, or local-only config
- routes implemented only in demo data while production persistence is missing
- feature flags or TODO stubs that expose unfinished launch-critical behavior

## Output Detail Standard

For every confirmed blocker, give enough detail that the project owner can decide whether to stop launch, brief a client, or hand the issue to a fixer without re-running the whole investigation.

Do not bury the finding in vague severity language. Spell out:

- what exactly is broken
- who or what is affected: customer, client admin, staff, owner, operator, payment provider, email recipient, integration, database table, storage object, or deployment environment
- what data, money, permissions, workflow, reputation, or operational process is at risk
- how the failure happens, step by step, from entry point to unsafe outcome
- why it must be fixed before launch rather than deferred
- what currently prevents or fails to prevent the bad outcome
- what a safe fix needs to guarantee
- what tests, browser flows, migration checks, provider checks, or deploy checks prove the fix

Include direct file/line evidence for claims about behavior. If a claim is an inference from code, label it as `Inference`. If it depends on runtime config, provider state, or missing credentials, label it as `Needs verification`.

Keep the report focused: full detail for confirmed launch blockers, not a broad list of smaller problems.

## Evidence Bar

Every reported blocker needs:

- a concrete unsafe path or failure mode
- file/line anchors for the relevant code/config/docs
- impact phrased in launch terms
- a minimal reproduction, command, browser scenario, trace, or reasoning chain
- a narrow fix direction and `$safe-feature-slice` handoff
- an explicit explanation of affected users, affected records/systems, and why the issue must be fixed before launch

Separate confirmed facts from `Hypothesis`. If the catastrophic part depends on runtime state you cannot inspect, say exactly what is confirmed and what must be verified.

If third-party API/framework behavior is central and may have changed, verify against current official documentation or primary sources before finalizing. Cite the source in the final answer when used.

## Lane Agent Brief

When delegating sweep lanes, give each agent a narrow read-only brief:

```text
You are running one lane of a launch-critical sweep.
Do not edit files, write files, run migrations, deploy, mutate provider state, or print secrets.
Launch target: [product/feature/release]
Critical journeys: [flows]
Lane: [auth/money/data loss/deploy/integrations/runtime/test-vs-prod]
Scope: [files/directories/config/docs]
Return only confirmed or very strongly evidenced P0/P1 blockers with file:line evidence, affected users/records/systems, failure chain, fix direction, required verification, and uncertainty. If none meet the bar, say so.
```

## Ranking And Stopping

Rank candidates by:

- blast radius at launch
- likelihood in real use
- ability to leak, corrupt, lose, double-charge, mis-authorize, falsely confirm, or block a critical journey
- proximity to customer/client workflows
- evidence strength
- fixability before launch

Return:

- `LAUNCH BLOCKED` if one or more confirmed blockers exist.
- `NO CONFIRMED LAUNCH BLOCKER FOUND` if the sweep did not confirm a blocker in the allowed scope.
- `INCONCLUSIVE` if scope, credentials, missing env, blocked checks, or time prevented a responsible verdict.

Report at most three confirmed blockers. If there are more, report the top three and say the rest should wait until those are fixed and re-run. Do not create a general backlog.

## Safe Fix Handoff

Do not start fixing during this skill unless the user explicitly asks for implementation.

For each confirmed blocker, include:

```text
Suggested safe-feature-slice fix:
Use $safe-feature-slice to fix [blocker title].
Invariant: [rule that must remain true].
Unsafe outcome to prevent: [bad state].
Likely scope: [files/modules].
Verification: [focused tests/checks/browser flow].
Extra instruction: [carry over relevant launch-sweep constraint].
```

If multiple blockers exist, each handoff must stay narrow enough to execute independently.

## Final Answer

Use the verdict words from Ranking and Stopping as the first signal:

- `LAUNCH BLOCKED`
- `NO CONFIRMED LAUNCH BLOCKER FOUND`
- `INCONCLUSIVE`

For detailed formatting, load [references/output-templates.md](references/output-templates.md) only when composing the final answer. Keep the answer focused on confirmed launch blockers, explicitly blocked checks, or the most important residual risk. Do not create a general backlog.

## Skill Maintenance

Do not write to files inside the installed skill during normal use. If a run reveals a durable improvement to this workflow, mention it in the final answer as a suggested skill update instead of mutating the skill package.
