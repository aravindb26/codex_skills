# Crypto Training Exploit Pattern Stub: TraitForge — incorrect percentage calculation in NukeFund and EntityForging

Source:
- https://crypto.training/hacks/37917-h-03-incorrect-percentage-calculation-in-nukefund-and-entity/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- math/percentage-calculation, logic/fee-miscalculation, loss-of-funds/fee-misallocation

Dedupe:
- id: `37917-h-03-incorrect-percentage-calculation-in-nukefund-and-entity`
- fingerprint: `a4676007e6cb7ad3d6ef449e7f3ff5d994ec587ecd60641ce487bc0175a831d6`

Core exploit idea:
- 1. taxCut is meant to be a percentage — the code's own comment calls the default value of 10 "the developer's share (10%)". 2. Both NukeFund.receive() and EntityForging.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
