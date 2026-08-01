# Crypto Training Exploit Pattern Stub: Party Protocol — single host can unfairly skip the veto period for a proposal

Source:
- https://crypto.training/hacks/29546-h-02-single-host-can-unfairly-skip-veto-period-for-proposal/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/identity-bypass, governance/veto-bypass

Dedupe:
- id: `29546-h-02-single-host-can-unfairly-skip-veto-period-for-proposal`
- fingerprint: `d6c077e1e209cdacfa31a084e11fbb5cd5cbc51203f6e4f4536131971d2f4508`

Core exploit idea:
- 1. After a proposal passes its vote threshold, hosts get a chance to accept it; once ALL hosts have accepted, the veto delay is skipped and the proposal becomes immediat…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
