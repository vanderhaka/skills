---
name: basic-skill
description: Replace this with a specific trigger-focused description that explains what the skill does and when Codex should use it.
---

# Basic Skill

## Overview

State the narrow capability this skill adds. Keep this short.

## Workflow

1. Inspect the user's request and the local repository context.
2. Load only the references or scripts needed for the task.
3. Execute the workflow with the smallest safe file and state changes.
4. Verify the result with command output, tests, browser checks, or source evidence.
5. Report changed files, checks run, residual risks, and behavior-preservation confidence when code changed.

## Resources

Add only the resource folders the skill actually needs:

- `scripts/` for deterministic helpers.
- `references/` for longer docs loaded on demand.
- `assets/` for templates and output resources.

