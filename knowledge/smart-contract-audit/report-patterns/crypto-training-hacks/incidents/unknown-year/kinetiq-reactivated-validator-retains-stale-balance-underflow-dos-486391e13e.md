# Crypto Training Exploit Pattern Stub: Kinetiq: reactivated validator retains stale balance (underflow DoS)

Source:
- https://crypto.training/hacks/58611-h-03-deactivated-validator-retains-old-balance-after-reactiv/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58611-h-03-deactivated-validator-retains-old-balance-after-reactiv`
- fingerprint: `486391e13e021b86cd9b3d494deb843f93971e7735d746fedc4d39432e295500`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
