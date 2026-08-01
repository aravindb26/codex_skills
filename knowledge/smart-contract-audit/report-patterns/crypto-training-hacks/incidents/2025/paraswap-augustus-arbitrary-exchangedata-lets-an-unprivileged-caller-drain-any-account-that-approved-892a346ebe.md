# Crypto Training Exploit Pattern Stub: ParaSwap Augustus — arbitrary `exchangeData` lets an unprivileged caller drain any account that approved the router — $2,299 DAI

Source:
- https://crypto.training/hacks/2025-06-ParaSwapDAIApproval/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Ethereum

Loss / impact summary:
- 2,298.68 USD (2,299.037 DAI) — full drain of the victim account's DAI balance [output.txt…

Tags:
- access-control/missing-auth, logic/missing-validation, dependency/unsafe-external-call

Dedupe:
- id: `2025-06-ParaSwapDAIApproval`
- fingerprint: `892a346ebebc0faeaf022255b77194ed1ee0c8ed4353634999df413e800481f0`

Core exploit idea:
- ParaSwap's AugustusSwapper is a DEX-aggregation router. Its simpleSwap(SimpleData) entry point is designed to take a fromToken/fromAmount from the caller and execute an…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
