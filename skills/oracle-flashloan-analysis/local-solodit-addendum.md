# Local Solodit Addendum: Oracle Flashloan Companion Mini-Skill

## Purpose
- Extend `oracle-flashloan-analysis` with distilled Solodit-style flash-loan oracle manipulation patterns.
- Avoid duplicating `audit-oracle/local-solodit-addendum.md`; read that file too when oracle validation details matter.

## When To Use

Use after reading `oracle-flashloan-analysis/SKILL.md` when price, share value, reserve, balance, or collateral state can be changed within one transaction.

## Companion Workflow

1. Map the exact value source: Chainlink, TWAP, spot pool, `balanceOf`, LP reserve, vault share price, or custom adapter.
2. Ask whether a flash loan, donation, swap, mint/burn, or callback can alter that value before the protocol uses it.
3. Trace the profit path: manipulate, borrow/mint/redeem/liquidate/swap, restore if needed, repay flash loan.
4. Check `audit-oracle/local-solodit-addendum.md` for stale/version/adapter/depeg details when relevant.
5. Search Solodit stubs by price source, pool type, and impacted function before escalating.

## Extra Search Terms

```text
balanceOf(address(this))
getReserves
slot0
sqrtPriceX96
virtual price
get_virtual_price
sharePrice
pricePerShare
exchangeRate
donate
flashLoan
flashSwap
sync
skim
TWAP
consult
observe
```

## Missing / Sharper Patterns To Check

### 1. Donation or balance-based share price manipulation

Shape:
- Protocol prices shares/assets from raw token balance or vault assets that can be donated or temporarily inflated.

Questions:
- Can attacker donate or flash-transfer assets before mint/redeem/borrow?
- Is share price based on internal accounting or raw balance?
- Can the attacker withdraw/dump inflated shares after restoring state?

### 2. Spot reserve manipulation through same-tx swaps

Shape:
- Borrowing, liquidation, or minting uses AMM spot reserves, `slot0`, or too-short TWAP.

Questions:
- Can flash swap move the pool enough to profit after fees?
- Is liquidity deep enough to make manipulation expensive, and is that proved?
- Does a multi-pool route depend on the weakest manipulable leg?

### 3. Circular dependency and self-pricing

Shape:
- Protocol prices a token/pool that it can mint, burn, rebalance, or provide liquidity to.

Questions:
- Can protocol action change its own oracle input?
- Can an attacker loop mint/burn/liquidity actions to move price then exploit the moved price?
- Is the oracle independent from protocol-controlled supply/liquidity?

### 4. Flash-loan liquidation manipulation

Shape:
- Attacker temporarily changes collateral/debt price to liquidate healthy users or avoid liquidation.

Questions:
- Is liquidation price sampled atomically from a manipulable source?
- Can the attacker unwind the manipulation after liquidation profit?
- Are liquidation discounts enough to cover manipulation cost?

## False-Positive Filters

Do not escalate unless:
- The value source is actually manipulable within the same transaction or short window.
- The manipulated value is used in state-changing logic.
- Profit or harm exceeds flash-loan fees, swap fees, slippage, and gas.
- TWAP/window/circuit protections are insufficient for the deployed liquidity and timing.
