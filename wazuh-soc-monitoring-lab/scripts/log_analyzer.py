#!/usr/bin/env python3
"""Educational Linux authentication-log analyzer."""
import re
import sys
from collections import Counter

FAILED_PATTERNS = ("Failed password", "authentication failure", "Invalid user")

def analyze(path):
    counts = Counter()
    total = 0
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if any(p in line for p in FAILED_PATTERNS):
                total += 1
                match = re.search(r"from\s+(\S+)", line)
                counts[match.group(1) if match else "unknown"] += 1

    print("=== SOC Authentication Log Triage ===")
    print(f"Suspicious authentication events: {total}")
    if not counts:
        print("No matching failed-authentication events found.")
        return
    print("\nSource summary:")
    for source, count in counts.most_common():
        severity = "HIGH" if count >= 10 else "MEDIUM" if count >= 5 else "LOW"
        print(f"- {source}: {count} failed attempts [{severity}]")
    print("\nRecommended analyst actions:")
    print("1. Validate whether the source IP is expected.")
    print("2. Review successful logins around the same time.")
    print("3. Check account lockouts and privilege activity.")
    print("4. Correlate with Wazuh and network telemetry.")
    print("5. Contain/block the source when malicious activity is confirmed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/log_analyzer.py <auth-log-file>")
        sys.exit(1)
    analyze(sys.argv[1])
