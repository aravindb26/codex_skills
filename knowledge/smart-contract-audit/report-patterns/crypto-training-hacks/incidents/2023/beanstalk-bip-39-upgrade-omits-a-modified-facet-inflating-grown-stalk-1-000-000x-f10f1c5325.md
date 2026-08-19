# Crypto Training Exploit Pattern Stub: Beanstalk BIP-39 upgrade omits a modified facet, inflating grown Stalk 1,000,000x

Source:
- https://crypto.training/hacks/31275-failure-to-add-modified-facets-and-facets-with-modified-depe/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dependency/upgradeable-contract, logic/upgrade-safety

Dedupe:
- id: `31275-failure-to-add-modified-facets-and-facets-with-modified-depe`
- fingerprint: `f10f1c5325ef2642803c5b78aa7d8cf8f416be8cd66b851931f486ee2066df01`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
