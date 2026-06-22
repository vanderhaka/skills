# Deepening Shallow Modules

Use this reference when the task is to improve a cluster of shallow modules, scattered helpers, pass-through wrappers, or awkward tests.

## Dependency Categories

Classify the dependencies before moving code:

- `In-process`: pure computation or in-memory state. Usually safe to move behind a deeper interface and test directly.
- `Local-substitutable`: filesystem, local database, or queue behavior that has a local test stand-in. Keep the external seam internal and test with the stand-in.
- `Remote but owned`: another service or worker controlled by the same product. Define a port where the network boundary is real, then use production and test adapters.
- `True external`: third-party API or provider. Inject the provider-facing adapter and test against fake or mocked behavior without hiding provider failure modes.

## Deepening Process

1. Pick one cluster, not the whole repo.
2. Identify the behavior callers actually need.
3. Design the desired external interface before rearranging files.
4. Move behavior behind that interface.
5. Delete or shrink callers that used to orchestrate the same details.
6. Replace brittle internal tests with behavior tests through the new interface.
7. Keep adapter tests narrow: they prove translation to the dependency, not the whole business workflow.

## Replace, Do Not Layer

Do not add a new deep module on top of the old shallow stack and leave both concepts active. If the deeper module earns its place, callers should move to it and the old pass-through code should shrink or disappear.

## Stop Conditions

Stop and recommend a smaller slice when:

- callers disagree on the behavior they need
- the domain language is unresolved
- the dependency category is unclear
- tests cannot prove current behavior before movement
- the proposed interface needs too many flags, modes, or escape hatches
