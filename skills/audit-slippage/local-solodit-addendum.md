# Local Solodit Addendum: Slippage Companion Mini-Skill

## Purpose
- Extend `audit-slippage` with distilled High/Medium Solodit DEX and routing patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this for missing exploit shapes around final-output protection, liquidation swaps, cross-chain swaps, route validation, and partial fills.

## When To Use

Use after reading `audit-slippage/SKILL.md` when code handles:
- swaps, liquidation swaps, redemptions, order fills, cross-chain swaps, DEX routers, LP mint/burn, vault rebalances, or keeper-executed trades.

## Companion Workflow

1. Load the original slippage skill first.
2. Search current code with the extra terms below.
3. Trace the full route from user input to final received asset and accounting update.
4. Verify who controls min-out/deadline/path/pool/fee tier and whether protection is final-output based.
5. Search Solodit stubs by router, DEX, swap function, route type, and impacted flow before escalating.

## Extra Search Terms

```text
amountOutMinimum
minTokenAmounts
minAmountOut
sqrtPriceLimitX96
priceLimit
deadline
executionPrice
oracleSlippage
slippagePercent
slippageLimit
updateOrder
fillOrder
partialFill
exactInput
exactOutput
addLiquidity
removeLiquidity
rebalance
liquidation_amount
destination chain
```

## Missing / Sharper Patterns To Check

### 1. Slippage parameter exists but is ineffective

Shape:
- A min-out or price-limit parameter is present but checked against the wrong token, old configuration, intermediate hop, or non-binding value.

Questions:
- Does the min-out protect the final user/protocol asset?
- Can `sqrtPriceLimitX96` or a route-specific field allow partial swaps with bad final output?
- Is the checked token amount the one that determines user value?

### 2. Liquidation and redemption swaps lack slippage

Shape:
- Liquidation, redemption, or collateral conversion swaps accept any output, causing unexpected collateral loss or bad debt.

Questions:
- Can liquidators or keepers route through bad liquidity and make users/protocol eat slippage?
- Is liquidation amount protected in collateral units and value units?
- Can bad slippage turn a solvent redemption/liquidation into loss?

### 3. Cross-chain or delayed execution slippage

Shape:
- User signs/requests a swap on one chain or time, but execution happens later or on another chain without binding final min-out/deadline.

Questions:
- Are destination-chain output, executor fee, route, and deadline bound to the user request?
- Can users be forced to accept any slippage after bridge delay?
- Is stale quote confidence treated as execution safety?

### 4. Route, pool, and fee-tier validation gaps

Shape:
- Code assumes a pool, fee tier, path, or router is correct but does not validate liquidity, token order, or pool authenticity.

Questions:
- Can path/pool be spoofed or collide with expected route validation?
- Can liquidity migrate to another fee tier, making the hardcoded tier unsafe?
- Does token order mismatch invert amounts or reserve meaning?

### 5. On-chain quoter or oracle-derived slippage

Shape:
- Min-out is calculated onchain from current spot, quoter, reserves, or manipulable oracle in the same transaction.

Questions:
- Can attacker manipulate the quote before the protected swap?
- Is TWAP or off-chain quote used, and is it long enough/fresh enough?
- Is quoter output used in state-changing logic, not just display?

### 6. Partial fills and order-fee slippage

Shape:
- Partial fills, batched orders, or constituent orders apply min-out/fees per piece instead of preserving whole-order economics.

Questions:
- Can a filler choose partial execution that passes local checks but violates global min-out?
- Are fees rounded/charged in a way that exceeds collected output?
- Can order update/cancel paths invalidate slippage assumptions?

## False-Positive Filters

Do not escalate unless:
- The swap/liquidity path moves user funds or protocol assets backing users.
- The attacker/MEV/keeper can influence timing, route, price, or liquidity.
- The loss remains after considering caller-provided min-out, upstream checks, and private/keeper execution assumptions.
- You can quantify expected vs actual received value or show a concrete bad execution path.
