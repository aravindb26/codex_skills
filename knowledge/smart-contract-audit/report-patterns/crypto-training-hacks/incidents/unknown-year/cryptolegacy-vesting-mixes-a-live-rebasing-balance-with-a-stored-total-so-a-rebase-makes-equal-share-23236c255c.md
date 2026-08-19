# Crypto Training Exploit Pattern Stub: CryptoLegacy: Vesting mixes a live rebasing balance with a stored total, so a rebase makes equal shares pay unequally

Source:
- https://crypto.training/hacks/61287-rebaseable-tokens-cause-unfair-vesting-and-claim-failures-/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61287-rebaseable-tokens-cause-unfair-vesting-and-claim-failures-`
- fingerprint: `23236c255ca2b8500fca81693ecb03fa753501061e5d0aa08fd9a9d619d6dbe7`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
