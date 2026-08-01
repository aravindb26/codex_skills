# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — `bringUnusedETHBackIntoGiantPool` loses idleETH addition and lets attackers steal ETH from the Giant Pool

Source:
- https://crypto.training/hacks/43033-h-10-giantmevandfeespoolbringunusedethbackintogiantpool-func/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/direct-drain

Dedupe:
- id: `43033-h-10-giantmevandfeespoolbringunusedethbackintogiantpool-func`
- fingerprint: `ec19ce2227eaa3b6235f346bba7d331dd1689dcbebd1e83b98be9994f31cbcab`

Core exploit idea:
- 1. totalRewardsReceived() is address(this).balance + totalClaimed - idleETH. 2. batchDepositETHForStaking correctly does idleETH -= amount when capital leaves. 3. bringU…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
