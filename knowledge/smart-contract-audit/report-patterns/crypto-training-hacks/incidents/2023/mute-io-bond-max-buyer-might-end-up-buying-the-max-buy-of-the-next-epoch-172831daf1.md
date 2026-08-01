# Crypto Training Exploit Pattern Stub: Mute.Io — Bond max-buyer might end up buying the max buy of the next epoch

Source:
- https://crypto.training/hacks/16038-h-01-bond-max-buyer-might-end-up-buying-the-max-buy-of-the-n/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `16038-h-01-bond-max-buyer-might-end-up-buying-the-max-buy-of-the-n`
- fingerprint: `172831daf1a23d7d5ae1a3e803fa90dbb49f31ccf80148a7c58312a707eeaf9f`

Core exploit idea:
- deposit(..., max_buy=true) ignores the caller's intended epoch and always takes the current epoch's remaining max. If the epoch rolls before inclusion, the buyer silentl…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
