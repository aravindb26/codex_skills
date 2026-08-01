# Crypto Training Exploit Pattern Stub: Sequence — partial session-signature replay / frontrun (H-02)

Source:
- https://crypto.training/hacks/63761-h-02-partial-signature-replayfrontrunning-attack-on-session/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/partial-replay, mev/frontrun, bridge/replay

Dedupe:
- id: `63761-h-02-partial-signature-replayfrontrunning-attack-on-session`
- fingerprint: `c8774c729539ed6af94e30d8693e26db3915dd1e5a75b014f43d9166872d366a`

Core exploit idea:
- 1. Calls.execute bumps the nonce, validates the session signature, then runs calls. 2. A later call with BEHAVIOR_REVERT_ON_ERROR reverts the entire transaction → nonce…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
