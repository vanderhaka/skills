# Shared Contract: {slug}

Status: READY FOR GRAPH
Date: {YYYY-MM-DD}
Approved by: {user approval text}
Worktree: {absolute path}
Branch: codex/{slug}
Base commit: {sha}

## 1. Approved Goal
{goal}

## 2. User-Facing Behavior
{behavior}

## 3. Data Shape
| Entity/Payload | Required fields | Optional fields | Invalid/missing handling |
| --- | --- | --- | --- |
| {name} | {fields} | {fields} | {handling} |

## 4. API Expectations
| Endpoint/function | Input | Output | Error behavior |
| --- | --- | --- | --- |
| {api} | {input} | {output} | {errors} |

## 5. Auth And Permissions
| Actor | Allowed behavior | Denied behavior | Evidence needed |
| --- | --- | --- | --- |
| {actor} | {allowed} | {denied} | {evidence} |

## 6. Files Parallel Workers Must Not Touch
| File/path | Reason | Owner |
| --- | --- | --- |
| {path} | {reason} | {owner} |

## 7. Test Expectations
| Area | Required proof | Command/check |
| --- | --- | --- |
| {area} | {proof} | {command} |

## 8. Demo Path
Route or command: {route/command}
Required data: {data}
Expected result: {result}

## 9. Rollback Risk
Risk level: LOW | MEDIUM | HIGH
Rollback path: {path}

## 10. External Dependency Status
| Dependency | Status | Required action |
| --- | --- | --- |
| {dependency} | READY | BLOCKED | NOT APPLICABLE | {action} |

