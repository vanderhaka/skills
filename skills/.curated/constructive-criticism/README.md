# Constructive Criticism

## What This Skill Does

`constructive-criticism` delivers a maximum-effort, evidence-backed critique of any work product — code, plans, documents, designs, architecture, copy, UX, or ideas — at any scale from a single function to an entire repo. Every finding is verified (by running code, tests, checks, or research) before it is reported, and every finding carries a concrete fix.

## Use It When

- You want honest, hard feedback on work before shipping or sharing it.
- You want a repo, feature, route, PR, plan, or document stress-tested.
- You want findings specific enough to hand to another engineer or a fresh agent context to fix without re-investigation.
- You say things like "tear this apart", "poke holes in this", "be brutal", or "what's wrong with this".

## How It Works

The skill identifies the target, matches its strategy to the scope (single deep pass at unit level, live exercise at feature level, subsystem decomposition with parallel agents at repo level), and runs seven critique lenses: correctness, completeness, structure, clarity, simplicity, risk, and fitness for purpose. Nothing unverified is presented as fact — suspected findings are labeled with what would confirm them.

## What You Get

- A full report at `plans/critiques/<target>-critique.md` with numbered findings (Where / Current behavior / Why it matters / Evidence / Fix / Done when).
- An Execution contract in the report: fix order, parallel-safe groups with write boundaries, skip list, constraints, per-fix verification protocol, and completion-report format.
- A short paste-ready handoff prompt in chat that points a fresh context at the report as the source of truth.
- Genuine strengths, "the one thing" to fix first, and a calibrated ship/fix/rethink verdict.

## Not For

Use `code-review` when the target is code under review specifically for correctness or merge readiness — a diff, a PR, a branch. This skill owns everything else (plans, docs, designs, copy, product ideas, mixed work products) plus any holistic "tear this apart" request that goes beyond merge review. Use `code-review` in `one` mode when you want exactly one confirmed finding. Use `launch-critical-sweep` for pre-launch P0/P1 blocker coverage.

## Install

Copy this folder into your skills directory:

- Claude Code: `~/.claude/skills/constructive-criticism/`
- Codex: `~/.codex/skills/constructive-criticism/`

Restart the agent session after installing.
