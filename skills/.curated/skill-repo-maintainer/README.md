# Skill Repo Maintainer

## What This Skill Does

`skill-repo-maintainer` keeps a public Codex skills repository installable, readable, and safe to publish. It treats each skill as a small product package.

## Use It When

- You are adding a new skill to a repo.
- You are converting local/private skills into public-safe curated skills.
- You need to validate skill metadata and folder shape.
- You want install instructions for `$skill-installer`.
- You need a public-safety audit before pushing.

## How It Works

The skill checks folder names, frontmatter, descriptions, resources, references, scripts, and install paths. It keeps `SKILL.md` focused, moves long support material into references, and removes private local context before publishing.

## What You Get

- Skill repo layout guidance.
- Public conversion checklist.
- Validation commands.
- Install command pattern.
- Public-safety review expectations.

## Not For

Use the individual skill READMEs to understand what a specific skill does. Use `cap` when the repo is ready to validate, commit, and push.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/skill-repo-maintainer
```

Restart Codex after installing new skills.
