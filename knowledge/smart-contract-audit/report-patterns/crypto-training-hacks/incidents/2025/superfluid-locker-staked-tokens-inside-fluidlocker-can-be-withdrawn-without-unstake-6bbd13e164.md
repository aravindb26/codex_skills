# Crypto Training Exploit Pattern Stub: Superfluid Locker — Staked tokens inside FluidLocker can be withdrawn without Unstake

Source:
- https://crypto.training/hacks/58281-h-1-staked-tokens-inside-fluidlocker-can-be-withdrawn-withou/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58281-h-1-staked-tokens-inside-fluidlocker-can-be-withdrawn-withou`
- fingerprint: `6bbd13e164ff3422fcf3938a5f8411f0817cd514c03debde5e0fc6e0c58a28c2`

Core exploit idea:
- 1. Owner stakes all FLUID in the locker (_stakedBalance = balance). 2. provideLiquidity(supAmount) does not check available balance — staked tokens leave to Uniswap. 3.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
