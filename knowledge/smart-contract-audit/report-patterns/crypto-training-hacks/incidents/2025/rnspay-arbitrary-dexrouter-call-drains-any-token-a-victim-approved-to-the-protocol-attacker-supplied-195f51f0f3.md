# Crypto Training Exploit Pattern Stub: RnsPay arbitrary `dexRouter` call drains any token a victim approved to the protocol — attacker-supplied exchange target lets `pay()` execute `transferFrom` against arbitrary victims

Source:
- https://crypto.training/hacks/2025-03-RnsPay/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Ethereum

Loss / impact summary:
- 1,050 USDC (~$1,050), laundered to 0.4632 ETH via Uniswap V2 output.txt:1565

Tags:
- access-control/missing-validation, logic/missing-check, dependency/unsafe-external-call

Dedupe:
- id: `2025-03-RnsPay`
- fingerprint: `195f51f0f37ac11b8204e6ee63b7bfe9c63905b2752e748581886f9fbd042f0c`

Core exploit idea:
- RnsPay is a payments contract intended to route a user's payment token through a DEX and forward the converted receipt token to a merchant. To support that, its pay() fl…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
