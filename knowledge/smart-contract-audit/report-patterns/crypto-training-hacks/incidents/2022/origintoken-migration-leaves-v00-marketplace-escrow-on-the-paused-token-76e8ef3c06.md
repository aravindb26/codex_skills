# Crypto Training Exploit Pattern Stub: OriginToken migration leaves V00 Marketplace escrow on the paused token

Source:
- https://crypto.training/hacks/17100-origin-token-migration-marketplace-reference/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Ethereum

Loss / impact summary:
- A 10 OGN listing deposit and a 20 OGN offer (30 OGN total) remain escrowed in the Marketp…

Tags:
- dependency/upgradeable-contract, logic/incorrect-state-transition, dos/lockup

Dedupe:
- id: `17100-origin-token-migration-marketplace-reference`
- fingerprint: `76e8ef3c065d9fae5312b3834014a0f8076f95904b0a39ea4b278db3ec102877`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
