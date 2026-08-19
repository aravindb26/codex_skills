# Crypto Training Exploit Pattern Stub: StrongBlock Governance Takeover — Abandoned Governor → Malicious Upgrade → Pool Drain

Source:
- https://crypto.training/hacks/2026-08-strongblockgovernancetakeover/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$72K — 32,695.76 STRONG + 383,447.17 STRNGR

Tags:
- access-control/missing-auth, logic/incorrect-state-transition

Dedupe:
- id: `2026-08-strongblockgovernancetakeover`
- fingerprint: `e87466008eaf32079a868375e98f58fc9747b750ac4032ae8bb4d0178c574859`

Core exploit idea:
- 1. StrongBlock left an on-chain Governor with live upgrade authority, while the STRONG vote token was economically worthless — so majority voting power was cheap. 2. Att…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
