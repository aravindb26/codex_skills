# Crypto Training Exploit Pattern Stub: DODO Cross-Chain DEX — `withdrawToNativeChain` swaps arbitrary ZRC20 inventory

Source:
- https://crypto.training/hacks/58581-h-4-gatewaytransfernativewithdrawtonativechain-allows-swappi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/broken-logic, loss-of-funds/direct-drain, logic/missing-token-match

Dedupe:
- id: `58581-h-4-gatewaytransfernativewithdrawtonativechain-allows-swappi`
- fingerprint: `cf9cafae0f7663b79b9542655e15b811f41d84191847df1787d892e38e23eed9`

Core exploit idea:
- 1. withdrawToNativeChain decodes DODO MixSwapParams from the user message. 2. _doMixSwap approves params.fromToken for the deposited amount — no check that fromToken ==…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
