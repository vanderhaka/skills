# Review Dimensions

Use these dimensions to stress-test a TDD plan before implementation. The goal is to catch the mistakes that are cheap to fix in planning and expensive to fix once code and tests exist.

## 1. Completeness

Check whether the plan covers the full user-facing behavior:

- missing user actions or system responses
- missing failure cases such as invalid input, auth expiry, or network errors
- missing edge cases such as empty states, boundary values, or single-item paths
- missing reverse flows such as cancel, undo, delete, or teardown
- missing feedback such as loading, success, or error states

## 2. Scope And Sizing

Check whether the issues are sliced into safe units:

- issues that touch too many files
- vague acceptance criteria that cannot turn into a clear test
- issues so small they should merge into a neighbor
- issue count that does not match the feature complexity
- issues that try to do too much at once

## 3. Dependencies And Ordering

Check whether the planned sequence will actually work:

- circular dependencies
- missing scaffold issues for types, schemas, or shared primitives
- supposedly parallel issues that touch the same files
- hooks, components, or services scheduled before their foundations exist
- integration work placed before cross-cutting concerns are ready

## 4. Technical Feasibility

Check whether the plan fits the actual codebase:

- API or service assumptions that are not real
- package or library assumptions that do not match the repo
- conflicts with current architecture or conventions
- performance risks such as N+1 queries or missing pagination
- security gaps such as missing auth checks or trusting client input

## 5. Test Strategy

Check whether the tests would prove the intended behavior:

- missing assertions compared with the acceptance criteria
- mocks that hide the real behavior too much
- shared setup that could create flaky or interdependent tests
- missing coverage for failure paths or regressions
- behaviors spanning multiple issues without a clear integration check

## 6. Assumptions And Ambiguity

Check for anything that could be interpreted two ways:

- fuzzy phrases such as `handle gracefully`
- implicit requirements that were never written down
- unclear behavior or UX decisions
- data shape assumptions, nullable fields, or default values not stated
- local-only assumptions that may fail in production

## Question Rules

When turning these findings into questions:

1. Be specific. Reference the exact issue number, file, dependency, or behavior.
2. Offer options when possible. `Should this be X or Y?` is better than an open-ended question.
3. Lead with plan-changing questions.
4. Group related questions instead of bouncing randomly across topics.
5. Skip anything the plan already answers clearly.
6. Keep a round to roughly 5-10 questions.
7. Follow up only when an answer is too thin to make the plan executable.
