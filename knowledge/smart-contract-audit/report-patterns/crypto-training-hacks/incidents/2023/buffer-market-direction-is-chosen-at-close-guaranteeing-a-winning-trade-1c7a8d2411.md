# Crypto Training Exploit Pattern Stub: Buffer market direction is chosen at close, guaranteeing a winning trade

Source:
- https://crypto.training/hacks/55635-h-03-market-direction-signature-can-be-abused-if-privatekeep/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/replay

Dedupe:
- id: `55635-h-03-market-direction-signature-can-be-abused-if-privatekeep`
- fingerprint: `1c7a8d2411c59f818e2589fb970a8cd7d9b480c54475cfed266a2148ce1fd7bd`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
