# Crypto Training Exploit Pattern Stub: INIT Capital — fillOrder executor front-run via limitPrice_e36

Source:
- https://crypto.training/hacks/30259-h-03-fillorder-executor-can-be-front-run-by-the-order-creato/

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
- logic/order-management

Dedupe:
- id: `30259-h-03-fillorder-executor-can-be-front-run-by-the-order-creato`
- fingerprint: `282e9413af9384d9ba34498b6b6d0b936886b9bbb73f889e4a81e93572eb16a9`

Core exploit idea:
- 1. fillOrder computes amtOut from order.limitPrice_e36 (creator's slippage param). 2. On the "long base, coll ≠ tokenOut" branch, amtOut = ceil(coll * limit / 1e36) - re…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
