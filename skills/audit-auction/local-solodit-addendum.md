# Local Solodit Addendum: Terminal LMSR Market Settlement

## Purpose
- Extend `audit-auction` with a focused terminal-state valuation check for LMSR-style markets.
- This is conditional; it does not apply to auctions or markets that do not use LMSR accounting.

## When To Use
- Use after the original skill when markets can fail, expire, settle, or liquidate positions using an LMSR cost function or marginal price.

## Focused Checks

### Terminal liquidation must preserve the market's defined payoff

Shape:
- A failed/expired market liquidates an accumulated position at the final marginal price, while the position's acquisition cost is the integral of a changing price curve. Applying one terminal point price to the whole position can overpay relative to the specified terminal payoff and drain pool value.

Questions:
- Does terminal resolution use the protocol's defined outcome payoff, the LMSR cost-function delta, or the current marginal price?
- Can the final marginal price differ materially from average acquisition cost for the entire position?
- Are failed and expired markets routed through distinct settlement branches?
- Who funds any excess payout, and is that behavior explicitly guaranteed?

Source pattern: [Terminal-market liquidation uses marginal price instead of position cost](../../knowledge/smart-contract-audit/report-patterns/solodit/high/terminal-market-liquidation-uses-marginal-price-not-position-cost-26083a2932.md).

## False-Positive Checks
- Do not assume purchase cost is always the correct payout. Compare against protocol specification, market outcome, and LMSR settlement invariant.
- Confirm the market is terminal and show a pool-funded excess after fees; price differences alone are not proof of loss.
