# Crypto Training Exploit Pattern Stub: INIT Capital — Order creator can update tokenOut to arbitrary token

Source:
- https://crypto.training/hacks/30258-h-02-orders-creator-can-update-tokenout-to-arbitrary-token-c/

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
- id: `30258-h-02-orders-creator-can-update-tokenout-to-arbitrary-token-c`
- fingerprint: `2144b21d518a40965f40bfd86e561c6a9ca81bd760da4bb2a097b0f6ac9a2c79`

Core exploit idea:
- 1. createOrder enforces tokenOut ∈ {baseAsset, quoteAsset}. 2. updateOrder rewrites order.tokenOut with no such check. 3. Executors commonly pre-approve the hook for man…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
