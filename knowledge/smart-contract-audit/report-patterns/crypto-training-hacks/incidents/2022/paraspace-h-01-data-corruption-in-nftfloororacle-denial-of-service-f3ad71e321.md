# Crypto Training Exploit Pattern Stub: ParaSpace — [H-01] Data corruption in NFTFloorOracle; Denial of Service

Source:
- https://crypto.training/hacks/25723-h-01-data-corruption-in-nftfloororacle-denial-of-service-cod/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `25723-h-01-data-corruption-in-nftfloororacle-denial-of-service-cod`
- fingerprint: `f3ad71e32142a9aff0f63632da850b0d5db24e8f9bd5341216375fd51363e165`

Core exploit idea:
- 1. Remove feeder B (middle): last feeder C is swapped into B's slot. 2. feederPositionMap[C].index still says 2 while array length is 2. 3. removeFeeder(C) reads feeders…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
