# Crypto Training Exploit Pattern Stub: Unverified6883 Fake-Pair Callback Hijack — UniswapV2 flash-swap callback trusts a freshly-created attacker pair and pays WETH into it

Source:
- https://crypto.training/hacks/2025-07-Unverified6883/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$1,006.89 (0.267592 WETH)

Tags:
- logic/missing-validation, access-control/missing-auth, defi/slippage

Dedupe:
- id: `2025-07-Unverified6883`
- fingerprint: `dd6dd7429efbd810b912a94c83fbb397d498430f9927fc6cdfe92d193482a0d3`

Core exploit idea:
- The victim (0x6883…) is an unverified swap helper/router that implements the UniswapV2 flash-swap callback uniswapV2Call. When invoked, it decodes an attacker-supplied p…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
