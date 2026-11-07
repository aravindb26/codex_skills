# Crypto Training Exploit Pattern Stub: Fence tranche pool — the UTC rollover credits a scheduled principal payment that was never paid, and draw pays it again

Source:
- https://crypto.training/hacks/2026-10-fencetranchepool/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Avalanche

Loss / impact summary:
- 1,013,353.611686 USDC (1013353611686), the pool's entire balance, on the second draw outp…

Tags:
- unknown

Dedupe:
- id: `2026-10-fencetranchepool`
- fingerprint: `ff6f0ea3ca36afd83d3a21e787b7a196a55bd21b5e88ee7e5dd729cfc6a03ad0`

Core exploit idea:
- A Valinor Digital / Fence Finance tranche pool on Avalanche lets anyone open a facility, name themselves borrower, fund principal, and draw it back. Cycle 1 is a wash: A…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
