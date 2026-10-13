# Solodit Pattern Stub: Daily withdrawal limit decreases with `totalPoolSize` reduction

Source:
- https://solodit.cyfrin.io/issues/daily-withdrawal-limit-decreases-with-totalpoolsize-reduction-mixbytes-none-dia-markdown

Imported:
- 2026-05-23

Status:
- distilled from the primary MixBytes DIA Lumina Staking report; client acknowledged as design

Severity:
- MEDIUM

Protocol:
- DIAExternalStaking (DIA Lumina Staking)

Source platform / firm:
- MixBytes public audit report, M-1 (Medium; acknowledged)

Tags:
- staking
- daily withdrawal cap
- pool-size-dependent limit

Dedupe:
- id: `57925`
- fingerprint: `fe2d0b282aa15574c691a4dab8331bbe37065b6d199fe0892a626538168a018f`

Core idea:
- `checkDailyWithdrawalLimit` recalculates `availableDailyLimit` from the current `totalPoolSize`. A prior unstake reduces the pool size and therefore shrinks the amount still withdrawable under the same daily cap; a later same-day unstake can be blocked even while substantial funds remain.
- The report recommended snapshotting the cap from the pool size at the start of the day. The client acknowledged the behavior as intentional, explaining that the limit decreases until it reaches the minimum cap and that amount selection was moved to the request stage.
- This is a design-dependent warning, not a universal invariant: verify whether the intended daily limit is a start-of-day snapshot or is supposed to follow current pool size.

Broken invariant:
- Under the report's proposed model, `remainingDailyWithdrawalCapacity` should be bounded by a cap computed from the start-of-day pool size, not a shrinking live pool size. The client explicitly rejected that model for this protocol, so do not treat it as a generic vulnerability pattern without matching product intent.

Where to look in code:
- Dynamic pool-size reads inside daily-limit checks, especially when earlier same-day withdrawals mutate the denominator or limit base.
- Compare the counter (amount already withdrawn today), the current pool size, any stored daily cap, and the exact reset point.

Attack path:
1. A user withdraws during the day, reducing `totalPoolSize`.
2. A later same-day withdrawal re-evaluates the daily cap using the smaller pool size.
3. The later request is rejected although the pool still holds substantial funds; the original report's client considered this intended behavior.

False-positive checks:
- Establish intended semantics from primary docs/code and client/program wording; a dynamic cap may intentionally tighten after withdrawals.
- Distinguish a shrinking withdrawal cap that blocks users from a stale debt-borrow allowance that remains too permissive after lender supply falls; these have different state transitions and impacts.
- Confirm the residual pool balance, minimum cap, reset timing, and whether users choose the amount at request or execution time.

PoC shape:
- Execute one same-day withdrawal, then a second withdrawal after pool size changes; compare a live-recomputed cap with a start-of-day snapshot. Demonstrate the second withdrawal's outcome and residual pool balance, and test against the protocol's stated intent.

Triage notes:
- Primary source: `DIA/Lumina Staking/DIA Lumina Staking Security Audit Report.pdf`, M-1. Status is Acknowledged, and client commentary says the decrease is by design. The report is a useful semantic/false-positive comparison, not an exact duplicate for unrelated protocols or for a stale borrowing quota.
