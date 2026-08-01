# Crypto Training Exploit Pattern Stub: THORWallet — MergeTgt has no deposit cap vs TGT_TO_EXCHANGE — late claimers stuck

Source:
- https://crypto.training/hacks/55396-h-1-mergetgt-has-no-handling-if-tgttoexchange-is-exceeded-du/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55396-h-1-mergetgt-has-no-handling-if-tgttoexchange-is-exceeded-du`
- fingerprint: `31d52a543a6950e9899453fd4e069fedfb948ff0d9378c712e20ce357511246f`

Core exploit idea:
- MergeTgt has no deposit cap vs TGT_TO_EXCHANGE — late claimers stuck. Harm demonstrated: Over-subscribed TGT deposits leave late claimers unable to redeem TITN.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
