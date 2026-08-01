# Crypto Training Exploit Pattern Stub: Prime Vaults — removed strategy remains callable during withdrawal

Source:
- https://crypto.training/hacks/64014-h-01-removed-strategy-bypass-removal-block-withdrawals/

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
- logic/incorrect-state-transition, dos/frozen-funds

Dedupe:
- id: `64014-h-01-removed-strategy-bypass-removal-block-withdrawals`
- fingerprint: `a28f30379df96da364046399575e810bcff05ffb99a62b4173f92eb61afc1bf9`

Core exploit idea:
- removeStrategy deletes a struct, resetting kind to SingleAsset and active to false. PrimeStrategy ignores active, so its withdrawal queue still calls the removed strateg…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
