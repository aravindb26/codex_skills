# Crypto Training Exploit Pattern Stub: LEND — Cross-chain borrow ignores existing debt in collateral validation

Source:
- https://crypto.training/hacks/58375-lend-cross-chain-borrow-ignores-existing-debt-in-collateral-validation/

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
- logic/missing-check, logic/liquidation-logic

Dedupe:
- id: `58375-lend-cross-chain-borrow-ignores-existing-debt-in-collateral-validation`
- fingerprint: `74876b299662b94c9a3238e065effe4d85ec7e60894d98c9ec65b876eb7e72a4`

Core exploit idea:
- Validation considers only the new borrow and omits debt already recorded on the destination chain, admitting an undercollateralized position.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
