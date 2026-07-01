# Pashov Audit Pattern: `joinRecurPool` can incorrectly increment `userPoolCounts`

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: HIGH
- Report: `Bunni-security-review-October` (team)
- Finding ID: `H-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Bunni-security-review-October.md#L347>
- Dedupe key: `team/md/Bunni-security-review-October.md#H-01`
- Fingerprint: `86e25daacb6afd8277b16e62bb3640bd255e03173062b560a5d61463e339c788`

## Core Idea

A stake-balance refresh path increments the user's pool-membership counter even when no new pool is joined, eventually making unlock eligibility inconsistent with actual memberships.

## Broken Invariant

Membership counters must equal the number of active distinct memberships; balance refreshes must not create phantom memberships.

## Where To Look

- Join functions that also refresh balances
- Counters updated outside first-entry branches
- Unlock or withdrawal checks derived from aggregate counters

## Attack Path

Repeatedly increase balance and call the refresh-capable join path; phantom counter increments leave the user permanently classified as active after real positions exit, blocking unlock.

## False-Positive Checks

- Confirm repeated calls are reachable for the same pool
- Trace all decrements and whether they can remove phantom increments
- Verify the counter gates a security-relevant unlock or withdrawal

## PoC Shape

Join once, refresh twice, exit once, then show zero active pools but a nonzero membership counter and failed unlock.

## Triage Note

General check: derive aggregate counters from idempotent set transitions, not every successful call.
