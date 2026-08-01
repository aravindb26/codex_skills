# Crypto Training Exploit Pattern Stub: Alchemix — `RevenueHandler.checkpoint` isn't correct when `poolAdapter` is 0

Source:
- https://crypto.training/hacks/38174-revenuehandlercheckpoint-isnt-correctly-immunefi-alchemix-gi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/double-counting, reward-calculation/wrong-amount, loss-of-funds/direct-drain

Dedupe:
- id: `38174-revenuehandlercheckpoint-isnt-correctly-immunefi-alchemix-gi`
- fingerprint: `0712d908ff3752f9706b13a3c3e1e2a81ef2ebfaae55a66ce96244af666b642e`

Core exploit idea:
- 1. RevenueHandler.checkpoint(), for a revenue token with poolAdapter == address(0) (a plain, non-alchemic token like DAI), sets amountReceived = thisBalance and does epo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
