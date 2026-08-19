# Crypto Training Exploit Pattern Stub: ZKPanther (Base) — Reality.eth governance module → proxy upgrades → ZKP drain

Source:
- https://crypto.training/hacks/2026-08-zkpanthergovernanceupgrade/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- ~5.12M ZKP (~$15.6k at ~$0.003/ZKP) + ~0.123 ETH; team: Base zone not yet in production,…

Tags:
- governance/proposal-manipulation, access-control/centralization, dependency/upgradeable-contract

Dedupe:
- id: `2026-08-zkpanthergovernanceupgrade`
- fingerprint: `cbf44fb5e66fb4a017abf063e6ff1423cbede41c5b17a5dba10ab2ae2c294650`

Core exploit idea:
- 1. Panther’s Base DAO is a Gnosis Safe with a Zodiac RealityModuleETH clone: anyone can addProposal, and a Reality.eth “yes” answer with only a 0.5 ETH bond becomes exec…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
