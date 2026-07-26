# Pashov Audit Pattern: Kick cleanup loops over attacker-amortized gauge and lock state

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: unbounded cleanup, liveness

## Core Idea

A user can build many vote entries across many transactions, but `kick` or cleanup must reverse all entries atomically. If cleanup loops over `userVotedGauges[user]` and nested `voteUserLockEntries[user][gauge]`, gas can exceed the block limit and leave stale votes uncleanable.

## Broken Invariant

State that can be created over many transactions must not require unbounded single-transaction cleanup for protocol correctness.

## Where To Look

- `kick`
- `ragequit`
- `userVotedGauges`
- `voteUserLockEntries`
- `maxVoteBuckets`
- `_reverseLockEntries`
- nested loops over gauges and locks

## Attack Path

Create many locks and vote across many gauges in separate transactions. After an action that requires cleanup, call the public cleanup function and observe it cannot process all entries within gas.

## False-Positive Checks

- Confirm setup is allowed across multiple transactions.
- Confirm cleanup is atomic and has no cursor/pagination.
- Confirm default or production parameters allow many entries.
- Do not dismiss as generic stale-vote issue if the root is amortized setup versus atomic cleanup.

## PoC Shape

Create maximum practical locks, vote across many gauges, trigger cleanup requirement, and measure or assert `kick` runs out of gas while smaller setups pass.
