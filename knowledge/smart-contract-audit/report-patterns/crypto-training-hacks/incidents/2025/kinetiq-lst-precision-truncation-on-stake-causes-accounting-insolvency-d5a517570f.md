# Crypto Training Exploit Pattern Stub: Kinetiq LST — precision truncation on stake causes accounting insolvency

Source:
- https://crypto.training/hacks/58596-precision-truncation-on-stake-may-lead-to-improper-accountin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/precision-loss, loss-of-funds/insolvency, math/truncation

Dedupe:
- id: `58596-precision-truncation-on-stake-may-lead-to-improper-accountin`
- fingerprint: `d5a517570f8cda6d98499a05fcf37fd0caaf47a97d979f7ae2c12881266168f3`

Core exploit idea:
- 1. HyperCore books HYPE with 8 decimals → transfers must be multiples of 1e10 wei. 2. _distributeStake sends truncatedAmount = amount / 1e10 * 1e10 but recordStake mints…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
