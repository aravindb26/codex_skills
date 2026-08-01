# Crypto Training Exploit Pattern Stub: Unbatched `startPool` can be front-run — initial mint theft

Source:
- https://crypto.training/hacks/16983-failure-to-use-the-batched-transaction-flow-may-enable-theft/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2021

Chain:
- Ethereum

Loss / impact summary:
- An honest LP's preloaded base is minted to a front-runner

Tags:
- defi/sandwich-attack, logic/missing-check

Dedupe:
- id: `16983-failure-to-use-the-batched-transaction-flow-may-enable-theft`
- fingerprint: `3c5c795188bec75231277ff96e3ebc8003e210859645e78d0347fd545c68dfab`

Core exploit idea:
- If liquidity is transferred to the Strategy before the router's batch reaches startPool, an attacker can front-run that call and receive the entire initial strategy-toke…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
