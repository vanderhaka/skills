# Skill Rev

## What This Skill Does

`skill-rev` is a lightweight pre-push reviewer for this skills repo. It checks
pending skill changes before they are pushed and creates dated audit snapshots
for all curated skills.

It also supports pull/update audits so you can tell whether the repo skills and
installed local skills are in sync.

## Modes

- `skill-rev` — full pre-push review including installed-skills comparison.
- `skill-rev push` — pre-push checks only, no installed-skills comparison.
- `skill-rev sync` — pull/update audit only: remote drift plus installed-vs-repo
  comparison for `~/.codex/skills` and `~/.claude/skills`.

## Use It When

- You are about to push skill changes to `vanderhaka/skills`.
- You want to check whether the remote skills repo is updated.
- You want a dated audit covering every curated skill.
- You want to compare repo skills against installed `~/.codex/skills` or
  `~/.claude/skills`.

## How It Works

The skill runs the repo validators, public-safety audit, diff whitespace check,
changed script syntax checks, and a timestamped all-skill audit snapshot.

It is intentionally smaller than `cap`: it does not stage, commit, push, repair,
or publish anything.

## What You Get

- A compact PASS/WARN/FAIL/BLOCKED result.
- A dated `.skill-audits/<timestamp>-skill-audit.md` report.
- Changed-skill review notes.
- Pull/update drift notes for repo versus installed skills.
- Clear next action.

## Not For

Use `cap` when you want the reviewed work committed and pushed. Use
`skill-repo-maintainer` when creating or restructuring a public skill package.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/skill-rev
```

Restart Codex after installing new skills.
