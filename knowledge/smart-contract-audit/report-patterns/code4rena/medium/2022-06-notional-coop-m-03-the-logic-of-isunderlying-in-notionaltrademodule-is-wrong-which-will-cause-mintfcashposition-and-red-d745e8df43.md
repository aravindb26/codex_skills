# Code4rena Pattern Stub: The logic of _isUnderlying() in NotionalTradeModule is wrong which will cause mintFCashPosition() and redeemFCashPosition() revert on fcash tokens which asset token is underlying token (asset.tokenType == TokenType.NonMintable)

Source:
- https://code4rena.com/reports/2022-06-notional-coop#m-03-the-logic-of-_isunderlying-in-notionaltrademodule-is-wrong-which-will-cause-mintfcashposition-and-redeemfcashposition-revert-on-fcash-tokens-which-asset-token-is-underlying-token-assettokentype--tokentypenonmintable

Imported:
- 2026-08-19

Status:
- needs distillation

Severity:
- MEDIUM

Report:
- Notional x Index Coop

Report date:
- 2022-07-18

Source platform:
- Code4rena

Dedupe:
- id: `2022-06-notional-coop#m-03-the-logic-of-_isunderlying-in-notionaltrademodule-is-wrong-which-will-cause-mintfcashposition-and-redeemfcashposition-revert-on-fcash-tokens-which-asset-token-is-underlying-token-assettokentype--tokentypenonmintable`
- fingerprint: `d745e8df43b0d77d764739269135c453b129c45a5455a493e591bee944596c22`

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
