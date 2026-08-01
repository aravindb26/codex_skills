# Crypto Training Exploit Pattern Stub: Aria — stRWIP is always minted for RWIP in a 1:1 ratio

Source:
- https://crypto.training/hacks/63676-h-01-strwip-is-always-minted-for-rwip-in-a-11-ratio-pashov-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation

Dedupe:
- id: `63676-h-01-strwip-is-always-minted-for-rwip-in-a-11-ratio-pashov-a`
- fingerprint: `67ae441b856e9a51fa1b3f1dcc594b414acc64fb2fde28e71857ba94ba822e5a`

Core exploit idea:
- 1. burnTicket always mints stRWIP equal to the ticket's RWIP amount (1:1). 2. unstake redeems stRWIP at the live exchange rate balance / supply. 3. After rewards inflate…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
