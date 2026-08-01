# Crypto Training Exploit Pattern Stub: Blueberry HyperliquidEscrow — tvl() omits in-flight USDC

Source:
- https://crypto.training/hacks/61494-h-01-escrowtvl-does-not-add-in-flight-usdc-amount-pashov-aud/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-state

Dedupe:
- id: `61494-h-01-escrowtvl-does-not-add-in-flight-usdc-amount-pashov-aud`
- fingerprint: `1ba1d172a955c5416296000efec9fa87100abbf98a0dda3473de2c43b705150c`

Core exploit idea:
- 1. Non-USDC assets add same-block in-flight bridge amounts into TVL. 2. The USDC branch only counts balanceOf and skips in-flight. 3. Deposit against understated TVL min…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
