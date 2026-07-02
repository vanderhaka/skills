---
name: skill-repo-maintainer
description: Maintain a public Codex skills repository - create, review, validate, scrub, and publish installable SKILL.md folders with lean instructions, safe resources, GitHub-ready layout, and reliable trigger metadata. Use when adding a skill to a repo, converting local skills into public-safe repo skills, auditing a skills catalog before publishing, or preparing install instructions for $skill-installer.
---

# Skill Repo Maintainer

## Overview

Use this skill to keep a skills repository installable, lean, and public-safe. Treat every skill as a small product package: clear trigger metadata, focused instructions, only necessary resources, and evidence that the folder can be installed from GitHub.

## Repo Shape

Prefer this layout:

```text
skills/
├── .curated/
│   └── skill-name/
│       ├── SKILL.md
│       ├── README.md
│       ├── agents/openai.yaml
│       ├── scripts/
│       ├── references/
│       └── assets/
└── .experimental/
    └── draft-skill/
```

Use `.curated` for skills that are ready for other agents. Use `.experimental` for draft or risky skills. Keep templates outside installable skill folders.

## Workflow

1. Read the target `SKILL.md` plus any directly linked resource files.
2. Confirm the skill folder name, frontmatter `name`, and install path match.
3. Keep frontmatter to `name` and `description`. The description must include the capability and the concrete triggers, because Codex sees it before loading the body.
4. Keep `SKILL.md` under 500 lines when practical. Move long docs into one-level `references/` files and link them from `SKILL.md`.
5. Give each curated skill a plain-English `README.md` with what it does, when to use it, and install instructions.
6. Add scripts only for deterministic, repeatable operations. Test each script or a representative sample.
7. Add assets only when they are used in generated output.
8. Read `references/public-safety-checklist.md` before publishing public repos or converting local/private skills.
9. Run this skill's `scripts/audit_skill_repo.py <repo-root>` before finalizing.
10. If the repo has a root validator, run it too.

## Public Conversion Rules

When converting local skills into a public GitHub repo:

- Do not bulk-copy private local skill folders without reviewing them.
- Remove client names, private repo paths, provider account IDs, internal URLs, secret names that imply access, and operational instructions that would expose live systems.
- Replace machine-specific absolute paths with placeholders or repo-relative paths.
- Preserve the skill's useful workflow, not its private context.
- Prefer a small curated first release over a large unscreened dump.

## Install Instructions

For each public skill, include an install command using the GitHub tree URL:

```bash
$skill-installer install https://github.com/<owner>/<repo>/tree/main/skills/.curated/<skill-name>
```

Also include the helper-script equivalent when useful:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/.curated/<skill-name>
```

End user-facing install notes with: restart Codex after installing new skills.
