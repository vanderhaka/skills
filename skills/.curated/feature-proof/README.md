# Feature Proof

## What This Skill Does

`feature-proof` is the final proof stage for `feature-orchestrator`. It checks the original requirements, not just whether the last worker finished.

## Use It When

- All graph nodes appear complete.
- The feature needs final requirement-by-requirement verification.
- Browser, boundary, migration, or provider proof must be accounted for.
- You need a final `PASS`, `PASS WITH RISKS`, `BLOCKED`, or `FAIL` verdict.

## How It Works

The skill reads the original request, plan, progress, decisions, and worker reports. It derives explicit requirements and matches each one to evidence from source files, tests, browser checks, migrations, API or provider proof, logs, or runtime artifacts.

## What You Get

- `verification.md`.
- Requirement-level proof table.
- Final checks run.
- Skipped checks with reasons.
- Residual risk.
- Behavior preservation confidence.
- Final verdict.

## Not For

Use `feature-integrator` while worker waves are still in progress. Use `cap` after the feature is proven and needs to be committed and pushed.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-proof
```

Restart Codex after installing new skills.
