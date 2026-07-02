# Code Review

## What This Skill Does

`code-review` reviews a diff, branch, PR, focused file set, or implementation plan for real issues. It prioritizes bugs, regressions, safety risks, missing tests, merge-readiness problems, and harsh structural maintainability findings over style nits.

This skill owns the strict thermo/code-judo review bar directly, and also owns
the single-issue review bar. Use it as the default review skill instead of
reaching for a separate thermo-nuclear review or a separate one-issue skill —
both have been fully absorbed here.

For TypeScript and JavaScript reviews, this skill runs `fallow` for
structural-analysis evidence — mandatory in `full` and `strict` modes,
skippable with a stated reason in `quick` and `one` modes. The Fallow evidence
line is always reported, either as a result or as skipped with the reason.

## Use It When

- You ask for a code review.
- You want to know if a branch is safe to merge.
- You want current local changes audited.
- You want a strict review or a focused review of one area.
- You want a harsh structural review for spaghetti branching, file sprawl, wrong-layer logic, unnecessary abstractions, casts, or missed simplification — a thermo-nuclear code quality review, thermonuclear review, deep code quality audit, or especially harsh maintainability review.
- You want a sharp single answer instead of a backlog — the single biggest problem, one high-impact finding, or one actionable issue.
- You want review findings before deciding what to fix.

## How It Works

The skill identifies the review target, reads the relevant code and repo rules, inspects behavior and risk surfaces, then reports findings ordered by severity. It applies a strict structural approval bar by default: working code is not enough if the implementation makes the codebase more tangled.

Two modes load dedicated reference files for their full operating rules:

- `one` mode loads `references/one-mode.md` — a read-only hard boundary, a
  strict evidence bar, a single-issue ranking rubric, a `safe-feature-slice`
  fix handoff, and both the confirmed-finding and honest-no-finding output
  shapes.
- `strict` mode loads `references/strict-structural-bar.md` — the
  direct-invocation core prompt (with scope substitution) and the Primary
  Review Questions checklist, layered on top of the Structural Standards in
  `SKILL.md`.

It routes only genuinely different workflows to specialist skills, such as `launch-critical-sweep` for go-live blockers or `cap` for final ship verification.

## What You Get

- Findings first, ordered by severity — or, in `one` mode, exactly one
  confirmed finding (or an honest no-finding result).
- File and line references.
- Impact and fix direction.
- Behavior preservation and structural quality confidence.
- Required Fallow structural-analysis evidence for JS/TS reviews.
- Open questions or assumptions.
- Brief summary only after the findings.

## Not For

Use `issue-fix-strategy` when you already have a pile of issues and want plain-English prioritization. Use `cap` when the work is already fixed and needs to be committed.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/code-review
```

Restart Codex after installing new skills.
