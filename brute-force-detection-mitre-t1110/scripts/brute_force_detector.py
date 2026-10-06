#!/usr/bin/env python3
"""Detect repeated failed authentication attempts from a CSV file.

Expected columns:
timestamp,source_ip,username,result
"""
import argparse
import csv
from collections import Counter

def detect(path, threshold):
    failures = Counter()
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        for row in csv.DictReader(fh):
            if row.get("result", "").lower() in {"failed", "failure", "denied"}:
                failures[row.get("source_ip", "unknown")] += 1

    print("=== Brute Force Detection ===")
    found = False
    for source, count in failures.most_common():
        if count >= threshold:
            found = True
            print(f"[ALERT] {source}: {count} failed authentication attempts")
            print("        ATT&CK mapping: T1110 - Brute Force")

    if not found:
        print("No source crossed the configured threshold.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error("threshold must be at least 1")
    detect(args.csv_file, args.threshold)
