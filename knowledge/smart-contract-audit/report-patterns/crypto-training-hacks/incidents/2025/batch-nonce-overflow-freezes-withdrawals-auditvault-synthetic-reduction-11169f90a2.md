# Crypto Training Exploit Pattern Stub: Batch nonce overflow freezes withdrawals — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62487-h-6-dos-might-happen-to-dinerowithdrawrequestmanager-initiat/

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
- arithmetic/overflow, dos/lockup

Dedupe:
- id: `62487-h-6-dos-might-happen-to-dinerowithdrawrequestmanager-initiat`
- fingerprint: `11169f90a28ad6907d59859071857414d7439e2728419809ba7ec9d8b12b2cd3`

Core exploit idea:
- This bug report discusses an issue that was found in the Notional Finance protocol by a group of individuals. The issue involves a function called DineroWithdrawRequestM…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
