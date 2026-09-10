# Crypto Training Exploit Pattern Stub: CashCowCoin (CCC) — `sell()` burns LP inventory then `sync()`, draining the CCC/WBNB pair

Source:
- https://crypto.training/hacks/2026-08-cashcowcoin/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$117K (165.471928251512413319 WBNB in the PoC and the live tx — output.txt:456)

Tags:
- logic/incorrect-state-transition, logic/missing-check, oracle/price-manipulation, governance/flash-loan-attack

Dedupe:
- id: `2026-08-cashcowcoin`
- fingerprint: `c0d63328d12b03f3c8847dc7f4d30e3b719810203dcd14de371d5975c3e2082a`

Core exploit idea:
- 1. CashCowCoin exposes a public sell(uint256,uint256,uint256) on an upgradeable proxy. Anyone who holds CCC can sell through it.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
