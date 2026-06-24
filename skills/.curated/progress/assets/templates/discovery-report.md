# Discovery Report: {slug}

Status: DISCOVERY
Date: {YYYY-MM-DD}
Repository: {absolute path}
Base branch: {branch}
Base commit: {sha}
Discovery checkout: {absolute path}
Implementation worktree: PENDING APPROVAL

## 0. Active Work Registry
Registry path: {absolute path}/plans/progress-registry.md
Registry owner checkout: {absolute path}
Registry storage policy: LOCAL ONLY unless explicitly approved for commit
Registry status: READY | BLOCKED
Conflict decision: NO HARD CONFLICT | HARD CONFLICT

| Active slug | Status | Worktree | Product area | Boundary confidence | Write boundaries | Conflict with this run |
| --- | --- | --- | --- | --- | --- | --- |
| {slug} | {status} | {path} | {area} | HIGH/MEDIUM/LOW | {paths} | YES/NO |

## 0.1 Boundary Evidence
Boundary confidence: HIGH | MEDIUM | LOW

| Boundary | Evidence | Notes |
| --- | --- | --- |
| Files/directories | {paths} | {notes} |
| Routes/screens/commands | {surfaces} | {notes} |
| APIs/jobs/functions | {surfaces} | {notes} |
| Data/migrations/fixtures | {surfaces} | {notes} |
| External providers/env | {env names only} | {notes} |
| Tests/browser flows | {commands/routes} | {notes} |

## 1. Product Summary
1. {what the app does}
2. {primary users}
3. {core workflows}

## 2. Structure Summary
| Area | Evidence | Notes |
| --- | --- | --- |
| Routes/pages | {files} | {notes} |
| API/server | {files} | {notes} |
| Data models | {files} | {notes} |
| External services | {files/env names only} | {notes} |
| Tests | {files/commands} | {notes} |
| Build/deploy | {files/commands} | {notes} |

## 3. Current Product Gaps
| Gap | Evidence | User impact | Risk |
| --- | --- | --- | --- |
| {gap} | {evidence} | {impact} | {risk} |

## 4. Constraints
| Constraint | Source | Effect |
| --- | --- | --- |
| {constraint} | {source} | {effect} |

## 5. No-Code-Edit Confirmation
Code edited during discovery: NO
