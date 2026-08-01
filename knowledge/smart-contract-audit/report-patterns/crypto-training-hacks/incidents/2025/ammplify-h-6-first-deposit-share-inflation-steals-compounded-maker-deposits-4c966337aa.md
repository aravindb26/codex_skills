# Crypto Training Exploit Pattern Stub: Ammplify — H-6: First-deposit share inflation steals compounded maker deposits

Source:
- https://crypto.training/hacks/63172-h-6-user-can-lose-all-funds-when-creating-or-increasing-comp/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63172-h-6-user-can-lose-all-funds-when-creating-or-increasing-comp`
- fingerprint: `4c966337aa0951581683247bdddbcb7a23e5b5efe01d1e3ada52636bc4e45f7a`

Core exploit idea:
- 1. Each compounded segment acts as a vault with shares = liq * totalShares / totalLiq (floor). 2. Attacker seeds min liquidity, donates, shrinks to 1 share, donates agai…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
