# Crypto Training Exploit Pattern Stub: Canto — native gas tokens stuck in `ASDRouter` on successful redemption

Source:
- https://crypto.training/hacks/32129-h-01-native-gas-tokens-can-become-stuck-in-asdrouter-contrac/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- fee/missing-refund, bridge/stuck-asset

Dedupe:
- id: `32129-h-01-native-gas-tokens-can-become-stuck-in-asdrouter-contrac`
- fingerprint: `933dfd7e2d896fc693c2bc0a06c0b5f3b34eab00ca837bf4d084bd682251171e`

Core exploit idea:
- 1. Successful lzCompose → _sendASD on same-chain delivery uses 0 of msg.value. 2. Error paths refund fully; success paths do not refund the remainder. 3. Protocol invari…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
