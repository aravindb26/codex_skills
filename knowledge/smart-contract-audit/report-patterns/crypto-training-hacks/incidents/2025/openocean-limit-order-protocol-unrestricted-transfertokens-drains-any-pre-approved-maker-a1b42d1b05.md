# Crypto Training Exploit Pattern Stub: OpenOcean Limit Order Protocol — unrestricted `transferTokens()` drains any pre-approved maker

Source:
- https://crypto.training/hacks/2025-02-LimitOrderProtocol/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Base

Loss / impact summary:
- 2,800,000 BRAINS (victim's full balance; 2.8e24 wei / 18 decimals) — see output.txt:1624

Tags:
- access-control/missing-modifier, access-control/missing-auth, logic/missing-validation

Dedupe:
- id: `2025-02-LimitOrderProtocol`
- fingerprint: `a1b42d1b05682e54686704c12eb36ffb3ccca8d56cd0257eb609848646f5ff4f`

Core exploit idea:
- OpenOcean's Base deployment of the Limit Order Protocol v2 is an upgradeable contract: a TransparentUpgradeableProxy (0xb5486f71…) delegates to an implementation (0xCe8D…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
