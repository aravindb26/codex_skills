# Crypto Training Exploit Pattern Stub: LooksRare "Infiltration" — attacker steals the grand prize by force ending the game

Source:
- https://crypto.training/hacks/27588-h-3-attacker-can-steal-reward-of-actual-winner-by-force-endi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, access-control/stale-authorization-slot, loss-of-funds/reward-theft

Dedupe:
- id: `27588-h-3-attacker-can-steal-reward-of-actual-winner-by-force-endi`
- fingerprint: `d13e9d4b8f0c8ad67f8299912b74ae03db4b6fd59f3a2d25813615f71f6506e2`

Core exploit idea:
- 1. The game force-ends the instant gameInfo.activeAgents == 1 (startNewRound reverts GameOver). 2. claimGrandPrize pays the prize to whoever owns the agent parked at the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
