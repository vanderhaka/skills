# Ripple

## What This Skill Does

`ripple` starts from one trigger — a reported bug or a planned business-rule change — and sweeps for related failures or inconsistencies elsewhere in the codebase. It is a strict, bounded blast-radius review, not a repo-wide audit. One engine runs both modes: intake, read-only contract, scoped fanout, evidence bar, and report shape are shared; only the diagnosis step differs.

- **Bug Mode**: reproduces or identifies the tightest feedback loop, minimizes the failure, ranks hypotheses, and names the user impact, root cause, location, prove-it regression test, and likely fix before searching for sibling bugs.
- **Logic Mode**: writes a rule contract, maps every surface the rule touches, and classifies each candidate as `Must Fix`, `Probably Same Rule`, `Canonicalization Candidate`, `Intentionally Different`, `Do Not Touch`, or `Research Recommended`.

## Use It When

- One bug feels like a sign that the same pattern may exist elsewhere ("what else could break like this?").
- You are changing pricing, tax, GST, discounts, totals, entitlements, permissions, validation, or state transitions and want to know where else the same rule must apply.
- You suspect similar code paths calculate or enforce the same rule differently, or duplicate a bug's root cause.
- You want a findings-first report and fix menu before any edits happen.

If the trigger is ambiguous, `ripple` classifies it in one sentence — observed failure means Bug Mode, intended rule change means Logic Mode — and asks one question only if it genuinely can't tell.

## How It Works

Both modes share intake, a read-only contract, bounded scoping, parallel read-only lane fanout (when explicitly authorized and available), an identical verdict vocabulary (BLOCKER/MAJOR/MODERATE, BLOCKED/FAIL/PASS WITH RISKS), and a hard-stop report before any implementation.

- Bug Mode lanes: same pattern elsewhere, boundary/data contracts, async/state, auth/ownership/money, persistence/migrations, integrations/provider events, UI/runtime surface, test coverage, skeptical pass, structural signal pass.
- Logic Mode lanes: same-rule surfaces, data/persistence, customer artifacts, provider/integration contracts, canonicalization, skeptic, verification.

## What You Get

- A diagnosis (Bug Mode) or rule contract (Logic Mode) with assumptions stated.
- A bounded blast-radius or rule-surface scope.
- Confirmed findings ranked BLOCKER, MAJOR, or MODERATE, each with file:line evidence.
- Structural risk or canonicalization opportunities when they materially increase sibling-bug or rule-drift risk.
- Missing tests and prove-it test ideas.
- A fix menu ordered by impact, ending in a hard stop asking which fixes to apply.

## Not For

Use `code-review` or `launch-critical-sweep` for broader audits not anchored to one bug or rule. Use `safe-feature-slice` when you are ready to implement the confirmed fixes.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/ripple
```

Restart Codex after installing new skills.
