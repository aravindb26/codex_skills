# Crypto Training Exploit Pattern Stub: Gondi — triggerFee stolen from other auctions in settleWithBuyout

Source:
- https://crypto.training/hacks/35207-h-05-triggerfee-is-stolen-from-other-auctions-during-settlew/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35207-h-05-triggerfee-is-stolen-from-other-auctions-during-settlew`
- fingerprint: `cf3a75e0e8563fc84202a2e76253408554a2cca653a1c6c14313ec1ee7ce824b`

Core exploit idea:
- 1. Multiple auctions share one contract balance of the principal asset. 2. Buyout correctly pulls other-lender repayment from the buyer. 3. triggerFee is paid with safeT…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
