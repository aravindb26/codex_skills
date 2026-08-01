# Crypto Training Exploit Pattern Stub: Bebop JamSettlement self-taker arbitrary-interaction drain — caller-supplied `transferFrom` calldata executed by the settlement contract against accounts that approved it

Source:
- https://crypto.training/hacks/2025-08-BaseBebopSettlement/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Base

Loss / impact summary:
- 3,875.46 USD (1,000 USDC + 901.467 uXRP)

Tags:
- access-control/missing-auth, logic/missing-validation, dependency/unchecked-return-value

Dedupe:
- id: `2025-08-BaseBebopSettlement`
- fingerprint: `691deff877813026c750250990280817f76f807d28b252f8e7deb18aeb4d4a5e`

Core exploit idea:
- Bebop's JamSettlement.settle(...) is meant to atomically execute a signed swap: a taker's signed JamOrder authorizes pulling the taker's sell tokens, then the solver pas…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
