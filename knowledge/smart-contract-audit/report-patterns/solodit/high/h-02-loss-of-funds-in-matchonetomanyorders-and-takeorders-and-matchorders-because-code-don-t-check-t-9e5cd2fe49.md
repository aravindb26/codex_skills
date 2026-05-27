# Solodit Pattern Stub: [H-02] Loss of funds in `matchOneToManyOrders()` and `takeOrders()` and `matchOrders()` because code don't check that different ids in one collection are different, so it's possible to sell one id multiple time instead of selling multiple id one time in one collection of order (lack of checks in `doTokenIdsIntersect()` especially for ERC1155 tokens)

Source:
- https://solodit.cyfrin.io/issues/h-02-loss-of-funds-in-matchonetomanyorders-and-takeorders-and-matchorders-because-code-dont-check-that-different-ids-in-one-collection-are-different-so-its-possible-to-sell-one-id-multiple-time-instead-of-selling-multiple-id-one-time-in-one-collection-of-order-lack-of-checks-in-dotokenidsintersect-especially-for-erc1155-tokens-code4rena-infinity-nft-marketplace-infinity-nft-marketplace-contest-git

Imported:
- 2026-05-23

Status:
- needs distillation

Severity:
- HIGH

Protocol:
- unknown

Source platform / firm:
- unknown

Tags:
- unknown

Dedupe:
- id: `2768`
- fingerprint: `9e5cd2fe4906f478a06622cce1d9989e075fe25f4a836efa57fff1c026052846`

Core idea:
- TODO: Distill the reusable attack pattern from the source.

Broken invariant:
- TODO

Where to look in code:
- TODO

Attack path:
1. TODO

False-positive checks:
- TODO

PoC shape:
- TODO

Triage notes:
- TODO
