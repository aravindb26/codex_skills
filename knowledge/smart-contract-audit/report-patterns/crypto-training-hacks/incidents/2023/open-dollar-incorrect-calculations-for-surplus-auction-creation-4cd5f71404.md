# Crypto Training Exploit Pattern Stub: Open Dollar — incorrect calculations for surplus auction creation

Source:
- https://crypto.training/hacks/29347-h-01-incorrect-calculations-for-surplus-auction-creation-cau/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `29347-h-01-incorrect-calculations-for-surplus-auction-creation-cau`
- fingerprint: `4cd5f7140424ada50978c051f644758009084e537991d254d3ff26893d148a30`

Core exploit idea:
- 1. auctionSurplus compares surplusTransferPercentage to ONE_HUNDRED_WAD (always true). 2. amountToSell uses wmul(ONE_HUNDRED_WAD - pct) → ~99× surplusAmount. 3. At 100%…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
