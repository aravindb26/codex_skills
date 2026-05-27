# Local Solodit Addendum: Smart Contract Code Graphs

## Purpose

Use this companion with `trailmark` when building or querying code graphs for smart contract audits.

The goal is to make graph analysis support manual audit work: entry points, value flow, privilege boundaries, callbacks, lifecycle paths, and blast radius.

## When To Use

Use this addendum when using Trailmark on:

- smart contract repositories
- appchain modules
- cross-chain systems
- polyglot Web3 projects with onchain and offchain components

## Companion Workflow

1. Build the graph only after scope is known.
2. Tag in-scope files and exclude tests unless the program includes them.
3. Query entry points that touch assets, privileges, signatures, or external integrations.
4. Trace graph paths from attacker-controlled entry points to state writes and value movement.
5. Use Solodit/local patterns to choose which graph paths deserve manual reading.
6. Treat graph output as navigation, not proof.

## High-Value Queries

Prefer paths involving:

- asset transfer, mint, burn, debt, share, reserve, or reward updates
- oracle reads and price consumers
- external calls, callbacks, hooks, and token integrations
- signature verification and nonce updates
- bridge message validation and replay protection
- queue, batch, epoch, and settlement state machines
- initialization, upgrade, and role boundaries

## False-Positive Filters

Do not report graph findings unless manual review proves:

- real reachability
- attacker control
- missing or broken invariant
- rewardable impact
- scope alignment

## Output Requirements

When this addendum is used, include:

- graph query purpose
- files and entry points selected
- paths requiring manual review
- Solodit/local pattern that motivated each path
- confirmed findings or killed branches
