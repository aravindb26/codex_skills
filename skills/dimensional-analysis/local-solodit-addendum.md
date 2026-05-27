# Local Solodit Addendum: Dimensional Analysis Companion

## Purpose
- Extend dimensional analysis with Solodit-derived unit and scaling failure modes.

## When To Use

Use after reading `dimensional-analysis/SKILL.md` when auditing arithmetic-heavy blockchain code.

## Companion Workflow

1. Identify units for every amount: token units, shares, price, debt, collateral, time, rate, index, basis points.
2. Track scale for each unit: token decimals, feed decimals, WAD/RAY, Q64.96, basis points, percentage precision.
3. Compare formulas against `audit-math-precision/local-solodit-addendum.md` and `audit-oracle/local-solodit-addendum.md`.
4. Search Solodit stubs by variable/function name and unit mismatch before escalating.

## Extra Unit Failure Modes

- Share units mixed with asset units.
- Price direction inverted but dimensions still "look" numeric.
- Feed decimals mixed with token decimals.
- Basis points mixed with WAD/RAY percentages.
- Time rates per second/day/year mixed across interest or rewards.
- Local-chain and global-chain supply units mixed.
- Pre-fee and post-fee amounts reused interchangeably.

## False-Positive Filters

Do not report a dimension mismatch unless it reaches a state-changing path with quantifiable fund, accounting, liquidation, or liveness impact.
