# Crypto Training Exploit Pattern Stub: TraitForge — the maximum number of generations is infinite

Source:
- https://crypto.training/hacks/37919-h-05-the-maximum-number-of-generations-is-infinite-code4rena/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-bounds-check, access-control/insufficient-guard, tokenomics/supply-cap-breach

Dedupe:
- id: `37919-h-05-the-maximum-number-of-generations-is-infinite-code4rena`
- fingerprint: `6b5ba876cbc35c6d61c962004055001ef8da235b309c811512ef67c900ac498c`

Core exploit idea:
- 1. TraitForgeNft is meant to cap total supply at maxGeneration generations of maxTokensPerGen NFTs each (real protocol: 10 x 10,000 = 100,000). 2. Filling a generation's…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
