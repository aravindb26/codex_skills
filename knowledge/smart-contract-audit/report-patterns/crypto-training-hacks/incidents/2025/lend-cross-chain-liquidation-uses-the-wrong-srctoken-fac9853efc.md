# Crypto Training Exploit Pattern Stub: LEND — Cross-chain liquidation uses the wrong srcToken

Source:
- https://crypto.training/hacks/58383-lend-cross-chain-liquidation-uses-the-wrong-srctoken/

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
- logic/wrong-condition, bridge/missing-validation

Dedupe:
- id: `58383-lend-cross-chain-liquidation-uses-the-wrong-srctoken`
- fingerprint: `fac9853efca79a11dc6e5d1feddbf971c7d21936e8ac2fcf210932e0809c4112`

Core exploit idea:
- The liquidation message encodes the destination token as srcToken, so the remote router debits a different market than the one liquidated.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
