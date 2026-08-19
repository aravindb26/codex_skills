# Crypto Training Exploit Pattern Stub: AZTEC Swap validator: missing elliptic-curve pairing check

Source:
- https://crypto.training/hacks/16736-aztec-swap-validator-missing-pairing-check/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `16736-aztec-swap-validator-missing-pairing-check`
- fingerprint: `a4eb9b0becb1a0f17ac2636b9f7a7dd41b840c82ee2eae502e46acc7f76709cc`

Core exploit idea:
- The AZTEC Swap validator verifies a confidential swap zero-knowledge proof but omits the elliptic-curve pairing check (validatePairing). The pairing is the only step tha…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
