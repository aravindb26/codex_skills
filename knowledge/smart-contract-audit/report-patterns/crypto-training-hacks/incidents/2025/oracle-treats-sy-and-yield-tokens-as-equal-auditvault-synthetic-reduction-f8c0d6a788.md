# Crypto Training Exploit Pattern Stub: Oracle treats SY and yield tokens as equal — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62489-h-8-incorrect-assumption-that-one-1-pendle-standard-yield-sy/

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
- oracle/price-calculation, arithmetic/decimal-mismatch

Dedupe:
- id: `62489-h-8-incorrect-assumption-that-one-1-pendle-standard-yield-sy`
- fingerprint: `f8c0d6a788714201318dc19e04c4868c32528520979efc67548b45fd86b9bffd`

Core exploit idea:
- This bug report is about an issue found in the Pendle yield strategy code. The bug was discovered by two individuals and it is caused by an incorrect assumption in the c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
