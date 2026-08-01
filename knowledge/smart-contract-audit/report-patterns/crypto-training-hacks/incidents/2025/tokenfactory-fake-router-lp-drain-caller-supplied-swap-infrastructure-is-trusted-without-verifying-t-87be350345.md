# Crypto Training Exploit Pattern Stub: TokenFactory fake-router LP drain — caller-supplied swap infrastructure is trusted without verifying the returned pair belongs to the new token

Source:
- https://crypto.training/hacks/2025-06-TokenFactory/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~657.17 USD (~1.006 WBNB of pair reserves, plus the attacker also received ~9.94e26 HODOG…

Tags:
- access-control/broken-logic, logic/missing-validation, dependency/unchecked-return-value

Dedupe:
- id: `2025-06-TokenFactory`
- fingerprint: `87be3503457ae52be85f39e6c1635b2186f2263c15ec2f4b8e18ec0734b5fde2`

Core exploit idea:
- TokenFactory is a BNB Chain "token-launchpad" contract: anyone pays a small fee, calls createTokenAndAddLiquidity, and the factory deploys a new ERC20, approves a Uniswa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
