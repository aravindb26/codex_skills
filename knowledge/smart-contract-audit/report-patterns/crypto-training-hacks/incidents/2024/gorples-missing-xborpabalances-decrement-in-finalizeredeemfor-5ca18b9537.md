# Crypto Training Exploit Pattern Stub: Gorples — missing `xBorpaBalances` decrement in `finalizeRedeemFor`

Source:
- https://crypto.training/hacks/51279-missing-xgorplestoken-decrement-in-finalizeredeemfor-halborn/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/missing-decrement, redeem/double-claim

Dedupe:
- id: `51279-missing-xgorplestoken-decrement-in-finalizeredeemfor-halborn`
- fingerprint: `5ca18b95371b9645a76abdb96835ac77a6153f415c179143d47e6290eedd73f1`

Core exploit idea:
- 1. finalizeRedeem correctly does xBorpaBalances[msg.sender] -= xAmount then pays Gorples. 2. finalizeRedeemFor pays via _easyFinalizeRedeem but never decrements xBorpaBa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
