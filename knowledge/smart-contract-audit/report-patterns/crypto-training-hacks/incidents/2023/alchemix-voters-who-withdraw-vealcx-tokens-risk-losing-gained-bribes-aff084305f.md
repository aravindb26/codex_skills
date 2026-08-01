# Crypto Training Exploit Pattern Stub: Alchemix — voters who withdraw veALCX tokens risk losing gained bribes

Source:
- https://crypto.training/hacks/38181-voters-who-withdraw-velacx-tokens-risk-losing-gained-bribes/

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
- access-control/ownership-check-after-burn, logic/missing-forced-claim, dos/frozen-funds

Dedupe:
- id: `38181-voters-who-withdraw-velacx-tokens-risk-losing-gained-bribes`
- fingerprint: `aff084305f249d06aa96784582461afa8977d9bb9d6c301dbd18b9c3af827ade`

Core exploit idea:
- 1. To close out a veALCX position, the documented sequence is: (i) Voter.reset(tokenId) if the position has voted, (ii) VotingEscrow.startCooldown(tokenId), (iii) wait f…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
