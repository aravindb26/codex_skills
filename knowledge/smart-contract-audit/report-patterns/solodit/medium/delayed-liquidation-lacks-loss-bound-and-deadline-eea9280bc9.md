# Solodit Pattern: Delayed liquidation lacks a loss bound and deadline

Source:
- https://solodit.cyfrin.io/issues/liquidate-has-no-loss-and-deadline-protection-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- liquidation execution, stale quote, minimum output, deadline

Dedupe:
- id: `75089`
- fingerprint: `eea9280bc9c0c2b49ceb9712fa706514ba50b4b51095798e5e740d8632e2798c`

Core mechanism:
- A liquidation commits debt repayment without a user/keeper-specified maximum debt input, minimum collateral received, or execution deadline. If execution is delayed or collateral pricing/liquidity changes, the liquidator can pay more than the collateral's realized value.

Invariant and audit checks:
- A delayed execution must remain bounded by explicit price/loss constraints evaluated against actual settlement amounts.
- Trace quote creation to execution, debt amount fixed at submission, collateral price and liquidity changes, caller-controlled bounds, and whether the transaction is atomic or queued.

False-positive checks:
- Verify the operation is actually delayed or price-sensitive and that no oracle bound, auction cap, keeper rule, or downstream min-out protects the position. Quantify loss after fees and available collateral.

PoC shape:
1. Submit or queue a liquidation at the initial quote.
2. Change the relevant price/liquidity before execution.
3. Execute and show debt paid exceeds the protected/realizable collateral value with no bound causing a revert.

Triage notes:
- Do not report missing parameters as a standalone best-practice issue; demonstrate a reachable harmful execution.
