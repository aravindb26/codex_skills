# Crypto Training Exploit Pattern Stub: H-4: Finalize-window auto-vote change manipulates past epoch

Source:
- https://crypto.training/hacks/62811-h-4-finalize-window-vote-changing-vulnerability-auto-voters/

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
- id: `62811-h-4-finalize-window-vote-changing-vulnerability-auto-voters`
- fingerprint: `7959d90899f7307351942e3a9b07822a00755c04ac736f2716b4f40c2c09d0d1`

Core exploit idea:
- Post-epoch auto-vote + live balance counted at finalize; WETH allocation manipulated

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
