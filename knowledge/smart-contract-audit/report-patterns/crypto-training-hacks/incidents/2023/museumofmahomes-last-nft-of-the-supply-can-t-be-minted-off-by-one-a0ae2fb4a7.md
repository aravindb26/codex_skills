# Crypto Training Exploit Pattern Stub: MuseumOfMahomes — last NFT of the supply can't be minted (off-by-one `>=`)

Source:
- https://crypto.training/hacks/26477-h-01-last-nft-from-the-supply-cant-be-minted-pashov-none-mus/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/off-by-one, dos/permanent-mint-block, loss-of-funds/protocol-value-loss

Dedupe:
- id: `26477-h-01-last-nft-from-the-supply-cant-be-minted-pashov-none-mus`
- fingerprint: `a0ae2fb4a7e8e771bd22e6e5e7bf2680963575a41a97334980e429ca34047bc7`

Core exploit idea:
- 1. mint() guards the supply with if (nextId + amount >= MAX_SUPPLY) revert ExceedsMaxSupply();. 2. Valid tokenIds are 0 .. MAX_SUPPLY-1 (that is MAX_SUPPLY tokens), and…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
