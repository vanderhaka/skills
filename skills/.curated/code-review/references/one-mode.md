# One Mode Reference

Load this reference when running `code-review` in `one` mode: return only the
single strongest confirmed issue. This absorbs the retired `one-major-issue`
skill's operating rules, evidence bar, ranking rubric, and output shapes.

## Goal

Find the single highest-impact confirmed issue in the review scope and report
only that issue. If no major issue can be responsibly confirmed in the allowed
scope, say so plainly and stop at the best next investigative target. The
output should feel like a sharp senior review finding or a clear no-finding
result, not a general audit or backlog. End confirmed findings with a narrow
suggested fix handoff that invokes `safe-feature-slice`.

Use `one` mode when the user wants one major flaw, gap, bug, issue, risk,
missing invariant, or production-readiness problem instead of a list. If the
user appends text after invoking the skill, treat it as binding extra
instruction.

Examples:

- `Use code-review in one mode`
- `Use code-review, one mode, extra instruction: focus auth and ownership only`
- `Use code-review one mode on checkout; ignore styling unless it blocks purchase`
- `Use code-review one mode, read-only, no tests that write to the DB`

## Operating Mode (Read-Only Hard Boundary)

Default to read-only investigation. Do not edit code, write migrations, change
data, or reformat files unless the user explicitly asks for fixes.

Extra instruction text after the skill call can constrain scope, priority,
evidence level, or verification method. Follow it over the default breadth of
this mode unless it would make the result unsafe or misleading.

If the user asks for `review only`, `read-only`, or similar, treat that as a
hard boundary. Tests, builds, and local app runs are allowed only when they do
not mutate shared state or violate the user's constraint.

## Evidence Bar

Only report a confirmed or very strongly evidenced major issue. Keep candidate
notes private and keep investigating until one issue clearly beats the others
or the allowed scope is exhausted.

A reportable issue should have most of:

- a concrete failure mode or unsafe state
- file/line anchors for the code path
- a plausible user, operator, security, money, data, or deploy impact
- a minimal reproduction, trace, or reasoning chain
- a specific fix direction

Do not pad the answer with weaker runner-up findings. Do not promote a minor
issue, style preference, generic missing test, or weak hypothesis just to
satisfy the "one issue" shape. If the best issue is still partly inferred,
label the uncertain part as `Hypothesis` and keep the confirmed facts
separate.

If third-party API/framework behavior is central to the issue and may have
changed, verify against current official documentation or primary sources
before finalizing.

## Ranking Rubric (Single-Issue Selection)

When multiple confirmed issues exist, choose the one issue with the highest
combination of:

- impact severity
- likelihood in real use
- proximity to production/customer workflows
- ability to corrupt, leak, lose, double-charge, mis-authorize, or silently
  mislead
- evidence strength
- fixability without a broad rewrite

Prefer a real P0/P1 correctness, security, data, money, deployment, or
workflow bug over style, architecture taste, missing polish, or generic test
coverage.

## Safe Fix Handoff

Do not start fixing during `one` mode unless the user explicitly asks for
implementation. For a confirmed issue, include a concise next-step prompt for
`safe-feature-slice` so the fix can be handled as one protected feature slice.
If there is no confirmed major issue, do not manufacture a fix handoff.

The handoff must be narrow enough to execute:

- Name the single issue to fix.
- State the invariant to preserve.
- State the unsafe outcome to prevent.
- Name the likely files or module surface.
- Include the minimum tests or runtime verification needed.
- Mention any user decision or external dependency that could block a safe
  fix.

Use this shape:

```text
Suggested safe-feature-slice fix:
Use safe-feature-slice to fix [issue title].
Invariant: [rule that must remain true].
Unsafe outcome to prevent: [bad state].
Likely scope: [files/modules].
Verification: [focused tests/checks/browser flow].
Extra instruction: [carry over any relevant user constraint from this review].
```

## Output Shape — Confirmed Finding

Return one confirmed finding only, using this shape:

```text
One major issue:
[short title]

Why it matters:
[impact in plain language]

Evidence:
- [file:line anchor and what it proves]
- [file:line anchor and what it proves]

How to reproduce or verify:
[minimal command, scenario, or reasoning path]

Fix direction:
[smallest credible fix]

Suggested safe-feature-slice fix:
Use safe-feature-slice to fix [issue title].
Invariant: [rule that must remain true].
Unsafe outcome to prevent: [bad state].
Likely scope: [files/modules].
Verification: [focused tests/checks/browser flow].
Extra instruction: [carry over any relevant user constraint from this review].

Confidence:
Confirmed / High confidence / Hypothesis, with a short reason
```

## Output Shape — Honest No-Finding

If no major issue can be responsibly confirmed in the available time or
allowed scope, say that plainly and report the best next investigative target
instead of inventing a finding.

```text
One major issue:
No confirmed major issue found in the allowed scope.

What I checked:
[brief evidence-backed scope]

Why I am not forcing one:
[why candidates did not meet the evidence bar]

Best next investigative target:
[single next surface, command, route, or module to inspect]

Confidence:
[short reason]
```

## Lessons And Memory Routing

Do not create or append `LESSONS.md` beside this skill. Use the active
environment's global lessons and memory system instead. Lessons are for
mistakes, corrections, and reusable failure-prevention rules; memories are for
durable user, project, or workflow context when the active instructions allow
memory updates. Keep entries concise and redact secrets, tokens, customer
data, and private details.
