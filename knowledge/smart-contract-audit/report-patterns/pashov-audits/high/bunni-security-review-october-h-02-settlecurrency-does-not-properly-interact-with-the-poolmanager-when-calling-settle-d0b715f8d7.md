# Pashov Audit Pattern: `_settleCurrency` does not properly interact with the `poolManager` when calling `settle`

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: HIGH
- Report: `Bunni-security-review-October` (team)
- Finding ID: `H-02`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Bunni-security-review-October.md#L423>
- Dedupe key: `team/md/Bunni-security-review-October.md#H-02`
- Fingerprint: `d0b715f8d762c2dae75cd95086b37c372239ace6eb05f452da86617c0c2e9746`

## Core Idea

A Uniswap V4 callback settles currency with the wrong PoolManager settlement sequence, so the integration's normal swap path cannot clear its transient debt and always reverts.

## Broken Invariant

Every unlock callback must settle each nonzero PoolManager currency delta using the exact native/ERC20 synchronization and settlement protocol expected by the integration.

## Where To Look

- Uniswap V4 unlockCallback implementations
- settle, sync, take, and native-value ordering
- Helpers that abstract different settlement modes behind one call

## Attack Path

Execute the affected swap path; the callback creates a currency delta, invokes the incompatible settlement method, and the PoolManager rejects final unlock because debt remains.

## False-Positive Checks

- Trace the exact installed PoolManager interface version
- Separate native currency from ERC20 settlement
- Verify no wrapper performs sync or value forwarding implicitly

## PoC Shape

Run a minimal real PoolManager swap through the callback and assert the delta remains or unlock reverts; then compare with the canonical settle sequence.

## Triage Note

Integration-specific but high value because happy-path tests with mocks often fail to enforce transient accounting.
