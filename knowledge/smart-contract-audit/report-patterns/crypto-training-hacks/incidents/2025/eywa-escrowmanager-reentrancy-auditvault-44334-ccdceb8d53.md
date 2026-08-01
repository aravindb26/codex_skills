# Crypto Training Exploit Pattern Stub: EYWA EscrowManager reentrancy — AuditVault 44334

Source:
- https://crypto.training/hacks/44334-eywa-escrow-reentrancy/

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
- reentrancy/single-function, logic/state-update

Dedupe:
- id: `44334-eywa-escrow-reentrancy`
- fingerprint: `ccdceb8d531dc0f2a00d77a2794bc5f59b281a04afe46f400a26f961e05c5df3`

Core exploit idea:
- Escrow performs the external receiver callback before its accounting transition, allowing nested withdrawals.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
