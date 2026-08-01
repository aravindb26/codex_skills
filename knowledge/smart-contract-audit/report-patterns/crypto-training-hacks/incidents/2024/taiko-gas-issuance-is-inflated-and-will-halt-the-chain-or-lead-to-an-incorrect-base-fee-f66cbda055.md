# Crypto Training Exploit Pattern Stub: Taiko — gas issuance is inflated and will halt the chain or lead to an incorrect base fee

Source:
- https://crypto.training/hacks/31929-h-01-gas-issuance-is-inflated-and-will-halt-the-chain-or-lea/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation, dos/liveness-brick, accounting/stale-reference

Dedupe:
- id: `31929-h-01-gas-issuance-is-inflated-and-will-halt-the-chain-or-lea`
- fingerprint: `f66cbda055cd59f4ee40ec1a4a22ed67b521924f117430c05ecb31570dd993f6`

Core exploit idea:
- 1. TaikoL2.anchor() is called once per L2 block by a fixed system address, passing the current L1 block height (_l1BlockId). It recomputes the EIP-1559 base fee via _cal…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
