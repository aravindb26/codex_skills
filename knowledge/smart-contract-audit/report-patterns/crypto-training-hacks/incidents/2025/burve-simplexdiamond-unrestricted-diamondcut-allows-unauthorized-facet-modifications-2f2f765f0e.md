# Crypto Training Exploit Pattern Stub: Burve SimplexDiamond — Unrestricted `diamondCut` allows unauthorized facet modifications

Source:
- https://crypto.training/hacks/55210-c-03-unrestricted-diamondcut-allows-unauthorized-facet-modif/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55210-c-03-unrestricted-diamondcut-allows-unauthorized-facet-modif`
- fingerprint: `2f2f765f0e4bd70db616edde6cff432a80b85df99619b6e4324f3f8c0a16b5af`

Core exploit idea:
- 1. SimplexDiamond exposes diamondCut without AdminLib.validateOwner() (or any auth). 2. Any address can add/replace/remove facet selectors. 3. Attacker adds a drain face…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
