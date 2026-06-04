# Commit and Memory

Use this reference only for modes that permit mutation.

## Stage and Review

Before committing, inspect what will actually be included:

```bash
git diff --cached --name-only
git diff --cached --stat
```

Review the staged diff for:

- secrets or credentials
- accidental generated artifacts
- unrelated files
- lockfile churn that was not actually needed

If anything looks wrong, fix the staging set before committing.

## Commit Message

Use Conventional Commits:

```text
<type>(<scope>): <subject>

<body>
```

Rules:

- Subject is imperative, lowercase, no trailing period, max 72 chars.
- Body explains why, what changed, and important trade-offs.
- Use the narrowest obvious scope.
- Use a single-quoted HEREDOC for multi-line messages.
- Do not add co-author trailers unless the repo or user explicitly wants them.

Before committing, show a concise summary of:

- files being committed
- separate verification-repair files or commit planned to restore green
- checks that passed
- the commit message about to be used

Then commit immediately. Do not ask for confirmation unless the staging scope is ambiguous.

## Post-Commit Memory Review

After each successful commit in the cap flow, review whether the work produced durable follow-up context.

- Run repo-local post-commit memory or lesson scripts only when they are documented and safe.
- Update lesson/memory systems only when active instructions permit it and the work uncovered a durable preference, project decision, operational detail, correction, or reusable failure pattern.
- If multiple commits happen in one cap run, avoid duplicate lesson or memory entries.

## Continuity Review

Before pushing, check whether this repo already uses continuity files such as:

- `HANDOFF.md`
- `plans/`
- `STATUS-*.md`
- repo-local notes or memory files

If the current work changed what the next session needs to know, update those existing files before pushing.

Rules:

- Preserve the repo's existing continuity system instead of inventing a new one.
- If the user explicitly asks for a handoff, use the relevant handoff workflow.
- Skip continuity edits in `cap fast` unless the changed file set is itself continuity work.
