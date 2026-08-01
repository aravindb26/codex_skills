# Crypto Training Exploit Pattern Stub: Licredity — self-triggered afterSwap back-run enables LP fee farming

Source:
- https://crypto.training/hacks/62349-self-triggered-licredity-afterswap-back-run-enables-lp-fee-f/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- mev/self-backrun

Dedupe:
- id: `62349-self-triggered-licredity-afterswap-back-run-enables-lp-fee-f`
- fingerprint: `e8cc857d0aae20fd4f5dd1c580c49f30c4c439a50449ab829697c9914d71e35b`

Core exploit idea:
- 1. When price hits/goes below 1, _afterSwap auto back-runs a reverse swap to restore parity. 2. That back-run pays swap fees to LPs. 3. A dominant LP around 1 captures n…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
