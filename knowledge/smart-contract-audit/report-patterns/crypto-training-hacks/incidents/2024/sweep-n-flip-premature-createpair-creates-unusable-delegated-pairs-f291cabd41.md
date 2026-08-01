# Crypto Training Exploit Pattern Stub: Sweep n Flip — Premature createPair creates unusable delegated pairs

Source:
- https://crypto.training/hacks/46466-premature-createpair-function-call-will-result-in-the-creati/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check

Dedupe:
- id: `46466-premature-createpair-function-call-will-result-in-the-creati`
- fingerprint: `f291cabd41e0605e63d0f13e0c38ff3d43ee2bea9ea18f460d142b0991438e3d`

Core exploit idea:
- 1. Wrapper addresses for ERC721 collections are CREATE2-predictable from the factory. 2. Ideal flow is createWrapper then createPair. An attacker can call createPair(usd…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
