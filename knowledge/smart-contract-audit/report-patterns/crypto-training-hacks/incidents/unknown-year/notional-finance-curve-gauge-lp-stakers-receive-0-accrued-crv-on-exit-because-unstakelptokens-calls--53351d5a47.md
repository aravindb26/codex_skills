# Crypto Training Exploit Pattern Stub: Notional Finance: Curve-gauge LP stakers receive 0 accrued CRV on exit because _unstakeLpTokens calls withdr

Source:
- https://crypto.training/hacks/63525-inability-to-claim-rewards-from-the-curve-gauge-mixbytes-non/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63525-inability-to-claim-rewards-from-the-curve-gauge-mixbytes-non`
- fingerprint: `53351d5a47e9268695215f8550a2707fea12208518fa5fb53efe329e94a60482`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
