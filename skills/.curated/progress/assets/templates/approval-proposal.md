# Approval Proposal: {slug}

Status: AWAITING APPROVAL
Date: {YYYY-MM-DD}
Repository: {absolute path}

## Registry Snapshot
Registry path: {absolute path}/plans/progress-registry.md
Recommended reservation slug: {slug}
Conflict result: NO HARD CONFLICT | BLOCKED

| Active slug | Status | Product area | Write boundaries | Decision |
| --- | --- | --- | --- | --- |
| {slug} | {status} | {area} | {paths} | ALLOW/BLOCK |

## Opportunity Matrix
| # | Opportunity | Problem | Impact | Demoable | Testable | Size | Risk | Dependency readiness | Registry overlap | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | {name} | {problem} | {impact} | {1-5} | {1-5} | {1-5} | {1-5 inverse} | {1-5} | NONE | {total}/30 |

Scoring rule: higher is better. Size score is higher when the work is smaller. Risk score is higher when risk is lower.

## Option 1: {name}
1. Problem: {problem}
2. Impact: {impact}
3. Proposed fix: {fix}
4. Affected areas: {areas}
5. Expected final behavior: {behavior}
6. Demo proof: {proof}
7. Risks: {risks}
8. Dependencies: {dependencies}
9. Registry overlap: NONE | BLOCKED BY {slug}
10. Score: {score}/30

## Recommendation
Recommended option: {number}
Reason: {reason}

## Approval Needed
Reply with one of:
- `Do 1`
- `Do 1 and 3`
- `Everything except 4`
- `Change 2 to include X`
