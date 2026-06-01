---
name: feature-proof
description: Final proof stage for feature-orchestrator flows. Use when all graph nodes appear complete and the feature needs requirement-by-requirement verification, full relevant checks, browser and boundary proof, migration evidence, skipped-check accounting, behavior preservation confidence, and a final PASS/BLOCKED/FAIL verdict in verification.md.
---

# Feature Proof

## Purpose

Prove the whole feature is complete. This stage must audit the original requested scope, not merely confirm the last worker finished.

## Workflow

1. Read the original request, `plan.md`, `progress.md`, `decisions.md`, and all relevant `agent-runs/*.md`.
2. Derive explicit requirements from the request and plan.
3. For each requirement, identify authoritative evidence:
   - source files
   - tests and command output
   - browser proof
   - database/migration state
   - API/provider evidence
   - logs or runtime artifacts
4. Run final verification:
   - targeted tests for changed areas
   - full test suite when practical
   - typecheck/lint/build when the repo exposes them
   - browser smoke for user-visible flows
   - boundary checks for DB/API/filesystem/third-party/auth/payment nodes
   - non-destructive migrations when required
5. Write `verification.md`.
6. Set final verdict:
   - `PASS`
   - `PASS WITH RISKS`
   - `BLOCKED`
   - `FAIL`

## Completion Bar

Mark `PASS` only when current evidence proves every in-scope requirement and all required nodes are `DONE` or explicitly `SKIPPED` with accepted reasons.

Use lower confidence when evidence is indirect, skips are material, previous intended behaviors are not strongly protected, or runtime proof could not run.

## Rules

- Do not redefine success around completed work.
- Do not use narrow tests as proof of broad requirements.
- Do not treat missing evidence as pass.
- Record skipped checks and residual risk plainly.
