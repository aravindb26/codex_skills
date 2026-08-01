# Crypto Training Exploit Pattern Stub: Level zero heartbeat blocks claims — AuditVault 63737

Source:
- https://crypto.training/hacks/63737-level-zero-heartbeat/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/stale-price, dos/frozen-funds

Dedupe:
- id: `63737-level-zero-heartbeat`
- fingerprint: `99b41addbebe54ac6e515a32f2fb84adf13204d99b140c760f9fa45ab8696f5d`

Core exploit idea:
- A zero heartbeat is treated as an invalid oracle state and causes every reward claim to revert.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
