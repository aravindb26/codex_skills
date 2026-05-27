# Local Solodit Addendum: Oracle Companion Mini-Skill

## Purpose
- Extend `audit-oracle` with distilled High/Medium Solodit oracle patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this only for missing sharper exploit shapes, extra search terms, duplicate-risk checks, and false-positive filtering.

## When To Use

Use after reading `audit-oracle/SKILL.md` when the code uses:
- Chainlink, Pyth, Redstone, API3, custom signed prices, TWAPs, LP/vault share pricing, keeper-supplied execution prices, or order-settlement oracle versions.
- Prices for borrowing, liquidation, minting, redemption, fee/funding settlement, collateral valuation, or share accounting.

## Companion Workflow

1. Load the original oracle skill first.
2. Search current code with the extra terms below.
3. Map matches to one of the sharper patterns in this file.
4. Re-read the full price path from source to final accounting effect.
5. Search Solodit stubs by oracle name, primitive, feed type, price function, and impacted flow before escalating.
6. Only build a PoC if the issue changes real user/protocol value, liquidation, solvency, or settlement outcomes.

## Extra Search Terms

```text
oracleVersion
requestedVersion
validFrom
validTo
publishTime
confidence
price_tick
signed price
keeper
executionPrice
minAnswer
maxAnswer
priceLimit
deviation
spotPrice
sharePrice
exchangeRate
lpPrice
vaultPrice
get_virtual_price
pricePerShare
fetchPrice
```

## Missing / Sharper Patterns To Check

### 1. Expired or missing oracle versions settle as valid

Shape:
- A requested oracle version expires, is not requested, or has no fresh response, but settlement falls back to a previous price, zero price, or default version.

Questions:
- Can empty/no-op orders avoid requesting a version but later settle with `price = 0` or stale previous data?
- Is version validity checked at settlement, not just request time?
- Does an expired version return invalid, or does it silently reuse old price?

### 2. Same-transaction or same-block price inconsistency

Shape:
- Different functions fetch price separately inside one transaction/block and can observe different values or update timing.

Questions:
- Can a user mint/redeem/borrow/liquidate using one price and settle/account using another?
- Is the price cached for a full state transition where consistency is required?
- Can an oracle update be sandwiched between protocol actions?

### 3. Keeper or off-chain executor price injection

Shape:
- Keeper/executor calldata includes price, execution price, slippage price, or oracle metadata that is weakly bound to real oracle state.

Questions:
- Where was the price calculated, when, and can referenced state change before execution?
- Is keeper input bounded against a live oracle/TWAP/deviation check?
- Can malicious or stale keeper input change fills, liquidation, funding, or vault share minting?

### 4. LP, vault, and share-price manipulation

Shape:
- Protocol prices LP tokens, vault shares, BPT, Curve/Uniswap positions, or strategy shares using manipulable balances, spot reserves, stale share supply, or incomplete accounting.

Questions:
- Can donation, flash loan, read-only reentrancy, virtual price lag, or stale total supply move the reported price?
- Does share price include pending fees, debt, losses, locked funds, or unclaimed rewards consistently?
- Is LP price based on reserves that can be changed inside one transaction?

### 5. Adapter, route, and wrapped-asset mismatch

Shape:
- Oracle adapter assumes the wrong pair, route, decimals, request type, wrapped asset, or depeg relationship.

Questions:
- Does WBTC use BTC/USD without WBTC/BTC depeg protection?
- Does stETH/ETH, LST/ETH, or wrapped-vault pricing account for wrapper exchange rate and depeg?
- Does multi-hop pricing multiply/divide in the correct direction for every leg?

### 6. Oracle bounds and invalid values are not fatal

Shape:
- Price equals zero, negative, below minAnswer, above maxAnswer, low confidence, or invalid status but is still used.

Questions:
- Are min/max/circuit checks applied after every adapter conversion?
- Are negative signed prices rejected before casts?
- Does invalid confidence/status freeze liquidations or allow bad settlement?

### 7. Oracle failure freezes safety-critical exits

Shape:
- Oracle revert, stale price, zero price, or down feed blocks liquidations, redemptions, withdrawals, or repayment paths.

Questions:
- Can bad debt grow because liquidations freeze when a feed fails?
- Is there a safe fallback, pause, or manual unwind path that does not privilege one side unfairly?
- Does failure handling protect users as well as protocol solvency?

## False-Positive Filters

Do not escalate unless:
- The price is used in an in-scope state-changing path, not display-only logic.
- The attacker can influence timing, input, liquidity, oracle version, or market state enough to profit or cause rewardable damage.
- The issue survives current deployment assumptions, feed configuration, and program exclusions.
- The impact is more than generic "oracle best practice" and changes funds, solvency, liquidation, or settlement.
