# HuntDeck Disclosed: Public Report Discovery

Source: <https://huntdeck.io/disclosed>; API reference: <https://huntdeck.io/api>
Reviewed: 2026-11-17

## When To Use

Use this as a discovery aid during Web2, OSS, native-code, API, or source-code audits when the target's language, framework, integration, or suspected bug class matches public bounty cases. It is not a scanner, audit skill, or source of authorization. Do not load it by default for unrelated audits or smart-contract contests.

The page provides searchable disclosure metadata such as report title, program, severity, weakness/CWE, dates, public bounty, votes, and a summary, with links to the original disclosure. The API documents filters for title, platform, severity, weakness, public bounty, date, and sort order. At review time the page listed about 11.3k reports; this count changes.

## Audit Use

1. Finish program scope, safe-harbor, and target-version checks first.
2. Search by the concrete code surface or behavior, not just a broad weakness label. Useful terms include parser, import/export, permission, authorization, session, deserialization, memory safety, cache, webhook, and API.
3. Filter to relevant severity/date and inspect the linked disclosure. Use the report to derive a testable invariant or attack question for the current code, not to copy its conclusion.
4. Verify the actual affected component, source revision, attacker prerequisites, control flow, and impact against the current target. Record whether the original technical details were accessible.
5. Search the existing `bug-patterns/` and reporting notes before adding anything. Distill only a distinct, reusable root cause; keep case-specific details separate and do not bulk-import the feed.

## Limits And Reliability

- Treat titles, severity labels, vote counts, bounty values, and short summaries as metadata, not proof that a similar issue exists or is rewardable in the current program.
- The page is an index, not a complete technical corpus. Follow the original report link for detail; if the full report is unavailable, mark the lesson as metadata-only and do not infer missing exploit steps.
- HuntDeck's API documentation describes disclosed data as HackerOne Hacktivity while exposing platform filters. Verify coverage and provenance for each item; do not assume all platforms or report classes are represented evenly.
- Some entries have no public bounty or an unrated severity. Disclosure does not by itself establish payout, program acceptance criteria, or current exploitability.
- Always check the current program's official scope and rules independently. A historical report never authorizes testing a related asset.

This source can complement the local source-code audit knowledge base, but it does not replace local deduplication, code reading, runtime validation, or triage checks.
