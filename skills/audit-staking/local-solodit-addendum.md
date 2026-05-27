# Local Solodit Addendum: Staking Companion Mini-Skill

## Purpose
- Extend `audit-staking` with distilled High/Medium Solodit staking and rewards patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this for missing exploit shapes around reward indexes, epoch boundaries, insufficient reward balances, and double claims.

## When To Use

Use after reading `audit-staking/SKILL.md` when code handles:
- staking, vault shares, rewards, emissions, epochs, vesting, validator stake/unstake queues, reward tokens, or claim accounting.

## Companion Workflow

1. Load the original staking skill first.
2. Search current code with the extra terms below.
3. Trace deposit, reward accrual, claim, withdraw, emergency exit, and reward top-up flows.
4. Test first depositor, zero total stake, dust stake, same-block deposit/withdraw, long epoch gap, and insufficient reward balance.
5. Search Solodit stubs by reward variable, epoch function, and claim path before escalating.

## Extra Search Terms

```text
rewardIndex
rewardPerToken
userRewardPerTokenPaid
accReward
claimable
claimed
lastRewardTime
rewardRate
periodFinish
epoch
cycle
vesting
stakeDuration
confirmChange
unstake
emission
rewardsWallet
totalStaked
zero total stake
```

## Missing / Sharper Patterns To Check

### 1. Zero-total-stake and first-deposit inflation

Shape:
- Reward/share math behaves differently when no one is staked or the first depositor controls initial exchange rate.

Questions:
- Where do rewards emitted before first stake go?
- Can the first staker claim historical rewards or set share price?
- Are virtual shares, minimum stake, or seed liquidity used correctly?

### 2. Reward token balance is assumed available

Shape:
- Claim or principal withdrawal depends on a reward wallet/pool balance that can be insufficient, paused, or separately drained.

Questions:
- Can lack of reward tokens block principal withdrawals?
- Are rewards pulled from a wallet that may not have allowance/balance?
- Is failure isolated to rewards, or does it lock all exits?

### 3. Reward index stale across top-up, readd, or rate change

Shape:
- Adding/removing reward tokens, changing rate, or topping up rewards does not settle old accrual first.

Questions:
- Are user indexes updated before reward configuration changes?
- Can re-adding a reward token corrupt `userRewardPerTokenPaid`?
- Does `set_rate` or top-up reset already-accrued fees/rewards?

### 4. Epoch, duration, and timestamp boundary bugs

Shape:
- Stake duration, epoch, reward cycle, or vesting state is uninitialized, stale, off by one, or bypassable.

Questions:
- Can users unstake immediately due to uninitialized duration?
- Can long gaps make claim loops revert or over-accrue?
- Can anyone front-run vesting/account creation to block it?

### 5. Double claim or missing claim finalization

Shape:
- Claim path transfers rewards before marking claimed, or unwind/retry paths preserve claimable state.

Questions:
- Is claimed state written before external calls?
- Can accrue/unwind/claim order double count rewards?
- Are historical tickets/epochs marked claimed exactly once?

### 6. Validator or queued stake griefing

Shape:
- Stake/unstake request queues can be flooded to block validator collateral claims or reward processing.

Questions:
- Can malicious users create many pending stake changes cheaply?
- Are queue processing limits and pagination safe?
- Does one validator/user's bad request block others?

## False-Positive Filters

Do not escalate unless:
- The issue affects user rewards, principal withdrawals, staking shares, validator collateral, or protocol solvency.
- The attacker can reach the edge state without trusted-role abuse.
- Reward loss/dilution/DoS is quantifiable or reproducible.
- Same-token staking or admin-seeded rewards are not explicitly documented and safe.
