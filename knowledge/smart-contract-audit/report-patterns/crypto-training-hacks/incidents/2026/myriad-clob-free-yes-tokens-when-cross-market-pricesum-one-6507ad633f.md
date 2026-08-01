# Crypto Training Exploit Pattern Stub: Myriad CLOB — free YES tokens when cross-market `priceSum > ONE`

Source:
- https://crypto.training/hacks/65419-myriadctfexchangematchcrossmarketorders-allows-taker-to-rece/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65419-myriadctfexchangematchcrossmarketorders-allows-taker-to-rece`
- fingerprint: `6507ad633f904904899e7a07da4b3adba359e8d46a168a3fb84f3753b9afeef8`

Core exploit idea:
- 1. Cross-market match requires only priceSum >= ONE, not equality. 2. Maker notionals sum with round-down; taker pays max(0, fill - notionalSoFar). 3. When priceSum > ON…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
