# Crypto Training Exploit Pattern Stub: Mellow Flexible Vaults — RedeemQueue batch vs claim timestamp mismatch

Source:
- https://crypto.training/hacks/62107-h-2-redeemqueue-accounting-mismatch-between-batch-creation-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `62107-h-2-redeemqueue-accounting-mismatch-between-batch-creation-a`
- fingerprint: `b499cb6ccb720111828b06957fea137a5d56fc320c27f11955474b9b258b6024`

Core exploit idea:
- 1. Batch creation excludes the last request at/before the report timestamp (index--). 2. Claim eligibility still allows any request with ts ≤ priceTimestamp. 3. User2 cl…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
