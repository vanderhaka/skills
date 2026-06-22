# Ask James

## What This Skill Does

`ask-james` routes a task to the right skill in James's Codex stack. It is the front door when the user is not sure whether to review, plan, grill, build, debug, commit, or hand off.

It also supports an inventory mode: use `ask-james list` or ask to list skills to see every curated James skill with a quick summary.

## Use It When

- The user asks which skill to use.
- The task is broad or ambiguous.
- The user asks for the next best workflow step.
- The user asks for `list`, all curated skills, or what skills are available.
- You need to decide between `feature-orchestrator`, `safe-feature-slice`, `codebase-design`, `prototype`, `code-review`, `issue-fix-strategy`, `bug-ripple`, `cap`, or another curated skill.

## How It Works

The skill recommends exactly one next skill by default, with a short reason and one optional alternative when the tradeoff matters. If the user asked only for advice, it stops there. If the user asked to proceed, it continues with the recommended workflow. In list mode, it skips routing and prints the curated skill inventory.

## What You Get

- A clear recommended skill.
- A plain-English reason.
- A warning for when not to use it.
- At most one alternative.
- A full curated skill list when `list` is requested.

## Not For

Do not use this when the correct skill is already explicit and the user wants action. In that case, use the named skill directly.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/ask-james
```

Restart Codex after installing new skills.
