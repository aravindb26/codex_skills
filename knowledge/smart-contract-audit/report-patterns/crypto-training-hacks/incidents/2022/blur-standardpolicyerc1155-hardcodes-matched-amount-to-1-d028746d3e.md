# Crypto Training Exploit Pattern Stub: Blur — StandardPolicyERC1155 hardcodes matched amount to 1

Source:
- https://crypto.training/hacks/42876-h-01-standardpolicyerc1155sol-returns-amount-1-instead-of-am/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, nft/amount-mismatch

Dedupe:
- id: `42876-h-01-standardpolicyerc1155sol-returns-amount-1-instead-of-am`
- fingerprint: `d028746d3e47760ff1522364a39c4ed1bf647d19a937fa8cb67eca29ea7558cf`

Core exploit idea:
- 1. canMatchMakerAsk / canMatchMakerBid return 1 instead of order.amount. 2. BlurExchange uses that amount in _executeTokenTransfer / ERC1155 transfer. 3. Settlement stil…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
