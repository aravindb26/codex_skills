# Crypto Training Exploit Pattern Stub: Kuiper — stale fee checkpoint after `totalSupply` reaches zero

Source:
- https://crypto.training/hacks/19837-h-01-wrong-fee-calculation-after-totalsupply-was-0-code4rena/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2021

Chain:
- Other

Loss / impact summary:
- Extra fee tokens are minted after a zero-supply interval, diluting basket holders' underl…

Tags:
- logic/fee-calculation, logic/state-update, arithmetic/precision-loss

Dedupe:
- id: `19837-h-01-wrong-fee-calculation-after-totalsupply-was-0-code4rena`
- fingerprint: `24a744e399c954ebdd163da153a461c55c0a4e646dad050e75eaf6d68b354e1c`

Core exploit idea:
- handleFees() returns immediately when totalSupply == 0 without advancing lastFee. After all holders burn, the first resupply leaves the old timestamp intact; the next mi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
