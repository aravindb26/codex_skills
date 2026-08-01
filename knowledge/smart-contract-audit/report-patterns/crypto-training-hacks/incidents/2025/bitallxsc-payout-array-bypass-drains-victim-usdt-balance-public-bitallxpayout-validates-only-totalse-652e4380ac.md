# Crypto Training Exploit Pattern Stub: BitallxSC payout-array bypass drains victim USDT balance — public `BitallxPayOut` validates only `totalSendAmount`, never `sum(amount[])`

Source:
- https://crypto.training/hacks/2025-05-bitallx/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- 2,029.47 USDT (2,029,473,999,999,999,986,000 wei) — full victim contract balance [output.…

Tags:
- access-control/missing-auth, logic/missing-validation, logic/missing-check

Dedupe:
- id: `2025-05-bitallx`
- fingerprint: `652e4380ac7ec02f2b2e2527d56a93568e9d4988f8171c11daad30052edcda9b`

Core exploit idea:
- BitallxSC is a small BSC rewards/payout contract holding ~2,029.47 USDT in treasury. It exposes a function BitallxPayOut(tokencontract, wallet[], amount[], totalSendAmou…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
