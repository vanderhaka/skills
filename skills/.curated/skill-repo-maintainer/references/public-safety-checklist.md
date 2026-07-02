# Public Safety Checklist

Use this checklist before publishing a skills repository or moving local skills into a public repo.

## Blockers

Do not publish files containing:

- API keys, tokens, cookies, private keys, recovery codes, or webhook secrets.
- `.env` values or screenshots of provider dashboards.
- Internal URLs, bypass URLs, deployment protection secrets, or private webhook endpoints.
- Client/customer names, emails, addresses, invoices, order details, or private business workflows unless already intended for public release.
- Instructions that let a stranger mutate a live provider account, database, payment flow, or deployment.

## Scrub Or Generalize

Replace:

- Absolute local paths with `$HOME`, `<repo>`, or repo-relative paths.
- Private GitHub owners and repo names with placeholders unless the repo is public and relevant.
- Project-specific rules with reusable decision rules.
- Live provider object IDs with fake examples.

## Keep

Keep:

- General workflow logic.
- Validation commands.
- Public documentation links.
- Reusable scripts with no embedded credentials or private endpoints.
- Examples that are synthetic, minimal, and clearly fake.

## Final Check

From the repo root, run the root validator (when the repo has one) and this skill's audit script:

```bash
python3 scripts/validate_skills.py
python3 skills/.curated/skill-repo-maintainer/scripts/audit_skill_repo.py .
git status --short
```

Adjust the audit script path to wherever this skill's `scripts/audit_skill_repo.py` lives in the target repo.

