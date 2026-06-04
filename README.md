# James's Codex Skills

Public-safe Codex skills and skill-authoring utilities.

## What I Found

Codex skills are normal folders that can live in a Git repository. The portable unit is:

```text
skill-name/
├── SKILL.md
├── README.md                # plain-English human overview
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
Each curated skill also has a plain-English `README.md` so humans can quickly understand what the skill is for before installing it.

Primary references used:

- OpenAI skills catalog: <https://github.com/openai/skills>
- Skill creator guidance: <https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md>
- Skill installer guidance: <https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md>

## Repo Layout

```text
skills/
└── .curated/
    ├── bug-ripple/
    ├── cap/
    ├── code-review/
    ├── feature-graph-plan/
    ├── feature-integrator/
    ├── feature-intake-grill/
    ├── feature-orchestrator/
    ├── feature-plan-grill/
    ├── feature-proof/
    ├── feature-slice-worker/
    ├── grill-me/
    ├── handoff/
    ├── issue-fix-strategy/
    ├── launch-critical-sweep/
    ├── logic-ripple/
    ├── one-major-issue/
    ├── safe-feature-slice/
    ├── skill-repo-maintainer/
    ├── tdd-plan-grill/
    ├── thermo-nuclear-code-quality-review/
    └── thin-slice-plan/
scripts/
└── validate_skills.py
templates/
└── basic-skill/
    └── SKILL.md
```

## Curated Skills

- `bug-ripple` — diagnose one bug, then run a strict bounded sibling-bug blast-radius review.
- `cap` — verify, commit, and push intended work safely without sweeping unrelated files, with a focused fast mode for tiny changes.
- `code-review` — unified review workflow with correctness, safety, tests, and maintainability lanes.
- `feature-orchestrator` — coordinate whole-feature delivery through one canonical graph, progress file, parallel-safe worker waves, and final proof.
- `feature-intake-grill` — clear product, data, permission, money, migration, external-contract, and live-risk decisions before graph planning.
- `feature-graph-plan` — turn a feature brief and decisions into RGR-ready dependency graph nodes, waves, write boundaries, and gates.
- `feature-plan-grill` — stress-test a feature dependency graph before worker launch.
- `feature-slice-worker` — execute one graph node with Red-Green-Refactor and required verification gates.
- `feature-integrator` — verify worker reports, update canonical progress, and advance dependency waves.
- `feature-proof` — run final requirement-level proof and behavior-preservation reporting before completion.
- `grill-me` — interview relentlessly about a plan or design until material decisions are resolved.
- `handoff` — write or resume concise project handoffs without overwriting repo conventions.
- `issue-fix-strategy` — chat-only executive triage for any issue source, with priority, fix approach, proof, and next-step routing.
- `launch-critical-sweep` — find confirmed P0/P1 launch blockers before go-live.
- `logic-ripple` — map every surface touched by a business-rule change before fixing or canonicalizing it.
- `one-major-issue` — find at most one confirmed high-impact issue and hand it to a safe fix slice.
- `safe-feature-slice` — unified plan-and-execute workflow for invariant-preserving feature work.
- `tdd-plan-grill` — stress-test a TDD plan before implementation and update it for `$tdd-deep`.
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
