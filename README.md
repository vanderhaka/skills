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
    ├── bug-ripple/
    ├── cap/
    ├── codebase-design/
    ├── code-review/
    ├── constructive-criticism/
    ├── dashboard-ui-ux/
    ├── feature-graph-plan/
    ├── feature-integrator/
    ├── feature-intake-grill/
    ├── feature-orchestrator/
    ├── feature-plan-grill/
    ├── feature-proof/
    ├── feature-slice-worker/
    ├── fallow/
    ├── grill-me/
    ├── grill-with-docs/
    ├── handoff/
    ├── issue-fix-strategy/
    ├── launch-critical-sweep/
    ├── logic-ripple/
    ├── one-major-issue/
    ├── progress/
    ├── prototype/
    ├── safe-feature-slice/
    ├── skill-repo-maintainer/
    ├── skill-rev/
    ├── tdd-plan-grill/
    ├── thermo-nuclear-code-quality-review/
    ├── thin-slice-plan/
    ├── wwh/
    └── write-goals/
scripts/
└── validate_skills.py
templates/
└── basic-skill/
    └── SKILL.md
```

## Curated Skills

- `ask-james` — route broad or ambiguous work to the right curated skill with one recommendation and one optional alternative.
- `bug-ripple` — diagnose one bug with a tight feedback loop, then run a strict bounded sibling-bug blast-radius review.
- `cap` — verify, commit, and push intended work safely without sweeping unrelated files, with a focused fast mode for tiny changes.
- `codebase-design` — shared architecture discipline for deep modules, clean interfaces, seams, adapters, and test surfaces.
- `code-review` — unified review workflow with correctness, safety, tests, and maintainability lanes.
- `constructive-criticism` — maximum-effort verified critique of any work at any scale, producing a fix-ready report with an execution contract and a paste-ready handoff prompt.
- `dashboard-ui-ux` — dense SaaS dashboard design and critique guidance with collapsible sidebars, card contrast, table tooling, chart interactions, and browser proof.
- `feature-orchestrator` — coordinate whole-feature delivery through one canonical graph, progress file, parallel-safe worker waves, and final proof.
- `feature-intake-grill` — clear product, data, permission, money, migration, external-contract, and live-risk decisions before graph planning.
- `feature-graph-plan` — turn a feature brief and decisions into RGR-ready dependency graph nodes, waves, write boundaries, and gates.
- `feature-plan-grill` — stress-test a feature dependency graph before worker launch.
- `feature-slice-worker` — execute one graph node with Red-Green-Refactor and required verification gates.
- `feature-integrator` — verify worker reports, update canonical progress, and advance dependency waves.
- `feature-proof` — run final requirement-level proof and behavior-preservation reporting before completion.
- `fallow` — run read-only Fallow structural analysis for JS/TS reviews and report required evidence.
- `grill-me` — interview relentlessly about a plan or design until material decisions are resolved.
- `grill-with-docs` — clarify material codebase decisions while updating `CONTEXT.md`, ADRs, and feature decision docs.
- `handoff` — write or resume concise project handoffs without overwriting repo conventions.
- `issue-fix-strategy` — chat-only executive triage for any issue source, with priority, fix approach, proof, and next-step routing.
- `launch-critical-sweep` — find confirmed P0/P1 launch blockers before go-live.
- `logic-ripple` — map every surface touched by a business-rule change before fixing or canonicalizing it.
- `one-major-issue` — find at most one confirmed high-impact issue and hand it to a safe fix slice.
- `progress` — discover the best real product improvement, get one approval, then execute through a fresh worktree, dependency graph, self-QA, and a demo-ready delivery package.
- `prototype` — build disposable UI or logic prototypes to answer design/state questions before production implementation.
- `safe-feature-slice` — unified plan-and-execute workflow for invariant-preserving feature work.
- `tdd-plan-grill` — stress-test a test-first plan before implementation and update it for the current implementation flow.
- `thin-slice-plan` — planning-only workflow for dependency-ordered slice plans.
- `thermo-nuclear-code-quality-review` — strict maintainability review for file sprawl, spaghetti branching, and abstraction quality.
- `wwh` — explain a decision, change, bug, issue, incident, plan, or request in simple who/what/when/where/how/why language, omitting irrelevant sections.
- `write-goals` — draft, critique, or rewrite Codex `/goal` objectives with clear success criteria and safe activation boundaries.
- `skill-repo-maintainer` — maintain and public-safety-check this skills repository.
- `skill-rev` — lightweight review and dated audit snapshot before pushing skill changes, plus pull/sync audits (`push` and `sync` modes).

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
