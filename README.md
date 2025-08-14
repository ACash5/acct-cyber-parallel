# Accounting ↔ Cybersecurity Parallel Controls Lab

Hands-on GitHub lab demonstrating how classic **accounting controls** map to **cybersecurity controls**, with runnable workflows and evidence you can collect from the repo itself.

## What you’ll learn
- Reconciliation ↔ Threat Hunting (detect anomalies by comparing two sources of truth)
- Authorization & Approvals ↔ Change Control (PR gates + metadata checks)
- Audit Trail ↔ Centralized Logging (commit metadata → evidence pack)
- Exception Handling ↔ Incident Response (issue templates + postmortems)
- Continuous Monitoring ↔ Vulnerability/Secret Management (Dependabot + regex scanner)
- Compliance Evidence (controls matrix with links to your artifacts)

## Quickstart
1. Create a **private** GitHub repo and upload this project.
2. In **Settings → Branches**, protect `main`:
   - Require PR before merging
   - Require **1+** approving review
   - Require **CODEOWNERS** review
   - Require status checks to pass
   - Disallow force pushes
3. Edit `CODEOWNERS` to use your user/team handles.
4. Open a PR that changes `/data/*` or `/src/*` and watch the checks run.

> Tip: The `Change Control Gate`, `Reconcile`, `Threat Hunt`, and `Secret Scan` workflows are designed to **fail** until you provide correct metadata or data fixes—just like real approvals.

## Evidence to capture
- Screenshots of protected branch settings
- PR showing _Required review from CODEOWNERS_
- Passing/Failing CI logs from **Reconcile** and **Threat Hunt**
- Closed “Incident” issue with root cause & corrective actions
- Completed `docs/controls-mapping.md` with links to PRs/runs

---

## Deep Dives Included
- **Reconciliation vs Threat Hunting**: `threat-hunt.yml` schedules weekly hunts that compare expected vs observed datasets (`/data/ledger.csv` vs `/data/transactions.csv`).
- **Authorization/Approvals vs Change Control**: `change-control-gate.yml` enforces PR metadata (Change Request ID, Risk rating) and label-based approvals.
- **Audit Trail vs Centralized Logging**: `evidence-pack.yml` compiles commit & workflow run metadata into `docs/evidence-pack.json`.
- **Exception Handling vs Incident Response**: incident issue template + runbook, link PRs and hunts to issues.
- **Continuous Monitoring**: `dependabot.yml` + `secret-scan.yml` regex scans.

See `docs/controls-mapping.md` and `docs/playbooks/*` for details.
