# Crypto Training Exploit Pattern Stub: BitCrown Distributor Drained via Unprotected batchTransfer — anyone could move the distributor's token balance to any recipient

Source:
- https://crypto.training/hacks/2025-06-BitCrown/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ≈ 7,939.27 USDT (≈ $7,939) — 100,000 BITCROWN drained from the distributor and dumped

Tags:
- access-control/missing-modifier, access-control/missing-auth, logic/missing-validation

Dedupe:
- id: `2025-06-BitCrown`
- fingerprint: `29e85a827f68141dea7ec41b95404c469827fdd2a23a18e26e28065c6f4e2ea8`

Core exploit idea:
- BitCrown is a BEP-20 token on BNB Chain that, like many low-cap launches, keeps a large portion of its supply inside a dedicated "distributor" contract (0x93b6…A2A7e) in…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
