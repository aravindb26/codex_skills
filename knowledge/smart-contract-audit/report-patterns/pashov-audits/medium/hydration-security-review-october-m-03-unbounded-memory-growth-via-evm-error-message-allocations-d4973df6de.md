# Pashov Audit Pattern: Unbounded memory growth via EVM Error message allocations

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `Hydration-security-review-October` (team)
- Finding ID: `M-03`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Hydration-security-review-October.md#L174>
- Dedupe key: `team/md/Hydration-security-review-October.md#M-03`
- Fingerprint: `d4973df6dee84d1ad009010ca16d0ae9adf9a5ba0908da1746c955715a8383ab`

## Core Idea

Error handling permanently leaks attacker-influenced EVM error strings with Box::leak, allowing unique failures to grow validator memory without reclamation.

## Broken Invariant

Repeated invalid transactions must have bounded temporary memory cost and must not create permanent process allocations from attacker-controlled error data.

## Where To Look

- Box::leak and leaked static strings in runtime error conversion
- Hex or string formatting of attacker-controlled revert data
- Long-lived node processes handling distinct error values

## Attack Path

Submit many calls that fail with unique return data; each error is encoded and leaked permanently, steadily increasing validator memory until process degradation or termination.

## False-Positive Checks

- Confirm the code runs in a long-lived native process rather than disposable Wasm memory
- Verify an unprivileged transaction controls unique error bytes
- Check transaction size, gas, and mempool limits that bound growth rate

## PoC Shape

Loop signed failing calls with unique revert payloads and measure resident memory after garbage collection or request completion.

## Triage Note

Severity depends on sustainable growth rate and whether consensus validators execute the leaking path.
