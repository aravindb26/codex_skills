# Gauge, Voting, Reward Accounting, and Cleanup Invariants

Source lesson: RAAC/Gundam private contest postmortem, July 2026. Several accepted reports were missed because similar symptoms were dismissed as known-issue overlap without proving exact root-cause equivalence.

Use this file for ve-token, gauge, staking, reward-distributor, emission, boost, and vote-cleanup audits.

## Core Lesson

Do not kill a gauge/reward candidate only because it resembles a known issue. Require exact root equality:

- same function or branch
- same state variable
- same stale cursor or denominator
- same rounding direction
- same attacker-controlled growth bound
- same payout/cursor semantics
- same impact path

If any item differs, treat it as a fresh variant until the current code disproves it.

## Mandatory Invariants

### Denominator Mutation Must Settle Dependent Integrals First

If a function mutates `workingSupply`, `totalSupply`, `boostedSupply`, `pointsSum`, or any reward denominator, every reward integral that depends on that denominator must be settled first.

Branch-specific checks matter. A main-reward branch may settle `rewardPerToken`, while an extra-reward branch may only checkpoint extras and still mutate the shared denominator.

Search terms:

```text
_updateWorkingBalance
workingSupply
_updateUserReward
_checkpointRewards
claimOnBehalfOf
claimFor
extraReward
lastUpdateTime
rewardPerTokenStored
```

Audit prompt:

```text
For every path that changes a user's working balance or global working supply, prove all reward integrals priced by that supply are settled before the mutation on every branch.
```

### Storage-To-Memory Struct Copies Can Deep-Copy Dynamic Arrays

In Solidity, assigning a storage struct containing dynamic arrays to memory deep-copies the arrays. A function that only needs `array.length` can accidentally become O(n) in accumulated history.

Danger shape:

```solidity
RewardData memory rData = rewardData[token];
cursor = uint32(rData.distributions.length);
```

Safer shape:

```solidity
cursor = uint32(rewardData[token].distributions.length);
```

Search terms:

```text
RewardData memory
memory rData
distributions.length
lock(
first lock
storage-to-memory
```

Audit prompt:

```text
For every storage-to-memory struct copy, inspect whether the struct contains a dynamic array, mapping-like field, bytes/string, or nested dynamic data. If yes, test gas growth against append-only history.
```

### Vote Reversal Rounding Must Preserve Global Weight Bounds

Forward projection and reverse cleanup must use compatible rounding. If live gauge weight decays with one rounding mode and cleanup subtracts with another, the global denominator can fall below a surviving gauge's weight.

Required invariant:

```text
pointsSum[epoch].bias >= max(pointsWeight[gauge][epoch].bias)
relativeWeight(gauge, epoch) <= 1e18
sum(relativeWeight(all gauges, epoch)) <= 1e18 + intended tolerance
```

Search terms:

```text
_reverseLockEntries
pointsSum
pointsWeight
relativeWeight
_getWeight
_projectWeight
clear vote
remove vote
```

Audit prompt:

```text
Clear or reverse votes at boundary timestamps and compare the remaining global denominator against every live gauge weight. Do not assume clamping one side preserves the ratio.
```

### Rate And Cursor Must Be Updated Atomically

Reward `rate` and `lastUpdateTime` are a coupled pair. If a new rate is installed while supply is zero, and the cursor is left stale, later supply can price the new rate over time before the reward existed.

Danger shape:

```solidity
reward.rate = newRate;
if (workingSupply > 0) {
    reward.lastUpdateTime = block.timestamp;
}
```

Search terms:

```text
rate =
lastUpdateTime
workingSupply > 0
_pullRewardsFromDistributor
notifyReward
rewardRate
periodFinish
```

Audit prompt:

```text
Whenever reward rate changes, prove the accounting cursor is advanced or the unpriced interval is explicitly carried forward. Test zero-supply, dust-supply, and supply-becomes-positive transitions.
```

### Partial Or Capped Payout Must Not Consume Full Entitlement Cursor

If a claim path caps payout to available funds or `totalDistributed`, it must not advance epochs, vesting windows, or claim cursors as if the full calculated amount was paid.

Danger shape:

```solidity
claimable = calculate(full range);
epochsClaimed = endEpoch;
payout = min(claimable, remainingPool);
transfer(payout);
```

Search terms:

```text
epochsClaimed
totalClaimed
totalDistributed
min(
cap
claimable
_claimReward
updateReward
```

Audit prompt:

```text
Force an over-subscribed reward pool and verify whether late claimers retain unpaid entitlement. Cursor movement must match paid amount, not requested amount.
```

### Cleanup Cost Must Be Bounded By Attacker-Amortized State

Setup can happen over many cheap transactions while cleanup often must happen atomically. A cleanup function that loops over `users * gauges * locks * entries` can be uncallable even if every setup call was individually valid.

Search terms:

```text
kick(
ragequit
userVotedGauges
voteUserLockEntries
maxVoteBuckets
_reverseLockEntries
delete vote
clear votes
```

Audit prompt:

```text
For every public cleanup function, calculate the maximum state an attacker can build across many transactions and the amount that must be processed in one cleanup call. If setup is amortized but cleanup is atomic, write a gas-growth harness.
```

## Known-Issue Overlap Discipline

Known issue overlap must be exact, not thematic. "Gauge rounding", "stale rewards", "claimOnBehalfOf", "kick cleanup", or "duplicate gauge state" are symptoms, not root causes.

Before killing a branch as duplicate or known, answer:

1. Is the same variable stale or corrupted?
2. Is the same function and branch responsible?
3. Is the same invariant broken by the same ordering?
4. Is the same attacker setup required?
5. Does the known issue cover this exact downstream impact?

If any answer is no, continue verification.

## Minimum Future Checks

For every gauge/reward audit, run at least these manual checks:

- Enumerate all functions that mutate a denominator used by reward math.
- Enumerate all functions that mutate rate, period, duration, or reward cursor fields.
- Search for storage-to-memory copies of structs containing dynamic arrays.
- Compare vote-add and vote-remove rounding at epoch boundaries.
- Stress claim caps, vesting cursors, and partial payout semantics.
- Stress cleanup loops with attacker-amortized state.
- Confirm known-issue equivalence by exact root cause before dismissal.
