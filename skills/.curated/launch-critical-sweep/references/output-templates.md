# Launch Critical Sweep Output Templates

Use these templates when `$launch-critical-sweep` needs a structured final answer.

## Confirmed Blockers

```text
Launch gate:
LAUNCH BLOCKED

Critical launch blocker 1:
[short title]

Issue in plain English:
[what is broken, in one or two concrete sentences]

Why it blocks launch:
[plain-language client/customer/team impact]

Who/what is affected:
- Users/roles: [customer/client/admin/operator/etc.]
- Data/records/systems: [tables, files, payments, emails, webhooks, deploy envs, etc.]
- Critical workflow: [journey or operation that breaks]

Failure chain:
1. [entry point or trigger]
2. [code/config behavior]
3. [unsafe outcome]

Evidence:
- [file:line anchor and what it proves]
- [file:line anchor and what it proves]

How to reproduce or verify:
[minimal command, scenario, trace, or reasoning path]

Why it needs to be fixed before launch:
[why deferring creates client/customer/team risk, and what could happen in production]

Fix direction:
[smallest credible fix, including the invariant the fix must enforce and any migration/provider/deploy concerns]

How the fix reduces risk:
[what bad outcome becomes impossible or detectable after the fix]

Verification required:
- Automated: [focused tests/typecheck/build/migration check]
- Runtime: [browser/API/provider/deploy check if needed]
- Regression guard: [specific unsafe case that must stay covered]

Suggested safe-feature-slice fix:
Use $safe-feature-slice to fix [blocker title].
Invariant: [rule that must remain true].
Unsafe outcome to prevent: [bad state].
Likely scope: [files/modules].
Verification: [focused tests/checks/browser flow, including affected workflow].
Extra instruction: [carry over relevant launch-sweep constraint].

Confidence:
Confirmed / High confidence / Hypothesis, with a short reason
```

## No Confirmed Blocker

```text
Launch gate:
NO CONFIRMED LAUNCH BLOCKER FOUND

What I checked:
[brief evidence-backed scope]

Most important surfaces covered:
- [auth/ownership/money/data loss/deploy/etc. and the evidence source]

Why I am not forcing one:
[why candidates did not meet the launch-blocker evidence bar]

Residual launch risk:
[single highest-risk area not fully proven, why it matters, and what would be affected if it failed; or "None beyond normal release risk"]

Best next verification:
[one command, browser flow, deploy check, or module to inspect]

Confidence:
[short reason]
```

## Inconclusive

```text
Launch gate:
INCONCLUSIVE

Blocked check:
[what could not be verified]

Why it matters:
[what catastrophic risk this check would prove or rule out]

Evidence gathered:
[what was checked successfully]

Affected surface if this check fails:
[users, records, workflow, provider, or deploy environment at risk]

Best next verification:
[specific command/access/env/browser flow needed]

Confidence:
[short reason]
```
