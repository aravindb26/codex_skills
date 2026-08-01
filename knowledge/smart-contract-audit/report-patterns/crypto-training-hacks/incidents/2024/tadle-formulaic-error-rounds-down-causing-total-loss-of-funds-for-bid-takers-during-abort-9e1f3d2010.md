# Crypto Training Exploit Pattern Stub: Tadle — formulaic error rounds down, causing total loss of funds for bid takers during abort

Source:
- https://crypto.training/hacks/38067-formulaic-error-rounds-down-causing-total-loss-of-funds-for/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- math/rounding-direction, math/integer-bounds, loss-of-funds/direct-drain

Dedupe:
- id: `38067-formulaic-error-rounds-down-causing-total-loss-of-funds-for`
- fingerprint: `9e1f3d2010ee3157aaf3de3349a29acb3210afdec1241b9af52997cbb5d2bfb1`

Core exploit idea:
- 1. abortBidTaker refunds a taker's deposit after their bid offer is aborted, using depositAmount = stockInfo.points.mulDiv(preOfferInfo.points, preOfferInfo.amount, Floo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
