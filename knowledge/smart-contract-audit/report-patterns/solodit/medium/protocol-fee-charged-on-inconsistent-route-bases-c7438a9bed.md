# Solodit Pattern: Equivalent routes charge a fee on inconsistent bases

Source:
- https://solodit.cyfrin.io/issues/one-protocolfee-is-applied-to-two-different-bases-so-the-same-move-costs-1-fee-more-through-reloan-than-through-borrow-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- fee accounting, borrow/reloan, inconsistent units

Dedupe:
- id: `75092`
- fingerprint: `c7438a9bed8343accd8d45a85cac2fc10d5bc5d150e2a6a8460b22f09c2fb350`

Core mechanism:
- Two user routes that represent the same economic operation apply the same protocol fee rate to different bases (for example, net assets on one route and gross liquidity on another). The routes therefore charge materially different effective fees.

Invariant and audit checks:
- Equivalent routes should apply the documented fee to the same economic quantity, or explicitly document and enforce their different semantics.
- Compare fee bases across borrow, reloan, exact-in/exact-out, and settlement paths; track gross/net values, accrued interest, and fee rounding at each transition.

False-positive checks:
- Compare equivalent inputs and final balances, not just fee expressions. Verify that the difference is not a documented fee tier or a necessary cost charged to a distinct beneficiary.

PoC shape:
1. Execute economically equivalent actions through each route with the same principal and rate.
2. Compare user debit, protocol fee accrual, and final debt/assets.
3. Repeat at dust and ordinary sizes to expose rounding amplification.

Triage notes:
- Quantify who receives or loses the difference and whether it is material; inconsistent formulas alone are not an exploit.
