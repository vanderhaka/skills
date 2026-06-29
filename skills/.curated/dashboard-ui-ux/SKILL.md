---
name: dashboard-ui-ux
description: Production SaaS and data dashboard UI/UX guidance for building, critiquing, or refactoring dashboards, admin panels, analytics views, CRM/ops consoles, billing screens, dense tables, KPI cards, charting surfaces, sidebars, filters, and contextual actions. Use when a user asks for dashboard design, dashboard UX review, mock-data dashboard proof, tactical UI polish, or conversion from a dashboard blueprint/spec into an implementable interface.
---

# Dashboard UI/UX

## Overview

Use this skill to produce dense, polished dashboard interfaces that feel operational, not marketing-led. Favor direct layouts, native controls, existing design systems, and the smallest component set that proves the workflow.

## Workflow

1. Identify the dashboard's actor, repeated workflow, key records, and risky decisions before styling.
2. Start with the usable app surface: sidebar, page header, KPI row, primary table/list, secondary analytics, and contextual actions.
3. Use realistic mock data when real data is unavailable; include enough rows and edge cases to test density, filtering, empty states, and status colors.
4. Keep advanced controls behind disclosure. Put search, filters, sort, date range, and bulk action affordances where users expect them.
5. Verify the interface in browser with desktop and narrow/mobile widths before calling it done.

## Layout Rules

- Use a 4px spacing system. Keep 32px between distinct layout blocks.
- Keep dashboard typography compact. Use one sans-serif family; cap prominent dashboard text at 24px.
- Keep `letter-spacing: 0` when current frontend standards prohibit negative tracking. Use weight, line-height, and spacing for polish instead.
- Avoid page-section cards and nested cards. Use cards only for repeated items, metrics, modals, and genuinely framed tools.
- Make the dashboard canvas visibly distinct from cards through background contrast, borders, and restrained shadow; cards should read as foreground without looking floaty.
- Prefer quiet, scan-friendly density over oversized hero sections, decorative panels, or explanatory feature copy.

## Component Rules

- Sidebar: profile card at top, grouped ghost-button navigation in the middle, settings/help/billing at bottom, clear active indicator, and a real collapse/expand control on desktop unless the product intentionally forbids it.
- Buttons: horizontal padding should be about 2x vertical padding. Include hover, active, disabled, and loading states for real actions.
- Iconography: use Lucide or the repo's icon library when available. Match icon size to adjacent text line-height. Do not use emojis.
- KPI cards: group summary numbers once; do not repeat the same KPI elsewhere.
- Data cards: top-left identifier, top-right critical metric/status, body label, bottom metadata.
- Tables: use subtle dividers and whitespace, not heavy grid lines. Include search, filtering, sorting, row actions, and a contextual bulk-action surface when selection exists.
- Charts: include grid lines, axis numbers, a summary total, a date range control, and exact hover values.
- Overlays: use popovers for non-blocking filters/settings, modals for complex creation, and toasts for confirmation/error feedback.

## Proof Checklist

- Initial load works with realistic mock or fixture data.
- Search, filters, sorting, row selection, and at least one primary action produce visible UI feedback.
- Empty state appears when filters remove all rows.
- Chart hover or focus exposes exact values.
- Narrow viewport keeps controls usable and text inside containers.
- Browser smoke records route, viewport, action tested, visible result, console/network status, and skipped checks.

## Reference

Read `references/dashboard-ui-blueprint.md` when building a full dashboard, auditing a dense UI, or resolving component-level details.
