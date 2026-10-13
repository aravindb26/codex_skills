# Pashov Audit Pattern: Cancelled redemptions can create temporary share-rate yield

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-01)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-10-01.pdf>
- Dedupe decision: Distinct transient-state attack: a request removes assets from the share-rate denominator and cancellation restores them after a high-water mark records the temporary increase.

## Core Idea

An account can request redemption to remove assets from `totalAssets`, let the vault record an inflated share rate, then cancel and restore the shares while the high-water mark remains high.

## Broken Invariant

Temporary reversible state changes must not create permanent yield accrual or transfer value between PT and YT holders.

## Where To Look

- Request/cancel flows that remove and restore assets
- High-water-mark or monotonic index updates
- Share-rate calculations that include pending requests asymmetrically

## Attack Path

Request redemption, trigger index update while the denominator is reduced, cancel the request, and leave PT under-backed while YT holders receive yield based on the temporary rate.

## False-Positive Checks

- Confirm cancellation restores the same assets and shares
- Confirm the high-water mark does not decrease after cancellation
- Reconcile PT backing, YT payout, and attacker cost over one complete cycle

## PoC Shape

Compare a control against request -> index update -> cancel and assert that the cancelled path changes the permanent index or backing.

## Triage Note

The claim requires an actual value transfer or solvency deficit; a temporary preview difference is not enough.
