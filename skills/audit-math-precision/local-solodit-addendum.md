# Local Solodit Addendum: Math Precision Companion Mini-Skill

## Purpose
- Extend `audit-math-precision` with distilled High/Medium Solodit arithmetic patterns.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Use this for sharper exploit shapes around rounding, shares, exchange rates, decimal scaling, bounds, and accounting drift.

## When To Use

Use after reading `audit-math-precision/SKILL.md` when code performs:
- share mint/burn, vault deposits/withdrawals, swaps, rewards, fees, interest, oracle conversions, LP valuation, downcasts, packed numbers, exponent/log math, or fixed-point scaling.

## Companion Workflow

1. Load the original math precision skill first.
2. Search current code with the extra terms below.
3. For each match, identify units, decimals, rounding direction, input bounds, and who benefits from the rounding.
4. Test zero, dust, first-deposit, max-value, different-decimal, and round-trip paths.
5. Search Solodit stubs by function name, primitive, and math shape before escalating.
6. Escalate only when arithmetic changes real asset balances, share supply, solvency, rewards, fees, or liveness.

## Extra Search Terms

```text
exchangeRate
pricePerShare
sharePrice
totalShares
totalSupply
convertToShares
convertToAssets
mulDiv
mulWad
divWad
wad
ray
mantissa
packedFloat
roundUp
roundDown
ceilDiv
unsafeCast
toUint
toInt
wExp
exp
pow
log
lastRewardTime
accReward
rewardIndex
```

## Missing / Sharper Patterns To Check

### 1. First-depositor and empty-vault exchange-rate manipulation

Shape:
- Initial shares/assets or near-empty vault state lets an attacker set an exchange rate that steals from later depositors or causes excessive rounding.

Questions:
- What happens when `totalSupply == 0`, `totalAssets == 0`, or one side is dust?
- Can donation or tiny first deposit skew later `convertToShares` or `convertToAssets`?
- Are virtual shares/assets or minimum liquidity used correctly?

### 2. Round-trip profit from asymmetric rounding

Shape:
- Deposit/withdraw, buy/sell, mint/redeem, or swap round-trip returns more value than input because opposite directions round in the attacker's favor.

Questions:
- Does a user gain value by repeating a small cycle?
- Are fees rounded down while payouts round up?
- Are constituent orders, partial fills, or multi-step swaps rounded independently then summed?

### 3. Division by zero and denominator collapse

Shape:
- Denominator can become zero or dust after state changes, disabled participants, zero supply, expired rounds, or all positions exiting.

Questions:
- Can a reward cycle, oracle, pool, or distribution permanently revert?
- Is denominator checked after filtering disabled/invalid entries?
- Can an attacker force all weight/shares/liquidity out before calculation?

### 4. Underflow/overflow becomes mint, lock, or insolvency

Shape:
- Arithmetic overflow/underflow is not merely revert-risk; it can mint excessive rewards, lock withdrawals, or corrupt accounting.

Questions:
- Does a subtraction assume monotonic state that can be violated by withdrawal, liquidation, time, or duplicate processing?
- Can underflow revert all exits or mint a huge value through unchecked/legacy arithmetic?
- Are exponent/log/pow upper bounds correct before fixed-point scaling?

### 5. Downcast and packed-number truncation

Shape:
- Values are cast or packed into smaller types without proving the upper/lower bound at the exact assignment point.

Questions:
- Is the bounds check performed on the same scaled value that is stored?
- Can signed-to-unsigned or unsigned-to-signed conversion flip semantics?
- Can truncation leave bad debt, stale fees, or wrong oracle values even after "complete" settlement?

### 6. Decimal scaling drift across assets and adapters

Shape:
- Protocol assumes 18 decimals or applies scaling twice/not at all across tokens, feeds, LPs, vault shares, or adapters.

Questions:
- Are token decimals, feed decimals, share decimals, and internal decimals all explicitly converted?
- Does moving from high-decimal to low-decimal assets lose material value?
- Does the same variable alternate between asset units and internal fixed-point units?

### 7. Reward and fee index drift

Shape:
- Updating rates, reward indices, or fee accumulators resets accrued value, uses stale time, or distributes rounded dust incorrectly.

Questions:
- Are accrued fees/rewards settled before rate changes?
- Can long gaps, disabled recipients, or time moving backward/forward trigger underflow or permanent DoS?
- Who receives or loses accumulated rounding dust?

## False-Positive Filters

Do not escalate unless:
- The precision loss is reachable in normal in-scope execution.
- The affected value is user/protocol funds, debt, rewards, collateral, or liveness.
- You quantify the loss or show a repeatable extraction/lock path.
- The issue is not a documented favor-user rounding choice with bounded impact.
