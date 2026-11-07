# Solodit Pattern: Terminal-market liquidation uses marginal price instead of position cost

Source:
- https://solodit.cyfrin.io/issues/failed-and-expired-markets-can-liquidate-shares-above-their-purchase-cost-trailofbits-none-automated-settlement-pdf

Imported:
- 2026-11-07

Severity:
- HIGH

Protocol / source:
- Automated Settlement / Trail of Bits

Tags:
- LMSR, market expiry, terminal state, liquidation valuation

Dedupe:
- id: `74858`
- fingerprint: `26083a29320877ee062009ecdcb122ad3c6323b134d6eb2640f4f44397f231d5`

Core mechanism:
- In failed or expired LMSR markets, liquidation values an entire position at the final marginal price rather than the integral/average cost at which the position was accumulated or the protocol's intended terminal settlement value. If the terminal marginal price exceeds average purchase cost, liquidation pays more than the position's cost and can transfer pool value to the holder.

Invariant and audit checks:
- Terminal settlement/liquidation must use the protocol's defined payoff and preserve the LMSR cost-function accounting across the full position, not substitute a point price for accumulated cost.
- Trace market status transitions, position-size history, LMSR cost/integral functions, final marginal price, and all claim/liquidation branches for failed and expired markets.

False-positive checks:
- Confirm LMSR is used, the market is actually terminal, and the payout exceeds the protocol-defined payoff after fees. Check whether a separate reserve/insurance explicitly funds this outcome.

PoC shape:
1. Build a multi-step position whose average acquisition cost differs from the final marginal price.
2. Transition the market to failed/expired and liquidate the whole position.
3. Compare the actual payout with the cost-function/terminal-payoff baseline and show the pool-funded excess.

Triage notes:
- This is specific to terminal-market economics, not a generic claim that final price must equal purchase cost; the protocol's payout specification controls.
