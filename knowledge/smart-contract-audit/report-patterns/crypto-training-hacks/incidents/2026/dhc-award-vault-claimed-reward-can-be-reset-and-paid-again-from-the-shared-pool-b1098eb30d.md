# Crypto Training Exploit Pattern Stub: DHC Award vault — claimed reward can be reset and paid again from the shared pool

Source:
- https://crypto.training/hacks/2026-09-dhc/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- On-chain 71,851.02 USDT. PoC reconstruction 71,100.63 USDT (single-pair dump vs original…

Tags:
- logic/incorrect-state-transition, logic/reward-calculation, logic/missing-check

Dedupe:
- id: `2026-09-dhc`
- fingerprint: `b1098eb30d9173fa7621fc407705ccfa36a559a996f52dae880ab0375a15bb42`

Core exploit idea:
- DHC (DeHealth / RedSonic-style "Award" staking) records a fixed reward in createAward with no per-award locked collateral. participateAward does not require the award to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
