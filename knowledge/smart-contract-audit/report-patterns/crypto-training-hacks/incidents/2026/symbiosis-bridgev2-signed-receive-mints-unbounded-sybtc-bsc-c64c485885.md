# Crypto Training Exploit Pattern Stub: Symbiosis BridgeV2 — signed receive mints unbounded syBTC (BSC)

Source:
- https://crypto.training/hacks/2026-09-symbiosisbridgev2sybtc/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- Headline ~$336k realized (4.39 WBTC dumped on Ethereum Uni V4). This PoC reproduces the B…

Tags:
- bridge/missing-validation, logic/missing-validation, input-validation/missing, auth/signature-validation

Dedupe:
- id: `2026-09-symbiosisbridgev2sybtc`
- fingerprint: `c64c485885c9ca8c4038d19abecf18a8c111bb390cdf474b983a4757f6620ac2`

Core exploit idea:
- Symbiosis BridgeV2 treats an MPC signature as sufficient to mint synthetic BTC.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
