# Pashov Audit Pattern: A guardian resolution commitment survives a changed pending history

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-03)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-09-17.pdf>
- Dedupe decision: Distinct commitment-reuse pattern; the hash omits mutable state such as collapse status, time, and change identity.

## Core Idea

A guardian commitment hashes only endpoint values and decomposition, so a later history can return to those endpoints and satisfy an old proposal.

## Broken Invariant

An approval or timelock commitment must bind the exact state transition that will execute, not only a state that can recur later.

## Where To Look

- Guardian or multisig hashes over live pending state
- Pending records mutated without clearing commitments
- Endpoint-only commitments without monotonic nonce, timestamp, or change identity

## Attack Path

Propose one transition, mutate the pending history through additional actions, return to the original endpoints, and execute the stale decomposition against the changed history.

## False-Positive Checks

- Confirm the pending state can mutate during the timelock
- Check every mutable field that affects execution is covered by the commitment
- Verify execution does not reload or revalidate the exact observed transition

## PoC Shape

Commit to A -> B, execute an intervening B -> C -> B cycle, and assert that the original commitment is rejected or incorrectly accepted.

## Triage Note

This is a state-commitment/replay issue, not merely a missing nonce best practice; prove wrong decomposition or value attribution.
