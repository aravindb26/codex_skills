# Code4rena Pattern Stub: Loss of funds in matchOneToManyOrders() and takeOrders() and matchOrders() because code don’t check that different ids in one collection are different, so it’s possible to sell one id multiple time instead of selling multiple id one time in one collection of order (lack of checks in doTokenIdsIntersect() especially for ERC1155 tokens)

Source:
- https://code4rena.com/reports/2022-06-infinity#h-02-loss-of-funds-in-matchonetomanyorders-and-takeorders-and-matchorders-because-code-dont-check-that-different-ids-in-one-collection-are-different-so-its-possible-to-sell-one-id-multiple-time-instead-of-selling-multiple-id-one-time-in-one-collection-of-order-lack-of-checks-in-dotokenidsintersect-especially-for-erc1155-tokens

Imported:
- 2026-08-19

Status:
- needs distillation

Severity:
- HIGH

Report:
- Infinity NFT Marketplace contest

Report date:
- 2022-08-16

Source platform:
- Code4rena

Dedupe:
- id: `2022-06-infinity#h-02-loss-of-funds-in-matchonetomanyorders-and-takeorders-and-matchorders-because-code-dont-check-that-different-ids-in-one-collection-are-different-so-its-possible-to-sell-one-id-multiple-time-instead-of-selling-multiple-id-one-time-in-one-collection-of-order-lack-of-checks-in-dotokenidsintersect-especially-for-erc1155-tokens`
- fingerprint: `c62e26e91a68345006633742c16c226e7eb1f6c4af80be090eac77bdd7bcb184`

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
