# Crypto Training Exploit Pattern Stub: Sat1Hook Forensics — Grindable Hook Identity, but No Confirmed Protocol Loss

Source:
- https://crypto.training/hacks/2026-05-Sat1Hook/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, logic/missing-validation, logic/state-update

Dedupe:
- id: `2026-05-Sat1Hook`
- fingerprint: `18b99bee712d6632285cebd3088f456965c43e7f1e97e4002be12e2e0f1f9308`

Core exploit idea:
- The initially supplied transaction is not a Sat1Hook drain. It is an MEV backrun placed immediately after a large, ordinary curve redemption. The backrun contract gained…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
