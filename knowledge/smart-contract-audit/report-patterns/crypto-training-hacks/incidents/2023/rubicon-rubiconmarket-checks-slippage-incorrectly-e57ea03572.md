# Crypto Training Exploit Pattern Stub: Rubicon — RubiconMarket checks slippage incorrectly

Source:
- https://crypto.training/hacks/48950-h-11-rubiconmarket-checks-slippage-incorrectly-code4rena-rub/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `48950-h-11-rubiconmarket-checks-slippage-incorrectly-code4rena-rub`
- fingerprint: `e57ea0357287b55aae471268e13e1e92d144c77cac75a6f2268a7071e982ad81`

Core exploit idea:
- sellAllAmount requires fill_amt >= min_fill_amount before calcAmountAfterFee, so a post-fee floor can be violated.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
