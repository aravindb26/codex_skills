# Crypto Training Exploit Pattern Stub: IQ AI — Adversary can win proposals with voting power as low as 4%

Source:
- https://crypto.training/hacks/50064-h-01-adversary-can-win-proposals-with-voting-power-as-low-as/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `50064-h-01-adversary-can-win-proposals-with-voting-power-as-low-as`
- fingerprint: `71b24412dc05ede80073b3d3a8b67cd2410d497ff5e37f61ac893b2ac9ac27d3`

Core exploit idea:
- 1. Constructor sets GovernorVotesQuorumFraction(4) with comment "quorum is 25% (1/4th)". 2. OZ quorumDenominator() defaults to 100, so quorum = supply * 4 / 100 = 4%. 3.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
