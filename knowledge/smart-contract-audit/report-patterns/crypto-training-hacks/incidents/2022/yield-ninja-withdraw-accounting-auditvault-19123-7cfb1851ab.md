# Crypto Training Exploit Pattern Stub: Yield Ninja withdraw accounting — AuditVault 19123

Source:
- https://crypto.training/hacks/19123-yield-ninja-withdraw-accounting/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, arithmetic/precision-loss

Dedupe:
- id: `19123-yield-ninja-withdraw-accounting`
- fingerprint: `7cfb1851ab8ad9c4041802ad239a94ada9754521b2d8608d1be6f38b52620684`

Core exploit idea:
- withdraw burns shares but fails to debit the corresponding assets.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
