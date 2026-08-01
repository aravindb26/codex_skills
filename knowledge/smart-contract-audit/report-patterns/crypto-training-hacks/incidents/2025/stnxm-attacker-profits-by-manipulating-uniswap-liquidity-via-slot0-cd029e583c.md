# Crypto Training Exploit Pattern Stub: stNXM — attacker profits by manipulating Uniswap liquidity via slot0

Source:
- https://crypto.training/hacks/64079-h-1-attacker-can-profit-by-manipulating-uniswap-liquidity-sh/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64079-h-1-attacker-can-profit-by-manipulating-uniswap-liquidity-sh`
- fingerprint: `cd029e583c325a429e91edb444064418b359e01e4132850a53bf92c5f75b456e`

Core exploit idea:
- dexBalances reads Uniswap V3 slot0 spot price to value LP inside totalAssets

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
