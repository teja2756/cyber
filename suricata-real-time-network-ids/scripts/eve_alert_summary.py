#!/usr/bin/env python3
"""Summarize Suricata EVE JSON alerts using only the Python standard library."""
import json
import sys
from collections import Counter

def summarize(path):
    signatures = Counter()
    sources = Counter()
    alerts = 0

    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for raw in fh:
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue

            if event.get("event_type") != "alert":
                continue

            alerts += 1
            alert = event.get("alert", {})
            signatures[alert.get("signature", "Unknown")] += 1
            sources[event.get("src_ip", "unknown")] += 1

    print("=== Suricata SOC Alert Summary ===")
    print(f"Total alerts: {alerts}")

    print("\nTop signatures:")
    for signature, count in signatures.most_common(10):
        print(f"- {signature}: {count}")

    print("\nTop source IPs:")
    for source, count in sources.most_common(10):
        print(f"- {source}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/eve_alert_summary.py <eve.json>")
        sys.exit(1)
    summarize(sys.argv[1])
