# Crypto Training Exploit Pattern Stub: AlpsCon AI Trade Hub — a public Hardhat address is whitelisted, and a zero entry index pays the historical USDC index

Source:
- https://crypto.training/hacks/2026-10-alpscon/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- BNB Chain

Loss / impact summary:
- On-chain net 152,295.3625 USDC to the attacker EOA (header of test/AlpsCon_exp.sol). The…

Tags:
- logic/reward-calculation, access-control/broken-logic, logic/missing-check

Dedupe:
- id: `2026-10-alpscon`
- fingerprint: `f6a110c71d32c6213fbc7fb2aebd8c1c49bfc134c7612ba084db06ad984ddd9d`

Core exploit idea:
- AlpsCon's AI Trade Hub sells ALPS "service credits" and later pays USDC "service results" from a per-share index. Reward entrypoints are gated by onlyVerified, which is…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
