# Crypto Training Exploit Pattern Stub: MOKE LP Dividend Drain — Stale `userLPRecord` Double-Claim via Unsynced LP Transfers

Source:
- https://crypto.training/hacks/2026-08-moke/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$907.7K (~1,546.5 BNB net to the attacker in the live tx; PoC drains ~1,639 BNB of a 1,6…

Tags:
- logic/reward-calculation, logic/incorrect-state-transition, logic/missing-check, governance/flash-loan-attack

Dedupe:
- id: `2026-08-moke`
- fingerprint: `df21796c372d361a426e0c589ebb24a19053f7c321e3c05432801cf171254ecd`

Core exploit idea:
- 1. MokeLPDividend pays BNB dividends proportional to MOKE/WBNB LP holdings, using a MasterChef-style debt model: userLPRecord, userDividendDebt, and global totalDividend…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
