---
name: write-goals
description: Draft, critique, or rewrite Codex /goal objectives for Goal mode. Use when the user asks to write a goal, turn a fuzzy task into a durable Codex goal, review an existing /goal prompt, decide whether /goal or /plan fits, or define success criteria and checkpoints for long-running Codex work.
---

# Write Goals

## Purpose

Turn rough intent into a Codex Goal mode objective that is bounded, verifiable, and safe for long-running autonomous work.

Goal text is both the starting prompt and the completion criteria. Write it so Codex can repeatedly answer: what should I do next, is progress converging, what must stay true, how do I prove it, and when do I stop?

## Decide The Surface

Use `/goal` when the work is bigger than one normal turn but still one coherent objective, and it has a clear validation loop or stopping condition.

Prefer `/plan` first when the target is fuzzy, product decisions are missing, or the user needs options before execution.

Do not recommend `/goal` for:

- a loose backlog of unrelated tasks
- pure research, discussion, or brainstorming with no artifact
- live-data, payment, destructive, provider-changing, or otherwise unbounded external-action work (spending, notifications, live-data mutation) without explicit caps and approval gates
- tasks with no observable end state
- work where Codex should stop after planning only
- work where success is mainly taste-dependent or requires repeated human preference choices

If the goal would exceed 4,000 characters, or the supporting brief needs more than a few compact paragraphs, keep `/goal` short and point it at a plan or brief file.

## Goal Contract

Draft one goal around the smallest contract that makes completion clear.

Always cover:

- **Objective:** one concrete outcome, not a list of loosely related wishes.
- **Starting context and baseline:** files, docs, routes, issues, logs, current failure, starting metric, artifact state, or known gap.
- **Scope boundaries:** what to preserve, what not to touch, and what is intentionally out of scope.
- **Constraints:** standards, repo conventions, safety rules, model/tool preferences, provider restrictions, or approval gates.
- **Verification:** the strongest independent check of success, plus supporting tests, browser flows, screenshots, output artifacts, or provider evidence.
- **Stop condition:** exact state where Codex should mark the goal complete.
- **Pause or blocked condition:** exact events that require stopping for user input instead of guessing.

For substantial, risky, flaky, or long-running goals, also add:

- **Iteration loop:** how Codex should respond to failed checks without redefining success.
- **Anti-cheating rules:** tests, benchmarks, scope, fixtures, and verifiers Codex must not weaken without explicit approval.
- **Checkpoints:** how Codex should break the work into resumable steps and report progress.
- **Review pressure:** when to use a skeptical review, side chat, fresh-context pass, or independent verification lane before completion.

Good goals make completion boring to judge. Weak goals use verbs like improve, clean up, explore, fix everything, or make it better without naming proof.

## Drafting Workflow

1. Extract the user's actual desired end state.
2. Identify prior behavior, data, files, or workflow that must be preserved.
3. Name risky boundaries that require explicit approval or should remain read-only.
4. Ground the goal in the smallest useful research pass: canonical local source, baseline, known attempts, tests, reproductions, or acceptance criteria.
5. Pick the smallest validation loop that proves the result and cannot be faked by weakening the proof.
6. Add checkpoint and status expectations for long-running work.
7. Ask at most three questions only when missing answers materially change the goal or safety boundary.
8. Otherwise make safe assumptions, label them, and draft the goal.

## Durable Context

Prefer the project's existing plan or progress files when they exist. If none exists and the goal needs durable context, suggest one of these files instead of stuffing detail into `/goal`:

- `GOAL.md`: outcome, baseline, constraints, success criteria, blocker criteria.
- `WORKLOG.md`: hypotheses, attempts, evidence, current state, next action.
- `RESULT.md`: final change, verification, remaining risks.

Do not create durable files in a drafting-only response. Create or update one only when the user asks for a durable artifact or asks you to set up the goal materials. Always read an existing goal packet before rewriting it.

## Red-Team Pass

For substantial or risky goals, and always before activation, check:

- Can Codex satisfy the words while missing the user's real outcome?
- Can success be faked by weakening a test, changing a benchmark, hiding a failure, over-mocking, or narrowing scope?
- Are irreversible, public, shared, costly, live-data, or provider actions separately approval-gated?
- Does the goal say what to do after a failed attempt, flaky check, or external wait?
- Is the completion evidence observable by something other than the running agent's assertion?
- If subagents are authorized, does every lane have disjoint ownership, its own verifier, and evidence to return to the parent?

## Output Format

When drafting a goal, respond with:

```text
Recommended goal:
/goal <objective, context, constraints, verification, stop condition, blocked condition>
```

Then add a short note with fit, assumptions, open risks, and activation state: `drafted`, `active`, or `not recommended`. Use `active` only when the user explicitly asked to start or set the goal and the goal tool succeeded. Keep the goal text concise enough that the user can paste it directly.

When critiquing an existing goal, use:

- **Keep:** what is already specific and useful
- **Tighten:** vague scope, missing proof, unsafe autonomy, or unrelated tasks
- **Rewrite:** a paste-ready `/goal ...` version

## Setting A Goal

Do not call `create_goal` just because you drafted goal text. Only set or start a goal when the user explicitly asks you to set, start, run, or use Goal mode.

Before setting a goal, inspect the current goal state when the tool is available. If a goal is already active or completed in the thread, do not create a competing goal. Explain the state and either follow the user's explicit edit/replace instruction or ask for the smallest clarification needed.

When a goal is active, do not mark it complete until the stated stop condition is actually achieved and verified. Mark it blocked only when the same blocker has recurred enough that no meaningful progress is possible without user input or an external change.

Never set a token budget unless the user explicitly requested one.

## Delegation

Use ordinary delegated tasks for lanes that can finish in one turn. Design goal-backed child lanes only when the user explicitly asks for subagents, parallel agent work, or a goal tree.

When goal-backed delegation is explicitly requested, keep the parent responsible for scope, integration, conflicts, and final completion. Give each child one bounded finish line, disjoint source or mutation ownership, a verifier, a stop condition, and the evidence it must return. Do not clone the parent goal into every child.

## Paste-Ready Patterns

### Implementation

```text
/goal Implement <feature> in <repo/path>. First read <context files> and record the baseline <failure/current state>. Preserve <existing behaviours>. Do not change <out of scope> or weaken <tests/benchmarks/verifiers>. Work in checkpoints with short progress notes. Verify with <tests/commands/browser flow>. Complete only when <observable end state> and <regression proof> are both satisfied. Pause and ask if <decision/risk/blocker>.
```

### Migration Or Refactor

```text
/goal Migrate <source system> to <target system> while preserving <contracts/user-visible behaviour>. Use <plan/tests/reference output> as the source of truth. Make incremental changes, run <verification> after each checkpoint, and keep rollback or compatibility where required. Complete only when <new path proof> and <regression proof> are both green. Pause if <schema/data/provider decision> is needed.
```

### Investigation With Repair

```text
/goal Diagnose and fix <symptom>. Start from <logs/repro/files> and capture the baseline failure. Do not assume the cause until reproduced. Preserve <known good behaviours>. Implement the smallest safe fix, verify with <repro/test/runtime evidence>, and summarize the root cause. Do not weaken the repro, fixture, or verifier unless explicitly approved. Complete only when the original symptom no longer reproduces across <required repeat count/state> and relevant regression checks pass. Pause if the fix requires <approval boundary>.
```

### Prototype Or Artifact

```text
/goal Build <artifact> from <brief/reference>. Keep the first screen/use case functional, not just planned. Use <style/technical constraints>. Verify by opening/running <artifact route/command> and checking <expected behavior>. Complete only when the artifact is usable and the verification evidence is reported. Pause if <missing asset/content/product decision> blocks fidelity.
```
