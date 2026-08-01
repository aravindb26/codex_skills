# Crypto Training Exploit Pattern Stub: Unverified `0xb309…28Cb` MEV Router — Unprotected `uniswapV3SwapCallback` Token Drain

Source:
- https://crypto.training/hacks/2024-09-unverified_a89f/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2024

Chain:
- Ethereum

Loss / impact summary:
- 0.36 WETH drained in this tx (≈ $0.9k at Sept-2024 prices; the campaign across the two kn…

Tags:
- access-control/missing-auth, logic/missing-check

Dedupe:
- id: `2024-09-unverified_a89f`
- fingerprint: `57cc39640e23faa89a552371847a59e828d6c0984ba2965ce8db91d004da4484`

Core exploit idea:
- 0xb309…28Cb is a MEV / arbitrage router that performs Uniswap-V3 flash swaps. A V3 swap works by optimistically sending the output to the recipient and then swap() invok…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
