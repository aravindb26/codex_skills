# Crypto Training Exploit Pattern Stub: Dumbo DUM staking reward inflation — permissionless, repeatable `distribute()` lets an attacker mint compounding rewards inside one transaction

Source:
- https://crypto.training/hacks/2025-05-Dumbo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- 628.447753459629926384 BUSD (≈ 628.45 BUSD) — reproduced locally [output.txt:1564-1565]

Tags:
- logic/incorrect-state-transition, dos/griefing, defi/flash-loan-attack

Dedupe:
- id: `2025-05-Dumbo`
- fingerprint: `5242054e263bac3fac317bf8c05d05588e8e9e453117406172c2d48ae87da2ba`

Core exploit idea:
- Dumbo ran an OlympusDAO-style "rebasing" staking system: users stake DUM, receive the receipt token sDUM, and a Distributor contract periodically calls distribute() to m…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
