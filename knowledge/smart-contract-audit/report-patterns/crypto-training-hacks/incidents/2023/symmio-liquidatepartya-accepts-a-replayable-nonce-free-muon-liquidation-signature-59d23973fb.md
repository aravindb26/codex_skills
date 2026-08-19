# Crypto Training Exploit Pattern Stub: SYMMIO `liquidatePartyA` accepts a replayable, nonce-free Muon liquidation signature

Source:
- https://crypto.training/hacks/26346-h-1-liquidatepartya-requires-signature-which-doesnt-have-non/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/replay, defi/liquidation

Dedupe:
- id: `26346-h-1-liquidatepartya-requires-signature-which-doesnt-have-non`
- fingerprint: `59d23973fb6b4c6258367968cd0f9236efecbd2445bb71149944783fbb898ccb`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
