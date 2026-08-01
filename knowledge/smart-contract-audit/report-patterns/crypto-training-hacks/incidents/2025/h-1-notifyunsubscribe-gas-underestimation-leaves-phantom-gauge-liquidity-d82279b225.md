# Crypto Training Exploit Pattern Stub: H-1: notifyUnsubscribe gas underestimation leaves phantom gauge liquidity

Source:
- https://crypto.training/hacks/62808-h-1-gas-consumed-in-notifyunsubscribe-is-underestimated-duri/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62808-h-1-gas-consumed-in-notifyunsubscribe-is-underestimated-duri`
- fingerprint: `d82279b22503c8ab3c6229246b5499e7da454d4a0d7fdf4d0e4ed28c49cb8910`

Core exploit idea:
- Uniswap unsubscribes while Deli gauge keeps full position liquidity (phantom dilution)

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
