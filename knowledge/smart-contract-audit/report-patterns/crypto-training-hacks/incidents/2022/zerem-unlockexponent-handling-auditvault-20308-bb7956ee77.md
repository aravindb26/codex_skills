# Crypto Training Exploit Pattern Stub: Zerem unlockExponent handling — AuditVault 20308

Source:
- https://crypto.training/hacks/20308-zerem-unlock-exponent/

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
- dos/frozen-funds, arithmetic/precision-loss

Dedupe:
- id: `20308-zerem-unlock-exponent`
- fingerprint: `bb7956ee773bca561bea16ffcf4c72438df662638784e7b339e392443f0b368e`

Core exploit idea:
- The unlock calculation only behaves as intended for exponent one; other exponents leave funds locked.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
