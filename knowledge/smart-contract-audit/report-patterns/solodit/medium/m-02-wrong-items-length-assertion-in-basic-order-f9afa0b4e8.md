# Solodit Pattern Stub: [M-02] Wrong items length assertion in basic order

Source:
- https://solodit.cyfrin.io/issues/m-02-wrong-items-length-assertion-in-basic-order-code4rena-opensea-opensea-seaport-contest-git
- https://code4rena.com/reports/2022-05-opensea-seaport

Imported:
- 2026-05-23

Status:
- distilled

Severity:
- MEDIUM

Protocol:
- OpenSea Seaport

Source platform / firm:
- Code4rena

Tags:
- seaport, basic-order, calldata-aliasing, consideration-length, validation-bypass

Dedupe:
- id: `2624`
- fingerprint: `f9afa0b4e8f8b80e327e49d160992dab64eace788479ae1d8d2ab789388bd1a0`

Core idea:
- In old Seaport basic orders, `_prepareBasicFulfillmentFromCalldata` checked `additionalRecipients.length + 1 >= totalOriginalAdditionalRecipients`, allowing one fewer supplied additional recipient than originally signed. Because the order hash loop read the original recipient data from fixed calldata positions while transfer logic used the supplied dynamic array length, a validated order could be fulfilled while skipping one signed consideration item.

Broken invariant:
- The set of consideration items included in the signed order hash must be the same set that settlement enforces/transfers.

Where to look in code:
- Basic order calldata offset validation.
- Comparison between `additionalRecipients.length` and `totalOriginalAdditionalRecipients`.
- Any path where signature bytes or dynamic array layout can alias expected recipient data.

Attack path:
1. Maker signs a basic order with at least one additional recipient.
2. Attacker validates the order using correct calldata/signature.
3. Attacker fulfills with crafted calldata where `additionalRecipients.length` is smaller but fixed offsets still make the order hash match.
4. Settlement transfers fewer consideration items than the maker signed.

False-positive checks:
- Check strict `additionalRecipients.length >= totalOriginalAdditionalRecipients` without a `+1` mismatch.
- Check `_assertValidBasicOrderParameters` enforces canonical dynamic offsets.
- Check tests cover `MissingOriginalConsiderationItems`.

PoC shape:
- Validate first with correct signature, then fulfill a basic order with crafted dynamic calldata that shortens `additionalRecipients` and aliases signature bytes/recipient words.

Triage notes:
- Historically medium because exploitation required a narrow calldata layout and small low-decimal amounts. For current Seaport versions, strict length and offset validation should kill the exact branch.
