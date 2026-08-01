# Crypto Training Exploit Pattern Stub: Zaros — incorrect logic for checking isFillPriceValid

Source:
- https://crypto.training/hacks/37984-incorrect-logic-for-checking-isfillpricevalid-codehawks-zaro/

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
- logic/wrong-condition, liveness/order-never-executes, loss-of-funds/missed-take-profit

Dedupe:
- id: `37984-incorrect-logic-for-checking-isfillpricevalid-codehawks-zaro`
- fingerprint: `c3342ebe3a30cf73daf9162d9b7587f5a3b53b326c68d4fd317fd3a5c0ce8e67`

Core exploit idea:
- 1. Offchain (take-profit / stop-loss) orders are gated by isFillPriceValid, which should let a buy order fill once fillPrice = targetPrice (don't undersell / lock in the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
