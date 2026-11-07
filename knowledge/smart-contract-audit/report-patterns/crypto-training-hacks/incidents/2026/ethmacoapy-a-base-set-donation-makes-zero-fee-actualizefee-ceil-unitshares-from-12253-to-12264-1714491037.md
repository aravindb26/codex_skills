# Crypto Training Exploit Pattern Stub: ETHMACOAPY — a base-set donation makes zero-fee actualizeFee ceil unitShares from 12253 to 12264

Source:
- https://crypto.training/hacks/2026-10-setprotocolethmacoapy/
- Same-root Set Protocol deployment/case: https://crypto.training/hacks/2026-10-setprotocol/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- 4.047988247781965824 WETH on this tx output.txt:416. The test header records a second tx…

Tags:
- arithmetic/rounding-direction, logic/fee-calculation, logic/missing-check

Dedupe:
- id: `2026-10-setprotocolethmacoapy`
- fingerprint: `1714491037ff258096415a9111eafcd53610486a1b437f77d876258e1438b233`
- merged source id: `2026-10-setprotocol`
- merged source fingerprint: `740ab13c5304ebe561660c0a6a0f64a71bbfd336686c407f8430ae95b73155b3`

Core exploit idea:
- A base-set donation changes the unit-share calculation, and a zero-fee `actualizeFee` path rounds `unitShares` upward. The resulting over-redemption lets the caller recover more base-set assets than the rebalancing shares justify. The two source reports describe the same Set Protocol rounding root and are kept as one pattern, not separate cards.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
