# Crypto Training Exploit Pattern Stub: Virtuals — stale `promptMulti` cache burns and misroutes user payments

Source:
- https://crypto.training/hacks/61827-h-06-missing-prevagentidupdate-in-promptmulti-function-may-c/

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
- logic/incorrect-state-transition, logic/state-update, logic/missing-check

Dedupe:
- id: `61827-h-06-missing-prevagentidupdate-in-promptmulti-function-may-c`
- fingerprint: `a7252e0e5630b3efcefcb87663c5acd108f0695e3eb5476cd67ba1f1b7625982`

Core exploit idea:
- promptMulti tries to cache an agent token-bound account for consecutive identical agent IDs. It loads an address when the ID changes, but never assigns the new ID to pre…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
