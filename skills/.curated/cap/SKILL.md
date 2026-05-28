---
name: cap
description: Run repo-appropriate checks, actively repair safe verification failures until the repo is green when possible, commit only the intended files or necessary repair files with Conventional Commit messages, and push safely. Use when the user says cap, asks to commit and push, or wants one flow that checks, commits, and pushes without sweeping unrelated changes into the commit.
---

# Cap

## Overview

Use this skill when the user wants one flow that verifies the current work, creates a clean commit, and pushes it.

The job is not "push whatever is lying around." The job is to push the intended work safely.
The preferred end state is a green verification run, not a report about why the repo stayed red.

## Core Rules

- Never skip verification unless the user explicitly accepts an unverified commit.
- Treat all-green verification as the target. If a required check is red and the fix is safe, local, and deterministic, repair it before offering a best-effort commit.
- Never stage unrelated changes just to make the commit convenient.
- Never commit secrets, `.env*`, private keys, tokens, or credential files.
- Never use destructive git commands such as `git reset --hard`, `git checkout --`, or force-push.
- Never use interactive git flows when a non-interactive command will do.
- Respect the active repo rules, dirty-worktree constraints, and Codex editing rules.

## Special Trigger

- `cap dry-run` means: run the cap flow up to the point where it would mutate git or remote state, then stop.
- In dry-run mode, inspect scope, choose verification commands, run safe read-only checks when useful, identify env drift, propose staging, and draft the commit message.
- In dry-run mode, do not stage, commit, push, deploy, create branches, mutate continuity files, or run auto-fix commands.
- `cap only` means: only commit changes made in this session or the explicitly requested file set.
- If that file set is ambiguous from the thread or git state, ask which files to include.
- If `cap only` conflicts with a needed baseline repair outside that file set, ask whether to create a separate repair commit first or stop without committing.

## Workflow

### 1. Preflight and Project Detection

Run these read-only inspections in parallel when possible.

Git state:

```bash
git status --short --branch
git diff --stat
git diff --cached --stat
git log --oneline -5
git rev-parse --abbrev-ref HEAD
```

Project detection from the repo root:

- `package.json` -> Node / JS / TS
- `pyproject.toml`, `requirements.txt` -> Python
- `Cargo.toml` -> Rust
- `go.mod` -> Go
- `Gemfile` -> Ruby

For Node repos, detect the package manager from the lockfile or `packageManager` field:

- `pnpm-lock.yaml` -> `pnpm`
- `yarn.lock` -> `yarn`
- `bun.lockb` or `bun.lock` -> `bun`
- otherwise use `npm`

In monorepos, run checks from the narrowest package root that contains the changed files unless the repo clearly requires root-level verification.

Repo-local cap hooks:

- If the repo documents cap hooks in `AGENTS.md`, `CONTRIBUTING.md`, `HANDOFF.md`, `scripts/`, or a project runbook, read the relevant hook instructions before staging.
- Run only hooks that are safe, repo-local, and directly relevant to verification, release, deploy, or continuity.
- Do not print private runbook sections or credential-bearing content. Use narrow reads and redact secrets.
- Do not invent global hooks for one repo's workflow.

After inspection:

- Decide the exact candidate files for staging.
- Prefer exact paths with `git add -- <path>...`.
- Do not use `git add -A`.
- If the worktree is already dirty, leave unrelated changes alone.
- If no relevant changes remain after filtering, stop and say so.

Push-default policy:

- A normal `cap` run pushes the resulting commit(s) to the current branch's upstream, including shared branches such as `main`, `master`, `production`, or `release`.
- Do not stop just because the current branch is shared.
- Stop before pushing only when the user explicitly asks for `cap dry-run`, says not to push, asks for local-only packaging, or when freshness / divergence / branch-protection checks fail.

### 2. Verification and Env Sync Check

Run code verification and the Vercel env-var sync check in parallel when they are independent.

Parallel safety:

- Only parallelize checks when their outputs are isolated.
- Do not parallelize commands that write the same generated output, cache, build directory, test database, lockfile, or other shared state.
- For Next.js and similar frameworks, do not run `build` and typecheck in parallel when either command may touch shared generated types such as `.next/types`.
- For database-backed tests, serialize test commands unless each process has an isolated database.

Node / JS / TS:

- Lint: repo lint script if present, otherwise `eslint` if configured
- Typecheck: `tsc --noEmit` if TypeScript is present
- Format check: only if a formatter is configured
- Tests: repo test script if it is real, or the established project runner
- Build: repo build script if present

Python:

- Lint: `ruff check .` or `flake8`
- Typecheck: `mypy` when configured
- Tests: `pytest`
- Format check: `black --check .` when configured

Other ecosystems:

- Use the standard lint, test, and build commands for that ecosystem if they are clearly configured in the repo.
- If the repo does not make the commands clear, say so instead of inventing commands.

Vercel env sync check:

- Skip silently if the `vercel` CLI is unavailable or no project is linked.
- Extract key names from `.env.local`, ignoring blank lines and comments.
- Never print `.env.local` values. Use a line-based parser that reports only key names or redacted presence flags.
- Run `vercel env ls` for the linked project.
- Compare both directions:
  - Local-only keys: missing at deploy time
  - Vercel-only keys: stale or not pulled locally
- Report mismatches as warnings, not blockers.
- For auth-capable web apps, also sanity-check public URL and auth redirect envs:
  - Identify URL-like keys such as `NEXT_PUBLIC_SITE_URL`, `NEXT_PUBLIC_APP_URL`, `SITE_URL`, `APP_URL`, `AUTH_URL`, `NEXTAUTH_URL`, `SUPABASE_AUTH_EXTERNAL_*`, and callback or redirect URL vars.
  - Never print secret values. It is acceptable to print non-secret public URL origins and redacted presence flags.
  - Flag production URL values that are localhost, preview-only domains, missing `https://`, or contain leading/trailing whitespace/newlines.
  - If Supabase auth is used, verify the app builds recovery and invite links through the intended public origin and callback route, not `window.location.origin` alone when that could inherit localhost or a preview URL.
  - If the Management API token is not safely available, do not guess or mutate Supabase Auth settings; report the required dashboard checks instead: Auth Site URL should be the production domain, redirect allowlist should include the callback route, and recovery/invite templates should use `{{ .ConfirmationURL }}` unless the app intentionally verifies tokens itself.
  - When a URL env value is changed, trigger or watch a fresh deployment before declaring cap complete, because Vercel env changes are only picked up by new deployments.

### 3. Failure Handling

General rule:

- When a required check fails, first decide whether it is safe to repair locally, even if the failure is outside the user's intended diff.
- Keep the user's requested changes and any verification-repair changes distinct in your reasoning and staging plan.
- Do not stop at the first "unrelated existing file" failure if restoring green is straightforward and reviewable.

Lint or format failures:

- Auto-fix when the tool supports it.
- Keep only safe, mechanical fixes.
- Re-run the check.
- Limit to 3 fix loops per category.

Typecheck or build failures:

- Fix when the failures are caused by the current changes or when a baseline failure has a clear, local, deterministic repair.
- Safe examples include stale imports, drifted type signatures, broken test typings, or narrow config mismatches.
- If the repair touches files outside the intended scope, prefer a separate preparatory commit when that keeps the history clearer.
- Re-run after each fix.
- Limit to 3 fix loops per category.

Test failures:

- Fix failures when they are local and deterministic, including safe baseline failures that block green verification.
- If failures look flaky, environment-specific, externally blocked, or risky to diagnose automatically, stop and report them instead of guessing.
- If required services, env vars, or fixtures are missing, say so explicitly.
- Limit to 3 fix loops per category.

When baseline failures are outside the intended diff:

- Treat green verification as the preferred outcome, not proof that the current task must stop.
- Repair the baseline when the change is small, reviewable, and unlikely to hide product decisions.
- If restoring green requires extra files, keep them out of the user's feature commit when a separate repair commit is the clearer option.
- If the repair is tiny and inseparable from the main change, one commit is acceptable, but explain it in the commit body and summary.

Hard stop:

- Stop before committing only if required verification still fails after the bounded repair attempts, unless the user explicitly authorizes a best-effort commit.

### 4. Stage and Review the Exact Commit

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

### 5. Commit

Use Conventional Commits:

```text
<type>(<scope>): <subject>

<body>
```

Rules:

- Subject is imperative, lowercase, no trailing period, max 72 chars
- Body explains why, what changed, and any important trade-offs
- Use the narrowest obvious scope
- Use a HEREDOC for the commit message
- Do not add co-author trailers unless the repo or user explicitly wants them

Before committing, show a concise summary of:

- files being committed
- any separate verification-repair files or commit planned to restore green
- checks that passed
- the commit message you are about to use

Then commit immediately. Do not ask for confirmation unless the staging scope is ambiguous.

### 6. Memory and Continuity Review

After each successful commit in the cap flow, review whether the session produced a durable lesson, memory, or repo-continuity update.

Rules:

- Use any repo-local memory, lesson, or handoff mechanism documented by the active environment.
- If no such mechanism exists, do a brief manual review instead of inventing files.
- Record only durable mistakes, preferences, project decisions, operational details, or references.
- Redact secrets and private provider/account details.
- If multiple commits happen in one cap run, avoid duplicate entries.

### 7. Continuity Review

Before pushing, check whether this repo already uses continuity files such as:

- `HANDOFF.md`
- `plans/`
- `STATUS-*.md`
- repo-local notes or memory files

If the current work changed what the next session needs to know, update those existing files before pushing.

Rules:

- Preserve the repo's existing continuity system instead of inventing a new one.
- If the user explicitly asks for a handoff, use `$handoff`.

### 8. Push

Check whether the branch has an upstream:

```bash
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

Freshness guard:

- Before pushing to a shared branch, fetch remote refs first with a non-destructive command such as `git fetch --prune`.
- Re-check `git status --short --branch` after fetch.
- If the branch has diverged or is behind its upstream, stop and report the divergence instead of attempting to push.
- Do not rebase, merge, or pull automatically during cap unless the user explicitly asked for that.

Push rules:

- If upstream exists, push normally
- If upstream does not exist and `origin` exists, use `git push -u origin HEAD`
- If no suitable remote exists, stop and report that instead of guessing
- Never force-push
- If push is rejected because of non-fast-forward or branch protection, report the exact reason and stop

Repo-specific deploy after push:

- If the repo has an established post-push deploy script, release workflow, or runbook, follow it exactly after the push only when the user requested the full ship/deploy flow or the repo's active instructions make deploy part of cap.
- Preserve production data and volumes by default.
- Run one-off hosted/runtime code as the app/runtime user when applicable; avoid root-owned runtime artifacts.
- Verify the documented health checks and any queue/worker/state checks the runbook requires.
- If no exact deploy script or runbook is available, stop and report that deploy is pending instead of improvising remote commands.

### 9. Post-Push Snapshot and Deployment Watch

After a successful push, run the branch snapshot and Vercel deployment watch in parallel when possible.

Branch snapshot:

```bash
git for-each-ref --sort=-committerdate refs/heads/ \
  --format='%(refname:short)|%(committerdate:relative)|%(subject)'
```

Summarize each branch in one line with:

- branch name
- how recently it changed
- latest commit subject

Flag branches untouched for 2 or more weeks as stale.

Vercel deployment watch:

- If `vercel` is unavailable or the repo is not linked, skip silently.
- Check the latest deployment with plain `vercel ls`; this installed CLI rejects `--limit`.
- Treat the first deployment row as the newest deployment, or use the URL printed first after the table.
- If the latest deployment is already `Ready`, `Error`, or `Canceled`, report it inline and stop.
- Otherwise, start a recurring 60-second check and report each tick briefly.
- Stop the watch when the deployment reaches `Ready`, `Error`, or `Canceled`.
- Treat `Ready` as success.
- Treat `Error` or `Canceled` as the start of an automatic recovery loop, not the end of the flow.
- If the watch cannot run in the background in the current environment, keep it in the foreground until it reaches a terminal state or the user asks to stop.
- If the watch runs for an unusually long time, continue reporting state rather than silently stopping.

Automatic recovery loop for failed deploys:

- When a deployment fails, inspect the failure immediately.
- Prefer Vercel MCP tools when available for deployment status and build or runtime logs.
- Otherwise use the best available CLI inspection commands such as `vercel inspect` and deployment logs.
- Classify the failure:
  - build error
  - runtime error
  - missing or mismatched env var
  - config or routing issue
  - external or authorization blocker
- If the cause is local and deterministic, fix it automatically.
- Re-run the narrowest relevant local verification before creating the next commit:
  - build issues -> build plus any nearby typecheck or lint
  - runtime issues -> the most relevant app tests plus build when needed
  - env or config issues -> relevant config validation plus build
- Stage only the fix-related files.
- Create a follow-up Conventional Commit, push it, and restart the 60-second deployment watch.
- Continue this diagnose -> fix -> verify -> commit -> push -> watch loop until the deployment reaches `Ready`.
- Do not stop just because one deployment failed; keep iterating automatically unless a real blocker appears.
- Stop after 3 follow-up recovery commits in one cap run, or earlier if the same failure signature repeats after a fix.
- When the recovery cap is reached, report the latest deployment identifier or URL, the repeated failure evidence, and the files changed during recovery.

Hard blockers for the recovery loop:

- missing secrets or credentials that Codex cannot safely create
- authorization, billing, quota, or org-level Vercel restrictions
- failures caused by external outages
- ambiguous product decisions or destructive schema or data migrations
- repeated nondeterministic failures where the root cause is not knowable from the repo and logs

When blocked:

- Stop and report the exact blocker, the latest deployment identifier or URL, and the evidence from logs.
- Do not fabricate env values, disable protections, or guess at risky production changes just to force a green deploy.

### 10. Final Workspace State and Evidence

Before finishing, run:

```bash
git status --short --branch
```

Report whether the repo is clean.

If files remain dirty:

- Separate intentionally excluded unrelated files from possible leftovers.
- Name any remaining staged files as a problem to fix before finalizing, unless the run stopped early before commit.
- If the remaining dirty files are generated artifacts from verification, remove them only when doing so is safe and non-destructive; otherwise report them clearly.

Command transcript:

- Include the exact verification commands that mattered.
- Include the exact commit hash and subject when a commit was created.
- Include the exact push target when a push succeeded.
- Include the deployment URL or deployment identifier and final status when a deploy watch ran.
- Keep the transcript concise; it should be enough for handoff/debugging, not a full terminal log.

## Output Format

Use this structure:

```text
## Cap Summary

### Scope
- Files to commit: ...
- Excluded unrelated changes: ...
- Verification repairs: <list or "none">

### Checks
- Lint: PASS | FAIL | SKIPPED
- Types: PASS | FAIL | SKIPPED
- Tests: PASS | FAIL | SKIPPED
- Build: PASS | FAIL | SKIPPED

### Env Vars
- Synced | <n> local-only | <n> Vercel-only | Skipped (no Vercel)

### Commit
<sha> <type>(<scope>): <subject>

### Continuity
- Updated files: <list or "none">

### Push
Pushed to <remote>/<branch>

### Open Branches
- <branch> | <last activity> | <last commit>

### Vercel
Ready | Recovering after failure | Error (blocked) | Canceled (blocked) | Building | Skipped

### Final Workspace
Clean | Dirty: <brief explanation>

### Evidence
- Commands: <key commands run>
- Deployment: <url/id and final status, or "not applicable">
```

If the flow stops early, say exactly why:

- no relevant changes
- dry-run complete
- ambiguous staging scope
- explicit no-push / local-only request
- verification failure after repair attempts
- push rejection

## Self-Refining Loop

Before each run, read the last 10 entries from `LESSONS.md` beside this `SKILL.md` if it exists.
After each run, append exactly two lines to that `LESSONS.md`: `input pattern: ...` and `result: what worked or failed, plus the fix`.
If `LESSONS.md` does not exist, create it beside this `SKILL.md` before appending.
Keep entries concise and redact secrets, tokens, customer data, and private details.
After every 10-20 entries, distill repeated lessons into durable rules in this `SKILL.md`, preserving the raw `LESSONS.md`.
