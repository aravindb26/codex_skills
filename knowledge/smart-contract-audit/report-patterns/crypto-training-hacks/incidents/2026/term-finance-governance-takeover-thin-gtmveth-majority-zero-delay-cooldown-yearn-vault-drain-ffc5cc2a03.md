# Crypto Training Exploit Pattern Stub: Term Finance Governance Takeover — Thin gtmvETH Majority → Zero Delay Cooldown → Yearn Vault Drain

Source:
- https://crypto.training/hacks/2026-08-termfinancegovernancetakeover/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$8.5M — this PoC reproduces 2,841.743517563533112109 WETH (~$6.86M at ~$2,414/ETH). A se…

Tags:
- governance/proposal-manipulation, governance/timelock-bypass, access-control/centralization

Dedupe:
- id: `2026-08-termfinancegovernancetakeover`
- fingerprint: `ffc5cc2a03bb9825bc35947ddaa6bd8dc0a9b2bb49cd29354c907ba2b44cad34`

Core exploit idea:
- Term Finance parked ETH in a Yearn V3 ETH Meta Vault, administered by a Gnosis Safe sitting behind a Zodiac Delay module (txCooldown = 608,400 seconds ≈ 7 days). DAO gov…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
