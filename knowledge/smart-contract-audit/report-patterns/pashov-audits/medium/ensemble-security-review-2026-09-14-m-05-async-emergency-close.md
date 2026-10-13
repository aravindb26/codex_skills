# Pashov Audit Pattern: Async cancellation does not precede emergency position closing

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Ensemble Security Review` (team PDF, M-05)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Ensemble-security-review_2026-09-14.pdf>
- Dedupe decision: Distinct asynchronous cancel-before-close ordering failure.

## Core Idea

An emergency function clears local rebalance state and submits cancellation and close orders together, so an old expansion can execute after the vault believes exposure is closed.

## Broken Invariant

Emergency liquidation must observe cancellation and a fresh zero-position state before declaring leveraged exposure removed.

## Where To Look

- Async exchange or bridge operations represented by local booleans
- Emergency paths that submit cancel and close messages in one transaction
- Position snapshots taken before asynchronous settlement

## Attack Path

Leave an expansion order pending, trigger emergency close, let the cancellation and reduce-only close execute in an unsafe order, and leave the vault leveraged during recovery.

## False-Positive Checks

- Verify the external system can process the operations out of order
- Check whether the close order covers positions created after the snapshot
- Check for a later fresh-position confirmation before withdrawals resume

## PoC Shape

Model delayed cancellation and reordered fills, then assert that emergency completion is impossible while any configured position remains nonzero.

## Triage Note

Do not report a stale local flag alone; prove the external ordering can create or retain exposure with an asset-impact path.
