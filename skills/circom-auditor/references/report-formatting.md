# Report Formatting

## Report Path

Save the report to `assets/findings/{project-name}-zksec-circom-audit-report-{timestamp}.md` where `{project-name}` is the repo root basename and `{timestamp}` is `YYYYMMDD-HHMMSS` at scan time.

## Output Format

Use this base template. Apply the local/delegated omissions in the rules below:
local reports omit triager metadata, while delegated reports include it only
when triage workers actually ran.

````
# 🔐 Circuit Security Review — <RepoName or template name>

---

## Scope

|                                  |                                                              |
| -------------------------------- | ------------------------------------------------------------ |
| **Mode**                         | ALL / default / filename                                     |
| **Files reviewed**               | `File1.circom` · `File2.circom`<br>`File3.circom`            | <!-- list every in-scope .circom, 3 per line -->
| **Confidence threshold (1-100)** | N                                                            |

---

## Findings

[95] **1. <Title>**

`TemplateName (file.circom:LL-LL) · signal: <signalName>` · Confidence: 95 · Detected by: agent-2, agent-8

**Description**
<The vulnerable constraint pattern and why it is exploitable, in 1 short sentence>

**Circuit / Constraint**

```circom
signal lambda <-- (in[1] - 1) / (in[0]);
// missing: IsZero(in[0]).out === 0;
```

**Fix**

```diff
- signal lambda <-- (in[1] - 1) / (in[0]);
+ component nz = IsZero(in[0]);
+ nz.out === 0;
+ signal lambda <-- (in[1] - 1) / (in[0]);
+ lambda * in[0] === in[1] - 1;
```

---

[82] **2. <Title>**

`TemplateName (file.circom:LL)` · Confidence: 82 · Detected by: agent-4

**Description**
<one short sentence>

**Circuit / Constraint**

```circom
// the offending line(s) verbatim
```

**Fix**

```diff
- vulnerable line(s)
+ fixed line(s)
```

---

< ... all above-threshold findings (≥ confidence threshold) >

---

[75] **3. <Title>**

`TemplateName (file.circom:LL)` · Confidence: 75 · Detected by: agent-13

**Description**
<one short sentence>

**Circuit / Constraint**

```circom
// the offending line(s)
```

---

< ... all below-threshold findings (Circuit / Constraint shown, no Fix block) >

---

Findings List

| # | Confidence | Detected by | Title |
|---|------------|-------------|-------|
| 1 | [95] | agent-2, agent-8 | <title> |
| 2 | [82] | agent-4 | <title> |
| 3 | [75] | agent-13 | <title> |

---

## Leads

_Vulnerability trails with concrete code smells where the full witness/exploit chain could not be completed in one analysis pass. These are not false positives — they are high-signal leads for manual review. Not scored._

- **<Title>** — `Template.signal` — Detected by: agent-7, agent-14 — Code smells: <missing range check, unchecked precondition, etc.> — <1-2 sentence description of the trail and what remains unverified>
- **<Title>** — `Template.signal` — Detected by: agent-3 — Code smells: <...> — <1-2 sentence description>

---

<Include this section only if delegated triage ran.>

## Triager Reasoning

_Independent verification of every finding by a triage subagent. Findings marked **Not Exploitable** are kept for visibility — review the reasoning before discarding._

**1. <Title>** — Exploitable

<2-4 sentences from the triager: what is going on and why it is exploitable, with concrete file:line and witness references.>

**2. <Title>** — Not Exploitable

<2-4 sentences from the triager: what guarding constraint or structural blocker makes this not exploitable.>

**3. <Title>** — Exploitable

<2-4 sentences.>

---

> ⚠️  This review was performed by a lightweight AI assistant. AI analysis cannot verify the complete absence of constraint bugs, and no guarantees are made regarding soundness, completeness, or zero-knowledge properties. A manual security review or a deep, continuous AI scan is strongly recommended. For a consultation regarding your circuit's security, visit [zksecurity.xyz](https://zksecurity.xyz). For deep AI audits, visit [zkao.io](https://zkao.io).

````

**Rules:**

- Follow the template above exactly, applying the local/delegated omissions in this section.
- Sort findings by confidence (highest first).
- The `TemplateName (file.circom:LL)` header replaces Solidity's `Contract.functionName`. When a finding is localized to a specific signal inside the template, append `· signal: <signalName>`.
- Every finding metadata line MUST include ` · Detected by: ...`. In delegated mode, list every sub-agent that reported the deduplicated item, sorted by numeric agent id and comma-separated, e.g. `Detected by: agent-2, agent-8, agent-14`. In local fallback mode, use `Detected by: local`.
- The Findings List table MUST include a `Detected by` column with the same detector set used on the finding metadata line.
- Every lead bullet MUST include `Detected by: ...` using the same rules as findings.
- Every finding gets a **Circuit / Constraint** block — the offending line(s) verbatim, OR a comment showing the missing constraint. This is the most important visual element for a Circom finding because it pins the bug to actual code.
- Findings ≥ confidence threshold get a **Fix** block (`diff` format showing the minimal patch). Findings below the threshold get **Circuit / Constraint** but no **Fix**.
- Use `Num2Bits_strict`, `IsZero`, `BigLessThan`, `<==`, etc. in fix diffs — the Circom-idiomatic safe patterns from `judging.md`.
- **Multiple distinct fixes (fix-preservation).** When the dedup pass preserved two or more genuinely distinct fixes for one finding — different added constraints, a different check direction, or a different remediation strategy (e.g. add `IsZero(den).out === 0` vs. switch the divisor to a provably-non-zero source) — render each as a labelled option, verbatim from the agent text. Do not paraphrase or collapse to one. Label intuitively (constrain / range-check / switch-primitive / forbid-sentinel):

  ````
  **Fix (Option A — constrain divisor)**

  ```diff
  + component nz = IsZero(in[0]);
  + nz.out === 0;
    signal lambda <-- (in[1] - 1) / in[0];
  + lambda * in[0] === in[1] - 1;
  ```

  **Fix (Option B — switch to safe primitive)**

  ```diff
  - signal lambda <-- (in[1] - 1) / in[0];
  + component add = EllipticCurveAdd(...);  // dispatch wrapper handles equal-x
  ```
  ````
- Draft findings directly in report format — do not re-generate.
- In local mode, omit triager verdicts and omit the `## Triager Reasoning` section.
- In delegated mode, include triager verdicts only when triage workers actually ran. In that case, every finding's metadata line ends with ` · **Triager Verdict:** Exploitable` or ` · **Triager Verdict:** Not Exploitable` after the `Detected by` field, and the `## Triager Reasoning` section lists every finding in report order with `**N. <Title>** — Exploitable|Not Exploitable` followed by the triager's reasoning.
