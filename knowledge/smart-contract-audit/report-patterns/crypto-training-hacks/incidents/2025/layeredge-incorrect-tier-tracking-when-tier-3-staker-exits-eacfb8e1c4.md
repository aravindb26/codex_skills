# Crypto Training Exploit Pattern Stub: LayerEdge — Incorrect tier tracking when tier 3 staker exits

Source:
- https://crypto.training/hacks/56947-h-1-incorrect-tier-tracking-when-tier-3-staker-exits-in-a-ce/

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
- id: `56947-h-1-incorrect-tier-tracking-when-tier-3-staker-exits-in-a-ce`
- fingerprint: `eacfb8e1c4b25c37a790c382954d8d792f738cd81e34c10bd47f341902fbd553`

Core exploit idea:
- 1. With 15 stakers, tiers are correctly (3, 4, 8). 2. A Tier-3 staker fully unstakes → expected (2, 4, 8). 3. Because new_t2 == old_t2, the removal path only rewrites ra…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
