# Domain Modeling Checklist

Use this reference when `grill-with-docs` is changing domain language, not merely reading it.

## What To Challenge

- overloaded terms such as account, customer, user, order, booking, lead, project, subscription, status, active, cancelled, complete
- actor names that mix people, companies, systems, and roles
- lifecycle states that are missing transitions or terminal states
- ownership rules that decide who can see, edit, delete, approve, pay, or recover something
- business rules that code appears to implement differently from the user description
- product copy that teaches users a different model from the database or API

## Scenario Questions

Prefer concrete scenarios over abstract taxonomy:

- What happens when the actor changes midway through the lifecycle?
- Can two actors own the same record at once?
- What is allowed before payment, after payment, after cancellation, and after deletion?
- Is this state reversible?
- Who can perform the action on behalf of someone else?
- What should happen to existing records when the rule changes?
- Which word would a real user use for this concept?

## Documentation Targets

Write only durable context:

- `CONTEXT.md`: canonical terms, actor relationships, lifecycle language, and business meaning.
- `plans/<feature-slug>/decisions.md`: feature-specific decisions, safe defaults, rejected options, blockers, and downstream implications.
- `docs/adr/YYYY-MM-DD-short-title.md`: hard-to-reverse decisions with real alternatives and future-reader value.

Do not put implementation details in `CONTEXT.md` unless the implementation name is also the domain term.

## Output Add-On

When domain modeling was active, include:

```text
Domain terms clarified:
Glossary conflicts resolved:
Scenarios tested:
Code/docs contradictions:
```
