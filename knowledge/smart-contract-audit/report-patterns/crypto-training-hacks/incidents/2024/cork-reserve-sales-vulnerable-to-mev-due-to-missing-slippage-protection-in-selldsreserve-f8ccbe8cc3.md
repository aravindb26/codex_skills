# Crypto Training Exploit Pattern Stub: Cork — Reserve sales vulnerable to MEV due to missing slippage protection in `_sellDsReserve`

Source:
- https://crypto.training/hacks/53125-reserve-sales-vulnerable-to-mev-due-to-missing-slippage-prot/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `53125-reserve-sales-vulnerable-to-mev-due-to-missing-slippage-prot`
- fingerprint: `f8ccbe8cc34018ab2b3e633792f2f811dc6611e9861f898922659ccd39d2917d`

Core exploit idea:
- 1. User RA→DS swaps can trigger a protocol reserve sale of DS for RA. 2. _sellDsReserve calls the swap with hardcoded amountOutMin = 0. 3. An MEV bot dumps DS into the p…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
