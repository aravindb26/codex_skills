# Crypto Training Exploit Pattern Stub: ParaSpace — [H-04] Anyone can prevent themselves from being liquidated

Source:
- https://crypto.training/hacks/15977-h-04-anyone-can-prevent-themselves-from-being-liquidated-as/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `15977-h-04-anyone-can-prevent-themselves-from-being-liquidated-as`
- fingerprint: `0bb2342fb0245c9418710e436b4ad98eb102981245b9e2bc47cec379fd2d3316`

Core exploit idea:
- 1. Comment says owner-only; modifier is only onlyWhenFeederExisted. 2. Anyone removes all feeders → no one can setPrice (UPDATER_ROLE revoked). 3. Liquidations that need…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
