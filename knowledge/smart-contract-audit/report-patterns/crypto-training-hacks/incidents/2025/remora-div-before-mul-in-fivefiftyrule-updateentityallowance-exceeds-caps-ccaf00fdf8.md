# Crypto Training Exploit Pattern Stub: Remora — div-before-mul in `FiveFiftyRule::_updateEntityAllowance` exceeds caps

Source:
- https://crypto.training/hacks/63780-divide-before-multiply-loses-precision-in-fivefiftyrule-upda/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/division-before-multiply, arithmetic/precision-loss

Dedupe:
- id: `63780-divide-before-multiply-loses-precision-in-fivefiftyrule-upda`
- fingerprint: `ccaf00fdf85d7e8a84b985fac335ca664e90e2c78b96f81cdc0c9e7a9939129d`

Core exploit idea:
- 1. Allowance updates use (REMORA_PERCENT_DENOMINATOR / equity) amount. 2. Integer division truncates first → delta is smaller than DENOM amount / equity. 3. On the reduc…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
