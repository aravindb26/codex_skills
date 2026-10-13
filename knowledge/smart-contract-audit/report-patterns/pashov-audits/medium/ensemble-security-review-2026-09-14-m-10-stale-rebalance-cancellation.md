# Pashov Audit Pattern: Stale rebalance cancellation can freeze the vault permanently

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Ensemble Security Review` (team PDF, M-10)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Ensemble-security-review_2026-09-14.pdf>
- Dedupe decision: Distinct stale-cancellation state machine; not merged with emergency close ordering because it blocks the cancellation/recovery transition itself.

## Core Idea

A cancellation path derives its request from stale rebalance state, so the external venue rejects the cancellation and the vault cannot clear the pending state.

## Broken Invariant

Every reachable pending-order state must have a valid cancellation or recovery transition that eventually restores deposits, redemptions, and rebalancing.

## Where To Look

- Cancellation functions using cached order ids, nonces, or asset lists
- Retry paths after partial fills, expiration, or venue-side rejection
- State machines where one failed cancel leaves all user actions gated

## Attack Path

Leave an order in a stale or partially updated state, trigger cancellation, and show that every later retry uses invalid state and keeps the vault frozen.

## False-Positive Checks

- Confirm the stale state is reachable through normal venue behavior
- Test all alternate cancellation and admin recovery paths
- Prove the lock affects user value movement, not only a keeper view

## PoC Shape

Simulate an expired or partially filled order, call the public cancellation path repeatedly, and assert that no valid transition clears the pending flag.

## Triage Note

Require a persistent user-impacting lock; a single retryable venue error is not enough.
