# Crypto Training Exploit Pattern Stub: Stake.Link reSDL bridge — stale approval steals returned lock

Source:
- https://crypto.training/hacks/29738-a-user-can-steal-an-already-transfered-and-bridged-resdl-loc/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-check, bridge/missing-validation

Dedupe:
- id: `29738-a-user-can-steal-an-already-transfered-and-bridged-resdl-loc`
- fingerprint: `981d313edeacb0fac602d8ffa910c8138969b3a53ab6c25b87f0a5cc5175ec2b`

Core exploit idea:
- handleOutgoingRESDL removes the lock owner but does not delete its transfer approval. When the same ID returns to a victim, the stale approved account transfers the lock…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
