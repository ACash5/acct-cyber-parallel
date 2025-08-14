import os, re, sys

# Simple regexes for common secrets. (Demonstration only)
PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Generic password": re.compile(r"(?i)(password\s*[:=]\s*[^\s]+)"),
    "Slack token": re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,48}"),
}

def scan_file(path):
    findings = []
    try:
        with open(path, 'r', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                for name, rx in PATTERNS.items():
                    if rx.search(line):
                        findings.append((i, name, line.strip()))
    except Exception:
        pass
    return findings

def main():
    findings_total = []
    for root, _, files in os.walk('.'):
        for fn in files:
            if fn.startswith('.git'):
                continue
            path = os.path.join(root, fn)
            results = scan_file(path)
            for res in results:
                findings_total.append((path, ) + res)
    if findings_total:
        print("Potential secrets detected:")
        for path, line_no, name, snippet in findings_total:
            print(f"{path}:{line_no}: [{name}] {snippet}")
        sys.exit(1)
    print("No secrets detected.")
    
if __name__ == '__main__':
    main()
