# Crypto Training Exploit Pattern Stub: Gondi — refinanceFromLoanExecutionData missing tokenId check

Source:
- https://crypto.training/hacks/35206-h-04-function-refinancefromloanexecutiondata-does-not-check/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35206-h-04-function-refinancefromloanexecutiondata-does-not-check`
- fingerprint: `10e628c5d294d439bfa58098d0bad7f28ab7e94bf99e02c413bee82ccc32d796`

Core exploit idea:
- 1. Refinance re-uses the NFT already in escrow (no transfer out/in). 2. Offer validation uses attacker-controlled executionData.tokenId. 3. No check that it matches the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
