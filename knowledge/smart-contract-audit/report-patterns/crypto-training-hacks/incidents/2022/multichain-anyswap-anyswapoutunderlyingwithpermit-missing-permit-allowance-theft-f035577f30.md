# Crypto Training Exploit Pattern Stub: Multichain (Anyswap) `anySwapOutUnderlyingWithPermit` — Missing-`permit` Allowance Theft

Source:
- https://crypto.training/hacks/2022-11-NUM/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Ethereum

Loss / impact summary:
- 557,754.45 NUM swapped out → attacker netted 13,822.28 USDC in this single reproduced tx;…

Tags:
- dependency/unchecked-return-value, logic/missing-validation

Dedupe:
- id: `2022-11-NUM`
- fingerprint: `f035577f3083a4f6fa32c828b2399ab6925b5a7ba3ef50dc82c95bf2accb0f25`

Core exploit idea:
- Multichain's AnyswapV4Router.anySwapOutUnderlyingWithPermit() is supposed to let a user authorize a cross-chain transfer with a single EIP-2612 signature: the router cal…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
