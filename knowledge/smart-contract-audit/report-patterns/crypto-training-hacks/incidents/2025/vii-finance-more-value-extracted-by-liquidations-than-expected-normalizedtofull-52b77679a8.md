# Crypto Training Exploit Pattern Stub: VII Finance — more value extracted by liquidations than expected (`normalizedToFull`)

Source:
- https://crypto.training/hacks/61329-more-value-can-be-extracted-by-liquidations-than-expected-du/

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
- logic/liquidation-logic

Dedupe:
- id: `61329-more-value-can-be-extracted-by-liquidations-than-expected-du`
- fingerprint: `52b77679a872de37e423d439e5242cf0d50283f425693e1629afe0529ae17821`

Core exploit idea:
- 1. Liquidation / value transfer walks every enabled tokenId and converts a unit-of-account amount into an ERC-6909 amount via normalizedToFull. 2. normalizedToFull multi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
