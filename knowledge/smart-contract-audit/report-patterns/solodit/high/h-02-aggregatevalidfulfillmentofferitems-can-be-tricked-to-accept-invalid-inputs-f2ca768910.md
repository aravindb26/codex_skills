# Solodit Pattern Stub: [H-02] `_aggregateValidFulfillmentOfferItems()` can be tricked to accept invalid inputs

Source:
- https://solodit.cyfrin.io/issues/h-02-_aggregatevalidfulfillmentofferitems-can-be-tricked-to-accept-invalid-inputs-code4rena-opensea-opensea-seaport-contest-git
- https://code4rena.com/reports/2022-05-opensea-seaport

Imported:
- 2026-05-23

Status:
- distilled

Severity:
- HIGH

Protocol:
- OpenSea Seaport

Source platform / firm:
- Code4rena / Spearbit submission

Tags:
- seaport, fulfillment-aggregation, zero-amount, overflow, match-orders

Dedupe:
- id: `2622`
- fingerprint: `f2ca768910f9c0b29ab2fae6b07967c61e3aa72780c96fc0594246c00e3fd326`

Core idea:
- In Seaport 1.0, fulfillment aggregation accumulated validation flags in `errorBuffer` where `1` meant zero amount and `2` meant overflow. If a malicious fulfillment produced both conditions, `errorBuffer == 3`; final handling only matched cases `1` and `2`, so `3` accidentally meant success and invalid aggregate amounts could execute.

Broken invariant:
- Any nonzero aggregation validation error must revert; combined error states must not fall through as success.

Where to look in code:
- Assembly aggregation loops for offer and consideration components.
- Error bitmasks or buffers with switch/case final handling.
- Amount summation followed by zeroing of source items.

Attack path:
1. Create a match/available-order fulfillment with one zero-amount component and another component that overflows the aggregate sum.
2. Aggregation ORs both conditions into a composite error value.
3. Vulnerable final handling misses the composite value.
4. Settlement executes with malformed or near-zero consideration, causing direct value leakage.

False-positive checks:
- Confirm every nonzero `errorBuffer` reverts.
- Confirm `errorBuffer == 3` is treated as overflow or generic failure.
- Confirm duplicated/spent components become zero-amount errors.
- Confirm final consideration checks still reject unmet consideration.

PoC shape:
- `matchOrders` or available-order fulfillment with malicious components that jointly create zero-amount and overflow conditions.

Triage notes:
- Historically high because it could buy assets at a major discount. For current Seaport versions, this is duplicate-prone unless the exact composite-error fallthrough reappears in a new aggregation path.
