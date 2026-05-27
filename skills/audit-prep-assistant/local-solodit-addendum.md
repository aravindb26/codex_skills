# Local Solodit Addendum: Smart Contract Audit Prep

## Purpose

Use this companion with `audit-prep-assistant` when preparing a smart contract or Web3 codebase for a serious audit.

The goal is to turn the repository and program rules into a practical audit map before hunting: scope, actors, money flow, critical files, invariants, likely bug classes, and test targets.

## When To Use

Use this addendum before hunting when:

- starting a new contest, bounty, protocol review, or repo audit
- preparing a local codebase for manual security review
- deciding which smart contract skills and tools should be used
- creating an audit coverage ledger or initial threat model

## Companion Workflow

1. Lock the program baseline: scope, exclusions, safe harbor, severity bar, known issues, prior audits, duplicate rules, PoC requirements, and deployment assumptions.
2. Create a full in-scope file list and mark unclear files as unresolved instead of assuming.
3. Map actors and privileges: users, liquidators, keepers, solvers, relayers, bridge executors, admins, guardians, oracles, and offchain services.
4. Map money flow: where value enters, where it exits, and how it moves through internal accounting.
5. Map lifecycle state machines: deposits, withdrawals, borrows, repayments, liquidations, claims, epochs, batches, queues, finalization, settlement, bridging, and upgrade flows.
6. Search Solodit stubs and local knowledge for the protocol type and primitives.
7. Convert matching public patterns into local review questions, not assumptions.
8. Build a targeted skill plan for the audit.
9. Produce a coverage ledger before deep hunting begins.

## Solodit-Informed Prep Questions

Ask these before choosing the first hunting surface:

- Which files directly move assets or mint/burn accounting claims?
- Which functions turn external data into protocol state?
- Which paths use oracle prices, quotes, signatures, bridge messages, callbacks, or token balance deltas?
- Which lifecycle steps can be repeated, skipped, reordered, finalized, unwound, or partially completed?
- Which modules look like glue code but silently enforce core invariants?
- Which token integrations assume standard ERC20 behavior?
- Which values are scaled, rounded, cached, snapshotted, or converted across units?
- Which public reports describe similar primitives, and what exact invariant failed there?

## Suggested Skill Routing

Use the relevant focused skills based on the prep map:

- `audit-context-building` for line-by-line comprehension
- `entry-point-analyzer` for state-changing call surfaces
- `state-invariant-detection` for accounting relationships
- `dimensional-analysis` for units, decimals, shares, prices, and indexes
- `audit-oracle` and `oracle-flashloan-analysis` for price paths
- `audit-reentrancy` and `reentrancy-pattern-analysis` for callbacks and hooks
- `audit-signature` and `signature-replay-analysis` for signed authorization
- `audit-slippage` for swap and quote execution
- `audit-lending` and `audit-liquidation` for lending markets
- `proxy-upgrade-safety` for upgradeable systems
- `token-integration-analyzer` for nonstandard token behavior
- `dos-griefing-analysis` for queue, gas, and liveness edges
- `fp-check` before presenting any candidate as strong

## False-Positive Filters

During prep, do not let Solodit/public reports bias the audit into pattern matching. A public pattern is only useful if:

- the same asset or invariant exists locally
- the same missing validation is reachable locally
- the current scope rewards the resulting impact
- the current deployment and trusted roles allow the attacker path

## Output Requirements

When this addendum is used, produce:

- program baseline
- in-scope file coverage plan
- actor and trust-boundary map
- money-flow and lifecycle map
- highest-risk surfaces
- relevant skills to use
- unresolved source/scope ambiguities
