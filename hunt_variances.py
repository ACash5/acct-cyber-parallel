import csv, sys

with open('data/ledger.csv') as f:
    ledger = {r['invoice_id']: float(r['amount']) for r in csv.DictReader(f)}

# Map invoice -> expected balance by summing invoices per "account" (simulated)
expected = {
    "ACC-101": 500,
    "ACC-102": 300,
    "ACC-103": 200
}

with open('data/transactions.csv') as f:
    observed = {r['account_id']: int(r['observed_balance']) for r in csv.DictReader(f)}

unexpected_accounts = set(observed.keys()) - set(expected.keys())
mismatched_balances = {acc: (expected[acc], observed[acc]) for acc in expected if acc in observed and expected[acc] != observed[acc]}

if unexpected_accounts or mismatched_balances:
    print("🔎 Anomalies Found:")
    if unexpected_accounts:
        print(f"  New/Unexpected Accounts: {sorted(unexpected_accounts)}")
    if mismatched_balances:
        for acc, (exp, obs) in mismatched_balances.items():
            print(f"  Balance mismatch for {acc}: expected {exp}, observed {obs}")
    sys.exit(1)
else:
    print("✅ No anomalies detected.")
