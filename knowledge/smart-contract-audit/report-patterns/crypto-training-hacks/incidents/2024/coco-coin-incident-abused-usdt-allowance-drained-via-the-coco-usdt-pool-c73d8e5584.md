# Crypto Training Exploit Pattern Stub: COCO COIN Incident — Abused USDT Allowance Drained via the COCO/USDT Pool

Source:
- https://crypto.training/hacks/2024-08-COCO/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- BNB Chain

Loss / impact summary:
- 280 BNB total across the campaign (per the PoC header / TenArmor). The reproduced slice m…

Tags:
- defi/slippage, logic/missing-validation

Dedupe:
- id: `2024-08-COCO`
- fingerprint: `c73d8e5584c4fc0896b79948fc046768a6a0b40db8c0fa3cd60c86626fd27aa9`

Core exploit idea:
- Despite the way the PoC is framed (and the empty "Vulnerable Contract" field in its header), there is no exploitable code defect in either the COCO token or the PancakeS…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
