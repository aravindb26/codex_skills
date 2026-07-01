# Pashov Audit Pattern: Incorrect principle tracking due to fee inclusion

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Rivus-security-review-October` (team)
- Finding ID: `M-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Rivus-security-review-October.md#L182>
- Dedupe key: `team/md/Rivus-security-review-October.md#M-01`
- Fingerprint: `2c3b0f6f37087c3ad61ba5d738dbe3e66542d11cfc0245bdc4678574f8826584`

## Core Idea

Deposit accounting adds the gross input to principal even though fees are removed before staking, inflating the base used for TVL, yield, and later state transitions.

## Broken Invariant

Recorded principal must equal assets actually committed to the yield-bearing position, excluding fees and amounts routed elsewhere.

## Where To Look

- Gross-versus-net deposit variables
- Fee deductions performed after accounting updates
- Principal, TVL, APY, or withdrawal calculations sharing one tracker

## Attack Path

Make fee-bearing deposits; each records more principal than reaches the staking position, and the mismatch compounds into incorrect accounting or downstream withdrawal behavior.

## False-Positive Checks

- Verify the documented meaning of principal
- Trace whether fees remain protocol-owned backing assets
- Show a security-relevant consumer of the inflated value

## PoC Shape

Deposit with nonzero fees and compare principal delta against the actual underlying balance or amount staked.

## Triage Note

If no security-sensitive path consumes principal, downgrade to accounting/display impact.
