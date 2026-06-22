---
name: wwh
description: Explain or structure a decision, change, bug, issue, incident, plan, request, or confusing situation using who, what, when, where, how, and why in simple language. Use when the user asks for a plain-English 5W1H breakdown, "who/what/when/where/how/why", simple language, what changed, why a bug matters, what decision is being made, or what someone needs to know.
---

# WWH

Use this skill to turn a messy thing into a simple, useful explanation.

## Core Workflow

1. Identify the thing being explained: decision, change, bug, issue, incident, plan, request, or unknown.
2. Gather only the context needed to answer the six questions. Use repo files, logs, screenshots, tickets, chat text, or user-provided notes when available.
3. Separate facts from assumptions. If a fact is missing, say `Unknown` instead of pretending.
4. Write for a smart person who is not already deep in the details.
5. Keep the answer short unless the user asks for depth.

## Output Shape

Default to this structure, but only include sections that matter for the context:

```markdown
**Plain Summary**
One sentence saying what is going on.

**Who**
- Owner:
- Affected people:

**What**
- The thing:
- Expected vs actual:  <!-- use for bugs/incidents only -->

**When**
- Timeline:
- Deadline or decision point:

**Where**
- Place in product/process/code/team:

**How**
- How it happens or how it will be done:

**Why**
- Reason, goal, or root cause:

**So What**
- Impact:
- Next step:
```

Delete any field or heading that does not apply. Do not include empty or irrelevant `Who`, `What`, `When`, `Where`, `How`, or `Why` sections just to complete the set.

## Plain-Language Rules

- Use short sentences and concrete nouns.
- Prefer common words over jargon. If jargon is necessary, define it once in plain language.
- Do not use filler phrases such as "leverage", "synergy", "robust", or "seamless" unless quoting source text.
- Do not hide uncertainty. Use `Unknown`, `Assumption`, or `Needs confirmation`.
- Do not over-explain process. The user wants the useful shape of the thing.

## Task-Specific Guidance

For a bug or incident:

- Explain the user-visible failure first.
- Include expected behavior, actual behavior, likely cause, affected area, and next proof step.
- Keep root-cause claims tied to evidence. If root cause is not proven, say "likely cause" or "unknown".

For a decision or change:

- Name the decision owner, affected groups, options if known, chosen direction, timing, and reason.
- Clarify what changes for the user, team, codebase, or business.
- Call out the smallest next action needed to unblock the decision.

For a plan or request:

- State who needs to act, what needs to happen, where it applies, when it matters, how to start, and why it matters.
- If the user needs something paste-ready for another person, write it in direct first-person or direct-request language.

## Missing Information

If the user gave too little information, do not stall by default. Produce the best useful breakdown with `Unknown` entries and end with the one most important question or next fact needed.

Ask before answering only when a wrong assumption could materially mislead someone about responsibility, timing, customer impact, money, security, compliance, or production behavior.
