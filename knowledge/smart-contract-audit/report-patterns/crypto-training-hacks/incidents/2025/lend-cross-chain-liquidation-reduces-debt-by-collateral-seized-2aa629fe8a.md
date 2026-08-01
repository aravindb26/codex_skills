# Crypto Training Exploit Pattern Stub: LEND — Cross-chain liquidation reduces debt by collateral seized

Source:
- https://crypto.training/hacks/58388-lend-cross-chain-liquidation-reduces-debt-by-collateral-seized/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic, bridge/missing-validation

Dedupe:
- id: `58388-lend-cross-chain-liquidation-reduces-debt-by-collateral-seized`
- fingerprint: `2aa629fe8ab01b2fc419ecd5b93115d93340053fe14dce7f5aa5b50b6c4cb9ae`

Core exploit idea:
- The cross-chain message reduces debt using collateral seized rather than the actual repayment, allowing debt to be erased at an incorrect rate.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
