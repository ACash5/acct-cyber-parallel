# Threat Hunt Playbook (Accounting Reconciliation Analogy)

**Objective:** Compare expected baseline vs observed data to detect anomalies early.

## Scope
- Datasets: `data/ledger.csv` (expected), `data/transactions.csv` (observed)
- Signals: New/unknown IDs, balance deltas > 0

## Procedure
1. Run workflow: _Threat Hunt_ (manual or scheduled).
2. If anomalies:
   - Open an **Incident** issue using the template.
   - Link the failed workflow run and offending commit/PR.
   - Root cause: was it legitimate change or suspicious?
3. Remediation:
   - Correct data or update baseline after approval.
   - Re-run hunt to verify.

## Metrics
- MTTR (detection → fix)
- Number of hunts with anomalies
