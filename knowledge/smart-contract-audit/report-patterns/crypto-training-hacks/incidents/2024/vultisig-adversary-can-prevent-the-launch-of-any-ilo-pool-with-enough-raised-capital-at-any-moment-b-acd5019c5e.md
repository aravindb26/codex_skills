# Crypto Training Exploit Pattern Stub: Vultisig — adversary can prevent the launch of any ILO pool with enough raised capital, at any moment, by providing single-sided liquidity

Source:
- https://crypto.training/hacks/35755-h-03-adversary-can-prevent-the-launch-of-any-ilo-pool-with-e/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/spot-price-manipulation, dos/permanent-launch-block

Dedupe:
- id: `35755-h-03-adversary-can-prevent-the-launch-of-any-ilo-pool-with-e`
- fingerprint: `acd5019c5ec55d82998c2a010d3e87811d44a71730e3dac16107c3f6d58f03cc`

Core exploit idea:
- 1. ILOManager.launch() requires the ILO pool's CURRENT Uniswap V3 price to exactly equal the price cached when the project was initialized — otherwise it reverts with "U…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
