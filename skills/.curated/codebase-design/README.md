# Codebase Design

## What This Skill Does

`codebase-design` gives James's skill stack one shared architecture vocabulary for deep modules, interfaces, seams, adapters, and test surfaces.

## Use It When

- A module or feature boundary is unclear.
- A refactor needs architecture judgement before coding.
- Code is hard to test because callers know too much.
- A review finds shallow wrappers or scattered orchestration.
- Another skill needs a reusable design standard.

## How It Works

The skill names the target behavior, identifies what callers currently need to know, proposes a smaller useful interface, decides where seams and adapters belong, and states how behavior should be tested through the interface.

## What You Get

- A recommended interface shape.
- A clear seam and dependency strategy.
- A test-surface recommendation.
- Trade-offs and next skill routing.

## Install

```bash
$skill-installer install https://github.com/vanderhaka/skills/tree/main/skills/.curated/codebase-design
```

Restart Codex after installing new skills.
