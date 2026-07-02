---
name: ripple
description: Diagnose one reported bug or one planned business-rule/invariant change, then run a strict, findings-first, read-only ripple sweep with parallel read-only agents when explicitly authorized and available. Bug mode triggers on bug ripple, sibling bugs, what else could break, fix and sweep. Logic mode triggers on logic ripple, business-rule ripple, pricing/tax/GST ripple, entitlement ripple, apply this rule everywhere, find duplicate rule logic, canonicalize. If the trigger is an observed failure, use Bug Mode; if it is an intended rule/invariant change, use Logic Mode.
---

# Ripple

## Purpose

Use this skill when a single trigger — one concrete bug, or one planned business-rule change — is a signal that related failures or inconsistencies exist elsewhere in the codebase. Diagnose the trigger precisely first, then search the same mental-model gap or rule surface for siblings. The default output is a findings-first report and fix menu, not code changes.

Two modes share one engine (intake, read-only contract, blast-radius scoping, parallel lane fanout, evidence bar, verdict vocabulary, report shape, hard stop). They differ only in how the trigger is diagnosed and what the lanes look for.

- **Bug Mode**: the trigger is an observed bug, stack trace, failing test, or "what else could break like this?" Diagnose root cause via reproduce/minimize/hypothesize, then sweep for sibling bugs.
- **Logic Mode**: the trigger is a planned business/domain rule, invariant, pricing/tax/entitlement change, or "apply this everywhere" / "find duplicate rule logic." Map every surface the rule touches, then classify and canonicalize.

**Mode rule**: an observed failure → Bug Mode. An intended rule/invariant change → Logic Mode.

**Ambiguous invocation** ("ripple this"): classify by whether the trigger is an observed failure (Bug Mode) or an intended rule change (Logic Mode) in one sentence; if genuinely unclear from the user's message and repo context, ask one question before proceeding.

The review posture is strict but bounded. Be blunt about confirmed risk, bad invariants, weak tests, and messy structure that makes siblings likely. Do not turn this into a repo-wide maintainability review, and do not pad the report with speculative nits.

## Hard Rules (Both Modes)

1. Read-only until the user explicitly approves fixes. Do not edit files, apply patches, commit, deploy, mutate provider state, run migrations, or write generated artifacts during the ripple review.
2. Do not spawn subagents unless the user explicitly invoked `$ripple`, said "bug ripple" / "logic ripple", asked for a multi-agent sweep, or otherwise clearly authorized delegation. If the runtime or active policy disallows subagents, use the local fallback and say so.
3. Keep the search bounded to the blast radius / rule surface. Do not turn one trigger into a repo-wide audit unless the user asks.
4. Do not print secrets, `.env*` contents, cookies, tokens, customer data, or provider payloads. Use redacted presence checks only when configuration is relevant.
5. Current framework, SDK, API, cloud, payment, browser, tax, legal, accounting, or standards claims need current primary docs, Context7, or official docs before being treated as confirmed.
6. Report confirmed or strongly evidenced findings only. Label hypotheses as hypotheses and keep them out of the primary fix menu unless they are cheap and important to verify.
7. If nothing is found, say that plainly. Never pad the report with style nits, speculative edge cases, or generic best practices.
8. Be demanding about severity and structure. Do not soften data, auth, money, tax, entitlement, destructive-action, or common-path regressions because the fix is awkward. Call out structural causes (unclear ownership, duplicated logic, unsafe casts, scattered branches) when they materially increase risk.
9. Harshness is for evidence and prioritization, not theater. Use direct language, but every hard call must be backed by file/line evidence, a realistic trigger, user impact, and a narrow verification path.

## Phase 0: Intake and Baseline (Both Modes)

Start from the target repo root when possible.

1. Read the user's trigger: bug description, stack trace, failing test, screenshot, PR comment, file reference, or requested business-rule change.
2. Load local instructions that can change behavior expectations: nearest `AGENTS.md`, repo docs, product/pricing/tax notes, test docs, schema notes, and relevant feature plans. Keep reads bounded.
3. Capture a read-only baseline:
   - `git status --short --branch`
   - `rg --files` or a narrow file inventory for the suspected area/rule surface
   - package/test/config names only when needed to understand the stack
4. If the trigger is missing and cannot be inferred, ask one concise question. If it can be inferred from repo evidence, proceed and state the assumption.
5. Determine mode per the mode rule above, then continue into the mode-specific diagnosis phase.

---

## Bug Mode: Diagnosis

Do this yourself before any fanout. The ripple is only as good as the root-cause statement.

### Diagnosis loop

1. Reproduce or identify the tightest available feedback loop:
   - failing test, if one exists
   - local route/action/component reproduction
   - log or stack trace tied to exact code
   - screenshot or browser proof tied to a route/state
   - static read only when runtime reproduction is unavailable
2. Minimize the failure to the smallest actor, trigger, state, and boundary that still explains the user's symptom.
3. Trace the bug to exact file and line evidence. Read the full relevant file, not only the failing line.
4. Identify what the user would see or lose.
5. Identify the mental-model gap, not just the broken statement. Examples: wrong ownership assumption, stale async state, nullable data treated as required, trusted client input, provider event assumed ordered, expanded object assumed present.
6. Rank 2-4 plausible hypotheses before settling on root cause. Test them against code evidence one at a time; do not stack guesses.
7. Instrument only when read-only evidence is insufficient and the user has approved mutation. Otherwise state the missing evidence and the safest way to capture it.
8. Define a prove-it regression test: expected behavior, current wrong behavior, exact assertion shape.
9. Identify the minimal fix, but do not apply it.
10. Check whether tests already cover the intended behavior.
11. Decide whether the original bug is a one-off mistake or a structural signal. Structural signals include scattered special cases, unclear ownership boundaries, loose object shapes, unsafe casts, silent fallbacks, non-atomic state changes, duplicated helpers, and framework/provider assumptions hidden in UI or shared code.

If the same hypothesis or failed diagnostic path repeats twice, stop blind retries. Name the repeated failure, narrow the next evidence needed, and use current primary docs or nearby working code before continuing.

Diagnosis output before fanout:

```markdown
## Diagnosis

Bug: ...
User impact: ...
Root cause: ...
Where: path/to/file.ext:line
Feedback loop: ...
Hypotheses considered: ...
Prove-it regression test: `expect(...).toBe(...)` currently ...
Suggested fix: ...
Existing coverage: covered / missing / unclear
Structural signal: one-off / likely pattern / unclear
Assumptions: ...
```

### Build the Blast Radius

Create `SCOPE_FILES` before ripple analysis. Include only files with a clear relationship to the bug:

- the root-cause file or files
- direct imports, exports, callers, and callees
- same feature directory or route/action/component family
- tests for the affected behavior
- schema, migration, policy, queue, webhook, or config files only when directly implicated
- shared helpers only when the bug depends on their contract

Default bounds:

- Aim for 8 to 30 files for normal app bugs.
- Use directories only when they are small and feature-specific.
- Exclude generated output, build caches, vendored dependencies, logs, broad `.env*` reads, and unrelated worktrees.
- If the blast radius must expand, state why before expanding.

Also create `SEARCH_PATTERNS` from the diagnosed root cause. Examples: missing null or empty handling, repeated unsafe type assertion, unawaited async work, stale closure or missing dependency, ownership/auth check missing, payment/webhook fulfillment before provider proof, non-idempotent mutation, stale cache after mutation, unchecked provider response shape, destructive action without scope guard.

### Bug Mode Lanes

Use as many lanes as make sense for the stack and blast radius. When three or more lanes apply, three agents is the minimum useful fanout; six to nine is appropriate for launch-critical or high-blast-radius bugs. Never pad with irrelevant lanes to reach a count.

1. Same pattern elsewhere: find repeats of the original bug shape.
2. Boundary and data contracts: nulls, empty values, invalid shapes, parsing, serialization.
3. Async and state: races, stale closures, ordering, cancellation, duplicate submits.
4. Auth, ownership, money, and destructive actions: missing tenant/user/payment/state guards.
5. Persistence and migrations: schema drift, constraints, RLS/policies, transaction boundaries.
6. Integrations and provider events: webhooks, retries, idempotency, env/config assumptions.
7. UI/runtime surface: routing, server/client boundaries, form pending states, cache invalidation.
8. Test coverage: missing characterization tests and assertions needed before fixing.
9. Skeptical pass: dedupe, false positives, and whether findings are actually user-impacting.
10. Structural signal pass: only when the original bug suggests architecture or maintainability caused the failure; look for sibling-prone complexity in the scoped blast radius, not broad style issues.

If fewer lanes apply, skip irrelevant lanes and report why.

### Bug Mode Agent Brief Template

Give each agent the same diagnosis and `SCOPE_FILES`, plus one lane-specific focus.

```text
You are a read-only sibling-bug hunter. You are not alone in the codebase.
Do not edit files, write files, run migrations, commit, deploy, or mutate external state.

Diagnosed bug:
- Bug:
- User impact:
- Root cause:
- Where:
- Suggested fix:

Your lane:
- Focus:

Scope:
- Search only these files/directories:

Required method:
1. Read the relevant scoped files before making claims.
2. Search for the diagnosed root-cause pattern and closely related failure modes.
3. Use current primary docs or Context7 for version-specific framework/API claims.
4. Report only realistic bugs with file:line evidence and a prove-it assertion.
5. Be strict about structural causes when they materially increase sibling-bug risk: unclear invariants, wrong ownership layer, duplicated logic, scattered branches, unsafe casts, or non-atomic state transitions.
6. If you find nothing, say "No sibling issues found."

Return:
- Findings, each with severity, file:line, user impact, cause, short snippet or symbol, fix idea, and prove-it assertion.
- Files inspected.
- Checks/docs used.
- Unresolved uncertainty.
```

---

## Logic Mode: Diagnosis

### Rule Contract

Write a working rule contract before any fanout.

```markdown
## Rule Contract

Rule under review: ...
Trigger for this ripple: ...
Applies when: ...
Does not apply when: ...
Inputs: ...
Outputs: ...
Rounding/ordering/state assumptions: ...
Customer-visible surfaces: ...
Persisted records affected: ...
Provider/external contracts affected: ...
Historical/immutable records: ...
Unknowns: ...
```

If the rule cannot be inferred safely from repo context and the user's prompt, ask one concise question. If it can be inferred, proceed and label assumptions.

### Build the Rule Map

Create `RULE_SURFACES` and `SEARCH_PATTERNS` before analysis.

For a pricing/GST/tax change, likely surfaces include:

- quote create, edit, duplicate, accept, expire, and revise flows
- line item calculations, discounts, deposits, shipping, surcharges, markups, commissions, refunds, credits, and voids
- invoice generation, PDFs, emails, payment/session creation, metadata, exports, reports, dashboards, receipts, and audit logs
- stored totals, derived totals, migrations, backfills, fixtures, tests, and seed data
- UI labels that imply tax-inclusive or tax-exclusive totals
- provider integrations such as Stripe, Shopify, Xero, accounting exports, or tax APIs when directly involved

For other rule types, adapt the surfaces:

- entitlements: UI gates, API guards, RLS/policies, downloads, webhooks, background jobs, tests, and billing state
- permissions/ownership: routes, server actions, queries, policies, admin tools, exports, and destructive actions
- state transitions: create/update/delete flows, jobs, retries, webhooks, notifications, audit history, and rollback paths
- validation: create/edit/import/bulk actions, API clients, schemas, forms, database constraints, and tests

Search by meaning, not only names:

- direct names: `gst`, `tax`, `vat`, `subtotal`, `total`, `inclusive`, `exclusive`
- formulas and operators: percent multipliers, rounding, line aggregation, discounts-before-tax, tax-after-discount
- data fields: stored totals, metadata keys, provider payload fields, denormalized snapshots
- user copy: "includes GST", "ex GST", "tax", "fees", "total due"
- tests and fixtures with hardcoded totals
- duplicate helper names or near-identical calculation shapes

### Classify Every Candidate

Every candidate must land in exactly one bucket:

- `Must Fix`: same business rule, current behavior would be wrong if not changed.
- `Probably Same Rule`: likely equivalent, but repo evidence leaves a meaningful uncertainty.
- `Canonicalization Candidate`: duplicate or near-duplicate rule logic should probably call one canonical implementation.
- `Intentionally Different`: similar shape, but a different domain rule or lifecycle stage.
- `Do Not Touch`: false match, display-only usage, historical data, irrelevant math, or unrelated feature.
- `Research Recommended`: equivalence depends on law, accounting, tax, provider, framework, or domain behavior not proven by repo context.

Classification evidence should answer: Why does this look related? What rule does it appear to implement? What user, data, money, auth, entitlement, or operational impact occurs if missed? What makes it safe or unsafe to change? What proof would confirm the classification?

Do not treat text similarity as rule equivalence. Similar math, names, helpers, labels, or fields can represent different domain meanings.

### Factor In / Factor Out

Factor in:

- same rule on different surfaces, roles, routes, jobs, provider events, exports, or customer artifacts
- same lifecycle rule at draft, accepted, invoiced, paid, refunded, credited, voided, or archived states
- UI/server/database/provider mismatches
- tests, fixtures, stories, snapshots, and seed data that encode the old rule
- canonical helpers that should own the invariant
- generated customer-facing artifacts such as PDFs, emails, receipts, downloads, and reports
- partial or duplicate calculations that would drift after the requested change

Factor out unless evidence says otherwise:

- similar math with different domain meaning, such as commission, markup, platform fee, shipping, surcharge, discount, or deposit handling
- display-only formatting that consumes already-computed values without owning the rule
- historical, accepted, paid, audited, or legal records that should remain immutable
- legacy import/backfill scripts not used by current runtime behavior
- analytics approximations that are intentionally non-authoritative
- country, region, customer type, or product category rules that only look equivalent
- tests that intentionally preserve old historical behavior

Danger cases to explicitly inspect when relevant:

- tax-inclusive versus tax-exclusive pricing
- rounding per line versus rounding once at total
- discounts before tax versus after tax
- mixed taxable and non-taxable line items
- partial payments, deposits, refunds, credit notes, write-offs, and voids
- stored totals versus derived totals
- draft mutable records versus accepted immutable records
- payment amount, invoice amount, PDF amount, and email amount disagreeing
- changing a shared helper without checking callers that depend on old behavior

### Research Gate

Use repo evidence first. Recommend external research when equivalence cannot be proven locally and the answer depends on tax, legal, compliance, or accounting treatment; payment provider semantics, invoices, taxes, refunds, deposits, metadata, or webhook behavior; framework, SDK, database, browser, or cloud behavior that may have changed; or industry/domain rules the codebase does not document.

If the user explicitly asked for research, perform it using current primary/official sources and cite them in the final report.

If the user did not ask for research, add a `Research Recommended` section and stop before classifying those items as `Must Fix`:

```markdown
### Research Recommended
| Candidate | Why It Looks Similar | Why Repo Context Is Insufficient | Suggested Research | Decision Needed |
|---|---|---|---|---|
```

Ask, alongside the final report rather than as a separate mid-flow stop:

```text
Do you want external research before I classify these as must-fix, intentionally-different, or probably-same-rule?
```

If research is declined, keep ambiguous items out of `Must Fix` and state the residual risk.

### Logic Mode Lanes

1. Same-rule surfaces: find every route/action/component/job/provider path using the rule.
2. Data and persistence: stored totals, snapshots, migrations, constraints, RLS/policies, fixtures, tests.
3. Customer artifacts: PDFs, emails, exports, reports, receipts, dashboard cards, labels.
4. Provider and integration contracts: payment/accounting/tax/webhook metadata and external docs when requested.
5. Canonicalization: duplicate formulas, helpers, branch chains, and near-identical logic that should share one owner.
6. Skeptic: false positives, intentionally different rules, immutable history, and over-broad scope.
7. Verification: prove-it tests, browser flows, provider checks, migration/backfill proof, and regression risks.

### Logic Mode Agent Brief Template

```text
You are a read-only logic-ripple investigator. You are not alone in the codebase.
Do not edit files, write files, run migrations, commit, deploy, or mutate external state.

Rule contract:
- Rule under review:
- Applies when:
- Does not apply when:
- Known unknowns:

Your lane:
- Focus:

Scope:
- Search only these files/directories/surfaces:

Required method:
1. Read relevant scoped files before making claims.
2. Classify each candidate as Must Fix, Probably Same Rule, Canonicalization Candidate, Intentionally Different, Do Not Touch, or Research Recommended.
3. Use current primary docs or Context7 for version-specific framework/provider claims when needed.
4. Report only candidates with file:line or route/schema/provider evidence.
5. Be strict about money, tax, auth, ownership, entitlements, accepted records, and customer-visible outputs.

Return:
- Candidates by classification, each with file:line, why it is related, why it may differ, risk if missed, proposed action, prove-it test, and confidence.
- Files inspected.
- Docs/checks used.
- Unresolved uncertainties.
```

---

## Fanout Mechanics (Both Modes)

If subagents are available and explicitly authorized, spawn the independent read-only agents in one parallel batch when possible. Use `explorer` agents for codebase questions. Do not assign overlapping write work because this skill is read-only.

When three or more lanes apply, three agents is the minimum useful fanout for that mode's lane list above. If subagents are unavailable, not authorized, or fail, run the lanes locally as separate passes. Label the report as "single-agent fallback" or "partial fanout" and do not invent consensus.

## Evidence Bar (Both Modes)

A finding qualifies for the main report only when it has: file and line (or route/schema/provider) evidence, a concrete user-visible or data-integrity impact, a specific trigger condition, a plausible root cause tied to the original trigger, a prove-it assertion or verification path, and a narrow fix idea.

Keep the bar high and the language plain. A finding is not "maybe cleaner"; it is "this can fail because..." or "this structure hides the same failure mode because...".

Severity:

- **BLOCKER**: should not ship/merge/launch as-is; data loss, unauthorized access, money/tax total wrong, entitlement bypass, destructive/state corruption, accepted customer record wrong, provider fulfillment error, app-wide outage, or launch blocker.
- **MAJOR**: should fix before merge unless consciously accepted; common user/rule path broken, persistent data corruption risk, security boundary weakening, broken payment/auth/integration path, customer-facing artifact disagreement, duplicated rule logic already diverged, or structure that makes a BLOCKER-tier failure hard to reason about.
- **MODERATE**: real issue with a realistic trigger; degraded workflow, missing recovery, brittle boundary, stale fixture/test, or duplicate logic likely to drift/hide regression.

Do not include MINOR/LOW items in the fix menu. Put them in notes only if useful.

Structural/canonicalization findings qualify only when tied to the diagnosed trigger or materially expanding real risk. Examples worth reporting: the same invariant reimplemented in multiple places with one copy already wrong; a shared helper accepting loose shapes or silent fallbacks that mask invalid state; a UI/server/provider boundary relying on casts or ad-hoc branching that can repeat the original failure; a state transition split across branches where partial state creates a sibling issue; feature-specific logic leaked into a shared path bypassing the intended guard; duplicate formulas that should share one canonical owner.

Do not report broad preferences such as naming, formatting, file length, or "could be cleaner" unless they directly hide or reproduce the failure mode, or reduce real rule drift.

## Report (Both Modes)

Deduplicate by root cause/rule, affected behavior, and file range. Track which agents or lanes found each issue. Consensus is a signal, not proof; a single well-evidenced critical finding still matters.

### Bug Mode report shape

```markdown
## Bug Ripple Report

Mode: parallel fanout / partial fanout / single-agent fallback
Agents or lanes completed: ...
Agents or lanes failed/skipped: ...
Verdict: BLOCKED (any BLOCKER finding) / FAIL (MAJOR findings, no BLOCKER) / PASS WITH RISKS (MODERATE findings or residual risk only) / NO SIBLING BUGS FOUND
Hard call: the most important decision from the review in one direct sentence

### Original Bug
- What's broken:
- Why:
- Where:
- Suggested fix:
- Test coverage:
- Structural signal:

### Blast Radius
- Files/directories searched:
- Scope exclusions:

### Confirmed Sibling Bugs
| # | Severity | File:Line | Found By | Issue | Fix |
|---|---|---|---|---|---|

### Structural Risk In The Blast Radius
Only include if it directly increases sibling-bug risk.

### Strong Hypotheses
Only include if important and clearly labeled.

### Missing Tests
- Original bug:
- Sibling bugs:

### Prove-It Tests To Write Before Fixing
- [ ] ...

### Fix Menu
- [ ] 0. Original bug: ...
- [ ] 1. Sibling bug: ...
- [ ] 2. Sibling bug: ...

### Residual Risk
- ...
```

### Logic Mode report shape

```markdown
## Logic Ripple Report

Mode: parallel fanout / partial fanout / single-agent fallback
Lanes completed:
Lanes skipped/failed:
Verdict: BLOCKED (any BLOCKER finding) / FAIL (MAJOR findings, no BLOCKER) / PASS WITH RISKS (MODERATE findings or residual risk only) / NO REQUIRED RIPPLE FOUND
Hard call: one direct sentence on the real scope.

### Rule Contract
- Rule under review:
- Applies when:
- Does not apply when:
- Unknowns:
- Assumptions:

### Required Ripple Fixes
| # | Severity | Area | File:Line | Why Same Rule | Risk If Missed | Proposed Fix | Confidence |
|---|---|---|---|---|---|---|---|

### Probably Same Rule
| Area | File:Line | Why It Looks Same | Why It May Differ | Decision Needed | Confidence |
|---|---|---|---|---|---|

### Canonicalization Opportunities
| # | Current Duplication | Proposed Canonical Owner | Why This Reduces Rule Drift | Confidence |
|---|---|---|---|---|

### Research Recommended
| Candidate | Why It Looks Similar | Why Repo Context Is Insufficient | Suggested Research | Decision Needed |
|---|---|---|---|---|

### Intentionally Different
| Area | File:Line | Why Similar | Why Different |
|---|---|---|---|

### Do Not Touch
| Area | Reason |
|---|---|

### Missing Tests And Proof
- ...

### Proposed Fix Menu
- [ ] 0. ...
- [ ] 1. ...

### Residual Risk
- ...
```

End either report with a hard stop:

```text
Tell me which fixes to apply, for example "fix all", "fix 0 and 2", "research first", or "just the original".
```

## If the User Approves Fixes (Both Modes)

The ripple review is complete. Switch into implementation mode for the selected fixes:

1. Preserve unrelated worktree changes.
2. In Logic Mode, create or update the canonical rule helper/service/model first when the approved fix requires it.
3. Write or update the prove-it test first where practical.
4. Confirm the test fails for the bug/rule gap when safe.
5. Apply the narrow fix(es).
6. Run repo-appropriate checks, browser/UI proof for customer-visible surfaces, provider proof when safe, and non-destructive migrations when relevant.
7. Report intentional behavior changes, preserved intended behavior, evidence, skipped proof, and behavior-preservation confidence from 0 to 100.

If the user says "fix all" after a ripple report, treat that as approval to implement the listed fix menu, not permission to broaden scope beyond it.
