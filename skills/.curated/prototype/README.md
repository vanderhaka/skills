# Prototype

## What This Skill Does

`prototype` builds a disposable experiment to answer one question before full implementation.

## Use It When

- The user wants UI options before committing to a design.
- A state model or workflow needs to be felt out interactively.
- A product direction is unclear and a tiny artifact would answer it faster than discussion.
- The work should not become production code yet.

## How It Works

The skill chooses either a logic prototype or a UI prototype, writes the question first, builds the smallest runnable artifact, captures the answer, and recommends deleting, isolating, or promoting the useful part.

## What You Get

- A clear prototype question.
- A runnable command or URL.
- A focused artifact for judging the design or state model.
- A cleanup or promotion path.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/prototype
```

Restart Codex after installing new skills.
