# Crypto Training Exploit Pattern Stub: Revamp referral-reward drain — a self-referral that pays contributors out of existing pool BNB

Source:
- https://crypto.training/hacks/2026-03-Revamp/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- 2.99 BNB (3.2078 BNB was the contract's entire native balance; ~2.9898 BNB is net attacke…

Tags:
- logic/reward-calculation, defi/flash-loan-attack, access-control/missing-validation

Dedupe:
- id: `2026-03-Revamp`
- fingerprint: `826ad66a3a14b439503819a409f86bd92ccae1e9298abe5220e9483817275cbd`

Core exploit idea:
- Revamp is a "revamp" / contribution protocol on BSC. Anyone can pay a listing fee to register an ERC-20, after which users call revamp(token, tokenAmount, referral) to s…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
