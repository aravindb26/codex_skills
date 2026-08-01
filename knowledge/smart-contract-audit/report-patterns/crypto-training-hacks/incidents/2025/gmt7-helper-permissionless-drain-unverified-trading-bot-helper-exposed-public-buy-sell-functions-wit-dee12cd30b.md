# Crypto Training Exploit Pattern Stub: GMT7 Helper permissionless drain — unverified trading bot helper exposed public buy/sell functions with no access control and infinite router approval

Source:
- https://crypto.training/hacks/2025-02-GMT7/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- BNB Chain

Loss / impact summary:
- 16.75 BNB (~$10.1k at the time; PoC final balance 16.791444737752979201 BNB [output.txt:1…

Tags:
- access-control/missing-auth, access-control/missing-modifier, defi/slippage

Dedupe:
- id: `2025-02-GMT7`
- fingerprint: `dee12cd30b9ffcf26255daa0c22c28c3e67238e66b6317403e6a42d611c1f989`

Core exploit idea:
- GMT7 is a low-liquidity BEP-20 token paired with USDT on PancakeSwap (0x5317545A…3006). The project deployed an off-the-shelf "robot" helper contract (0x9AD9…31E3, unver…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
