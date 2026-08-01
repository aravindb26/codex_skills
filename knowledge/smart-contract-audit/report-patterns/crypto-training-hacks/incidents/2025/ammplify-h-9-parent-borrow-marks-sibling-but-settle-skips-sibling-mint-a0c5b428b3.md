# Crypto Training Exploit Pattern Stub: Ammplify — H-9: Parent borrow marks sibling but settle skips sibling mint

Source:
- https://crypto.training/hacks/63175-h-9-liquidity-borrowed-from-or-repaid-to-parent-nodes-is-not/

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
- unknown

Dedupe:
- id: `63175-h-9-liquidity-borrowed-from-or-repaid-to-parent-nodes-is-not`
- fingerprint: `a0c5b428b378440b1516ad0fb23d391a27d5409e272f39cfe870a9155631d2b4`

Core exploit idea:
- 1. Taker demand on a child forces borrow from parent. 2. Sibling also receives preBorrow (parent liq = both children). 3. Settle walks only the op route (child+parent),…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
