# Progress Registry

Status: ACTIVE
Last reconciled: {YYYY-MM-DD}
Repository: {absolute path}
Registry owner checkout: {absolute path}

## Status Rules

- `proposed`: soft reservation. It warns later runs but does not block unrelated work.
- `approved`: hard reservation. It blocks overlapping work.
- `active`: hard reservation. It blocks overlapping work.
- `blocked`: hard reservation until the user abandons it or the blocker is removed.
- `complete`: historical record. It does not block unrelated work.
- `abandoned`: historical record. It does not block work.

## Active Work

| Slug | Status | Worktree | Branch | Goal | Product area | Write boundaries | Routes/APIs/Data | Forbidden overlap | Last updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {slug} | proposed | {path or PENDING} | codex/{slug} | {goal} | {area} | {paths} | {surfaces} | {conflicts} | {YYYY-MM-DD} |

## Conflict Decisions

| Date | Incoming slug | Existing slug | Decision | Evidence |
| --- | --- | --- | --- | --- |
| {YYYY-MM-DD} | {incoming} | {existing} | BLOCKED | {evidence} |

## Reconciliation Notes

| Date | Finding | Action |
| --- | --- | --- |
| {YYYY-MM-DD} | {finding} | {action} |
