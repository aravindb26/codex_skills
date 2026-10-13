# Crypto Training Exploit Pattern Stub: Cozy Finance v2 — UMA Optimistic Oracle fake YES drains the protection Set

Source:
- https://crypto.training/hacks/2026-09-cozyfinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Base

Loss / impact summary:
- ~$160K USDC.e. PoC: Set drained 158,148.088467 USDC.e; attacker net 165,718.768963 USDC.e…

Tags:
- oracle/missing-validation, oracle/missing-circuit-breaker, logic/missing-check, access-control/missing-auth

Dedupe:
- id: `2026-09-cozyfinance`
- fingerprint: `4844d73900aba31805673cc1eeb1d71f1c0f70c041669c6c8c32e32a4d5faffd`

Core exploit idea:
- Cozy v2 protection markets pay out if a UMA Optimistic Oracle request settles YES. Anyone may proposePrice. The trigger's priceProposed callback only requires proposedPr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
