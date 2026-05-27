# Local Solodit Addendum: Behavioral State Analysis Companion

## Purpose
- Extend BSA with Solodit-derived behavioral failure modes.
- Do not replace `SKILL.md`.

## When To Use

Use after reading `behavioral-state-analysis/SKILL.md` during DeFi or smart-contract behavior decomposition.

## Companion Workflow

1. Classify contract type and lifecycle states.
2. For each behavior, map expected state transition and asset/accounting invariant.
3. Match high-risk behaviors to focused local addenda: oracle, math, lending, liquidation, reentrancy, signature, slippage, staking, DoS, token integration, proxy, or state invariant.
4. Search Solodit stubs for the behavior name and lifecycle transition before escalating.

## Behavioral Failure Modes

- State transition skips required status update.
- Aggregate accounting changes without per-user/per-position update.
- External callback occurs during temporary lifecycle state.
- Off-chain input was calculated before state changed.
- Queue/batch pointer advances while old requests remain unresolved.
- User-facing path and admin/keeper path preserve different invariants.

## False-Positive Filters

Do not surface a behavioral mismatch unless it creates a concrete security impact under the current program scope.
