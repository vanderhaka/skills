# Worker Contract

Use this reference before launching implementation workers.

## Launch Rule

Launch a worker only when:

- The node's dependencies are `DONE`, `SKIPPED` with accepted reason, or not required.
- The node has one clear `When X, then Y` behavior or is explicitly a scaffold/refactor/verification node.
- Write boundaries are disjoint from every other active worker.
- Shared-state risks are absent or intentionally single-threaded.
- Product/business decisions needed for the node are resolved.

The worker prompt must be self-contained. Include only the context the worker needs, but include enough that it can succeed without relying on the main chat history.

## Worker Brief Template

```text
You are implementing one graph node for a tracked feature flow.
You are not alone in the codebase. Do not revert unrelated changes.
Do not edit progress.md. Write your report to agent-runs/{node}-{attempt}.md or return it to the orchestrator.
Do not spawn child codex processes.

Feature:
Core invariant:
Previous intended behaviors:
Intentional behavior changes:

Node:
Specific goal:
Tier:
Actor/trigger:
Behavior to test:
Acceptance criteria:
Regression guards:
Unsafe outcomes:
Dependencies already satisfied:

Allowed write scope:
Must not touch:
Shared-state risks:

Required loop:
1. RED - write/locate failing behavior test and prove it fails for the intended reason.
2. GREEN - smallest code change to pass.
3. REFACTOR - only safe cleanup after green.
4. Repo Gate - targeted tests plus typecheck/lint/build as required.
5. Browser Gate - required for user-visible work via Codex in-app browser when available.
6. Boundary/Migration Gate - run integration, DB, API, filesystem, third-party, auth, or non-destructive migration proof when required.

Debugging standard:
- If a bug, test failure, build failure, or unexpected behavior appears, find and state the root cause or current evidence-backed hypothesis before changing code.
- If the same error or failed fix repeats twice, stop blind retries and research current official docs or reputable current sources before trying another fix.

External docs:
- Use Context7/current official docs before coding if this node touches third-party APIs, frameworks, SDKs, cloud services, or standards where current behavior matters.

Return:
- Files changed
- Root cause or reason no debugging was needed
- Failed attempts, if any
- RED evidence
- GREEN evidence
- REFACTOR summary or skipped reason
- Repo gate commands/results
- Browser/boundary/migration evidence or skipped reason
- Previous behaviors preserved and evidence
- Residual risk
- Recommendation: DONE | BLOCKED | NEEDS ATTENTION
```

## Report Format

```markdown
# Agent Run: {node} {attempt}

Status: DONE | BLOCKED | NEEDS ATTENTION
Worker:
Started:
Completed:

## Scope
- Node:
- Allowed write scope:
- Files changed:

## RGR Evidence
- RED:
- GREEN:
- REFACTOR:

## Root Cause / Investigation
- Root cause or hypothesis:
- Failed attempts:

## Gates
- Repo Gate:
- Browser Gate:
- Boundary/Migration Gate:

## Behavior Preservation
- Previous intended behaviors checked:
- Evidence:
- Confidence:

## Residual Risk
- ...

## Handoff Notes
- ...

## Recommendation
DONE | BLOCKED | NEEDS ATTENTION
```

## Integration Rule

The orchestrator must verify the report before accepting it:

- Spec pass: node behavior, acceptance criteria, decisions, intentional changes, and previous behavior preservation are satisfied.
- Quality pass: changed files match the write scope, tests are meaningful, contracts still fit, and the node did not absorb unrelated work.
- No required gate is missing.
- Skipped gates have explicit reasons.
- Any newly discovered required work becomes a new graph node.
