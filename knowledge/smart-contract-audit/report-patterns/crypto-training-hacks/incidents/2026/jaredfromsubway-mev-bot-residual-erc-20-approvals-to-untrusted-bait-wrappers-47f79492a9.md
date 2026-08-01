# Crypto Training Exploit Pattern Stub: JaredFromSubway MEV Bot — Residual ERC-20 Approvals to Untrusted Bait Wrappers

Source:
- https://crypto.training/hacks/2026-06-JaredFromSubway/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Ethereum

Loss / impact summary:
- CertiK ~4,424 ETH (~$7.5M) after stables → ETH conversion; other outlets cite ~$7.5–15M c…

Tags:
- logic/missing-allowance, dependency/unsafe-external-call, access-control/broken-logic, logic/missing-check

Dedupe:
- id: `2026-06-JaredFromSubway`
- fingerprint: `47f79492a94c40eb32338e444c236c4340e7d4f316adf05f09d4c846aff59575`

Core exploit idea:
- 1. Over weeks, an attacker deployed ~66 fake tokens / forged Uniswap-v2-style pairs and bait wrappers that looked like profitable sandwich / multi-hop arb opportunities…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
