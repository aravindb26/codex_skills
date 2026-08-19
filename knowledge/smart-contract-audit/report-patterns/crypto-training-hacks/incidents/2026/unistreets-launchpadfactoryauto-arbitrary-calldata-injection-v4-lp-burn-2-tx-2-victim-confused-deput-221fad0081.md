# Crypto Training Exploit Pattern Stub: Unistreets LaunchpadFactoryAuto — Arbitrary Calldata Injection → V4 LP Burn (2-tx, 2-victim confused deputy)

Source:
- https://crypto.training/hacks/2026-08-unistreetslaunchpadfactory/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, logic/arbitrary-call, logic/confused-deputy

Dedupe:
- id: `2026-08-unistreetslaunchpadfactory`
- fingerprint: `221fad0081c5201d68c8802a766b6c7056a60b58308ce7dd7da0e2a9722c2a02`

Core exploit idea:
- LaunchpadFactoryAuto is the ERC-721 owner of the Uniswap v4 liquidity position minted for every token it launches. Its launch() function takes a caller-controlled modify…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
