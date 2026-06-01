# Graph And Progress Contract

Use this reference when creating or updating `plans/<feature-slug>/plan.md`, `progress.md`, `decisions.md`, or `verification.md`.

## `plan.md`

```markdown
# Feature Plan: {feature}

Status: PLANNING | READY | IN_PROGRESS | BLOCKED | COMPLETE | RETIRED
Last updated: YYYY-MM-DD
Owner: feature-orchestrator

## Working Brief
- Feature:
- Primary actors:
- Core invariant:
- Previous intended behaviors:
- Intentional behavior changes:
- Unsafe outcomes:
- Evidence:
- Assumptions:
- Out of scope:

## Risk Classification
- Overall tier:
- Live-data risk:
- Migration risk:
- External-contract risk:

## Dependency Graph
| Node | Title | Tier | Depends On | Parallel Group | Shared-State Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | Example behavior | T1 | none | W1-A | none | PENDING |

## Nodes

### S1 - {short behavior title}
Status:
Tier:
Type: scaffold | behavior | integration | verification | refactor | ops
Actor/trigger:
Behavior to test: When X, then Y
Invariant protected:
Intentional behavior changes:
Previous intended behaviors preserved:
Unsafe outcomes:
Dependencies:
Expected files:
Write boundaries:
Acceptance criteria:
- [ ] ...
Regression guards:
- ...
RGR:
- RED:
- GREEN:
- REFACTOR:
Gates:
- Repo gate:
- Browser gate:
- Boundary/migration gate:
External docs needed:
Parallelization:
Worker role:
Exit evidence:
Blocked on:
```

## `progress.md`

`progress.md` is the canonical live state. The orchestrator is the only writer.

```markdown
# Feature Progress: {feature-slug}

Status: PLANNING | READY | IN_PROGRESS | BLOCKED | COMPLETE | RETIRED
Current wave: W1
Last updated: YYYY-MM-DD
Owner: feature-orchestrator

## Graph Summary
| Node | Title | Tier | Depends On | Parallel Group | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | Example behavior | T1 | none | W1-A | unassigned | PENDING |

## Gate Progress
| Node | RED | GREEN | REFACTOR | Repo Gate | Browser Gate | Boundary Gate | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | TODO | TODO | TODO | TODO | TODO | TODO | none | TBD |

## Blockers
| Node | Blocker | Required Decision Or Evidence |
| --- | --- | --- |

## Completed Evidence
- None yet.
```

Allowed node statuses: `PENDING`, `IN_PROGRESS`, `VERIFYING`, `DONE`, `BLOCKED`, `SKIPPED`, `ALREADY_RESOLVED`.

Allowed gate statuses: `TODO`, `IN_PROGRESS`, `DONE`, `SKIPPED`, `BLOCKED`.

## `decisions.md`

Record every user decision and every safe default that affects scope:

```markdown
# Decisions: {feature-slug}

## Confirmed Decisions
- YYYY-MM-DD: ...

## Safe Defaults
- ...

## Open Questions
- ...

## Rejected Options
- ...
```

## `verification.md`

```markdown
# Verification: {feature-slug}

## Final Status
PASS | PASS WITH RISKS | BLOCKED | FAIL

## Requirement Audit
| Requirement | Evidence | Result |
| --- | --- | --- |

## Commands
- ...

## Runtime And Boundary Proof
- ...

## Skipped Checks
- ...

## Behavior Preservation
- Previous intended behaviors:
- Intentional behavior changes:
- Evidence:
- Confidence: 0-100%

## Residual Risk
- ...
```

## Update Rules

- Move nodes to `IN_PROGRESS` before worker launch.
- Mark gates `DONE` only with exact evidence.
- Mark `DONE` only after all required gates pass or have accepted skip reasons.
- Mark `BLOCKED` with the exact missing decision, unsafe shared state, or failing check.
- Add newly discovered required work as a new graph node; do not silently expand active nodes.
- Keep skipped work visible with the reason.
