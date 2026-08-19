# Code4rena Pattern Stub: fee loss in AutoPxGmx and AutoPxGlp and reward loss in AutoPxGlp by calling PirexRewards.claim(pxGmx/pxGpl, AutoPx*) directly which transfers rewards to AutoPx* pool without compound logic get executed and fee calculation logic and pxGmx wouldn’t be executed for those rewards

Source:
- https://code4rena.com/reports/2022-11-redactedcartel#h-06-fee-loss-in-autopxgmx-and-autopxglp-and-reward-loss-in-autopxglp-by-calling-pirexrewardsclaimpxgmxpxgpl-autopx-directly-which-transfers-rewards-to--autopx-pool-without-compound-logic-get-executed-and-fee-calculation-logic-and-pxgmx-wouldnt-be-executed-for-those-rewards

Imported:
- 2026-08-19

Status:
- needs distillation

Severity:
- HIGH

Report:
- Redacted Cartel contest

Report date:
- 2023-01-27

Source platform:
- Code4rena

Dedupe:
- id: `2022-11-redactedcartel#h-06-fee-loss-in-autopxgmx-and-autopxglp-and-reward-loss-in-autopxglp-by-calling-pirexrewardsclaimpxgmxpxgpl-autopx-directly-which-transfers-rewards-to--autopx-pool-without-compound-logic-get-executed-and-fee-calculation-logic-and-pxgmx-wouldnt-be-executed-for-those-rewards`
- fingerprint: `30ffecf4a2da9816feb1babf9f3d2e985a0ddd54d6c807be7bfd82ac3a7c8fc9`

Core idea:
- TODO: Distill the reusable attack pattern from the source.

Broken invariant:
- TODO

Where to look in code:
- TODO

Attack path:
1. TODO

False-positive checks:
- TODO

PoC shape:
- TODO

Triage notes:
- TODO
