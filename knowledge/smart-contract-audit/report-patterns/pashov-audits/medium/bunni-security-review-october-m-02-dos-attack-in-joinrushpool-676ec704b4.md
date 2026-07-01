# Pashov Audit Pattern: DOS Attack in joinRushPool

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Bunni-security-review-October` (team)
- Finding ID: `M-02`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Bunni-security-review-October.md#L582>
- Dedupe key: `team/md/Bunni-security-review-October.md#M-02`
- Fingerprint: `676ec704b497cc49ef26b56cc51d64e5b09a83e674ead0577e3e75d4a38154f3`

## Core Idea

An immediately reversible stake can temporarily fill a capped pool, allowing an attacker to sandwich every victim join and release the capacity after the victim reverts.

## Broken Invariant

A capacity cap should ration scarce participation fairly and must not let costless transient occupancy censor other users.

## Where To Look

- Capped deposits or staking pools
- Same-block join and exit
- No cooldown, reservation, minimum duration, or victim slippage parameter

## Attack Path

Front-run a victim by filling remaining capacity, let the victim revert at the cap, then back-run by exiting and repeat for later victims at only gas cost.

## False-Positive Checks

- Confirm stake can exit immediately without meaningful penalty
- Check private order flow or per-user reservations
- Measure whether repeated censorship has rewardable availability impact

## PoC Shape

Bundle attacker join, victim join, and attacker exit in order; prove final attacker balance is restored while the victim consistently reverts.

## Triage Note

Do not overclaim permanent DoS if the attacker must continuously pay gas and cannot guarantee ordering.
