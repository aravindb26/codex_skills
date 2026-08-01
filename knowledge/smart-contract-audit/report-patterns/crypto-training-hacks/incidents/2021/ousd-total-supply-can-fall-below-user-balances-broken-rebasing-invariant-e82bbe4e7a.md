# Crypto Training Exploit Pattern Stub: OUSD total supply can fall below user balances — broken rebasing invariant

Source:
- https://crypto.training/hacks/18214-ousd-total-supply-can-be-arbitrary-even-smaller-than-user-ba/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- ERC-20 supply accounting becomes inconsistent and can understate claims

Tags:
- logic/wrong-condition, arithmetic/rounding

Dedupe:
- id: `18214-ousd-total-supply-can-be-arbitrary-even-smaller-than-user-ba`
- fingerprint: `e82bbe4e7a6ba00ec41967b9ec7f19948adeab3e26a3d9446ffd476e72b8b168`

Core exploit idea:
- An opted-out account keeps its balance while changeSupply lowers the aggregate total. The common balanceOf(x) <= totalSupply() invariant is immediately false.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
