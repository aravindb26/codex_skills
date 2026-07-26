# Pashov Audit Pattern: Replacing reward rate while supply is zero leaves a stale cursor

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: reward accrual, zero-supply state

## Core Idea

A reward pull or notify path replaces `rate` while `workingSupply` is zero but only updates `lastUpdateTime` when supply is positive. Later, when supply appears, the new rate is applied from the old cursor, backdating rewards to time before the rate existed.

## Broken Invariant

Reward rate and reward cursor are coupled. Whenever rate changes, the cursor must be advanced or the unpriced interval must be explicitly accounted for.

## Where To Look

- `rate =`
- `lastUpdateTime`
- `workingSupply > 0`
- `_pullRewardsFromDistributor`
- `notifyReward`
- `periodFinish`
- zero-supply branches

## Attack Path

Keep supply at zero, pull or notify a new reward rate, wait or reuse an old cursor, then enter supply and claim rewards for a time interval that should not accrue under the new rate.

## False-Positive Checks

- Confirm rate changes before the cursor update condition.
- Confirm cursor remains stale when supply is zero.
- Confirm later calculation multiplies current rate by `block.timestamp - lastUpdateTime`.
- Do not dismiss as a generic first-staker issue if the root is rate/cursor non-atomicity.

## PoC Shape

Zero supply, advance time, pull rewards, add stake, update rewards, and compare paid rewards against the interval after the pull only.
