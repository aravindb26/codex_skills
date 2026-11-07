# Upstream Skills And Report-Feed Refresh: 2026-11-07

Compared upstream content with installed files and local report indexes. Updates were selective;
no upstream package wholesale replaced local Codex adaptations, addenda, or the private Solidity
Auditor V3. The canonical source registry is
[`tracked-upstream-sources.md`](tracked-upstream-sources.md).

## Changed Upstream Heads Reviewed

| Source | Checked commit | Result |
|---|---|---|
| [`pashov/skills`](https://github.com/pashov/skills) | `eacfc09b365d2697b83355909d0300607e596ffc` | Merged the improved Solidity entry-point parser into the existing X-Ray skill; retained local V3 and Codex rules. |
| [`trailofbits/skills`](https://github.com/trailofbits/skills) | `e4dd0bb5b15535f7c5a0834187dffba6ac37e4ff` | Merged verified Aptos/Sui entry-point and access-classification corrections, CodeQL/Semgrep coverage caveats, C-review trusted-tool search boundary, and two zeroize helper fixes. |
| [`hackenproof-public/skills`](https://github.com/hackenproof-public/skills) | `6b7bed4851857df8d6a4e433d062696a2d9d33df` | Adapted the distinct citation/evidence verifier as an explicit-use Codex skill; excluded its reputation, fraud, and severity judgments. |
| [`OpenZeppelin/openzeppelin-skills`](https://github.com/OpenZeppelin/openzeppelin-skills) | `584262af9eed516bdb1d2d897246502218e3917a` | Reviewed the Defender-to-CRE migration; no audit-finding improvement or reason to replace local skills. |
| [`forefy/.context`](https://github.com/forefy/.context) | `b95739dc2385da4d39918566c2655f7acfd74c81` | Content review found no distinct, low-noise audit improvement to merge. |
| [`shuvonsec/claude-bug-bounty`](https://github.com/shuvonsec/claude-bug-bounty) | `8060af0c1b0b6ecc6595ee3261f50aa613038620` | Reviewed updated content; no validated improvement beyond existing filtered Web2 references. No wholesale sync. |
| [`uphiago/recon-skills`](https://github.com/uphiago/recon-skills) | `fd7e2e8105e8c83c5a3820bfd67082a754a69ac0` | Reviewed content changes; broad recon/workflow churn and mass-recon commands were not imported. |
| [`openai/codex-security`](https://github.com/openai/codex-security) | `3aa36e216501f746bc975647f69466a8692f78e3` | Large expansion reviewed; no wholesale sync into the curated reference snapshot. See its dated review note. |
| [`pashov/ai-web3-security`](https://github.com/pashov/ai-web3-security) | `d9465f8a146c6399ef972f8ef6c3b46f28f2ed48` | Discovery hub reviewed candidate by candidate. Installed only conditional Vyper `fyzz`; other candidates were duplicative, noisy, or deployment-specific. |
| [`rafael-abuawad/skills/fyzz`](https://github.com/rafael-abuawad/skills/tree/c98990cc5882c9f8c4f78a4a62636da4da9f090e/fyzz) | `c98990cc5882c9f8c4f78a4a62636da4da9f090e` | Installed under `/home/dinesh/.codex/skills/fyzz/` with a conditional Codex addendum; isolated tests passed. |

## Unchanged Sources Rechecked

These heads are unchanged from the 2026-10-13 review. Content comparison found no update to
install or merge:

| Source | Checked commit |
|---|---|
| `Cyfrin/solskill` | `d17bda028df073c61711a1fe156b5ca5dea91642` |
| `quillai-network/qs_skills` | `8bdd3c058704cd855ce29b8e2385708b59152606` |
| `auditmos/skills` | `c958b3abb0ce189d9f39a05caf94b5a5da655010` |
| `kadenzipfel/scv-scan` | `114985581450cfed35c277831a065c6478e2c328` |
| `0xiehnnkta/nemesis-auditor` | `75cecc6dbd798f82ed8928d1a906078be9c575de` |
| `heavyw8t/The-Judge` | `20703caee08ffdb2736866e7d21d1df2b3e21968` |
| `J4X-Security/K.I.T` | `1e18ece9cf0e7e9b73f8579e1b706a084586f47e` |
| `cholakovvv/foundry-poc-mainnet-fork` | `e02ebcb75d41575eb69127039da3de85a7b72da5` |
| `zzzuhaibmohd/solana-token-extensions-security` | `3e56671dd55c15465cbb55c91675597bf6fd54de` |
| `0xCyrildev/Chase` | `c8c4f18999024119ddb6cbf7f29dbf9e996f9016` |
| `DarkNavySecurity/web3-skills` | `2d00159558dd921d67fc90106a83557e963adf33` |
| `melanke/defi-builder-skills` | `fa24571dba27768d73f9c52a95ebfbf26acb894c` |
| `0xsimao/0xsimao-ai` pinned attack lenses | `3f81e5803174182a7db07eca87849d2b3d571113` |
| `pantheraudits/move-auditor` pinned DeFi patterns | `21610f0db7982dc991b356e09d38e06e149f7331` |
| `SnailSploit/Claude-Red` | `a8de813edc9f66f60d44cfe42d47750e89d9930b` |
| `mukul975/Anthropic-Cybersecurity-Skills` | `54a798831d2266a3ca61ce68a7acb80b81160d57` |
| `pashov/audits` | `e615d8a5319647f95e217616d21770b3d8372f50` |
| `Auditware/AuditVault` | `392eb3eee1cb99b9ba227b9c182cdaa1dab40abe` |
| `zksecurity/zk-skills` | `f56ed630f15b7782885342cc55dacbe5692a7b9` |
| `0xfirefistt/solidity-auditor-private` | Unavailable through the configured remote; local V3 preserved unchanged. |

## Installed And Merged

- `/home/dinesh/.codex/skills/x-ray/scripts/entry_points.py`: added Pashov's parser to enumerate
  Solidity entry points missed by the previous grep patterns. The skill still requires manual
  verification. Smoke test on the local EIP-7702 proxy repo found 3 entry points in 2 of 4 Solidity
  files.
- `/home/dinesh/.codex/skills/entry-point-analyzer/`: corrected Aptos public-function reachability,
  Sui shared-object overclassification, Vyper callback-name classification, and related access
  control false positives. Preserved the local Solodit addendum.
- `/home/dinesh/.codex/skills/codeql/workflows/run-analysis.md` and
  `/home/dinesh/.codex/skills/semgrep/workflows/scan-workflow.md`: require explicit extraction,
  ignore, and skipped-code coverage reporting so an incomplete scan is not mistaken for a clean
  result.
- `/home/dinesh/.codex/skills/c-review/SKILL.md`: helper discovery no longer searches the target
  repository for its own tool scripts.
- `/home/dinesh/.codex/skills/zeroize-audit/tools/generate_poc.py`: unreadable source files no
  longer qualify for source inclusion, and uppercase `.C` files remain recognized as C++.
- `/home/dinesh/.codex/skills/fyzz/`: installed Vyper stateful fuzzing with a local rule requiring
  manual code understanding and invariants before bounded, reviewed fuzz campaigns.
- `/home/dinesh/.codex/skills/hackenproof-citation-verifier/`: installed a renamed and narrowed
  report-citation verification workflow. It checks citations/evidence only; it does not judge
  report honesty, severity, vulnerability validity, reputation, or program disposition.
- `/home/dinesh/.codex/offensive-skills/codex-security-reference/`: recorded the latest checked
  upstream head and the decision not to wholesale-sync unrelated cloud/publishing workflows. The
  imported snapshot commit remains unchanged.

No `AGENTS.md` or private Solidity Auditor V3 changes were made in this refresh.

## Report-Feed And Dedupe Results

- Solodit public retrieval found 12 unseen High/Medium source records with no exact local ID,
  fingerprint, or URL match. Ten distinct patterns were distilled into cards and matching skill
  addenda. Two router-replacement reports share one root and overlap the existing initializer
  front-run pattern, so they were not duplicated.
- Code4rena latest-by-sitemap-modification dry run: `reports=30 imported=0 skipped=263 failed=0`.
  No newly discovered High/Medium report card was missing from the local dedupe coverage.
- Pashov audits dry run: `total=1289 imported_high=0 imported_medium=0`; no new High/Medium
  reports were imported.
- Crypto Training Hacks parsed `1709` current entries. The importer dry run reported `590` unseen
  rows because changed source IDs/URLs defeat its exact dedupe. Title normalization reduced this
  to 70 candidates not already represented by title: 26 2026 incident entries and 44 older or
  date-less entries. The 590 count was not treated as new content.
- From the 2026 entries, 18 selected source records were imported as 17 compact cards because the
  two Set Protocol reports share one rounding root. The dTRINITY near-empty-aToken case was added
  as corroborating evidence to the existing BoJ same-root card. Fox Market was already indexed.
  Six other cases were not imported: FlashLoopAdapter is duplicate-prone with the existing rsETH
  self-call/Safe-auth incident; the MakerDAO-branded item is a third-party keeper issue, not a
  MakerDAO core issue; MALT and TIPMine are covered by existing balance-delta/AMM reserve and
  nonstandard-token patterns; X100 Senate and Yapeswap are protocol-specific governance-capture
  variants without a distinct reusable check beyond the existing governance patterns.
- The 44 older/date-less title candidates were not imported: none had an exact normalized-title
  match in the Solodit or Code4rena indexes, but their root causes were not individually checked
  against all source pages. They remain an explicit deferred set; no claim is made that this set
  is duplicate-free.

## Validation

- Vyper `fyzz`: isolated pytest run, `14 passed, 4 skipped` (optional Ape/Moccasin environments
  unavailable).
- Python parser and zeroize helper: `py_compile` passed.
- Zeroize helper regressions: unreadable source returns no line count; `.C` is C++; `.c` is not.
- Solodit index validation: no duplicate dedupe IDs or fingerprints and all indexed local card
  paths exist.
- Audit behavior remains manually led; scanners and fuzzers are lead/evidence generators only.
