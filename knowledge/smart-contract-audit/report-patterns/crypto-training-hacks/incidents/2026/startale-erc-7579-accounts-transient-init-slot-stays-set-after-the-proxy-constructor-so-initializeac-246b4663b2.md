# Crypto Training Exploit Pattern Stub: Startale ERC-7579 accounts — transient `INIT_SLOT` stays set after the proxy constructor, so `initializeAccount` can be called again in the same transaction

Source:
- https://crypto.training/hacks/2026-09-startale/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 32.555561 USDC swept from 3 reconstructed pre-funded accounts. Attacker USDC 0 → 32.55556…

Tags:
- logic/incorrect-initialization, access-control/missing-auth, dependency/unsafe-external-call, logic/delegatecall-target-confusion

Dedupe:
- id: `2026-09-startale`
- fingerprint: `246b4663b24ae98bb9b1c7601693f07c1bd7387d9786879d9555af1d3d4a1f52`

Core exploit idea:
- 1. Users pre-fund the counterfactual address of a Startale ERC-7579 account (ERC-4337 / factory CREATE2) before anyone deploys it. 2. AccountProxy's constructor calls In…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
