# Crypto Training Exploit Pattern Stub: Pyth validation is not payable — AuditVault 51984

Source:
- https://crypto.training/hacks/51984-pyth-missing-payable/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, logic/missing-validation

Dedupe:
- id: `51984-pyth-missing-payable`
- fingerprint: `eb2b2ea5c86d1b6d8e40061cb742996bd2c4bacf7aa42eb6c2ab07da474c10c9`

Core exploit idea:
- The update function is non-payable, so a caller cannot forward the provider fee.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
