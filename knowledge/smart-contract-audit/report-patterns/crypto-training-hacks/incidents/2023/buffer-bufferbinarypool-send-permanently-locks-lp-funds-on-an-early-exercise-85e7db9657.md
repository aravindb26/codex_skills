# Crypto Training Exploit Pattern Stub: Buffer `BufferBinaryPool.send()` permanently locks LP funds on an early exercise

Source:
- https://crypto.training/hacks/55634-h-02-bufferbinarypool-can-permanently-lock-funds-on-early-ex/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `55634-h-02-bufferbinarypool-can-permanently-lock-funds-on-early-ex`
- fingerprint: `85e7db96579c8773572792ae1b40bf581c1738bf01be730031f3b522db26caa2`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
