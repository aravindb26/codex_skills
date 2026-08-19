# Crypto Training Exploit Pattern Stub: Barter DAO: A malicious taker re-enters swap() for a second same-maker order sharing the same takerTok

Source:
- https://crypto.training/hacks/63500-double-order-attack-via-callback-mechanism-mixbytes-none-bar/

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
- id: `63500-double-order-attack-via-callback-mechanism-mixbytes-none-bar`
- fingerprint: `ebb13c94f407000afa36f506230cb1cdc8370041668208a27146123f40128d04`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
