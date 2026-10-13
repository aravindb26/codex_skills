# Pashov Upstream PDF Review - 2026-10-13

Source repository:
- https://github.com/pashov/audits
- Reviewed commit: `e615d8a5319647f95e217616d21770b3d8372f50`

## Imported Medium Pattern Cards

- Ensemble 2026-09-14: M-01, M-05, M-07, M-10, M-14
- Pare 2026-09-17: M-01, M-03, M-04, M-06
- Pare 2026-10-01: M-01, M-02, M-03, M-04

Each imported card is a compact lead only. It must be checked against the
current code, program scope, exact root cause, intended behavior, known issues,
and runtime evidence before it can influence a finding.

## Skipped Findings

- Ensemble M-02: deployment-specific builder fee configuration.
- Ensemble M-03: exact source-pool authorization overlap with existing CCIP knowledge.
- Ensemble M-04 and M-12: same opportunistic emergency-pause family with bounded impact.
- Ensemble M-06: nonstandard-token integration already covered by the token integration knowledge.
- Ensemble M-08 and M-11: reward-farming patterns already represented locally.
- Ensemble M-09, M-13, M-15, and M-16: protocol-specific lock, dust, or insolvency variants already represented.
- Pare 2026-09-17 M-02: numeraire mismatch covered by dimensional-analysis and decimal-mismatch checks.
- Pare 2026-09-17 M-05: generic downward TWAP manipulation is already heavily represented; M-06 was retained for its fixed redemption-floor mechanism.
- Pare 2026-09-28: no High or Medium findings.
- Low and Informational findings from all reviewed PDFs: not imported into the High/Medium pattern library.
