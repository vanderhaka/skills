# Dashboard UI Blueprint

Use this reference for tactical dashboard construction and critique. The active `SKILL.md` has the operating checklist; this file carries the fuller source blueprint.

## Global Systems

### Spatial System

- Base unit: 4px.
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64.
- Desktop: fluid width; prioritize whitespace over strict column adherence.
- Tablet: use 8-column grid guidelines.
- Mobile: use 4-column grid guidelines.
- Maintain 32px between distinct layout blocks.

### Typography Engine

- Use one sans-serif family only.
- Dashboard text should stay compact; max prominent size is 24px.
- Original blueprint suggested negative tracking for headers and display numbers. Current Codex frontend standards require `letter-spacing: 0`; keep spacing at `0` and use line-height, weight, and layout rhythm instead.
- Use 110% to 120% line-height for H1, H2, and prominent numbers.

### Color And Depth

- Start from one primary brand color, then derive light backgrounds and darker text from it.
- Do not use arbitrary AI-generated hex piles. Keep palettes intentional and not one-note.
- Light mode cards: shadows should be low opacity, high blur, and slight Y-axis offset. If the shadow is obvious first, reduce it.
- Dashboard backgrounds should be distinct from foreground cards through subtle contrast, borders, and restrained depth.
- Popovers need stronger elevation than standard cards.
- Dark mode: create depth through brightness differences, not shadows.
- Dark mode chips, borders, and colored text should have lower saturation and brightness to avoid eye strain.
- Never place text directly on raw images; use a gradient/blur treatment that creates a readable text surface.

## Component Anatomy

### Iconography

- Prefer Phosphor, Lucide, or the repo's existing icon set.
- Do not use emojis or mismatched icon line weights.
- Icon size should match adjacent text line-height. For 14px text on 20px line-height, use a 20x20 icon.

### Buttons And Actions

- Standard button padding: horizontal padding about 2x vertical padding.
- Use ghost buttons for secondary calls to action and sidebar navigation.
- Include default, hover, active/pressed, disabled, and loading states.
- Copy-to-clipboard and similar micro-actions must create visible physical feedback, such as a toast or confirmation chip.

### Sidebar Navigation

- Sidebar is the app spine.
- Top slot: profile management in a card layout, with avatar, name, and dropdown arrow.
- Middle slot: primary navigation grouped by intent, using ghost buttons with icon and short text.
- Bottom slot: settings, help, billing.
- Active indicator: left-edge vertical rectangle or high-contrast fill.
- Desktop sidebars should expose a clear collapse/expand control unless the product intentionally forbids collapse.
- Collapsed sidebars should move nested links into popovers.

### Data Cards

- Internal padding: 20px to 24px.
- Top-left: visual identifier such as avatar, logo, or semantic icon.
- Top-right: critical metric such as status, price, or bold total.
- Body: primary label in larger, darker type.
- Bottom: secondary metadata, muted and smaller.

### Tables And Lists

- Avoid heavy grid lines. Use whitespace and subtle 1px dividers.
- Include checkboxes for bulk actions.
- Selecting items should reveal contextual bulk actions or a floating bar.
- Collapse edit/delete into row menus, or reveal icon actions on hover.
- Tables need search, filtering, and sorting.

### Analytics And Charts

- Do not repeat the same KPI numbers in multiple places.
- Line charts need grid lines, axis numbers, summary totals, and a date range selector.
- Bar charts should include identifying icons such as favicons or avatars beside labels.
- Hovering over a data point should show exact values or percentages.
- Hovering over one bar should dim the others.
- Use maps with shaded regions when spatial data is the real decision surface.

### Billing And Pricing

- Maximum three plans.
- Monthly cost is the largest visual element; plan name is secondary.
- Annual discounts should state the exact saving.
- Checkmarks should describe what each plan adds over the previous plan.

## Interaction Architecture

- Progressive disclosure: show what the user needs, reveal more when asked.
- Creation flows: place basic inputs front and center; tuck advanced options behind a toggle.
- Optimistic UI: safe updates/deletes can update immediately before the server responds, then recover on failure.
- Popovers are non-blocking and close on outside click.
- Modals are blocking and require Cancel or Save.
- Toasts communicate success, warnings, and errors without blocking the screen.
