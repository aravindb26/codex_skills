# Crypto Training Exploit Pattern Stub: Majority Protocol — free cross-game participation via unbound questionId

Source:
- https://crypto.training/hacks/65374-users-can-participate-in-an-infinite-number-of-games-they-ha/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65374-users-can-participate-in-an-infinite-number-of-games-they-ha`
- fingerprint: `9c4068cb1a42b34ad123f12e2edcd19f51fc75e7ef23e9ca6119379cdaf2c5bd`

Core exploit idea:
- commitReaction only checks the caller joined _gameId, then forwards an arbitrary _questionId to the prompt strategy. Reactions are stored by questionId alone, so a free-…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
