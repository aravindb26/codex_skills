# Solodit Pattern: Opening at the liquidation threshold permits immediate liquidation

Source:
- https://solodit.cyfrin.io/issues/positions-can-be-opened-at-the-liquidation-edge-with-hf1-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- HIGH

Protocol / source:
- BarterLab / MixBytes

Tags:
- lending, health factor, liquidation buffer, rollover

Dedupe:
- id: `75087`
- fingerprint: `1557c9936c84f5c296b4cc8f483393a9510b5fbcc4c9b1796f6bfc2b65d5222b`

Core mechanism:
- Position-opening and liquidation logic use the same threshold with no safety buffer, so a position can be accepted at health factor 1 and become liquidatable immediately after a normal state/price transition. In the reported rollover path, an unbounded or insufficiently validated debt factor and caller-selected rate/tick can push a position close to the threshold.

Invariant and audit checks:
- Successful borrowing/opening must leave the position above the liquidation boundary by the documented safety margin under the same units and price model used by liquidation.
- Compare open, borrow, rollover, and liquidation formulas; validate configuration bounds, user/keeper-controlled rates, rounding, and the next accrual/price update.

False-positive checks:
- Reproduce the exact health factor with deployed parameters and accepted oracle behavior. Confirm ordinary next-step accrual can trigger liquidation and that the threshold is not deliberately shared by protocol design.

PoC shape:
1. Open or roll over a position at the most favorable in-scope boundary.
2. Apply one permitted accrual/price update.
3. Show liquidation becomes immediately valid without an independent market shock.

Triage notes:
- Severity depends on whether the user knowingly selected a risky position, whether the path is permissionless, and whether liquidation creates a real borrower loss or protocol bad debt.
