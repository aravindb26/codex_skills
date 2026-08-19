# Code4rena Pattern Stub: Mailbox.requestL2Transaction() checks the deposit limit of msg.sender ( L1WethBridge ) instead of the real depositor of weth from L1, as a result, after certain time, nobody will be able to deposit weth anymore from L1

Source:
- https://code4rena.com/reports/2023-10-zksync#m-15-mailboxrequestl2transaction-checks-the-deposit-limit-of-msgsender-l1wethbridge-instead-of-the-real-depositor-of-weth-from-l1-as-a-result-after-certain-time-nobody-will-be-able-to-deposit-weth-anymore-from-l1

Imported:
- 2026-08-19

Status:
- needs distillation

Severity:
- MEDIUM

Report:
- zkSync Era

Report date:
- 2024-02-29

Source platform:
- Code4rena

Dedupe:
- id: `2023-10-zksync#m-15-mailboxrequestl2transaction-checks-the-deposit-limit-of-msgsender-l1wethbridge-instead-of-the-real-depositor-of-weth-from-l1-as-a-result-after-certain-time-nobody-will-be-able-to-deposit-weth-anymore-from-l1`
- fingerprint: `153eb2085502d9b52ecda92ea04dd446d36b029042999282b27e26782d81b81e`

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
