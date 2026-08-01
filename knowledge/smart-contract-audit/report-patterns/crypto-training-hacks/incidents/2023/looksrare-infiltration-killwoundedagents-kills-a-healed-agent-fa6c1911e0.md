# Crypto Training Exploit Pattern Stub: LooksRare "Infiltration" — _killWoundedAgents kills a healed agent

Source:
- https://crypto.training/hacks/27586-h-1-killwoundedagents-sherlock-looksrare-git/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, state/stale-status-check, loss-of-funds/direct-drain

Dedupe:
- id: `27586-h-1-killwoundedagents-sherlock-looksrare-git`
- fingerprint: `fa6c1911e0e68ce4f78a1640b8f863cf0ec853a1315c9427c94d54fb53fea329`

Core exploit idea:
- 1. _killWoundedAgents(roundId, ...) kills every agent in its list whose status == AgentStatus.Wounded — but it never checks woundedAt == roundId. 2. A player's agent is…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
