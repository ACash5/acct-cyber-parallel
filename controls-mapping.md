# Control Mapping Matrix

| ID | Accounting Control | Cybersecurity Control | Design (How) | Operation (Who/When) | Evidence (Where) |
|---|---|---|---|---|---|
| C-01 | Segregation of Duties | Least Privilege | `CODEOWNERS` + branch protection | Reviewers on each PR | PR page; Settings screenshots |
| C-02 | Authorization & Approvals | Change Control | PR template + metadata checks | Each merge to `main` | PR timeline; `Change Control Gate` logs |
| C-03 | Audit Trail | Centralized Logging | Commit metadata → evidence JSON | On pushes to `main` | `docs/evidence-pack.json` |
| C-04 | Reconciliation | Threat Hunting | Compare expected vs observed datasets | Weekly hunt + on-demand | `Threat Hunt` workflow logs |
| C-05 | Continuous Monitoring | Vuln/Secret Mgmt | Dependabot + regex secret scanner | Continuous / on PR | Security alerts; `Secret Scan` logs |
| C-06 | Exceptions | Incident Response | Incident issue template & runbook | As needed | Closed incident issues with links |

---

## Reconciliation ↔ Threat Hunting (Deep Dive)

- **Baseline (expected)**: `data/ledger.csv`
- **Observed (telemetry)**: `data/transactions.csv`
- **Signal**: New IDs or mismatched balances
- **Artifact**: Failed hunt logs; linked issues; corrective PRs

## Authorization/Approvals ↔ Change Control (Deep Dive)

- Require PR template entries:
  - `Change-Request-ID:` (ticket or approval number)
  - `Risk:` (Low/Medium/High)
- Require label: `approved`
- Block merge until metadata + label are present and reviews are done.

## Audit Trail ↔ Centralized Logging (Deep Dive)

- Evidence pack (`docs/evidence-pack.json`) includes:
  - last N commits (author, time, files changed)
  - last workflow run status for each control
- Use this as your “SOX evidence bundle”.

