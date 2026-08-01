# Crypto Training Exploit Pattern Stub: VTSwapHook reserve/fee accounting divergence — Uniswap V4 custom-curve hook books full specified amount into reserves while pricing output on the fee-reduced input

Source:
- https://crypto.training/hacks/2026-03-VTSwapHook/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Arbitrum

Loss / impact summary:
- 4,507,034.03 vATH + 2,007,935.14 ATH (per @KeyInfo)

Tags:
- logic/incorrect-state-transition, logic/state-update, defi/fee-manipulation

Dedupe:
- id: `2026-03-VTSwapHook`
- fingerprint: `2d610695e9e7210bb62bf32948fe08d979ac3f5bd1b62b257b2697dd57bb0e47`

Core exploit idea:
- VTSwapHook is an Aethir-style vesting-token (VT) swap pool built as a Uniswap V4 custom-curve hook (beforeSwapReturnDelta = true). Instead of using V4's concentrated-liq…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
