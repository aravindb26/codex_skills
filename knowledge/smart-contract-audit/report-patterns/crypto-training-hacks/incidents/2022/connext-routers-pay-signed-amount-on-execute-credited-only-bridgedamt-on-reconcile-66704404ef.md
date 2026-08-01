# Crypto Training Exploit Pattern Stub: Connext — routers pay signed amount on `execute`, credited only `bridgedAmt` on reconcile

Source:
- https://crypto.training/hacks/25133-h-04-in-execute-the-amount-routers-pay-is-what-user-signed-b/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/amount-mismatch, logic/wrong-condition

Dedupe:
- id: `25133-h-04-in-execute-the-amount-routers-pay-is-what-user-signed-b`
- fingerprint: `66704404ef5a2c918f7814a54fa7e9c54c477c59bbe91fbc4e7c78e560747715`

Core exploit idea:
- 1. Origin xcall swaps adopted → local; only bridgedAmt is messaged. 2. Destination execute (fast path) debits routers from the user-signed _args.amount. 3. _reconcile cr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
