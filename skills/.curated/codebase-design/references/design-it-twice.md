# Design It Twice

Use this reference when a design decision is important enough that the first plausible interface may not be good enough.

## When To Use

Use this for modules that are central, hard to reverse, likely to grow, or already causing repeated bugs and awkward tests.

Do not use it for tiny helpers, one-off UI polish, or obvious mechanical refactors.

## Process

1. Frame the design target:
   - current pain
   - callers
   - invariants
   - dependencies
   - constraints
2. Produce at least three materially different interface shapes:
   - minimal interface
   - flexible interface
   - common-case-first interface
   - adapter-oriented interface, when a real remote or provider seam exists
3. Compare them on:
   - caller simplicity
   - behavior hidden behind the interface
   - testability through the interface
   - seam placement
   - domain-language fit
   - cost to migrate
4. Recommend one option or a hybrid.
5. Name what would make the recommendation wrong.

## Output

```text
Design target:
Option A:
Option B:
Option C:
Comparison:
Recommendation:
Risk:
Next proof:
```
