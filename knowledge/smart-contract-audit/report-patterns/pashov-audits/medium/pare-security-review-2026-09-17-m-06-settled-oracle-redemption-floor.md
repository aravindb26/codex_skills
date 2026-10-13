# Pashov Audit Pattern: A settled collateral oracle can price below its fixed redemption claim

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-06)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-09-17.pdf>
- Dedupe decision: Distinct post-settlement invariant: the oracle ignores a deterministic redemption floor even though the market still uses an AMM price.

## Core Idea

After settlement fixes the stock redemption amount per PT, the oracle still accepts a lower manipulable AMM price and exposes collateral to underpriced liquidation.

## Broken Invariant

A settled claim must not be valued below the amount the protocol itself guarantees on redemption.

## Where To Look

- Oracles that switch behavior at maturity or settlement
- AMM/TWAP prices used after a fixed redemption value exists
- Lending liquidation paths lacking a post-settlement floor

## Attack Path

Depress the PT/stock TWAP below the fixed redemption claim, liquidate borrowers at the lower value, then redeem the seized PT for the higher fixed amount.

## False-Positive Checks

- Confirm settlement makes the redemption amount deterministic and enforceable
- Confirm the AMM price remains in the liquidation oracle after settlement
- Account for TWAP manipulation cost and the market's liquidation threshold

## PoC Shape

Settle a vault, force a lower oracle price, liquidate a near-threshold position, and compare the seized PT redemption value with the liquidation credit.

## Triage Note

Do not merge with generic TWAP manipulation unless the fixed redemption floor is the missing invariant and fix.
