# Crypto Training Exploit Pattern Stub: HeisenbergHook Fee Path Hijack — Unrestricted `poolKey` overwrite + permissionless `processFees`/`processBurn`

Source:
- https://crypto.training/hacks/2026-05-HeisenbergHook/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- Ethereum

Loss / impact summary:
- 0.425919592403168892 ETH attacker profit (gas-free PoC; on-chain net after ~0.0044 ETH ga…

Tags:
- logic/incorrect-state-transition, defi/fee-manipulation, logic/missing-check, input-validation/missing

Dedupe:
- id: `2026-05-HeisenbergHook`
- fingerprint: `6834526b5668f5084879241d117fe0c0d701f6ed80a4f6325307da04c8299721`

Core exploit idea:
- 1. HeisenbergHook is a Uniswap v4 hook for the $HEIST / ETH pool. Sell-side fees accumulate as pendingFeeHEIST (~5,261 HEIST pre-attack); buy-side fees split into treasu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
