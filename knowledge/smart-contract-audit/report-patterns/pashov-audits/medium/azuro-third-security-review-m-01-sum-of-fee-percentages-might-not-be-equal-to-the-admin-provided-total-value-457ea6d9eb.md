# Pashov Audit Pattern: Sum of fee percentages might not be equal to the admin provided `total` value

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Azuro-third-security-review` (solo)
- Finding ID: `M-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/solo/md/Azuro-third-security-review.md#L126>
- Dedupe key: `solo/md/Azuro-third-security-review.md#M-01`
- Fingerprint: `457ea6d9ebd9e8778d83e53ee925c3cb521665f206e3e1d01d9c7c2a7a253cdf`

## Core Idea

Configuration validates both aggregate fee and component percentages independently but never requires their sums to agree, so accounting deducts one total while distributing another.

## Broken Invariant

The fee charged to a user must equal the sum allocated to all fee recipients for every accepted configuration.

## Where To Look

- Cached total plus component fee fields
- Independent upper-bound checks without equality checks
- Deduction and distribution paths reading different configuration fields

## Attack Path

Set component percentages whose sum differs from total, process fee-bearing activity, and accumulate either undistributed stuck value or over-distribution/loss depending on the direction of mismatch.

## False-Positive Checks

- Check whether total intentionally includes an undistributed reserve
- Trace rounding tolerances and denominator units
- Verify the setter is reachable under the program's trusted-role model

## PoC Shape

Configure sum(components) below and above total, execute one bet or payment, and reconcile user deduction, recipient transfers, and residual balance.

## Triage Note

Privileged configuration may be out of scope; retain the invariant as a strong code-review check but verify the attacker model before reporting.
