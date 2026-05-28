---
name: code-review
description: Unified code review workflow for PRs, current diffs, changed files, focused repo areas, or implementation plans. Use when the user asks for code review, review this branch, audit current changes, find issues, compare reviewers, run a normal/strict/one-issue review, assess merge safety, or decide whether code is ready. Routes to specialist workflows when the request is really launch readiness, safe refactor, sibling-bug ripple, or cap/ship verification.
---

# Code Review

## Overview

Run a findings-first code review that combines correctness, security, data safety,
tests, and thermo-level maintainability. Default to read-only review unless the
user explicitly asks for fixes, commits, deploys, or shipping.

The job is not to produce a long backlog. The job is to identify the highest-value
confirmed issues, explain why they matter, and give a safe fix/verification path.

## Mode Selection

Infer the mode from the user request and repo evidence:

- `quick`: current diff or named files, concise findings only.
- `full`: broader repo/PR review with parallel lanes and a ranked plan.
- `one`: return only the single strongest confirmed issue.
- `thermo`: strict maintainability/structure pass.
- `launch`: use `$launch-critical-sweep` when the real question is go-live safety.
- `refactor-safe`: use `$tdd-review-deep` when the task is behavior-preserving refactor.
- `ripple`: use `$bug-ripple` when one bug suggests sibling bugs.
- `ship`: use `$cap` when the user asks to verify, commit, push, or ship.

If the user names a specialist skill, use that specialist directly. If the user
asks for a normal code review and the scope also has structural risk, include the
thermo lens inside this skill instead of requiring a second invocation.

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
   may have changed, verify against Context7 or current primary/official docs
   before treating the claim as confirmed.

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

5. Thermo maintainability
   - file crossing or sprawling past 1000 lines without strong reason
   - spaghetti growth from scattered conditionals and special cases
   - feature logic leaking into shared/general paths
   - thin wrappers, identity abstractions, magic generic handling
   - casts, `any`, `unknown`, optionality, or loose ad-hoc shapes obscuring the invariant
   - duplicated canonical helpers or logic living in the wrong layer
   - missed simplification that could delete whole branches, layers, or concepts

## Evidence Bar

Only report findings that are confirmed or strongly evidenced. A finding needs:

- specific file/line or hunk evidence
- a concrete failure mode or maintainability regression
- user, operator, data, security, money, deploy, or future-maintenance impact
- a focused fix direction
- the verification needed to prove the fix

Do not pad with low-value style nits. Do not invent a finding to satisfy the
shape. Label `Hypothesis` when the evidence is incomplete and keep hypotheses out
of blocker lists unless verification is cheap and important.

## Ranking

Rank by this order unless the user requested a specific lens:

1. P0/P1 correctness, security, money, auth, data loss, destructive action,
   migration, or launch-blocking workflow failures.
2. High-likelihood user-visible or operational regressions.
3. Missing invariant/ownership/state protections around Tier 1 behavior.
4. Test gaps that hide a realistic serious regression.
5. Thermo structural regressions that make the codebase materially harder to
   reason about.
6. Performance, observability, DX, and maintainability concerns.

For `one` mode, return only the strongest confirmed issue. For `full` mode, keep
the list high-signal and deduplicated.

## Specialist Routing

Keep these workflows standalone:

- Use `$launch-critical-sweep` for go-live, release readiness, catastrophic-risk,
  or "is this safe to launch?" questions.
- Use `$tdd-review-deep` when the user wants refactor/cleanup with behavior locked
  by characterization tests.
- Use `$bug-ripple` after diagnosing one concrete bug when similar sibling bugs
  may exist.
- Use `$safe-feature-slice` as the default next step after actionable review
  findings when the user wants fixes, hardening, or implementation. It can plan
  first for broad/multi-finding work and then execute eligible slices.
- Use `$cap` when the user asks to verify, commit, push, deploy, or finish the
  branch.

When routing, explain the reason in one line and continue with the specialist if
the current request clearly matches it.

## Subagent Pattern

Use subagents only when available and allowed by the active environment/user
instructions. Keep the critical path local and delegate independent lanes.

Good lanes to delegate:

- correctness/runtime
- auth/ownership/security
- money/state/webhooks/migrations
- tests/verification gaps
- thermo maintainability
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
```

Severity labels:

- `BLOCKER`: should not merge/launch as-is.
- `MAJOR`: should fix before merge unless consciously accepted.
- `MODERATE`: real issue, but can be scheduled if risk is understood.
- `MINOR`: include only when no higher-value findings exist.

For review-only requests, do not edit files. For implementation requests, finish
the review judgment first, then move into the appropriate fix workflow.

When there are actionable findings, end with a suggested next step:

- `Use $safe-feature-slice to fix [specific issue]` for one narrow fix or hardening task.
- `Use $safe-feature-slice to create/update a slice plan for [scope] and execute the first eligible slice` when there are multiple related findings or broad work.
- `Use $launch-critical-sweep` when the real decision is go-live safety.
- `Use $tdd-review-deep` when the next move is behavior-preserving refactor with characterization tests.
- `Use $bug-ripple` when one confirmed bug implies likely sibling bugs.
- `Use $cap` when the code is reviewed and the user asks to verify, commit, push, or ship.
- `No action` when there are no material findings.

## Behavior Preservation

For any review of changed behavior, explicitly separate:

- previous intended behaviors that should remain true
- intentional behavior changes from the request
- possible accidental drift
- evidence used: tests, source, runtime/browser checks, docs, schemas, provider
  truth, or current official documentation

Do not give high confidence merely because the new path works. Confidence must
also account for unintended regressions.
