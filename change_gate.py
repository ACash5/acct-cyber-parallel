import json, os, sys

event_path = os.environ.get("GITHUB_EVENT_PATH")
if not event_path or not os.path.exists(event_path):
    print("No event context available.")
    sys.exit(0)

with open(event_path, "r") as f:
    evt = json.load(f)

pr = evt.get("pull_request", {})
body = pr.get("body") or ""
labels = {lbl.get("name", "") for lbl in pr.get("labels", [])}

errors = []

# Require Change-Request-ID
if "Change-Request-ID:" not in body:
    errors.append("Missing 'Change-Request-ID:' in PR body (use PR template).")

# Require Risk
if "Risk:" not in body:
    errors.append("Missing 'Risk:' in PR body (Low|Medium|High).")

# Require 'approved' label to simulate CAB/manager approval
if "approved" not in {l.lower() for l in labels}:
    errors.append("Missing required 'approved' label.")

if errors:
    print("Change Control Gate FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Change Control Gate PASSED.")
