# Crypto Training Exploit Pattern Stub: Polynomial Protocol — KangarooVault.removeCollateral updates storage without removing collateral

Source:
- https://crypto.training/hacks/20227-h-04-kangaroovaultremovecollateral-updates-storage-without-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-external-call, loss-of-funds/locked-funds, accounting/state-desync

Dedupe:
- id: `20227-h-04-kangaroovaultremovecollateral-updates-storage-without-a`
- fingerprint: `d5a9e82dbb810e40cd35ef5863940869244f9408fee0b395f0b06312ca16cfd8`

Core exploit idea:
- 1. addCollateral transfers collateral to the Exchange and increments usedFunds / positionData.totalCollateral — real assets move. 2. removeCollateral decrements the same…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
