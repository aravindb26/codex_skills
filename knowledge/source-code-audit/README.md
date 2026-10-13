# Source Code Audit Knowledge Base

Use this directory as reusable memory for Web2, OSS, native-code, parser, API, and general source-code security audits.

This directory is passive knowledge, not an active skill pack. Search it when a non-smart-contract audit touches matching bug classes, languages, frameworks, parsers, auth flows, import/export logic, update systems, or generated artifacts.

## Directory Guide

- `bug-patterns/`: reusable vulnerability patterns distilled from public reports, incidents, rejected findings, and audit lessons.
- `reporting/`: reusable triager-facing report-writing and reproduction guidance.

## Usage Rule

Do not bulk-load every file. During a source-code audit:

- identify the target surface and behavior first
- search this directory for matching project type, bug class, function names, and value/security boundaries
- open only the matching notes
- convert each matched note into concrete checks against the current code
- treat these notes as lead generators, not proof

Before drafting a bounty submission, read the matching `reporting/` guidance and compare it with the program's form and any triager feedback. Program-specific requirements take precedence.

## Promotion Rule

- One report becomes a knowledge note.
- Many similar reports become a reusable bug-pattern note.
- A repeatedly useful checklist can later become an `offensive-skills/` workflow or addendum.

## Current Z.ai-Derived Patterns

- Parser state confusion across nested boundaries.
- Trusted metadata rendered without escaping.
- Typed write granularity mismatch in binary parsers.
- Generated report/query permission bypass.
