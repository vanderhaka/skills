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
    ├── ask-james/
    ├── cap/
    ├── codebase-design/
    ├── code-review/
    ├── constructive-criticism/
    ├── dashboard-ui-ux/
    ├── fallow/
    ├── feature-orchestrator/
    ├── grill-me/
    ├── handoff/
    ├── issue-fix-strategy/
    ├── launch-critical-sweep/
    ├── progress/
    ├── prototype/
    ├── ripple/
    ├── safe-feature-slice/
    ├── skill-repo-maintainer/
    ├── skill-rev/
    ├── tdd-plan-grill/
    ├── write-goals/
    └── wwh/
scripts/
└── validate_skills.py
templates/
└── basic-skill/
    └── SKILL.md
```

## Curated Skills

- `ask-james` — route broad or ambiguous work to the right curated skill with one recommendation and one optional alternative.
- `cap` — check, repair safe verification failures, commit exact intended files, and push safely, with fast/dry-run/verify/only/watch/release modes.
- `codebase-design` — shared architecture discipline for deep modules, clean interfaces, seams, adapters, and test surfaces.
- `code-review` — harsh unified code review workflow for PRs, diffs, changed files, or plans, including `one` mode for a single high-impact finding and `strict` mode for thermo-nuclear maintainability scrutiny.
- `constructive-criticism` — maximum-effort verified critique of any work at any scale, producing a fix-ready report with an execution contract and a paste-ready handoff prompt.
- `dashboard-ui-ux` — dense SaaS dashboard design and critique guidance with collapsible sidebars, card contrast, table tooling, chart interactions, and browser proof.
- `fallow` — run read-only Fallow structural analysis for JS/TS reviews and report required evidence.
- `feature-orchestrator` — end-to-end feature delivery orchestration through one canonical dependency graph and progress file, with intake-grill, graph-plan, plan-grill, worker, integrator, and proof stages packaged as references.
- `grill-me` — interview the user about a plan or design until reaching shared understanding, with a docs mode that keeps `CONTEXT.md`, ADRs, and feature decision docs current as decisions resolve.
- `handoff` — write or resume concise project handoffs without overwriting repo conventions.
- `issue-fix-strategy` — chat-only executive triage for any issue source, with priority, fix approach, proof, and next-step routing.
- `launch-critical-sweep` — find confirmed P0/P1 launch blockers before go-live.
- `progress` — discover the best real product improvement, get one approval, then execute through a fresh worktree, dependency graph, self-QA, and a demo-ready delivery package.
- `prototype` — build disposable UI or logic prototypes to answer design/state questions before production implementation.
- `ripple` — diagnose one reported bug or one planned business-rule/invariant change, then run a strict, findings-first, read-only ripple sweep, with bug mode and logic mode.
- `safe-feature-slice` — safety-first workflow for planning, building, continuing, or reviewing one or more feature slices while preserving invariants, including a `plan-only` mode for dependency-ordered slice plans.
- `skill-repo-maintainer` — maintain and public-safety-check this skills repository.
- `skill-rev` — lightweight review and dated audit snapshot before pushing skill changes, plus pull/sync audits (`push` and `sync` modes).
- `tdd-plan-grill` — stress-test a test-first plan before implementation and update it for the current implementation flow.
- `write-goals` — draft, critique, or rewrite Codex `/goal` objectives with clear success criteria and safe activation boundaries.
- `wwh` — explain a decision, change, bug, issue, incident, plan, or request in simple who/what/when/where/how/why language, omitting irrelevant sections.

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
3. Add a plain-English `README.md` (and optional `agents/openai.yaml`) beside `SKILL.md`, plus only the resources the skill genuinely needs.
4. Run:

```bash
python3 scripts/validate_skills.py
python3 skills/.curated/skill-repo-maintainer/scripts/audit_skill_repo.py .
```

5. Review public safety before pushing.
