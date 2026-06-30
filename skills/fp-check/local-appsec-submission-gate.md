# Local AppSec Submission Gate

Use this addendum with `fp-check` for Web2/source-code bounty findings before calling anything report-worthy.

The goal is to stop "interesting local behavior" from being misclassified as a real security issue when the actual security boundary still holds downstream.

## Mandatory Pre-Submission Questions

For every surviving AppSec/source-code candidate, answer these before recommending submission:

1. What is the exact claimed security boundary?
2. Where is that boundary promised?
3. What exact new capability does the attacker gain?
4. Is the gained capability beyond what the attacker can already do with their own account, token, role, org membership, or client configuration?
5. Is the final protected backend/service using:
   - the attacker's own credentials or token, or
   - stronger shared/server credentials?
6. Does the PoC prove unauthorized access at the real boundary, or only prove a missing local check?

If any answer is unclear, do not call it strong.

## Hard Gates

Mark `NOT WORTH SUBMITTING` if any of the following are true:

- The PoC proves only a local validation gap, but not a privilege delta.
- The backend still authorizes every operation using the attacker's own token/account/role.
- The claimed impact depends on interpreting docs/config more strongly than their exact wording supports.
- A mocked backend is used to prove authorization impact rather than just control flow.
- The issue is defense-in-depth or product-hardening only, while the primary security control still blocks unauthorized access.
- The user can only act within orgs/projects/resources they already legitimately belong to.

## Required Evidence Before "Strong"

Require all of the following:

- Exact doc/config wording for the claimed boundary.
- Exact code path for admission/authentication.
- Exact code path for final authorization/data access.
- Proof of what credential reaches the final backend call.
- Proof that the attacker can cross an actual authz/tenant/security boundary, not just supply a surprising parameter.
- Strongest likely triager rebuttal written down first, then disproved with code or runtime evidence.

## Mocking Rule

Mocking is acceptable for:

- proving routing,
- proving local state transitions,
- proving parameter control,
- proving a missing re-check.

Mocking is not sufficient for:

- proving unauthorized access,
- proving privilege escalation,
- proving cross-tenant or cross-user impact,
- proving that a backend would honor an attack the same way.

If authorization impact is the claim, the PoC must show that impact against the real auth boundary or an exact equivalent with the same credential model.

## Primary Control Check

Always ask:

- Is this config/check the primary security control?
- Or is it only an admission filter, UX restriction, convenience boundary, or defense-in-depth control?

If the primary control is elsewhere and still holds, default to `NOT WORTH SUBMITTING` unless the bypass still creates a real security impact.

## Submission Recommendation Rule

Do not recommend submission until the candidate proves:

- real boundary crossed,
- real unauthorized capability,
- real impact,
- triager rebuttal beaten.

Interesting behavior, surprising parameter control, incomplete local validation, or ambiguous documentation are not enough by themselves.
