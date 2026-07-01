# Pashov Audit Pattern: Unbounded storage iteration in EVM address registration migration

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Hydration-security-review-October` (team)
- Finding ID: `M-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Hydration-security-review-October.md#L107>
- Dedupe key: `team/md/Hydration-security-review-October.md#M-01`
- Fingerprint: `e8c0c6c2c64812c49ef0387891a42d942c465ccdf9f56691042e3618c8b3d6d7`

## Core Idea

A runtime upgrade migrates every registered asset in one unbounded storage loop, so a sufficiently large live registry can exceed the upgrade block weight and make the migration fail.

## Broken Invariant

A mandatory runtime migration must complete within the chain's bounded block-weight budget for every reachable pre-upgrade state.

## Where To Look

- on_runtime_upgrade and migration hooks
- Full-map or full-registry iteration
- Missing cursor, batching, try-runtime weight proof, or item cap

## Attack Path

Grow the registry to a reachable large size, then trigger the scheduled upgrade; migration work exceeds the allowed block budget and disrupts or blocks the upgrade.

## False-Positive Checks

- Measure the maximum reachable item count
- Include database read/write weights, not only loop count
- Check whether the migration is multi-block or administratively pre-bounded

## PoC Shape

Populate the registry near its reachable maximum, execute the migration under the configured weight meter, and show exhaustion before completion.

## Triage Note

Keep distinct from generic user-call loop DoS: this occurs in mandatory consensus/runtime upgrade execution.
