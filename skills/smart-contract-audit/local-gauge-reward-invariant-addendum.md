# Local Gauge and Reward Invariant Addendum

## Purpose

Use this after `smart-contract-audit/SKILL.md` for gauge, ve-token, staking, reward-distributor, emission, boost, and vote-cleanup audits.

This addendum exists because prior audits missed accepted findings by treating "similar to known gauge issue" as enough to stop. It is not enough. Known-issue overlap requires exact root-cause equality.

## Mandatory Routing

Load the knowledge lesson:

```text
/home/dinesh/.codex/knowledge/smart-contract-audit/bug-patterns/gauge-reward-accounting-and-cleanup-invariants.md
```

Then route to focused skills when relevant:

- `audit-staking` for reward accrual, boost, vesting, and claim paths.
- `state-invariant-detection` for supply, denominator, cursor, and vote-weight invariants.
- `audit-math-precision` and `dimensional-analysis` for rounding, scaling, and relative-weight math.
- `dos-griefing-analysis` for kick, cleanup, queue, and unbounded-loop paths.
- `fp-check` before killing a candidate as known, intended, or weak.

## Required Searches

Run these search groups or equivalent codebase-specific variants:

```text
claimOnBehalfOf|claimFor|claimReward|claimExtra|_checkpointRewards|_updateUserReward|_updateWorkingBalance
workingSupply|totalSupply|boostedSupply|rewardPerTokenStored|lastUpdateTime|rewardRate|rate =
RewardData memory|memory rData|distributions.length|storage-to-memory
_reverseLockEntries|pointsSum|pointsWeight|relativeWeight|_getWeight|_projectWeight
epochsClaimed|totalClaimed|totalDistributed|claimable|_claimReward|updateReward
kick\(|ragequit|userVotedGauges|voteUserLockEntries|maxVoteBuckets|clear vote
```

## Do-Not-Skip Checks

1. Every denominator mutation must settle every dependent integral first on every branch.
2. Every reward rate replacement must update or reconcile the accounting cursor immediately.
3. Storage-to-memory struct copies must be checked for hidden dynamic-array deep copies.
4. Vote reversal math must be checked against forward/projection rounding and `relativeWeight <= 1e18`.
5. Capped payout paths must preserve unpaid entitlement instead of consuming the full claim cursor.
6. Cleanup functions must be bounded against state an attacker can build over many transactions.
7. Known issue overlap must be exact: same function, same branch, same variable, same invariant, same impact path.

## Required Candidate Questions

Before marking a gauge/reward branch `NOT WORTH SUBMITTING`, answer:

- What exact invariant was tested?
- Which current-code path proves the invariant cannot break?
- Did the branch differ from known issues in state variable, branch, rounding, cursor, or cleanup bound?
- Was zero-supply, dust-supply, first-user, late-claimer, boundary-epoch, and max-state cleanup tested or disproven?
- If a PoC was not written, what exact code condition makes a PoC unnecessary?

If these answers are not concrete, the branch is not finished.
