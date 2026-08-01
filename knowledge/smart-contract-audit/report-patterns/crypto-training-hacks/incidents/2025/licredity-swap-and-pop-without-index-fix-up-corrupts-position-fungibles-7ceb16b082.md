# Crypto Training Exploit Pattern Stub: Licredity — swap-and-pop without index fix-up corrupts Position fungibles

Source:
- https://crypto.training/hacks/62348-swap-and-pop-without-index-fix-up-corrupts-positions-fungibl/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- data-structure/stale-index, accounting/desync

Dedupe:
- id: `62348-swap-and-pop-without-index-fix-up-corrupts-positions-fungibl`
- fingerprint: `7ceb16b082cfff2a7b5859eb0b80ae012cdc608c3801a0f517f2e07bed13459e`

Core exploit idea:
- 1. Position tracks fungibles in an array and a fungibleStates mapping (1-based index + balance). 2. On full remove, the code swap-and-pops the array but never updates th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
