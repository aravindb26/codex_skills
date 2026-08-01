# Crypto Training Exploit Pattern Stub: ZeroLend — Incorrect reward distribution when t == roundedTimestamp

Source:
- https://crypto.training/hacks/40820-incorrect-reward-distribution-when-t-roundedtimestamp-in-fee/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `40820-incorrect-reward-distribution-when-t-roundedtimestamp-in-fee`
- fingerprint: `2ec43c4830e26d9d2f8a8918f4db412ba3a04bc38d131d733a213117e8a07b0c`

Core exploit idea:
- 1. At an exact epoch boundary, t == roundedTimestamp. 2. The loop uses > so it still writes veSupply[t] from the current locker point. 3. Bob locks more after the checkp…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
