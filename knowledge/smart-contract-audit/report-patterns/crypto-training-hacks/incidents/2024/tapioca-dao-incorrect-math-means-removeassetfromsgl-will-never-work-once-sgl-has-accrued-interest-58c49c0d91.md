# Crypto Training Exploit Pattern Stub: Tapioca DAO — Incorrect math means removeAssetFromSGL will never work once SGL has accrued interest

Source:
- https://crypto.training/hacks/32318-h-07-incorrect-math-means-dataremoveandrepaydataremoveassetf/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/argument-type-confusion, availability/liveness-brick, accounting/rebase-scaling

Dedupe:
- id: `32318-h-07-incorrect-math-means-dataremoveandrepaydataremoveassetf`
- fingerprint: `58c49c0d91be235c53f7629c7fb011134715e97bd2c92a0fada11709f3cab9d7`

Core exploit idea:
- 1. A user asks the Magnetar periphery helper to withdraw a specific amount of the underlying asset from a Singularity market via removeAssetFromSGL. 2. Magnetar converts…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
