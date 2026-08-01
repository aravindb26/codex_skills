# Crypto Training Exploit Pattern Stub: Alchemix — loss of unclaimed bribes after burning a veALCX token

Source:
- https://crypto.training/hacks/38175-loss-of-unclaimed-bribes-after-burning-vealcx-token-immunefi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/ownership-check-after-burn, logic/missing-forced-claim, dos/frozen-funds

Dedupe:
- id: `38175-loss-of-unclaimed-bribes-after-burning-vealcx-token-immunefi`
- fingerprint: `3677c9262ae2c1881f14789eefa87efd443f39aead9afd9c1ad8d3262f70b318`

Core exploit idea:
- 1. A veALCX holder votes for a pool through Voter.vote(). The pool's Bribe contract earns them third-party reward tokens (e.g. BAL) for that epoch. 2. When the lock expi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
