# Crypto Training Exploit Pattern Stub: VaderPoolV2 synth redemption priced off manipulable spot reserves drains the pool

Source:
- https://crypto.training/hacks/42333-h-02-redemption-value-of-synths-can-be-manipulated-to-drain/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- defi/price-manipulation, oracle/spot-price, defi/direct-drain

Dedupe:
- id: `42333-h-02-redemption-value-of-synths-can-be-manipulated-to-drain`
- fingerprint: `b95a621e095e347539b82bd2e00ffc8a273db8ae5a2bebdfc027349bfcfca6ee`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
