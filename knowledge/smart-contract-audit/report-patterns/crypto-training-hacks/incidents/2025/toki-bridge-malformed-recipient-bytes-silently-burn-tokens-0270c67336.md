# Crypto Training Exploit Pattern Stub: Toki Bridge — malformed recipient bytes silently burn tokens

Source:
- https://crypto.training/hacks/64067-h-01-recipient-bytes-silent-burn-non-20-byte/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/wrong-type, bridge/missing-validation, dos/frozen-funds

Dedupe:
- id: `64067-h-01-recipient-bytes-silent-burn-non-20-byte`
- fingerprint: `0270c67336f9e9843603267feeeaf2c04a7dd8aeb6e9da418c9f9ea7e508f999`

Core exploit idea:
- The bridge accepts any non-empty recipient bytes, but the destination decoder accepts only 20-byte EVM addresses. Decode failure enters an unrecoverable branch without a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
