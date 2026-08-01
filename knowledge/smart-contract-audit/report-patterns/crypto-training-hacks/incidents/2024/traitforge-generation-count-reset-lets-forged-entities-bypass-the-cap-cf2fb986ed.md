# Crypto Training Exploit Pattern Stub: TraitForge generation count reset lets forged entities bypass the cap

Source:
- https://crypto.training/hacks/37918-h-04-generation-mint-count-reset-forged-token-cap-bypass-code4rena/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- The per-generation entity cap is bypassed; forged entities are omitted from the next gene…

Tags:
- logic/wrong-condition, logic/state-update, input-validation/boundary

Dedupe:
- id: `37918-h-04-generation-mint-count-reset-forged-token-cap-bypass-code4rena`
- fingerprint: `cf2fb986edf7dc7bd57e3aab97426e1542270495c4c2febaa3c2b6e7ea08046f`

Core exploit idea:
- forge() can create an entity assigned to the next generation and increment that generation's counter before the generation is active. When the current generation reaches…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
