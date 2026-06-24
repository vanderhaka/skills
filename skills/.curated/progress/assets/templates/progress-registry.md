# Progress Registry

Status: ACTIVE
Last reconciled: {YYYY-MM-DD}
Repository: {absolute path}
Registry owner checkout: {absolute path}
Storage policy: LOCAL ONLY unless explicitly approved for commit

## Status Rules

- `proposed`: soft reservation. It warns later runs but does not block unrelated work.
- `approved`: hard reservation. It blocks overlapping work.
- `active`: hard reservation. It blocks overlapping work.
- `blocked`: hard reservation until the user abandons it or the blocker is removed.
- `complete`: historical record. It does not block unrelated work.
- `abandoned`: historical record. It does not block work.

## Active Work

| Slug | Status | Worktree | Branch | Goal | Product area | Boundary confidence | Write boundaries | Routes/APIs/Data | Forbidden overlap | Blocked by | Last updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {slug} | proposed | {path or PENDING} | codex/{slug} | {goal} | {area} | HIGH/MEDIUM/LOW | {paths} | {surfaces} | {conflicts} | none | {YYYY-MM-DD} |

## Conflict Decisions

| Date | Incoming slug | Existing slug | Decision | Evidence |
| --- | --- | --- | --- | --- |
| {YYYY-MM-DD} | {incoming} | {existing} | BLOCKED | {evidence} |

## Blocked Reservation Suggestions

| Blocked slug | Suggested action | Reason | User approval needed |
| --- | --- | --- | --- |
| {slug} | keep block/narrow reservation/split/sequence/abandon | {reason} | YES/NO |

## Reconciliation Notes

| Date | Finding | Action |
| --- | --- | --- |
| {YYYY-MM-DD} | {finding} | {action} |

## Archived Work

| Slug | Final status | Worktree | Branch | Goal | Final evidence |
| --- | --- | --- | --- | --- | --- |
| {slug} | complete/abandoned | {path} | codex/{slug} | {goal} | {evidence} |
