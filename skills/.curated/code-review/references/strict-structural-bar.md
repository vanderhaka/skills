# Strict Structural Bar Reference

Load this reference when running `code-review` in `strict` mode, or when the
user asks for a "thermo", "thermo-nuclear", "thermonuclear", "deep code
quality audit", or "especially harsh maintainability review". This absorbs the
retired `thermo-nuclear-code-quality-review` skill's direct-invocation core
prompt and question checklist. The Structural Standards, Approval Bar
presumptive blockers, and Review Tone phrasing for this bar already live in
the main `code-review/SKILL.md` — this file adds only what is not already
stated there.

## Core Prompt

Start from this baseline, substituting the user's stated scope for "the
current branch's changes" when one is given:

> Perform a deep code quality audit of the current branch's changes.
> Rethink how to structure / implement the changes to meaningfully improve code quality without impacting behavior.
> Work to improve abstractions, modularity, reduce Spaghetti code, improve succinctness and legibility.
> Be ambitious, if there is a clear path to improving the implementation that involves restructuring some of the codebase, go for it.
> Be extremely thorough and rigorous. Measure twice, cut once.

Be ambitious about structural simplification. Do not stop at "this could be a
bit cleaner." Look for opportunities to reframe the change so that whole
branches, helpers, modes, conditionals, or layers disappear entirely. Prefer
the solution that makes the code feel inevitable in hindsight. Assume there is
often a "code judo" move available: a re-organization that uses the existing
architecture more effectively and makes the change dramatically simpler and
more elegant. If you see a path to delete complexity rather than rearrange it,
push hard for that path.

## Primary Review Questions

For every meaningful change, ask:

- Is there a "code judo" move that would make this dramatically simpler?
- Can this change be reframed so fewer concepts, branches, or helper layers
  are needed?
- Does this improve or worsen the local architecture?
- Did the diff add branching complexity where a better abstraction should
  exist?
- Did a previously cohesive module become more coupled, more stateful, or
  harder to scan?
- Is this logic living in the right file and layer?
- Did this change enlarge a file or component past a healthy size boundary?
- Are there repeated conditionals that signal a missing model or missing
  helper?
- Is the implementation direct and legible, or does it rely on special cases
  and incidental control flow?
- Is this abstraction actually earning its keep, or is it just a wrapper?
- Did the diff introduce casts, optionality, or ad-hoc object shapes that
  obscure the real invariant?
- Is this logic living in the canonical layer, or did the diff leak details
  across a boundary?
- Is this orchestration more sequential or less atomic than it needs to be?

## Standalone Direct-Invocation Note

When this bar is invoked directly for a maintainability-only audit (no
correctness, security, test, or merge-readiness scope requested), scope the
review to structural findings only and still report through the standard
`code-review` output shape. When correctness, security, tests, or
merge-readiness are also in scope, that is a normal `strict`-mode review — use
the full `code-review/SKILL.md` flow, not a maintainability-only pass.
