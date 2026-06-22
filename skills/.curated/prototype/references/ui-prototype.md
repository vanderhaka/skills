# UI Prototype

Use this branch when the uncertainty is about page structure, layout, information hierarchy, interaction model, or visual direction.

## Shape

Prefer variants inside the real page or nearest realistic host. A prototype with real navigation, density, copy, and data pressure is more useful than a clean empty route.

Use a throwaway route only when no existing surface can host the idea.

## Process

1. Write the design question.
2. Default to three variants. Never exceed five without a strong reason.
3. Make variants structurally different, not just different colors or copy.
4. Keep existing data fetching and auth when using an existing page; only swap the rendered subtree.
5. Use a visible prototype switcher or URL parameter so variants are easy to compare.
6. Keep mutations stubbed or read-only unless the mutation itself is the design question.
7. Verify in a real browser before asking for design judgement.
8. Capture the winning direction and delete or fold in the rest.

## Variant Bar

When appropriate, add a small fixed switcher that:

- cycles previous and next
- updates the URL or local route state
- shows the current variant label
- is clearly marked as prototype-only
- is gated out of production builds when the project has a production build concept

## Avoid

- variants that differ only by color, spacing, or copy
- shared layouts that make every variant secretly the same
- wiring prototype UI to real destructive writes
- leaving prototype routes or switchers behind after the decision is made
- promoting prototype code without rewriting the production-quality parts
