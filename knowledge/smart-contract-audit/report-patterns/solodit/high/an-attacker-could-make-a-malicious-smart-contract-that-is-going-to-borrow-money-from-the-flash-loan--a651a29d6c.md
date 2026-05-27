# Solodit Pattern Stub: An attacker, could make a malicious smart contract that is going to borrow money from the flash loan function, and in the flashCallback function that he implements, he could call the send function from the DeBridgeGate contract, adding the balance back in the contract but also emitting a Send event, that will be captured by the validators and tokens will be minted on the other chains. After that, he can burn the tokens from the other chains to retrieve them back in the original chain and stole all the liqui

Source:
- https://solodit.cyfrin.io/issues/in-the-debridgegate-contract-initialize-function-it-would-be-useful-to-add-in-the-for-loop-condition-an-or-logical-operator-to-check-for-the-gas-left-this-way-if-the-_supportedchainids-array-is-too-large-the-execution-will-not-stop-with-out-of-gas-and-block-it-zokyo-none-debridge-markdown

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
- id: `56153`
- fingerprint: `a651a29d6c414318d7167803f2d4da2b61e950757cae1f98dc036c0a4bb6ca57`

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
