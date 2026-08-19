# Crypto Training Exploit Pattern Stub: SukukFi: withdraw()/redeem() lack a msg.sender==owner / allowance check

Source:
- https://crypto.training/hacks/65495-h-01-missing-authorization-check-allows-unauthorized-fund-wi/

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
- id: `65495-h-01-missing-authorization-check-allows-unauthorized-fund-wi`
- fingerprint: `fad2bd8ac7088849251b9bc4f034aa38605796f075072d76744b03e3ee6acbc8`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
