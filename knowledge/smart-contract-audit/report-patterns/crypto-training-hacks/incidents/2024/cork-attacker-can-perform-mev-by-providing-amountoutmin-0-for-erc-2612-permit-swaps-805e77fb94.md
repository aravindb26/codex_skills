# Crypto Training Exploit Pattern Stub: Cork — Attacker can perform MEV by providing amountOutMin = 0 for ERC-2612 permit swaps

Source:
- https://crypto.training/hacks/53124-attacker-can-perform-mev-by-providing-amountoutmin-0-for-all/

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
- id: `53124-attacker-can-perform-mev-by-providing-amountoutmin-0-for-all`
- fingerprint: `805e77fb947743d6f5a1e92a830f439ed5ffdd251aa90602ac4bb062a1501f49`

Core exploit idea:
- 1. User signs an EIP-2612 permit so the router can pull RA without a prior approve tx. 2. Any third party can submit that permit to swapRaforDs(..., amountOutMin, user,…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
