# Crypto Training Exploit Pattern Stub: Pendle Reflector — reflect() operated on Reflector-held balances using caller-supplied, unvalidated market and limit-router addresses

Source:
- https://crypto.training/hacks/2025-08-PendleReflector/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Arbitrum

Loss / impact summary:
- ~2,304.18 USD (Reflector's full balances of PT-mPendle-27MAR2025 and PT-stk-EPendle-27MAR…

Tags:
- access-control/missing-auth, input-validation/missing, defi/slippage

Dedupe:
- id: `2025-08-PendleReflector`
- fingerprint: `a6c551415ba4b845dca5ef794b4f5ae8538272bb90965c51114eba53248b0f2b`

Core exploit idea:
- Pendle's Reflector is a thin fronting contract whose only job is to take a blob of calldata, re-scale the input amount to whatever balance Reflector itself happens to ho…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
