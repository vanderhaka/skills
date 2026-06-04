# Push and Branch Safety

Use this reference only for modes that permit push.

## Push Default

A normal `cap` run pushes the resulting commit(s) to the current branch's upstream, including shared branches such as `main`, `master`, `production`, or `release`.

Do not stop just because the current branch is shared.

Stop before pushing only when:

- the user explicitly asks for `cap dry-run`
- the user says not to push
- the user asks for local-only packaging
- freshness/divergence/branch-protection checks fail

## Upstream Check

Check whether the branch has an upstream:

```bash
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

## Freshness Guard

Before pushing to a shared branch, fetch remote refs first:

```bash
git fetch --prune
git status --short --branch
```

If the branch has diverged or is behind its upstream, stop and report the divergence instead of attempting to push.

Do not rebase, merge, or pull automatically during cap unless the user explicitly asked for that.

## Push Rules

- If upstream exists, push normally.
- If upstream does not exist and `origin` exists, use `git push -u origin HEAD`.
- If no suitable remote exists, stop and report that instead of guessing.
- Never force-push.
- If push is rejected because of non-fast-forward or branch protection, report the exact reason and stop.

## Branch Snapshot

Branch snapshot is not part of the default fast path. Run it for `cap release`, when the user asks about branch hygiene, or when branch state is relevant to the handoff.

```bash
git for-each-ref --sort=-committerdate refs/heads/ \
  --format='%(refname:short)|%(committerdate:relative)|%(subject)'
```

Summarize each branch in one line with:

- branch name
- how recently it changed
- latest commit subject

Flag branches untouched for 2 or more weeks as stale.
