# Crypto Training Exploit Pattern Stub: Superfluid Locker — Pumponomics can be skipped via `provideLiquidity`

Source:
- https://crypto.training/hacks/58282-h-2-pumponomics-can-be-skipped-when-using-fluidlockerprovide/

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
- unknown

Dedupe:
- id: `58282-h-2-pumponomics-can-be-skipped-when-using-fluidlockerprovide`
- fingerprint: `dfdb60a12713f35309cd72218dd64b4c9457542e0c6f8cd6c237f9fb17d6175d`

Core exploit idea:
- 1. Owner pre-sends WETH into the locker (not via provideLiquidity). 2. Calls provideLiquidity{value: dust}(supAmount). 3. Only dust * 1% is pumped (buy SUP); the positio…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
