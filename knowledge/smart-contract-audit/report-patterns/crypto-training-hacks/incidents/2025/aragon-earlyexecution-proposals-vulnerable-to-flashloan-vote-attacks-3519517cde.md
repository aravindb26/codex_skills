# Crypto Training Exploit Pattern Stub: Aragon — EarlyExecution proposals vulnerable to flashloan vote attacks

Source:
- https://crypto.training/hacks/62256-proposals-created-with-voting-mode-earlyexecution-are-vulner/

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
- governance/flashloan-vote

Dedupe:
- id: `62256-proposals-created-with-voting-mode-earlyexecution-are-vulner`
- fingerprint: `3519517cdefae864dadfec82bba0e34771b1b70961cab189ca12a0107cbaf7f1`

Core exploit idea:
- 1. EarlyExecution mode executes a proposal as soon as a YES vote pushes it over the support threshold. 2. If the lock token is flashloanable/flashmintable, an attacker c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
