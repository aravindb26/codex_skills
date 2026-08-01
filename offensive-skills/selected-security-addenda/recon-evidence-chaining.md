# Recon Evidence And Chain Validation Addendum

Source distilled from `uphiago/recon-skills`:

- `meta/recon-playbook/SKILL.md`
- `redteam/evidence-hygiene/SKILL.md`
- `chains/cross-attack-chains/SKILL.md`

Use this for authorized Web2/API/recon work when scope allows external discovery or when an existing recon dump needs to be converted into validated attack paths.

## Recon Discipline

Before running recon, lock:

- allowed assets and explicit exclusions
- rate limits and stop conditions
- allowed identities and test accounts
- whether active probing, port scanning, archive crawling, and state-changing tests are allowed
- output directory for this audit only

Keep every hostname, URL, endpoint, and hypothesis tied to provenance. Historical URLs, CT logs, JS bundle paths, and scanner output are leads, not proof that the current product is vulnerable.

## Output Layout

Use target-local storage so cleanup is safe:

```bash
export OUTPUT_DIR="${OUTPUT_DIR:-.context/recon}"
mkdir -p "$OUTPUT_DIR/assets" "$OUTPUT_DIR/http" "$OUTPUT_DIR/urls" "$OUTPUT_DIR/evidence"
```

Record scope and tool versions beside outputs. Do not scatter recon artifacts into global directories.

## Evidence Hygiene

Before screenshots, HAR exports, terminal transcripts, or report attachments:

- redact session cookies, bearer tokens, CSRF tokens, API keys, and refresh tokens
- redact real third-party PII unless that exact field is necessary to prove impact
- leave useful trace IDs, request IDs, endpoint paths, response shapes, and test-account identifiers visible
- avoid screenshots showing browser cookie storage, full `Copy as cURL`, or Burp request headers with live secrets
- label redactions in the report so triage understands what was hidden and why

For HAR or JSON artifacts, sanitize auth headers and cookies before attaching. Preserve unredacted evidence locally only when required and safe.

## Attack-Chain Validation

Do not claim a chain because findings are merely on the same host. A chain requires a proven dependency:

```text
Finding A output -> accepted as Finding B input -> produces stronger confirmed impact
```

Use these evidence states:

- `Observed`: seen in output but not security-confirmed
- `Confirmed`: reproduced with a control and real boundary impact
- `Inferred`: plausible but not safely tested
- `Not tested`: blocked by scope, safety, or missing prerequisites

Every arrow must have evidence. Examples:

- source map reveals hidden API base URL and that exact URL resolves now
- enumeration produces an object ID and the ID works in a cross-account request
- CORS misconfig plus credentialed browser context returns protected data
- exposed token is valid only for an approved synthetic resource

If a downstream step is unsafe or out of scope, stop and label it inferred. Do not upgrade severity beyond demonstrated impact.
