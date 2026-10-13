# Crypto Training Exploit Pattern Stub: Nimiq HTLC handlers — OpenGSN `execute()` ignores the signature and opens an HTLC as the liquidity wallet

Source:
- https://crypto.training/hacks/2026-09-nimiq/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Polygon

Loss / impact summary:
- 50,463.792096 USD of 6-decimal stables: 26,130.641710 USDC + 24,332.489269 USDT0 + 0.6611…

Tags:
- access-control/missing-auth, auth/signature-bypass, bridge/htlc

Dedupe:
- id: `2026-09-nimiq`
- fingerprint: `7195e8a31f7e29bdaace8ed486f026a04f3abd06072d4a522aed2c4d7c207ff5`

Core exploit idea:
- Nimiq's Polygon swap handlers custody HTLCs for USDC, USDT0, and bridged USDC.e. The liquidity wallet had approved both handlers for unlimited token. A direct open() wou…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
