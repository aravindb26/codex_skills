# Crypto Training Exploit Pattern Stub: FixedTokenBSwap RTV drain — attacker-supplied `path` + fake-token `transferFrom` bypass the on-chain price check, extracting a fixed 10 RTV per call

Source:
- https://crypto.training/hacks/2025-06-FixedTokenBSwap/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Ethereum

Loss / impact summary:
- 500 RTV drained from the swap contract (~2,203.63 USD headline; ~1,617 USD in realized ET…

Tags:
- logic/price-calculation, oracle/price-manipulation, logic/missing-validation

Dedupe:
- id: `2025-06-FixedTokenBSwap`
- fingerprint: `0c1623e6c29892aaf5361161f46588814096da4c36f3d8dc66800ce9563806e9`

Core exploit idea:
- FixedTokenBSwap is a "swap X for a fixed 10 RTV" sale contract. The price of the input token is computed on-chain with router.getAmountsIn(tokenBOut, path), where the en…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
