# Crypto Training Exploit Pattern Stub: SXT — [C-01] Accepting duplicate signatures from one signer

Source:
- https://crypto.training/hacks/63314-c-01-accepting-duplicate-signatures-from-one-signer-pashov-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63314-c-01-accepting-duplicate-signatures-from-one-signer-pashov-a`
- fingerprint: `d83a8aea532bad855cdc55026216bddeb5dd1cd3c795ee6cb7568a63553d1b92`

Core exploit idea:
- Threshold = 2. Attacker submits the same valid (v,r,s) twice. Both recover to one attestor; both count. validateMessage returns true.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
