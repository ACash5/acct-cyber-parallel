import csv, sys

def load(path):
    with open(path, newline='') as f:
        return {r['invoice_id']: float(r['amount']) for r in csv.DictReader(f)}

ledger = load('data/ledger.csv')
payments = load('data/payments.csv')

missing = []
for inv, amt in ledger.items():
    if payments.get(inv, 0.0) != amt:
        missing.append(inv)

if missing:
    print("Unreconciled invoices:", ", ".join(missing))
    sys.exit(1)
else:
    print("Reconciliation OK")
