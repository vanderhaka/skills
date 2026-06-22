# WWH

## What This Skill Does

`wwh` turns a messy decision, change, bug, issue, incident, plan, or request into a simple who/what/when/where/how/why explanation.

## Use It When

- The user asks for a plain-English breakdown.
- The user asks who, what, when, where, how, or why of a thing.
- A bug, decision, or change needs to be explained to someone who is not deep in the details.
- The user wants the important context without empty sections or filler.

## How It Works

The skill identifies the thing being explained, separates facts from assumptions, and writes a short explanation using only the relevant 5W1H sections. If one of the sections does not matter for the context, it is omitted.

## What You Get

- A plain summary.
- Relevant who/what/when/where/how/why sections.
- Impact and next step when useful.
- Unknowns called out directly.

## Not For

Do not use this for deep investigation, full code review, broad planning, or root-cause analysis when the underlying facts have not been gathered yet. Use the relevant diagnostic or planning skill first, then use `wwh` to explain the result.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/wwh
```

Restart Codex after installing new skills.
