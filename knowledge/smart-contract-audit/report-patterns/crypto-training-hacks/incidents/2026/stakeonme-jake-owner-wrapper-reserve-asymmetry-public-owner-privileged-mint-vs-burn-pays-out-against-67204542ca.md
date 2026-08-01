# Crypto Training Exploit Pattern Stub: StakeOnMe JAKE owner-wrapper reserve asymmetry — public owner-privileged mint vs. burn pays out against an inflated ETH reserve

Source:
- https://crypto.training/hacks/2026-03-unverified_237d/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Ethereum

Loss / impact summary:
- 0.28 ETH (≈ 0.2793 ETH net to attacker; 1.919 ETH drained from the wrapper pool)

Tags:
- logic/price-calculation, access-control/missing-auth, defi/fee-manipulation

Dedupe:
- id: `2026-03-unverified_237d`
- fingerprint: `67204542cab03d9e850c5c726bfb3f8be801d720bf1a195841c7d75e0de17e0d`

Core exploit idea:
- The JAKE meToken (0x277697FA…, a Bancor-style bonding-curve token) is governed by an unverified public contract at 0x237d…4b3f that the meToken reports as its owner() [o…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
