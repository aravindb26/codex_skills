# Crypto Training Exploit Pattern Stub: RipIt: burnPacketFromInventory swap-pops the tail packet into the burned slot but never updates t

Source:
- https://crypto.training/hacks/62594-h-01-missing-index-updates-in-burnpacketfrominventory-cause/

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
- id: `62594-h-01-missing-index-updates-in-burnpacketfrominventory-cause`
- fingerprint: `c4c2cd6cdd6ac7e74c2142bbf90770523fd6ef4203b5a3f8752e3f2a2fbc09dd`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
