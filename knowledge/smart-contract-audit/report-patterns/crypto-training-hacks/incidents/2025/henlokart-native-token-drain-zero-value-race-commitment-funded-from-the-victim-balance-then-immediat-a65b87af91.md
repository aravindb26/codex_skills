# Crypto Training Exploit Pattern Stub: HenloKart native-token drain — zero-value race commitment funded from the victim balance, then immediately cancelled back to the attacker

Source:
- https://crypto.training/hacks/2025-02-HenloKart/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Base

Loss / impact summary:
- 0.59 ETH (reported in @KeyInfo)

Tags:
- logic/wrong-condition, logic/incorrect-state-transition, logic/missing-validation, dependency/unchecked-return-value

Dedupe:
- id: `2025-02-HenloKart`
- fingerprint: `a65b87af910562e4d1bd290669beafed6276c19cefd2441955ce13b6842a157e`

Core exploit idea:
- HenloKart is an on-chain hamster-racing game (HenloKart) built as a UUPS-upgradeable proxy on Base. Players "commit to a race" by depositing a bet token (ETH or an ERC-2…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
