# Crypto Training Exploit Pattern Stub: ERC-20 fees are permanently locked in Treasury — frozen funds

Source:
- https://crypto.training/hacks/57056-erc-20-tokens-cannot-be-withdrawn-from-treasury-contract-tra/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Ethereum

Loss / impact summary:
- ERC-20 fee balances sent to Treasury cannot be recovered

Tags:
- dos/frozen-funds, logic/missing-check

Dedupe:
- id: `57056-erc-20-tokens-cannot-be-withdrawn-from-treasury-contract-tra`
- fingerprint: `6c52ffd76da8637a7288f9aba112f5abb64df19b5c5b9a7dfe4cc542eba760de`

Core exploit idea:
- The Treasury exposes a native-ETH withdrawal only. ERC-20 fee tokens accumulate at the contract and the attempted token recovery selector reverts, leaving the balance fr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
