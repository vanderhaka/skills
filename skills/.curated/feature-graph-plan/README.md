# Feature Graph Plan

## What This Skill Does

`feature-graph-plan` turns a feature brief, explicit decisions, and strongly inferred defaults into an executable dependency graph. It is the planning stage that prepares work for `feature-orchestrator` workers.

## Use It When

- The feature is clear enough to plan.
- Decisions have already been made or safely assumed.
- Work needs dependency ordering, write boundaries, risk tiers, and verification gates.
- The next step after triage is building a graph, not asking more questions.

## How It Works

The skill reads the feature request, decisions, relevant source evidence, and graph reference material. It applies routine technical, UX, UI, and product-taste defaults before marking anything decision-needed, then creates or updates `plans/<feature-slug>/plan.md` and `progress.md` with small graph nodes that can be tested and assigned safely.

Each node names the actor, behavior, invariant, previous behavior to preserve, dependencies, write boundaries, RED/GREEN/REFACTOR plan, and required gates.

## What You Get

- Dependency graph.
- Parallel-safe and single-threaded groups.
- Risk tiers.
- Worker-ready node definitions.
- Canonical progress tracking seeded for execution.

## Not For

Use `feature-intake-grill` first when product, data, permission, money, migration, or live-risk decisions are still unclear.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/feature-graph-plan
```

Restart Codex after installing new skills.
