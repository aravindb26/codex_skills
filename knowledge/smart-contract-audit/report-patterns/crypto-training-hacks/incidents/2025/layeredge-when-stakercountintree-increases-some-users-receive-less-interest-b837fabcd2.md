# Crypto Training Exploit Pattern Stub: LayerEdge — When stakerCountInTree increases, some users receive less interest

Source:
- https://crypto.training/hacks/56948-h-2-when-stakercountintree-increases-some-users-may-receive/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `56948-h-2-when-stakercountintree-increases-some-users-may-receive`
- fingerprint: `b837fabcd2a1f709119a35510a54a67d70f519df73a0dc0d94322ba3a7b118cb`

Core exploit idea:
- 1. Staking grows from 14 → 15 users: tiers should go (2,4,8) → (3,4,8). 2. Rank 7 must promote T3 → T2. 3. Because new_t2 == old_t2, the add path only updates old_t1 + o…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
