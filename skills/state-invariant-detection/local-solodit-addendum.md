# Local Solodit Addendum: State Invariant Companion Mini-Skill

## Purpose
- Extend `state-invariant-detection` with distilled High/Medium Solodit accounting-desync patterns.
- Do not replace `SKILL.md` or references.
- Use this for missing invariant shapes around stale aggregates, debt/collateral sync, queue lifecycle, cross-chain accounting, and fee/reward drift.

## When To Use

Use after reading `state-invariant-detection/SKILL.md` when code has:
- shares/assets, supply/balances, debt/collateral, queues, settlements, bridge messages, rewards/fees, vault accounting, or lifecycle status variables.

## Companion Workflow

1. Load the original state invariant skill first.
2. Search current code with the extra terms below.
3. For each aggregate variable, identify the per-user/per-position/per-chain records it summarizes.
4. Trace every function that updates only one side of the relationship.
5. Search Solodit stubs by aggregate variable, lifecycle function, and invariant shape before escalating.

## Extra Search Terms

```text
totalAssets
totalShares
globalShares
localShares
totalDebt
activeDebt
totalCollateral
pending
withheld
settled
finalized
processed
claimed
burned
minted
bridgeSupply
chainSupply
rewardIndex
feeGrowth
currentBatch
```

## Missing / Sharper Patterns To Check

### 1. Stale aggregate used for mint, burn, or refund

Shape:
- A total, active debt, share supply, withheld amount, or pool balance is read before it is updated, causing incorrect mint/burn/refund/accounting.

Questions:
- Is aggregate state refreshed before user shares/assets are calculated?
- Can stale totals let users mint more, burn less, or receive excess refund?
- Does one path update aggregate while another equivalent path forgets?

### 2. Global and local accounting diverge

Shape:
- Global vault/pool totals and local user/market/chain totals change by different formulas or at different times.

Questions:
- Does sum(local) equal global after deposit, withdrawal, settlement, fee, and loss?
- Are settlement fees applied consistently to both sides?
- Can cross-chain or per-vault supply drift from global supply?

### 3. Debt and collateral lifecycle desync

Shape:
- Debt, collateral, shares, or health state changes outside the main borrow/repay/liquidate paths.

Questions:
- Can transfer/burn/migration change a debt-bearing object without debt validation?
- Does liquidation update collateral, debt, bad debt, and total assets atomically?
- Can stale debt/collateral make health factor wrong?

### 4. Queue, batch, and status handoff gaps

Shape:
- Requests move through pending/finalized/settled/unwound/claimed states, but status and accounting can be skipped, repeated, orphaned, or processed out of order.

Questions:
- Can a later batch transition make older requests unreachable?
- Are request counts, hashes, totals, and statuses updated together?
- Can failed settlement leave assets locked while counters reset?

### 5. Mint/burn conservation broken by alternate paths

Shape:
- Main mint/burn path preserves supply, but a helper, bridge, liquidation, reward, or emergency path creates phantom supply or burns without releasing assets.

Questions:
- Does every mint have matching asset/debt/collateral increase?
- Does every burn have matching release/settlement?
- Are bridge mint/burn events reconciled across chains?

### 6. Fee and reward accounting drift

Shape:
- Fees or rewards are accumulated in one variable but paid, reset, or claimed through another path.

Questions:
- Are accrued fees settled before rate/config changes?
- Can users claim old rewards after state says they are consumed?
- Does rounding dust accumulate to a stealable or loss-causing amount?

### 7. Cross-chain supply and message accounting

Shape:
- Source-chain burn/lock and destination-chain mint/release are not conserved across retries, failures, replays, or partial settlement.

Questions:
- Is every cross-chain message id consumed exactly once?
- Can failure on destination still mark source as settled?
- Does total supply across chains equal canonical supply after retry/unwind?

## False-Positive Filters

Do not escalate unless:
- The invariant is intended by code/docs/economics and not merely an assumed relationship.
- A reachable function breaks the invariant persistently or profitably.
- The broken invariant affects funds, solvency, supply, debt, collateral, rewards, or liveness.
- You can state the invariant before/after and identify the exact missing or wrong state update.
