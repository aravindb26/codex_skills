# Local Solodit Addendum: Lending Companion Mini-Skill

## Purpose
- Extend `audit-lending` with distilled High/Medium Solodit lending patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this for missing exploit shapes around debt integrity, collateral lifecycle, market status, stale indexes, and lender/borrower griefing.

## When To Use

Use after reading `audit-lending/SKILL.md` when code handles:
- borrow, repay, collateral enable/disable, credit delegation, markets, interest indexes, loan auctions, refinancing, liquidation prerequisites, or bad debt clearing.

## Companion Workflow

1. Load the original lending skill first.
2. Search current code with the extra terms below.
3. Trace the loan lifecycle from creation to repayment/default/liquidation/closure.
4. Track debt, collateral, shares, indexes, market status, and pause flags across every transition.
5. Search Solodit stubs by protocol primitive, debt variable, market status, and lifecycle function before escalating.

## Extra Search Terms

```text
activeDebt
totalDebt
borrowShares
debtShares
creditDelegation
marketStatus
deprecated
blacklist
isBorrowPaused
isRepayPaused
isLiquidateBorrowPaused
collateralEnabled
collateralFactor
minLoanSize
refinance
takeOverDebt
clearBadDebt
badDebt
interestIndex
borrowIndex
utilization
```

## Missing / Sharper Patterns To Check

### 1. Market status blocks existing positions

Shape:
- Pausing, deprecating, blacklisting, or disallowing a token/market blocks repayment, liquidation, withdrawal, or collateral rescue for existing loans.

Questions:
- Are existing positions grandfathered when a market is disabled?
- Can repayments be paused while liquidations remain active, or liquidations paused while bad debt grows?
- Can token blacklist/paused NFT transfer prevent liquidation forever?

### 2. Debt validation missing in non-obvious flows

Shape:
- Burn, transfer, group/account migration, delegation, or market cleanup modifies a debt-bearing object without checking outstanding debt.

Questions:
- Can debt be erased, moved, or made uncollectible outside the main repay path?
- Does every transfer/burn/migration validate both principal and shares?
- Is debt checked before collateral or identity ownership changes?

### 3. Stale debt, interest, and index accounting

Shape:
- Debt, interest, utilization, P2P indexes, or market indexes are read before accrual or updated in the wrong order.

Questions:
- Is interest accrued before borrow, repay, withdraw, liquidation, and health checks?
- Can stale total debt or borrow index make a position safer/riskier than reality?
- Does repay update interest rate before or after debt changes in a way that leaks value?

### 4. Collateral withdraw while obligations remain

Shape:
- A borrower withdraws collateral or profit while pending fees, guaranteed orders, liquidation fees, or hidden debt are not included in the health check.

Questions:
- Are all pending liabilities counted before withdrawal?
- Can collateral be removed during liquidation mode or near liquidation?
- Does positive PnL or unrealized profit let the borrower remove all liquidation incentive?

### 5. Repay and loan-close edge failures

Shape:
- Repay uses the wrong account, wrong shares, wrong maturity, wrong token recipient, or closes a loan without fully settling debt.

Questions:
- Is repayment credited to the actual borrower/loan, not `msg.sender` or initiator by mistake?
- Can full repayment leave dust debt or bad debt state?
- Can close/cancel/settle paths bypass principal, interest, or fee settlement?

### 6. Refinancing, assignment, and takeover manipulation

Shape:
- Refinancing, auction cancellation, loan assignment, or debt takeover changes lender/borrower economics without preserving original constraints.

Questions:
- Can borrower extend default indefinitely through refinance/cancel loops?
- Can a lender be forced into an unwanted or undercollateralized loan?
- Can takeover/liquidation reenter or reorder debt assignment and vault balance updates?

### 7. Dust and small-position griefing

Shape:
- Protocol allows tiny loans/positions that are unprofitable to liquidate or costly to process.

Questions:
- Are min loan, min collateral, and min debt checks applied after fees and interest?
- Can attackers create many dust loans to grief lenders/liquidators?
- Can dust bad debt accumulate into systemic insolvency?

### 8. Last lender / bank-run accounting

Shape:
- Bad debt, negative collateral, or liquidation shortfall is not socialized/accounted correctly, causing the last withdrawing lenders to eat losses.

Questions:
- Is bad debt removed from total assets before share withdrawals?
- Are losses assigned when they happen or deferred until later users exit?
- Can accounting show inflated liquidity after liquidation or bad debt clearing?

## False-Positive Filters

Do not escalate unless:
- The affected lifecycle path is reachable for in-scope users or permissionless liquidators.
- The issue changes repayment, collateral, debt, liquidation eligibility, lender withdrawals, or bad debt.
- Admin-only parameter risk has immediate user-fund impact or violates program scope.
- The protocol does not document and compensate for trusted liquidators/manual bad-debt handling.
