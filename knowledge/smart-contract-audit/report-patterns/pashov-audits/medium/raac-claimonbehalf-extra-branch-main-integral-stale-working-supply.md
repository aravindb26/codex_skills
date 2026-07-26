# Pashov Audit Pattern: Extra-reward claim changes working supply without settling the main reward integral

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: gauge reward accounting

## Core Idea

A claim branch that handles extra rewards can mutate a user's working balance and global `workingSupply` without first settling the main reward integral. The next main-reward settlement then prices a stale time interval using the new denominator.

## Broken Invariant

Any mutation to a denominator used by reward math must settle every integral that depends on that denominator before the mutation, on every branch.

## Where To Look

- `claimOnBehalfOf`, `claimFor`, or split claim functions
- Extra-reward-only checkpoint paths
- `_checkpointRewards` vs `_updateUserReward`
- `_updateWorkingBalance`
- `workingSupply`
- `lastUpdateTime`

## Attack Path

Trigger the extra-reward branch for one user, change their working balance, then let another user claim main rewards. The stale main integral can be underpriced or overpriced for all stakers depending on denominator movement.

## False-Positive Checks

- Verify the branch really updates `workingSupply`.
- Verify the main reward cursor is not advanced before the denominator change.
- Compare against every branch, not only the normal main-claim branch.
- Do not mark duplicate unless the known issue covers this exact branch and denominator/integral ordering.

## PoC Shape

Two stakers, one main reward stream, one extra-reward claim path that changes boost or working balance. Compare expected main reward split with actual payout after the branch.
