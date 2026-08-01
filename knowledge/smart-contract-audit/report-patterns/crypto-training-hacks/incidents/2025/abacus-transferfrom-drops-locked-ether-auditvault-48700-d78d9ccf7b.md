# Crypto Training Exploit Pattern Stub: Abacus transferFrom drops locked ether — AuditVault 48700

Source:
- https://crypto.training/hacks/48700-abacus-locked-ether-transfer/

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
- logic/state-update, logic/incorrect-state-transition

Dedupe:
- id: `48700-abacus-locked-ether-transfer`
- fingerprint: `d78d9ccf7b2061061bd3d2444a18d343f931a7a769692437f0720f778ad0ac8c`

Core exploit idea:
- Position ownership moves without moving the corresponding ethLocked amount.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
