# Crypto Training Exploit Pattern Stub: Pepper — minting limit uses `totalSupply`, blocking legitimate minter airdrops

Source:
- https://crypto.training/hacks/52222-minting-limit-calculation-may-prevent-legitimate-claims-halb/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, mint/shared-cap

Dedupe:
- id: `52222-minting-limit-calculation-may-prevent-legitimate-claims-halb`
- fingerprint: `ebc04024665d51f16142a53a1590743d55295db0e6cf2808ee7b4b9324ba4aef`

Core exploit idea:
- 1. mint (MINTER_ROLE) caps against global totalSupply, intended as a 40% airdrop budget. 2. claim also increases totalSupply outside that role. 3. After claims alone hit…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
