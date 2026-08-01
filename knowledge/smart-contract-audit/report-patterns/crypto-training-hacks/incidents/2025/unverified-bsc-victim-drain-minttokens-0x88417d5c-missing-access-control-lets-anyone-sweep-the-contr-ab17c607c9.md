# Crypto Training Exploit Pattern Stub: Unverified BSC Victim Drain (mintTokens 0x88417d5c) — missing access control lets anyone sweep the contract's ERC20 balances

Source:
- https://crypto.training/hacks/2025-05-unverified_0000/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- 5,658.46 USD (reported in @KeyInfo; reproduced drained balances below)

Tags:
- access-control/missing-auth, access-control/missing-modifier, logic/missing-check

Dedupe:
- id: `2025-05-unverified_0000`
- fingerprint: `ab17c607c9924f232e92c32802d790a06fa82b6cb2634e528fce1c03ea617b01`

Core exploit idea:
- The victim contract at 0x000004…D0000 exposes a function with selector 0x88417d5c whose decoded signature is mintTokens(uint256,bool,bool,(address,uint256)[]) (the test'…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
