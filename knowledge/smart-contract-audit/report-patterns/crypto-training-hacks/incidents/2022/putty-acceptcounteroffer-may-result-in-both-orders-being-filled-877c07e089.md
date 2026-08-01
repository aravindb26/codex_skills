# Crypto Training Exploit Pattern Stub: Putty — acceptCounterOffer may result in both orders being filled

Source:
- https://crypto.training/hacks/42730-h-02-acceptcounteroffer-may-result-in-both-orders-being-fill/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `42730-h-02-acceptcounteroffer-may-result-in-both-orders-being-fill`
- fingerprint: `877c07e08905dd297fcac60c93afcb36f1fcbdb63db0f116f1ba0c21ac62b85f`

Core exploit idea:
- 1. acceptCounterOffer cancels originalOrder then fills the counter order. 2. cancel() does not revert if the order was already filled. 3. Frontrunner fills original firs…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
