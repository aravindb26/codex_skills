# Crypto Training Exploit Pattern Stub: Primev — Overpayment to bidder in `slash` due to incorrect amount transfer

Source:
- https://crypto.training/hacks/46246-overpayment-to-bidder-in-slash-function-due-to-incorrect-amo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-transfer-amount, accounting/fee, logic/direct-drain

Dedupe:
- id: `46246-overpayment-to-bidder-in-slash-function-due-to-incorrect-amo`
- fingerprint: `2a6f6b56c60b60881260338097cce4a8bd3d123b3ed5cdd4a000edd9cda13dd7`

Core exploit idea:
- 1. slash computes residualAmt = amt * residualBidPercentAfterDecay / 100%. 2. Provider stake is reduced by residualAmt + fee (correct). 3. Bidder is paid amt instead of…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
