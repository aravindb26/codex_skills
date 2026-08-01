# Crypto Training Exploit Pattern Stub: DittoETH — Users can lose collateral when exiting a short

Source:
- https://crypto.training/hacks/27476-users-can-loose-collateral-when-exiting-a-short-codehawks-di/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/stale-snapshot, loss-of-funds/permanent-lock, logic/self-match

Dedupe:
- id: `27476-users-can-loose-collateral-when-exiting-a-short-codehawks-di`
- fingerprint: `5f781397cce4ef6b6c5ff2b1bb87b08464ee82166131678e24914637d9f314e6`

Core exploit idea:
- 1. exitShort closes a short by placing a bid to buy back its debt. 2. If a user has a partially-filled short (some debt already locked into a ShortRecord, the rest still…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
