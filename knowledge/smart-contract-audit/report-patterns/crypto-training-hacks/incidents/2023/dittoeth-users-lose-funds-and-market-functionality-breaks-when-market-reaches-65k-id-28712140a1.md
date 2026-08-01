# Crypto Training Exploit Pattern Stub: DittoETH — Users lose funds and market functionality breaks when market reaches 65k id

Source:
- https://crypto.training/hacks/27443-users-lose-funds-and-market-functionality-breaks-when-market/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-check, loss-of-funds/permanent-lock, logic/missing-refund

Dedupe:
- id: `27443-users-lose-funds-and-market-functionality-breaks-when-market`
- fingerprint: `28712140a1972d8597037d47907d8b6abcb06403b02fb8f39759eec9a2949855`

Core exploit idea:
- 1. When a user places a limit order, the amount they commit is deducted from their escrowed virtual balance and locked into the order. 2. The normal cancel path, cancelB…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
