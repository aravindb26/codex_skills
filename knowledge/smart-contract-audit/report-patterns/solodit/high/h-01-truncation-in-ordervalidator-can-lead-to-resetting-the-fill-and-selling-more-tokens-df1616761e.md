# Solodit Pattern Stub: [H-01] Truncation in `OrderValidator` can lead to resetting the fill and selling more tokens

Source:
- https://solodit.cyfrin.io/issues/h-01-truncation-in-ordervalidator-can-lead-to-resetting-the-fill-and-selling-more-tokens-code4rena-opensea-opensea-seaport-contest-git
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
- seaport, partial-fill, uint120, order-status, fill-accounting

Dedupe:
- id: `2621`
- fingerprint: `df1616761effb915df4d97cb6fa593a9ce283daa0b992a87c114d5998c30c7fa`

Core idea:
- In Seaport 1.0, partial-fill status packed numerator and denominator into uint120 fields after cross-multiplying fractions. A filler could choose large equivalent fractions so that the computed filled fraction overflowed or truncated back to zero when stored, resetting fill accounting and allowing the same order to be filled beyond the maker's intended amount.

Broken invariant:
- Filled amount for an order must be monotonic and must never wrap, truncate, or reset after any sequence of partial fills.

Where to look in code:
- Order validation/status packing for partial fills.
- Any code that combines existing fill fractions with a requested fill fraction.
- Any downcast or bit-pack into smaller integer fields after fraction arithmetic.

Attack path:
1. Maker signs a partially fillable ERC1155/orderbook order for a limited amount.
2. Filler performs a partial fill using a large equivalent fraction that sets stored numerator/denominator near uint120 bounds.
3. Filler performs another fill with a different denominator, forcing cross-multiplication and truncation.
4. Stored fill resets or under-represents actual fill, allowing additional fills beyond the signed allocation.

False-positive checks:
- Check whether numerator and denominator are masked before use.
- Check whether combined numerator and denominator are reduced by GCD before storage.
- Check whether a second overflow check reverts if numerator or denominator still exceeds the packed width.
- Check whether overfill/carry reverts or returns false before storage.

PoC shape:
- Two-step partial-fill PoC using ERC1155 amounts, first with a large equivalent fraction, second with a small fraction that forces cross-denominator multiplication.

Triage notes:
- High impact because non-consenting maker inventory can be sold beyond the signed amount. For current Seaport versions, this is duplicate-prone unless a distinct new path bypasses the added uint120/GCD/overflow protections.
