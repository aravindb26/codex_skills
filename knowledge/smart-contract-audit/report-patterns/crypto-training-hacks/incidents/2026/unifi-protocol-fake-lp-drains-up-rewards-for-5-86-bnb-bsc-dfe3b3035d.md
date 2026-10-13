# Crypto Training Exploit Pattern Stub: Unifi Protocol — fake LP drains UP rewards for ~5.86 BNB (BSC)

Source:
- https://crypto.training/hacks/2026-09-unififakelprewards/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~5.86 BNB. PoC realizes 5.859108237446175701 BNB; controller native 15.024751453223642762…

Tags:
- logic/reward-calculation, input-validation/missing, logic/missing-check, access-control/broken-logic

Dedupe:
- id: `2026-09-unififakelprewards`
- fingerprint: `dfe3b3035d17655174847ce26e51667248f6ea507437b071c56bf0009f6a7c24`

Core exploit idea:
- Unifi's UP reward manager lets the caller pick the LP. It checks that the pool looks like a WBNB pair and sizes the reward from balanceOf / totalSupply on that same addr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
