# Crypto Training Exploit Pattern Stub: Phi — signature replay in `signatureClaim` ignores chain id

Source:
- https://crypto.training/hacks/41087-h-01-signature-replay-in-signatureclaim-results-in-unauthori/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-chain-binding, signature/replay-across-chains, logic/discarded-validation-field

Dedupe:
- id: `41087-h-01-signature-replay-in-signatureclaim-results-in-unauthori`
- fingerprint: `7edc011b41b968c0dfa129b78adbfc3c6dc00712e5be16e2e75ded44a929b69c`

Core exploit idea:
- 1. PhiFactory.signatureClaim unpacks its signed encodeData_ into (expiresIn_, minter_, ref_, verifier_, artId_, , data_) — the sixth tuple slot is bound to nothing; it i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
