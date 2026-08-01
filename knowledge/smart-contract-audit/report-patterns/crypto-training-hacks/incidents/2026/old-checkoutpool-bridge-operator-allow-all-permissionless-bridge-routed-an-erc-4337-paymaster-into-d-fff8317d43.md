# Crypto Training Exploit Pattern Stub: Old CheckoutPool Bridge Operator (`_ALLOW_ALL_`) — permissionless bridge() routed an ERC-4337 paymaster into draining CheckoutPool's USDC excess

Source:
- https://crypto.training/hacks/2026-03-unverified_1304/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Polygon

Loss / impact summary:
- 85,730 USDC (85,729 from CheckoutPool._POOL_EXCESS_ + 1 USDC held by the checkout)

Tags:
- access-control/missing-auth, access-control/broken-logic, logic/missing-check

Dedupe:
- id: `2026-03-unverified_1304`
- fingerprint: `fff8317d43feaac55c6af09f7996414e5eccb9bffebaff40f7ee127f06a7965f`

Core exploit idea:
- CheckoutPool is an ERC-4337 (account abstraction) payments pool: users register a "checkout" (a desired on-chain payment, e.g. pay 85,730 USDC to a recipient), lock up f…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
