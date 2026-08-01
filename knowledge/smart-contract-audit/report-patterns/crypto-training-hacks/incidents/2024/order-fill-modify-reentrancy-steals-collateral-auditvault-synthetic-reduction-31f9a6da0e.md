# Crypto Training Exploit Pattern Stub: Order fill/modify reentrancy steals collateral — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44373-h-3-lack-of-nonreentrant-modifier-in-fillorder-and-modifyord/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/cross-function, dependency/unsafe-external-call

Dedupe:
- id: `44373-h-3-lack-of-nonreentrant-modifier-in-fillorder-and-modifyord`
- fingerprint: `31f9a6da0eced6ad49da933c94a84c44d8f0c1f13ec1dd76f675d6289b53f0dd`

Core exploit idea:
- This bug report highlights an issue with the lack of a certain modifier in the code, which can allow an attacker to steal funds from the victim. The report explains the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
