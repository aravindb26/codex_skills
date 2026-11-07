# Solodit Pattern: Zero-rounded seizure blocks bad-debt socialization

Source:
- https://solodit.cyfrin.io/issues/nodebttoliquidate-blocks-bad-debt-socialisation-when-discounted-collateral-recovery-floors-to-zero-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- liquidation, dust, rounding, bad debt

Dedupe:
- id: `75093`
- fingerprint: `b33ccca0550b795f5f9cc6f70577a1514bcbdd7728a158c455abb341b5b286af`

Core mechanism:
- The discounted collateral amount available to seize floors to zero. A `NoDebtToLiquidate`-style guard then rejects liquidation, while bad-debt socialization is reachable only after collateral is fully exhausted. Residual dust can therefore leave economically unrecoverable debt recorded as healthy protocol assets.

Invariant and audit checks:
- A zero collateral payout due only to integer rounding must not prevent debt write-off or another safe resolution path.
- Trace collateral conversion, liquidation discount/bonus, rounding order, zero-output guards, partial liquidation, and the exact condition that clears or socializes debt.

False-positive checks:
- Prove the position is liquidatable and that collateral cannot be recovered through another route. Quantify the residual debt and show it is not intentionally covered by insurance or a dust threshold.

PoC shape:
1. Construct the smallest collateral/debt state where discounted seizure rounds to zero.
2. Show liquidation reverts while the bad-debt path remains unreachable.
3. Show the stale debt affects solvency, accounting, or other users.

Triage notes:
- Dust alone is not impact. Demonstrate material aggregate loss, impaired accounting, or a protocol-wide denial of resolution.
