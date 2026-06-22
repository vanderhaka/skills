# Logic Prototype

Use this branch when the uncertainty is about state, business rules, workflow, data shape, or an API.

## Shape

Build a tiny interactive runner around a small pure core:

- reducer
- state machine
- plain functions over a data type
- small module with explicit methods

The runner is disposable. The pure core may later be lifted into production if the design proves useful.

## Process

1. Write the question at the top of the prototype or in a short README.
2. Use the host project's language and runner.
3. Keep all state in memory unless persistence is the question.
4. Show the full relevant state after every action.
5. Keep commands obvious, such as `[a] approve`, `[r] reject`, `[q] quit`.
6. Add one command to run it, using the existing task runner when available.
7. Capture what the prototype proved before deleting or promoting anything.

## Avoid

- real provider calls
- production databases
- polished error handling
- generic frameworks for a one-question experiment
- hiding state changes in logs that are hard to compare
- letting terminal UI code leak into the pure core
