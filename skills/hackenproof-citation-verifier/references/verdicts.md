# Citation Verdicts

Use one verdict per citation and keep the result limited to the claim checked.

| Verdict | Meaning |
|---|---|
| `verified` | The cited fact is present at the stated source and matches. |
| `verified-with-drift` | The fact exists, but its path, line, or referenced value differs. |
| `citation-without-commit` | The claim may be checkable, but it is pinned only to a moving branch or version. |
| `unresolvable` | The check could not run or the source could not be established. |
| `contradicted` | A complete, relevant source was checked and disproves this specific citation. |

`unresolvable` is not a negative result. Rate limits, unavailable providers, pruned chain history,
incomplete trees, missing commits, and ambiguous versions must remain unresolved until a reliable
source can answer the question.

## Prose PoC

A narrated result without an observed response, identifier, log, attachment, transaction, or runnable
reproduction may be weak evidence. That is a report-quality observation, not proof of dishonesty and
not a citation verdict. Use `hackenproof-report-quality-scorer` for overall actionability when
requested.

## Output

```text
# Citation Check

Commit checked: <sha and how established, or unavailable>
Looked up on: <YYYY-MM-DD>
Target type: <repository, web, mobile, or other>

| Citation | Verdict | Detail | Exact command/source |
|---|---|---|---|
| `path.sol:12-18` | verified | quote matches | `<command actually run>` |

PoC evidence form: <observed artifact, prose-only, or not assessed>
Limitations: <unresolved checks and why>
```

Never turn a citation verdict into a claim about a submitter's honesty, finding validity, severity,
program disposition, or reputation. State what was checked, what it showed, and what remains unknown.
