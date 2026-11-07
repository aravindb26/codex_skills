# Crypto Training Exploit Pattern Stub: Pancake V3 Swap Helper — Signed Swap Delta Misread as the WBNB Payout

Source:
- https://crypto.training/hacks/2026-09-pancakev3swaphelper/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- 1.648868884526157960 BNB after the live tx fee (1,132,330 gas × 0.05 gwei = 0.0000566165…

Tags:
- logic/missing-validation, logic/incorrect-state-transition, logic/price-calculation

Dedupe:
- id: `2026-09-pancakev3swaphelper`
- fingerprint: `6836632bc99607f84afa4d3174d01f8c6b3a22f1700ce5023540cd15623c9a78`

Core exploit idea:
- 0x222C8580eaA32f6f5a728bda0129CFA485eCc52D is an unverified helper that pulls an ERC-20, swaps it for WBNB on Pancake V3, unwraps WBNB, and forwards BNB to a caller-chos…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
