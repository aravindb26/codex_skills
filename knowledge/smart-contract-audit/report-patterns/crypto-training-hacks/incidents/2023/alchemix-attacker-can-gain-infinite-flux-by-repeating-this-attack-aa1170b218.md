# Crypto Training Exploit Pattern Stub: Alchemix — Attacker can gain infinite FLUX by repeating this attack!

Source:
- https://crypto.training/hacks/38186-attacker-can-gain-infinitive-flux-by-repeating-this-attack-i/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `38186-attacker-can-gain-infinitive-flux-by-repeating-this-attack-i`
- fingerprint: `aa1170b2185a6af3da363c24c96dc6a4107d13769e08a8232e6b7a576573ad0a`

Core exploit idea:
- 1. Voter.reset(tokenId) is capped to once per epoch per tokenId by onlyNewEpoch. It calls veALCX.abstain(tokenId) (sets voted = false) and then accrues FLUX proportional…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
