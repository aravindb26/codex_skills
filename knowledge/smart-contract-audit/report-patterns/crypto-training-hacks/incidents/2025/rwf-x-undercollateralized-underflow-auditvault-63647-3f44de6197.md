# Crypto Training Exploit Pattern Stub: RWf(x) undercollateralized underflow — AuditVault 63647

Source:
- https://crypto.training/hacks/63647-rwfx-undercollateralized-underflow/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, logic/liquidation-logic

Dedupe:
- id: `63647-rwfx-undercollateralized-underflow`
- fingerprint: `3f44de61979e7ac979077c1ade91344341fcfc3c69a1c9dd0a895df022c85b22`

Core exploit idea:
- loadSwapState subtracts debt from collateral without handling an undercollateralized system.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
