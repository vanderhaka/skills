---
name: ask-james
description: Router and inventory helper for James's Codex skill stack. Use when the user asks which skill or workflow to use, says ask James, wants the next best skill, asks to list skills, uses ask-james list, is unsure whether to review/plan/build/commit, or gives a broad task that should be routed before execution.
---

# Ask James

Pick the right skill or flow for the user's situation. This skill is a router, not a replacement for the specialist skills.

## Inventory Mode

If the user invokes `ask-james list`, says "list", asks to "list all skills", asks "what skills do we have", or otherwise wants an inventory, do not route to one skill. List the curated James skill stack with one quick summary each.

Use this output shape:

```text
James skills:
- `skill-name` — quick summary.
```

Keep summaries short. Do not include plugin/system skills unless the user explicitly asks for installed non-curated skills too.

### Curated Skill Inventory

- `ask-james` — route broad or ambiguous work to the right curated skill.
- `cap` — verify, exact-stage, commit, and push intended work safely.
- `code-review` — harsh correctness, safety, test, and maintainability review, including `one` mode (single biggest issue) and `strict` mode (thermo-nuclear maintainability scrutiny).
- `codebase-design` — design deeper modules, cleaner interfaces, seams, adapters, and test surfaces.
- `constructive-criticism` — maximum-effort verified critique of any work product at any scale, producing a fix-ready report and handoff prompt.
- `dashboard-ui-ux` — build, critique, or polish dense production dashboards, admin panels, and analytics UIs.
- `fallow` — run read-only JS/TS structural analysis with Fallow.
- `feature-orchestrator` — coordinate whole-feature delivery through a canonical dependency graph, worker waves, integration, and final proof (packages the intake-grill, graph-plan, plan-grill, worker, integrator, and proof stages as references).
- `grill-me` — interview a plan or design until material decisions are clear, including docs mode to keep `CONTEXT.md`/ADRs current as decisions resolve.
- `handoff` — write or resume concise next-session project handoffs.
- `issue-fix-strategy` — triage messy issues, findings, logs, screenshots, or diagnostics into a fix order.
- `launch-critical-sweep` — find confirmed P0/P1 blockers before launch.
- `progress` — discover and deliver one approved production-ready improvement through a fixed worktree, graph, QA, and demo protocol.
- `prototype` — build disposable UI or logic experiments before real implementation.
- `ripple` — diagnose one bug and sweep for sibling bugs (bug mode), or map the blast radius of a business/domain logic change (logic mode).
- `safe-feature-slice` — plan and execute risky or narrow feature slices safely, including `plan-only` mode for a planning-only dependency-ordered slice plan.
- `skill-repo-maintainer` — create, validate, scrub, and publish public-safe skill folders.
- `skill-rev` — review skill repo changes and push/pull/sync installed skills with the repo.
- `tdd-plan-grill` — stress-test a test-first or feature-orchestrator plan.
- `write-goals` — draft or critique Codex `/goal` objectives.
- `wwh` — explain decisions, bugs, plans, or requests in simple who/what/when/where/how/why form.

## Operating Rule

Recommend exactly one next skill by default. If another route is genuinely defensible, list one alternative with a one-line tradeoff. Do not list a menu of every possible skill.

If the user only asked for advice, stop after the recommendation. If the user asked to proceed, continue with the recommended skill after giving the routing call.

## Main Routes

### Broad Feature Work

Use `feature-orchestrator` when the user wants a complete feature, broad multi-slice fix, many agents coordinated, canonical `plans/<feature-slug>/progress.md`, or "keep going until complete" execution.

Use `progress` when the user wants Codex to find the best product improvement first, get one approval, create a fresh worktree, execute through a strict dependency graph, self-QA, and produce a demo-ready delivery package.

Use `safe-feature-slice` when the work is one narrow feature/fix or a small risky slice touching money, permissions, ownership, destructive actions, state transitions, webhooks, migrations, integrations, or customer-visible records.

Use `safe-feature-slice` in `plan-only` mode when the user explicitly wants planning only and no implementation yet.

### Decisions Before Work

Use `grill-me` in docs mode (also triggered by "grill with docs") when a codebase feature, refactor, product/design choice, or architecture decision needs material decisions clarified and the results should land in `CONTEXT.md`, ADRs, or `plans/<feature-slug>/decisions.md`.

Use `grill-me` when the user wants to stress-test a plan or design, but no durable project docs need to be updated.

Use `feature-orchestrator`'s intake-grill stage (`references/stages/intake-grill.md`) when the only missing piece is the orchestrator's decision gate before graph planning.

Use the relevant `feature-orchestrator` stage reference when the ask is shaped like one pipeline stage of an in-flight feature: intake (`references/stages/intake-grill.md`), graph planning (`references/stages/graph-plan.md`), plan review (`references/stages/plan-grill.md`), worker execution (`references/worker-contract.md`), integration (`references/stages/integrator.md`), or final proof (`references/stages/proof.md`).

Use `codebase-design` when the task is mainly about module shape, architecture vocabulary, interface design, seam placement, adapters, or making code easier to test before implementation.

Use `prototype` when the next best step is a disposable UI or logic experiment to answer a design, state, data-shape, or workflow question before full implementation.

Use `dashboard-ui-ux` when the ask is dashboard, admin-panel, or analytics UI design, critique, or tactical polish — layout, tables, KPI cards, charts, sidebars, filters, or a mock-data dashboard proof. For whole-feature dashboard delivery, route to `feature-orchestrator` and apply `dashboard-ui-ux` as the UI standard.

### Issues, Reviews, And Bugs

Use `issue-fix-strategy` when the user has a messy issue list, review findings, UX complaints, logs, screenshots, failing tests, or tool diagnostics and wants plain-English priority, fix order, proof, and routing.

Use `code-review` when the user asks for review, audit, merge readiness, harsh maintainability critique, branch/diff review, or implementation-plan review.

Use `ripple` in bug mode when one concrete bug may imply sibling bugs nearby, or the user asks what else could break in the same pattern.

Use `ripple` in logic mode when a business/domain rule change may need to be applied consistently across the codebase.

Use `code-review` in `one` mode when the user wants only the single biggest confirmed issue, not a backlog.

Use `launch-critical-sweep` when the decision is go-live readiness or catastrophic launch risk.

### Finish, Handoff, And Skill Repo Work

Use `cap` when the user wants checks, exact staging, commit, push, deploy watch, or "finish this safely."

Use `handoff` when the user wants to wrap the session or create next-session continuity.

Use `write-goals` when the user wants a durable Codex `/goal` objective or needs to decide whether goal mode fits.

Use `skill-repo-maintainer` when creating, editing, publishing, or public-safety-checking skills.

Use `skill-rev` when reviewing skill repo changes before push, pulling skill updates onto a device, or syncing installed skills with the repo.

## Output Shape

```text
Recommended: <skill>
Why: <one plain-English reason>
Use it now if: <trigger condition>
Do not use it if: <main counter-signal>
Also viable: <one alternative or "None">
```

## Routing Bias

- Prefer `issue-fix-strategy` before planning when the input is a pile of findings.
- Prefer `grill-me` in docs mode before graph planning when product/domain decisions need to survive the chat.
- Prefer `feature-orchestrator` for whole-feature execution.
- Prefer `progress` before `feature-orchestrator` when the product target still needs discovery and one approval.
- Prefer `safe-feature-slice` for one risky slice.
- Prefer `cap` only after the work is ready to verify, commit, and push.
- Prefer discussion over action when the source evidence is too weak to route safely.

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this installed skill. Use the active environment's global lessons and memory system instead. Lessons are for mistakes, corrections, and reusable failure-prevention rules; memories are for durable user, project, or workflow context when the active instructions allow memory updates. Keep entries concise and redact secrets, tokens, customer data, and private details.
