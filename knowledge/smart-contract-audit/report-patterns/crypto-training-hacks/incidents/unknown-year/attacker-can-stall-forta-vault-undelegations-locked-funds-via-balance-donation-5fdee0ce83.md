# Crypto Training Exploit Pattern Stub: Attacker can stall Forta vault undelegations (locked funds via balance donation)

Source:
- https://crypto.training/hacks/32467-attacker-can-stall-undelegations-openzeppelin-none-forta-sta/

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
- logic/incorrect-value-source, defi/griefing, math/underflow-dos

Dedupe:
- id: `32467-attacker-can-stall-undelegations-openzeppelin-none-forta-sta`
- fingerprint: `5fdee0ce83e6f77047630ca818ded9296fdfbb08f6fb42704b547d6c5f72fbaa`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
