# Solodit Pattern Stub: The contracts that are implementing the DesctructibleInterface give the owner too much control, the owner can call the destroyAndSend function and transfer all the ether from the contracts to an arbitrary address this is a risk especially if the private key of the owner gets compromised, this kind of functionalities should be used with a multi-sig.

Source:
- https://solodit.cyfrin.io/issues/the-contracts-that-are-implementing-the-desctructibleinterface-give-the-owner-too-much-control-the-owner-can-call-the-destroyandsend-function-and-transfer-all-the-ether-from-the-contracts-to-an-arbitrary-address-this-is-a-risk-especially-if-the-private-key-of-the-owner-gets-compromised-this-kind-of-functionalities-should-be-used-with-a-multi-sig-zokyo-none-stampsdaq-markdown

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
- id: `56281`
- fingerprint: `84ec5b819a26c7b0a5e47bdeb896de7451c15a98060720a72fb1ad5f6181a9ea`

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
