# Feature Plan: {slug}

Status: READY
Last updated: {YYYY-MM-DD}
Owner: progress
Worktree: {absolute path}
Branch: codex/{slug}

## Working Brief
- Feature: {feature}
- Primary actors: {actors}
- Core invariant: {invariant}
- Previous intended behaviors: {behaviors}
- Intentional behavior changes: {changes}
- Unsafe outcomes: {outcomes}
- Evidence: {evidence}
- Assumptions: {assumptions}
- Out of scope: {scope}

## Dependency Graph
| Node | Title | Type | Tier | Depends On | Parallel Group | Blocking Class | Shared-State Risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | {title} | {type} | T1/T2/T3 | none | W1-A | Blocking | {risk} | PENDING |

## Worker Waves
| Wave | Nodes | Parallel-safe reason | Integration gate |
| --- | --- | --- | --- |
| W1 | {nodes} | {reason} | {gate} |

## Nodes

### S1 - {title}
Status: PENDING
Type: scaffold | behavior | integration | verification | refactor | ops
Risk tier: T1 | T2 | T3
Blocking class: Blocking | Parallel-safe | Dependent | QA | Demo/documentation
Depends on: {nodes}
Parallel group: {group}
Actor/trigger: {actor}
Observable behavior: When {trigger}, then {result}
Protected invariant: {invariant}
Write boundaries: {paths}
Forbidden files: {paths}
Acceptance criteria:
- [ ] {criterion}
Regression guards:
- {guard}
Required tests:
- {test}
Repo gate: {command}
Browser gate: {check or NOT APPLICABLE}
Boundary gate: {check or NOT APPLICABLE}
Exit evidence: {evidence}
Blocked on: none

