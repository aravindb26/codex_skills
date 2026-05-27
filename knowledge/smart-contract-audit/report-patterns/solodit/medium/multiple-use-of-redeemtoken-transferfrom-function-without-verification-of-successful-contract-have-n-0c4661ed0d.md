# Solodit Pattern Stub: Multiple use of redeemToken.transferFrom() function without verification of successful, contract have no control over the redeemToken implementation, it just knows it is implementing an interface of type IERC20, if the underlying ERC20 contract is not implementing allowance properly or other cases, the execution on erc20 may be unsuccessful but the next function from Unvest contracts will be executed: e.g. mint function.

Source:
- https://solodit.cyfrin.io/issues/multiple-use-of-redeemtokentransferfrom-function-without-verification-of-successful-contract-have-no-control-over-the-redeemtoken-implementation-it-just-knows-it-is-implementing-an-interface-of-type-ierc20-if-the-underlying-erc20-contract-is-not-implementing-allowance-properly-or-other-cases-the-execution-on-erc20-may-be-unsuccessful-but-the-next-function-from-unvest-contracts-will-be-executed-eg-mint-function-zokyo-none-unvest-markdown

Imported:
- 2026-05-23

Status:
- needs distillation

Severity:
- MEDIUM

Protocol:
- unknown

Source platform / firm:
- unknown

Tags:
- unknown

Dedupe:
- id: `56055`
- fingerprint: `0c4661ed0d03a5840ab451eda24473e0eb26cf54e93e389e9184a76a71ff1182`

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
