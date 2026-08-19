# Crypto Training Exploit Pattern Stub: Yield V2 Witch `buy`/`payAll` accepted vaults that were not under auction

Source:
- https://crypto.training/hacks/16980-yield-v2-witch-buy-payall-no-auction/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, defi/liquidation

Dedupe:
- id: `16980-yield-v2-witch-buy-payall-no-auction`
- fingerprint: `0f4962c92731491bd7bb3fd271f45bc2eb65f21a0c219fa3bff0442dd0e67f25`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
