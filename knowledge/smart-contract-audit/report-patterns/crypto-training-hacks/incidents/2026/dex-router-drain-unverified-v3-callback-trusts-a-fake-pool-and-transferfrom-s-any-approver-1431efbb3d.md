# Crypto Training Exploit Pattern Stub: DEX router drain — unverified V3 callback trusts a fake pool and `transferFrom`s any approver

Source:
- https://crypto.training/hacks/2026-09-routerdrain/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- Incident ~62.28 WBNB from 29 victims. This PoC drains a representative 3 (OCEAN, Kandura,…

Tags:
- access-control/missing-auth, input-validation/missing, logic/missing-check

Dedupe:
- id: `2026-09-routerdrain`
- fingerprint: `1431efbb3d3247a2cd33bd9df5dd66bd9cc8ea58c61c5f9f73c56ec5145dedf4`

Core exploit idea:
- The router exposes a permissionless swap entry (selector 0x33411b5e). Routes carry an attacker-chosen pool. The router calls pool.swap(0x128acb08) without checking that…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
