# Crypto Training Exploit Pattern Stub: AnyswapV4Router permit-fallback drain — trusting a non-reverting `permit()` on a token that does not enforce it

Source:
- https://crypto.training/hacks/2025-07-AnyswapWETHPermit/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- 200 WETH (amount modelled in the PoC; the on-chain attack tx drained a victim who had a s…

Tags:
- dependency/unchecked-return-value, logic/missing-validation, access-control/missing-auth

Dedupe:
- id: `2025-07-AnyswapWETHPermit`
- fingerprint: `b350c1fe6b617a798af0e53caa19d4f2ad6757096ff0ca7a64cd4751d31a62f3`

Core exploit idea:
- AnyswapV4Router is a cross-chain bridge router. Its anySwapOutUnderlyingWithPermit entry point is meant to take an EIP-2612 permit signature from a user, apply it on the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
