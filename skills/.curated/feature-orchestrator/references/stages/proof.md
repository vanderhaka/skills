# Feature Proof

## Purpose

Prove the whole feature is complete. This stage must audit the original requested scope, not merely confirm the last worker finished.

Core rule: no completion claim without fresh verification evidence. If the proof did not run in this pass, record it as skipped or stale; do not imply it passed.

## Workflow

1. Read the original request and, from `plans/<feature-slug>/`: `plan.md`, `progress.md`, `decisions.md`, and all relevant `agent-runs/*.md`.
2. Derive explicit requirements from the request and plan.
3. For each requirement, identify authoritative evidence:
   - source files
   - tests and command output
   - browser proof
   - database/migration state
   - API/provider evidence
   - logs or runtime artifacts
4. Build an evidence table where every claim has a command, file, browser flow, provider check, or explicit skipped reason.
5. Run final verification:
   - targeted tests for changed areas
   - full test suite when practical
   - typecheck/lint/build when the repo exposes them
   - browser smoke for user-visible flows
   - boundary checks for DB/API/filesystem/third-party/auth/payment nodes
   - non-destructive migrations when required
6. Write `plans/<feature-slug>/verification.md` using the template in `feature-orchestrator/references/graph-and-progress.md`, including behavior preservation confidence 0-100.
7. Set final verdict:
   - `PASS`
   - `PASS WITH RISKS`
   - `BLOCKED`
   - `FAIL`

## Completion Bar

Mark `PASS` only when current evidence proves every in-scope requirement and all required nodes are `DONE`, `ALREADY_RESOLVED` with fresh evidence, or explicitly `SKIPPED` with accepted reasons.

Use lower confidence when evidence is indirect, skips are material, previous intended behaviors are not strongly protected, or runtime proof could not run.

Use `PASS WITH RISKS` when the requested behavior appears implemented but proof is incomplete, broad checks are skipped, previous behavior preservation is weak, or runtime/provider/browser verification could not run.

Use `BLOCKED` when verification of an in-scope requirement cannot proceed: missing decision, credentials, environment, or an unsafe live check. Use `FAIL` when fresh evidence shows an in-scope requirement unmet or an invariant broken.

## Rules

- Do not redefine success around completed work.
- Do not use narrow tests as proof of broad requirements.
- Do not treat missing evidence as pass.
- Record skipped checks and residual risk plainly.
- Do not trust worker or integrator summaries without checking the underlying evidence where practical.
- Do not use positive language like "complete", "fixed", "passes", or "done" unless the matching evidence is in `verification.md`.
