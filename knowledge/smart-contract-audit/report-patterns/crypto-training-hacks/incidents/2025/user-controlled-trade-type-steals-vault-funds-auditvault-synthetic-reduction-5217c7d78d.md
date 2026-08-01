# Crypto Training Exploit Pattern Stub: User-controlled trade type steals vault funds — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62491-h-10-malicious-user-can-change-the-tradetype-to-steal-funds/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, logic/wrong-condition

Dedupe:
- id: `62491-h-10-malicious-user-can-change-the-tradetype-to-steal-funds`
- fingerprint: `5217c7d78d9f1cbae4cd15984afffcb3c5ade7db3ca2d611053ea243effd7277`

Core exploit idea:
- This bug report discusses a vulnerability found in the Notional Exponent protocol. The vulnerability allows malicious users to exploit the protocol and steal funds from…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
