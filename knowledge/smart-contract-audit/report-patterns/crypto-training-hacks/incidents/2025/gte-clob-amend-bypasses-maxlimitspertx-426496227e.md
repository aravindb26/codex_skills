# Crypto Training Exploit Pattern Stub: GTE CLOB — amend bypasses maxLimitsPerTx

Source:
- https://crypto.training/hacks/64871-h-03-dos-attack-via-order-amendment-bypassing-maxlimitspertx/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64871-h-03-dos-attack-via-order-amendment-bypassing-maxlimitspertx`
- fingerprint: `426496227e3ebbfbfed1dcfaee56669a8ad8697406c1f602edd5e3077eedb62a`

Core exploit idea:
- 1. postLimitOrder enforces maxLimitsPerTx via incrementLimitsPlaced. 2. amend to a new price creates a new book position without incrementing. 3. Attacker posts up to th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
