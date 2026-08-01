# Crypto Training Exploit Pattern Stub: Curve `UnderlyingBurner.execute()` — Zero-Slippage Sandwich on the 3pool

Source:
- https://crypto.training/hacks/2023-08-CurveBurner/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Ethereum

Loss / impact summary:
- ~$36,700 — 36,700.27 USDT extracted from the Curve 3pool by sandwiching the burner

Tags:
- defi/sandwich-attack, defi/slippage, access-control/missing-auth

Dedupe:
- id: `2023-08-CurveBurner`
- fingerprint: `258c93013b28d9780ae1d08b5aaede5c7bd07bafaeb6315208168aecccc2f261`

Core exploit idea:
- Curve's UnderlyingBurner is a fee-processing contract: it accumulates DAI/USDC/USDT (the fees the protocol skims), then anyone can call its public execute() function to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
