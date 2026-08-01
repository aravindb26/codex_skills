# Crypto Training Exploit Pattern Stub: TraitForge generation rollover is permanently blocked by the wrong modifier

Source:
- https://crypto.training/hacks/37920-h-06-entropy-generator-initialize-alpha-indices-wrong-modifier-code4rena/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- Generation rollover reverts, bricking mintToken, mintWithBudget, and forge at the boundar…

Tags:
- access-control/missing-modifier, dos/init-constraint, logic/wrong-condition

Dedupe:
- id: `37920-h-06-entropy-generator-initialize-alpha-indices-wrong-modifier-code4rena`
- fingerprint: `5e812671de4620785cf7f3e3efccfe74334b1663090bcc023a295100fdaf435a`

Core exploit idea:
- TraitForgeNft is configured as EntropyGenerator.allowedCaller, but the audited function uses onlyOwner. On every generation rollover the NFT calls initializeAlphaIndices…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
