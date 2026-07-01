# Pashov Audit Pattern: `principle` not updated in `rebase()` leading to underflow and withdrawal failures

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: HIGH
- Report: `Rivus-security-review-October` (team)
- Finding ID: `H-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Rivus-security-review-October.md#L68>
- Dedupe key: `team/md/Rivus-security-review-October.md#H-01`
- Fingerprint: `0e597defc91552bdd13ef3b3f80516c808397d3bb9d1765405f24e652661d7a0`

## Core Idea

Rebase changes claimable token supply without updating the principal tracker, so later withdrawals subtract rebased amounts from stale principal and can underflow or freeze exits.

## Broken Invariant

Principal/deposit accounting must remain consistent with every supply-changing operation used by withdrawal calculations.

## Where To Look

- Rebasing wrappers with separate principal or TVL variables
- Supply updates that bypass deposit/withdraw accounting
- Withdrawal subtraction after positive rebases

## Attack Path

Deposit, apply a positive rebase that increases redeemable balances but leaves principal stale, then withdraw an amount whose principal subtraction exceeds the tracker and reverts.

## False-Positive Checks

- Determine whether principal intentionally excludes yield
- Check whether withdrawal should subtract cost basis or rebased balance
- Trace checked arithmetic and all principal synchronization hooks

## PoC Shape

Record principal and supply, perform a positive rebase, withdraw the rebased entitlement, and show stale principal causes underflow or blocks redemption.

## Triage Note

The strongest impact is withdrawal failure or fund lock, not merely inaccurate TVL.
