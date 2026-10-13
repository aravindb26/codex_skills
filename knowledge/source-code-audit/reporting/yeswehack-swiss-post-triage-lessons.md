# Swiss Post E-Voting: Triage Lessons

## Source

Distilled from the reporter's submitted YesWeHack reports and the triager comments pasted on 2026-09-29. The reports were submitted on 2026-06-06 and 2026-06-10. These are program-specific lessons; the current program rules and VEleS instructions remain authoritative.

## Voter-visible verification failures

The truncated `shortChoiceReturnCodes` report was closed as **Informative**. The triager's stated reason was that a voter who follows the voting instructions and sees return codes that do not match the expected codes must not enter the Ballot Casting Key, and should alert election administrators. Attacks detectable by the voter are out of scope under the program's stated interpretation.

Apply this gate before treating client-side fail-open behavior as a security finding:

- Read the exact voter instructions and determine what the voter is expected to compare, including the number and placement of codes.
- Walk the UI as a correctly instructed voter. Do not equate “the malformed response is accepted,” “the UI hides a value,” or “the next route is reachable” with an undetected cast.
- Establish whether the voter can detect the anomaly from the legitimate voting card or other instructed check. If so, stop and assess the program's explicit exclusion before building a severity claim.
- A viable stronger claim needs a reproducible path where the attacker achieves a security impact while the voter follows the prescribed ceremony, or an independently demonstrated CIA impact that does not depend on the voter ignoring a warning or mismatch.
- Do not describe a malformed-but-detectable verification display as bypassing individual verifiability unless the PoC demonstrates that the prescribed check can still pass incorrectly.

## Duplicate roots and consequence escalation

The verifier tally ZIP traversal report was closed as **Duplicate** of public issue `#YWH-PGM2323-498`. The report demonstrated both arbitrary path escape and overwrite of `context/configuration-anonymized.xml`, but triage matched it to the already-submitted Zip Slip root.

- Compare exact root cause before PoC/report work: attacker-controlled archive path, whitelist acceptance, path resolution, and write outside the extraction root.
- A more consequential target file or downstream effect does not create a distinct issue when it follows from the same vulnerable extraction primitive and validation failure.
- Search the current public issue/results corpus early, then confirm whether the root is fixed in the exact in-scope revision. Do not infer uniqueness from a new impact narrative.
- Treat an already disclosed root as closed unless current code has a materially different validation defect, attacker setup, affected state, and independent impact path.

## VCPS signature-check/file-reopen race

The public program-results issue `#YWH-PGM2323-324` identifies the exact VCPS race where `VerifySignatureEvotingConfigCommand` / `VerifySignatureEvotingPrintCommand` verify a file path, then later commands reopen that path for XML deserialization. The public disposition records physical access and elevated filesystem privileges as necessary, Low severity, and no meaningful additional impact because an attacker with those capabilities could already alter/re-sign output files.

- Treat the same signature-then-reopen ordering as a known issue, not a fresh report, even if a current source revision still has it.
- Do not build a race harness that only swaps a local file between calls; first prove a permitted attacker can write/replace the trusted offline input path under the program threat model.
- If a future version changes the attacker precondition or adds a distinct impact, compare the exact entry point, state, and root before treating it as a new variant.

Source: Swiss Post public program-results update 31 March 2026, issue `#YWH-PGM2323-324`.

## Practical audit/report gate

For Swiss Post candidates, first prove the attacker-controlled entry point and the complete state/impact path on the current scoped source. Then test the exact user-facing or protocol ceremony, compare it with the current specification and voter instructions, and check public known issues. A unit test showing malformed input is accepted is supporting evidence, not sufficient proof of an in-scope election impact.

## VCM tenant-header and public-audit overlap

The Swiss Federal Chancellery's public Orange Cyberdefense report P023007 (E-Voting 1.5.2.2, December 2025; published 2026-01-27) records a successful request to `/vs-ws-rest/api/v1/votingcardmanager/votingcards/` with `x-tenant-id: it`, returning voting-card metadata. The report discusses enumerating card IDs across elections. This is prior public disclosure of the VCM search/header behavior and should be treated as known/duplicate risk for card enumeration. It does **not** establish cross-tenant access: the shown request uses one supplied tenant and does not demonstrate a tenant-A caller accessing tenant B.

The April 2026 public report P023125 (E-Voting 1.5.3.2) mentions the VCM card-block endpoint as an action available to a malicious/compromised Online-SDM operator after command execution. Do not misstate that privileged chain as proof of an independent low-privilege authorization bypass.

For a distinct cross-tenant claim, require exact evidence for the mTLS/client identity-to-tenant binding at the Access Layer and a representative two-tenant PoC showing the same authenticated tenant-A identity can read or block a tenant-B card. A direct service call or mock proxy that forwards an arbitrary `x-tenant-id` proves only application-level parameter selection, not the deployed authorization boundary.

Primary public sources:
- [Swiss Federal Chancellery, P023007 E-voting 1.5.2.2 Security Audit Report](https://www.bk.admin.ch/dam/bk/en/dokumente/pore/E_Voting/Examination_reports_January_2026/Scope%204%20Final%20Report%20Orange%20Cyberdefense%2027.01.2026.pdf.download.pdf/Scope%204%20Final%20Report%20Orange%20Cyberdefense%2027.01.2026.pdf)
- [Swiss Federal Chancellery, P023125 E-voting 1.5.3.2 Security Audit Report](https://www.bk.admin.ch/dam/bk/de/dokumente/pore/Vote--lectronique/Scope%204%20Final%20Report%20Orange%20Cyberdefense%2030.04.2026.pdf.download.pdf/Scope%204%20Final%20Report%20Orange%20Cyberdefense%2030.04.2026.pdf)
- [Public GitLab issue #40](https://gitlab.com/swisspost-evoting/e-voting/e-voting/-/work_items/40), which concerns the separate election-event URL tenant-selection branch; issue notes/disposition were not publicly accessible during this check.
