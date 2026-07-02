---
name: constructive-criticism
description: Deliver maximum-effort constructive criticism of any work product at any scale — a single function, a route, a feature, a PR, a plan, a document, a design, or an entire repo or product. Use whenever the user asks for constructive criticism, a critique, honest or harsh feedback, "tear this apart", "poke holes in this", "what's wrong with this", "be brutal", devil's advocate, a second opinion, or wants work stress-tested before shipping or sharing — even if they don't say the word "criticism". Runs at maximum depth by default, verifies claims with every available tool, and spawns a bounded number of parallel agents when the target is large enough to warrant them. Produces a findings report file (plans/critiques/) plus a short paste-ready handoff prompt so a junior engineer or fresh agent context can fix every finding without re-investigating. When the target is code under review specifically for correctness or merge readiness (a diff, PR, or branch), route to code-review instead — this skill owns everything else (plans, docs, designs, copy, product ideas, mixed work products) and any holistic "tear this apart" request that goes beyond merge review.
---

# Constructive Criticism

## Goal

Give the user the critique a world-class peer would give: direct, evidence-backed, and actionable. Every criticism earns its place by carrying three things — what is wrong, why it matters, and a concrete way to make it better. Criticism without a path forward is complaint; this skill never stops at complaint.

This is not a roast and not a compliment sandwich. Flattery wastes the user's time and false negatives cost them real damage later. The kindest possible feedback is the truth, organized so they can act on it.

If the user appends text after invoking the skill, treat it as binding extra instruction (scope, focus area, audience, constraints).

**Boundary with code-review**: when the target is code under review specifically for correctness or merge readiness — a diff, a PR, a branch — route to the `code-review` skill instead. This skill owns everything else: plans, docs, designs, copy, product ideas, mixed work products, and any holistic "tear this apart" request that goes beyond merge review (architecture, product fit, an entire repo, a feature considered end to end).

## Effort Level

Default to **maximum effort**. That means:

- Read the entire target, not a sample. For code, read the files and their callers; for a plan, read the code it will touch; for a doc, read what it references.
- Verify instead of speculating. Run the code, run the tests, type-check, execute the query, fetch the URL, search the web for the claimed fact or the prior art. A criticism you confirmed is worth ten you guessed.
- Take multiple independent passes with different lenses (see below) rather than one general read.
- Only scale down when the user explicitly asks ("quick pass", "just a skim") or the target is genuinely trivial.

Thinking time is not the bottleneck. Draft the critique, then reread it adversarially: would a staff-level reviewer sign this? Is anything vague, unverified, or missing a fix?

## Identify the Target

Figure out what is being critiqued before critiquing:

- **Uncommitted work**: `git status` / `git diff` if the user says "my changes", "this branch", "before I commit".
- **Code / repo area**: the named files plus enough surrounding context (callers, tests, schema, config) to judge them fairly.
- **Plan / document / spec**: the file or pasted text, plus the codebase or facts it makes claims about — critique the plan against reality, not in a vacuum.
- **Design / UI / live product**: run it and look at it (dev server, browser tools, screenshots) rather than critiquing from source alone.
- **Prose / idea in the message**: the message itself; research external claims before judging them.

If the target is genuinely ambiguous, ask once, briefly. Otherwise pick the obvious reading, state it, and proceed.

## Match the Approach to the Scope

Maximum effort means maximum *useful* depth at the given scale — the strategy changes with the size of the target:

- **Unit level** (a function, a file, a doc, a single screen): one deep pass by you. Read it and everything it touches. Agents add overhead, not rigor. Findings can be exhaustive.
- **Feature / route / PR level** (a route and its data flow, a feature across several files, a branch diff): read all of it plus its blast radius — callers, tests, schema, the docs it contradicts. Exercise it live (run the route, click the flow, trigger the edge cases), don't judge it from source alone. Fan out lens agents if the surface is too big for one context to hold honestly.
- **Repo / product level**: reading everything at full depth is impossible, so don't pretend to. Map first — file tree, manifests, docs, schema, route map, test layout — then decompose into subsystems and spawn one agent per subsystem carrying all lenses (or one agent per lens across the whole repo, whichever matches the repo's shape). Follow with a synthesis pass you do yourself: at this scale, cross-cutting themes ("error handling is inconsistent everywhere", "there is no ownership check pattern") are worth far more than a backlog of local nits. Be explicit about what was sampled versus read exhaustively — silent sampling reads as full coverage and misleads.

Lens emphasis shifts with scale too: unit level leans correctness and clarity; feature level leans completeness and fitness for purpose; repo level leans structure, risk, and consistency of conventions. Cover every applicable lens regardless — this is about where the depth goes.

## Critique Lenses

Cover every lens that applies to the target's type. Each lens is an independent pass — do not let one strong finding satisfy the whole review.

1. **Correctness** — Does it actually work / hold true? Bugs, logical errors, false claims, broken flows. Verify by execution wherever possible.
2. **Completeness** — What is missing? Unhandled cases, unanswered questions, skipped audiences, absent error paths, gaps between what it promises and what it does.
3. **Structure** — Is it organized so a newcomer succeeds? Architecture, information flow, abstraction quality, file/section layout, dependencies.
4. **Clarity** — Can the intended audience understand it? Naming, jargon, buried ledes, ambiguity, misleading framing.
5. **Simplicity** — Is anything over-built? Unnecessary abstraction, premature generality, scope creep, complexity that will tax every future reader.
6. **Risk** — How does this fail in the real world? Security, data integrity, money paths, performance under load, operational failure modes, reputational exposure.
7. **Fitness for purpose** — Even if flawless internally, does it solve the actual problem for the actual audience? Is there a stronger approach entirely?

## Use Every Tool Available

Adapt to the environment; the standard is the same either way — no unverified criticism presented as fact.

**Claude Code**: everything is fair game — file reading and search, Bash (tests, builds, type checks, linters), LSP, git history, dev-server/browser preview tools, web search and fetch for factual claims and prior art, and connected MCP tools when relevant. If the `codex` CLI is installed, an independent second-model opinion (`codex exec` with a focused critique prompt, read-only sandbox) is a legitimate extra lens for high-stakes targets.

**Codex**: same investigation standard using the shell — `rg`, file reads, running tests and builds, `git log`/`blame`, web search if enabled.

Findings you could not verify are still reportable — label them explicitly as suspected, with what evidence would confirm them.

## Spawning Agents

Spawn parallel agents when the target is large or multi-faceted enough that one context would go shallow: several lenses over a big diff, a multi-file feature, a plan touching many subsystems, or a product critique needing code reading plus live-app testing simultaneously.

Cap fan-out at 8 concurrent agents per wave. If the natural split (subsystems × lenses) exceeds that, group subsystems into at most 8 batches and run waves sequentially rather than spawning everything at once — never launch an unbounded number of agents in one message.

- **Claude Code**: launch one agent per lens (or per subsystem), up to the cap above, via the Agent tool, all in a single message so they run concurrently. Give each a self-contained prompt: the exact target, its single lens, the verification standard ("confirm by reading/running, not by guessing"), and the required return shape (findings with file:line or section, severity, why it matters, suggested fix). Critique agents are read-only — say so in the prompt.
- **Codex**: no agent tool — run background `codex exec` subprocesses (read-only sandbox) as workers, or take the lens passes sequentially yourself. Sequential passes at full depth beat one shallow combined pass.

You are the editor, not a courier: verify agents' claims sample-wise, deduplicate, kill anything that doesn't survive scrutiny, and rank what remains. Small targets don't need agents — a single deep pass by you is faster and just as rigorous.

## Deliverables

The critique produces two things: a report file and a handoff prompt. The report is written for an implementer who has **zero access to this conversation** — a junior engineer or a fresh agent context must be able to open the file and fix every finding without re-investigating or asking questions. That standard drives everything below: if a finding needs the reader to "figure out" anything, it isn't done.

### 1. The report file

Write the full critique to `plans/critiques/<target-slug>-critique.md` (create the directory if needed; honor a different path if the user gives one). Derive `<target-slug>` as a short kebab-case name for the target (file/route/feature name, or a 2-4 word summary for a repo-wide or prose target — e.g. `plans/critiques/full-repo-critique.md`, `plans/critiques/checkout-flow-critique.md`). If a file at that path already exists, overwrite it — the report reflects the latest critique of that target, not a history of them. ALWAYS use this structure:

```
# Critique: [target]
[One paragraph: what was reviewed, at what depth, what was read exhaustively vs sampled.]

## What's genuinely strong
[2-4 real strengths — specific, never padding. What should be kept or repeated.]

## Findings
[Ranked by severity: Critical / Major / Minor. At repo/product scale, group by theme or subsystem,
lead with cross-cutting themes, cap at the findings that would actually change a decision, and
summarize the long tail in one paragraph instead of dumping a backlog. For each finding:]
### [F1] [severity] — [one-line statement of the problem]
- **Where**: exact file path(s) and line numbers, section, or screen
- **Current behavior**: what the code/doc does now — quote the relevant lines or claim
- **Why it matters**: the concrete consequence if unaddressed
- **Evidence**: what you ran/read/checked (or "suspected — unverified, confirm by ...")
- **Fix**: the specific change to make — which function/section, what it should do instead,
  edge cases the fix must preserve. Concrete enough to implement without judgment calls;
  include a sketch of the code or wording when that removes ambiguity.
- **Done when**: how the implementer verifies the fix — the command to run, the test to
  pass or write, the behavior to observe.

## The one thing
[If they fix only one thing, this is it, and why.]

## Verdict
[Honest overall read: ship it / fix criticals first / rethink the approach. One short paragraph.]

## Execution contract
[This section is the binding work order — the implementer follows it, not their own judgment
about sequencing. Spell out:]
- **Fix order**: the exact sequence (e.g., F3 → F1 → F5 → F2), with the reason when it isn't
  obvious — dependencies between findings, shared files, "F3's schema change must land before
  F1's query fix", riskiest first, etc.
- **Parallel groups**: which findings can be fixed concurrently by separate workers, and which
  must stay sequential. Declare a group parallel-safe only when you verified its findings touch
  disjoint files with no shared contract (type, schema, API shape) between them — when in doubt,
  keep it sequential. Give each group an explicit write boundary (the files it may touch) so
  parallel workers cannot collide, and state where the groups rejoin (e.g., "Group A (F2, F5)
  and Group B (F4) in parallel after F3 lands; full verification only after both merge").
  If nothing is parallel-safe, say so explicitly rather than leaving it to inference.
- **Skip list**: findings that are optional or explicitly deferred (typically Minors), so the
  implementer doesn't guess at scope.
- **Constraints**: what must not change — files/behaviors that are off-limits, patterns to
  preserve, "read-only toward the DB", branch/commit rules.
- **Per-fix protocol**: after each finding, run its Done-when check before starting the next;
  what to do on failure (stop and report vs retry once).
- **Full verification**: the project's complete check command(s) to run after all fixes
  (tests, type check, lint, build — the actual commands for this repo).
- **Completion report**: what to report back — each finding marked fixed / skipped / disputed
  (with reasoning and evidence for disputed ones).
```

Number findings (F1, F2, ...) so the contract, handoff, and any follow-up conversation can reference them unambiguously. The execution contract must be self-sufficient: assume the implementer reads only this file, never the chat.

### 2. The chat handoff

In chat, give a short summary (verdict, counts by severity, the one thing) — do not duplicate the full report — followed by a paste-ready handoff prompt in a fenced code block. The prompt is directional, not the contract: it points at the file and establishes the file's authority. Do not restate fix order, constraints, or verification details in the prompt — anything worth saying there belongs in the Execution contract instead. Shape:

```
Read plans/critiques/<slug>-critique.md in full before changing anything.

It contains [N] verified findings ([counts by severity]) from a critique of [target].
Execute its "Execution contract" section exactly — fix order, skip list, constraints,
per-fix Done-when checks, and the completion report format are all defined there.
The file is the source of truth; if anything in it seems wrong, stop and flag it in
your report rather than improvising.
```

Only the bracketed summary bits vary — the block must work verbatim when pasted into a fresh context.

## Tone

- Critique the work, never the person. "This function loses the error" not "you forgot".
- Be specific or be silent — every finding names its location and its fix.
- No hedging on confirmed findings; explicit labeling on suspected ones.
- Strengths must be real. If you can't find genuine strengths, say the work needs a rethink rather than inventing praise.
- Do not soften the verdict to be agreeable, and do not manufacture severity to seem thorough. Calibrated is the goal: a "ship it" from this skill should mean something.
