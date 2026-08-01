# Crypto Training Exploit Pattern Stub: INIT Capital — MarginTradingHook#updateOrder lacks access control

Source:
- https://crypto.training/hacks/30257-h-01-margintradinghookupdateorder-lacks-access-control-code4/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier, logic/order-management

Dedupe:
- id: `30257-h-01-margintradinghookupdateorder-lacks-access-control-code4`
- fingerprint: `b7f7507fe663533e3892cf95f6c88d15937ee097e2b690e97eadab1435cba1e8`

Core exploit idea:
- 1. MarginTradingHook.updateOrder(_posId, _orderId, ...) resolves the CALLER's own initPosId from _posId and checks only that it is non-zero (that the caller owns SOME po…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
