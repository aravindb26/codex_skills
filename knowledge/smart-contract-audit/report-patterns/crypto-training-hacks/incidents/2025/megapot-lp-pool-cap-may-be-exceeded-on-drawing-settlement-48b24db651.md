# Crypto Training Exploit Pattern Stub: Megapot — LP pool cap may be exceeded on drawing settlement

Source:
- https://crypto.training/hacks/64142-h-03-lp-pool-cap-may-be-exceeded-on-drawing-settlement-code4/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64142-h-03-lp-pool-cap-may-be-exceeded-on-drawing-settlement-code4`
- fingerprint: `48b24db6518ba90bd4a35f03b807cd3352f718dd975ceb2803cf435f4c1b418b`

Core exploit idea:
- processDrawingSettlement computes newLPValue without the same pool-cap clamp used on deposits

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
