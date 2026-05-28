# James's Codex Skills

Public-safe Codex skills and skill-authoring utilities.

## What I Found

Codex skills are normal folders that can live in a Git repository. The portable unit is:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml        # optional UI metadata
├── scripts/                  # optional deterministic helpers
├── references/               # optional docs loaded only when needed
└── assets/                   # optional templates/images/fonts/etc.
```

The required file is `SKILL.md`. It starts with YAML frontmatter containing only:

```yaml
---
name: skill-name
description: What this skill does, and the exact situations that should trigger it.
---
```

Keep `SKILL.md` lean. Put long docs in `references/`, repeatable code in `scripts/`, and output templates or media in `assets/`.

Primary references used:

- OpenAI skills catalog: <https://github.com/openai/skills>
- Skill creator guidance: <https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md>
- Skill installer guidance: <https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md>

## Repo Layout

```text
skills/
└── .curated/
    ├── code-review/
    ├── safe-feature-slice/
    ├── skill-repo-maintainer/
    ├── thermo-nuclear-code-quality-review/
    └── thin-slice-plan/
scripts/
└── validate_skills.py
templates/
└── basic-skill/
    └── SKILL.md
```

## Curated Skills

- `code-review` — unified review workflow with correctness, safety, tests, and maintainability lanes.
- `safe-feature-slice` — unified plan-and-execute workflow for invariant-preserving feature work.
- `thin-slice-plan` — planning-only workflow for dependency-ordered slice plans.
- `thermo-nuclear-code-quality-review` — strict maintainability review for file sprawl, spaghetti branching, and abstraction quality.
- `skill-repo-maintainer` — maintain and public-safety-check this skills repository.

## Install A Skill

From this repository:

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/skill-repo-maintainer
```

Or with the installer helper:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo vanderhaka/skills \
  --path skills/.curated/skill-repo-maintainer
```

Restart Codex after installing new skills.

## Add A Skill

1. Copy `templates/basic-skill/` into `skills/.curated/<skill-name>/`.
2. Edit `SKILL.md` so `name` exactly matches the folder name.
3. Add only the resources the skill genuinely needs.
4. Run:

```bash
python3 scripts/validate_skills.py
python3 skills/.curated/skill-repo-maintainer/scripts/audit_skill_repo.py .
```

5. Review public safety before pushing.
