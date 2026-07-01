# Pashov Audit Pattern: Users can frontrun rebase to extract profits at the expense of long-term stakers

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Rivus-security-review-October` (team)
- Finding ID: `M-03`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Rivus-security-review-October.md#L318>
- Dedupe key: `team/md/Rivus-security-review-October.md#M-03`
- Fingerprint: `3c67481ab1cfea8721d874cdc310f8a64e2f0ae132ee6ef2bbaeae4111af68a1`

## Core Idea

A predictable positive rebase rewards balances present only at execution time, allowing atomic or short-lived deposits to capture yield earned by long-term stakers.

## Broken Invariant

Rebase yield should accrue to capital over the earning interval, not to users who enter immediately before distribution.

## Where To Look

- Permissioned or scheduled rebases
- Instant deposit and exit around supply expansion
- No snapshots, vesting, cooldown, or time-weighted ownership

## Attack Path

Observe a pending rebase, deposit immediately before it, receive a share of the supply increase, then exit after rebase and dilute incumbent stakers.

## False-Positive Checks

- Account for entry, bridge, withdrawal, and slippage costs
- Check whether rebase amount already includes the new deposit
- Verify cooldowns or snapshots prevent same-epoch capture

## PoC Shape

Compare an incumbent-only control against attacker deposit-rebase-withdraw ordering and show attacker profit plus reduced incumbent yield.

## Triage Note

Quantify extractable value after all fees; predictable timing alone is not sufficient.
