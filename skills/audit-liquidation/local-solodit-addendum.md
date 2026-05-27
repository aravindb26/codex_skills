# Local Solodit Addendum: Liquidation Companion Mini-Skill

## Purpose
- Extend `audit-liquidation` with distilled High/Medium Solodit liquidation patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this for missing exploit shapes around liquidation freezes, bad debt accounting, collateral valuation, and liquidation avoidance.

## When To Use

Use after reading `audit-liquidation/SKILL.md` when code handles:
- liquidation eligibility, collateral seizure, auctions, bad debt, stability pools, insurance funds, partial liquidation, liquidator rewards, or liquidation pause flags.

## Companion Workflow

1. Load the original liquidation skill first.
2. Search current code with the extra terms below.
3. Trace the liquidation path from health check to debt repayment, collateral transfer, fee distribution, and bad-debt accounting.
4. Test price crash, oracle failure, no-liquidity, dust, whale, partial-liquidation, and already-insolvent states.
5. Search Solodit stubs by liquidation function, collateral primitive, and bad-debt variable before escalating.

## Extra Search Terms

```text
liquidationFee
liquidationPenalty
liquidationShare
seize
seizedCollateral
shortfall
badDebt
negativeCollateral
stabilityPool
insuranceFund
partialLiquidation
closeFactor
healthFactor
collateralValue
isLiquidateBorrowPaused
clearBadDebt
underwater
auction
honorarium
```

## Missing / Sharper Patterns To Check

### 1. Liquidation freezes under oracle failure or no-liquidity state

Shape:
- A position is liquidatable economically, but liquidation reverts because an oracle returns zero/stale/reverts, stability pool lacks the required asset, or collateral reserve has no liquidity.

Questions:
- Can bad debt grow while liquidation is blocked?
- Does the system have an alternate path for oracle-down or no-liquidity liquidation?
- Can a borrower intentionally move into a state that no liquidator can process?

### 2. Bad debt becomes negative collateral or last-user loss

Shape:
- Liquidation leaves a user/account/market with negative collateral, shortfall, or stale total assets that later withdrawals socialize incorrectly.

Questions:
- Is shortfall recognized immediately in total assets/share price?
- Can early users withdraw at inflated value while later users absorb bad debt?
- Is the insolvent account fully cleared or left with toxic state?

### 3. Partial liquidation bypasses full bad-debt accounting

Shape:
- Partial liquidation repays/seizes profitable portions but leaves loss-making debt unaccounted or lets liquidators extract remaining collateral while protocol absorbs shortfall.

Questions:
- Is bad debt checked before and after partial liquidation?
- Can multiple partial liquidations drain collateral without clearing debt?
- Does close factor interact correctly with fees, penalties, and shortfall?

### 4. Collateral omitted or misvalued during liquidation

Shape:
- Health factor/liquidation value excludes some collateral, includes ineligible collateral, misprices LP/BPT/vault collateral, or ignores liquidation fees.

Questions:
- Are all collateral sources included exactly once?
- Are liquidation fees deducted before determining what can be seized or withdrawn?
- Can a user deposit collateral into a wrapper/vault that the liquidation path ignores?

### 5. Borrower front-runs or mutates state to avoid liquidation

Shape:
- Borrower can change flags, ownership, collateral mode, short records, market membership, or position composition after becoming unsafe but before liquidation.

Questions:
- Can the borrower front-run flagging and make liquidation revert?
- Can they split, merge, transfer, or remove a position to escape eligibility?
- Are liquidation preconditions based on stale state from an earlier flag?

### 6. Pause and repayment asymmetry harms borrowers or protocol

Shape:
- Repayment disabled while liquidation remains enabled, or liquidation disabled while borrowing/interest continues.

Questions:
- Can borrowers be liquidated without a chance to repay after pause/unpause?
- Can bad debt accumulate because liquidations are paused but risky actions continue?
- Are grace periods applied after unpause or oracle recovery?

### 7. Liquidation incentive fails at edge CR or dust

Shape:
- At collateral ratio near 1, dust size, high gas, or low reward, trustless liquidators lose money or receive less than repaid.

Questions:
- Does incentive remain positive after gas, slippage, and transfer fees?
- Are minimum debt/collateral sizes enforced after accrued interest?
- Can attackers create many unprofitable underwater accounts?

### 8. Liquidation callback/reentrancy state gaps

Shape:
- Liquidation transfers collateral or calls external code before debt, seized collateral, auction state, or accounting is finalized.

Questions:
- Can callback reenter to modify debt/collateral or call another liquidation path?
- Are seized collateral and repaid debt updated before external transfer?
- Does reentrancy turn liquidation into vault-fund theft or permanent freeze?

## False-Positive Filters

Do not escalate unless:
- The position can realistically become unsafe under accepted market/deployment assumptions.
- The failure changes liquidation, bad debt, collateral seizure, or user/protocol solvency.
- Trusted liquidator/manual intervention assumptions are not explicit or not sufficient.
- The economic analysis shows liquidation is actually unprofitable/frozen, not merely less optimal.
