# Crypto Training Exploit Pattern Stub: Blackhole — inverted `setRouter` zero-address check bricks pool launches

Source:
- https://crypto.training/hacks/58333-h-01-router-address-validation-logic-error-prevents-valid-ro/

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
- access-control/broken-logic, logic/wrong-condition, liveness/admin-brick

Dedupe:
- id: `58333-h-01-router-address-validation-logic-error-prevents-valid-ro`
- fingerprint: `12f2b00c08a5611ec6c8b9bcd3ff1cf81632f810ac2fe5c45ef1ba170752c6fc`

Core exploit idea:
- 1. setRouter(address _router) is meant to let the owner update the DEX router used when a GenesisPool launches and adds liquidity. 2. The require is inverted: require(_r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
