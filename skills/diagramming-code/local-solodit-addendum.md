# Local Solodit Addendum: Smart Contract Audit Diagrams

## Purpose

Use this companion with `diagramming-code` when diagrams help a smart contract audit.

The goal is to visualize security-critical flows clearly: money flow, lifecycle transitions, cross-chain messages, trust boundaries, and exploit paths.

## When To Use

Use this addendum when:

- the protocol has complex state machines
- a candidate spans several contracts or modules
- a report needs a clear attack path
- cross-chain, oracle, liquidation, or settlement flows are hard to explain

## Companion Workflow

1. Choose a diagram type based on audit need: call graph, money flow, state machine, trust boundary, or exploit sequence.
2. Include only security-relevant nodes.
3. Mark actors, assets, privileged roles, external integrations, and state writes.
4. Compare diagrammed flows against known public bug patterns.
5. Use the diagram to find missing checks or stale assumptions, then verify in code.

## False-Positive Filters

Diagrams are explanatory, not proof. Do not use a diagram alone to claim:

- reachability
- exploitability
- impact
- duplicate uniqueness

## Output Requirements

When this addendum is used, include:

- diagram purpose
- source files used
- key security assumptions shown
- flows that need manual verification
- confirmed or killed candidate paths
