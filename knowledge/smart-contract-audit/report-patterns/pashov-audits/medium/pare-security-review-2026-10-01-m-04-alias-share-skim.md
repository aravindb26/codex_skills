# Pashov Audit Pattern: Address-only share protection lets an alias be swept

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-04)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-10-01.pdf>
- Dedupe decision: Distinct identity-alias issue: protection is tied to one token address while another address reaches the same underlying share ledger.

## Core Idea

Permissionless `skim` protects the configured share-token address but accepts an alias or wrapper address that represents the same backing balance, allowing the balance to be swept.

## Broken Invariant

An asset's protected status must follow its economic identity, not only one address representation.

## Where To Look

- `skim`, rescue, or sweep functions checking exact token addresses
- Share wrappers, aliases, proxies, or multiple entrypoints over one ledger
- Treasury transfers that can move vault-held backing without settling positions

## Attack Path

Pass the alias address to the permissionless sweep, bypass the protected-address check, and transfer backing needed by outstanding PT/YT positions to the treasury.

## False-Positive Checks

- Confirm the alias can actually access or represent the same backing balance
- Check whether the alias is intentionally sweepable surplus
- Trace all position backing and settlement effects after the sweep

## PoC Shape

Create a position backed by the canonical share, invoke `skim` with the alias, and assert that the backing leaves the vault while the position remains outstanding.

## Triage Note

The exact alias relation must be proven; a merely similar token or unrelated wrapper is not enough.
