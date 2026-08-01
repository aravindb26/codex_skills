# Crypto Training Exploit Pattern Stub: Stake.Link rewards — incoming bridge update makes rewards insolvent

Source:
- https://crypto.training/hacks/29745-not-update-rewards-in-handleincomingupdate-function-of-sdlpo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, dos/frozen-funds

Dedupe:
- id: `29745-not-update-rewards-in-handleincomingupdate-function-of-sdlpo`
- fingerprint: `c19ed180c991080dc371efa16a34a11baf4111196942537102e0d3f338d4855a`

Core exploit idea:
- The controller's effective balance is increased before its already accrued rewards are checkpointed. It then claims old rewards on newly added stake, exceeding the funde…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
