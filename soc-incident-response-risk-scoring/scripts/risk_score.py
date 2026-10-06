#!/usr/bin/env python3
"""Simple educational SOC risk-scoring calculator."""
import argparse

def score(severity, confidence, exposure):
    value = severity * confidence * exposure
    if value >= 81:
        priority = "CRITICAL"
    elif value >= 51:
        priority = "HIGH"
    elif value >= 21:
        priority = "MEDIUM"
    else:
        priority = "LOW"
    return value, priority

parser = argparse.ArgumentParser()
parser.add_argument("--severity", type=int, choices=range(1, 6), required=True)
parser.add_argument("--confidence", type=int, choices=range(1, 6), required=True)
parser.add_argument("--exposure", type=int, choices=range(1, 6), required=True)
args = parser.parse_args()

risk, priority = score(args.severity, args.confidence, args.exposure)
print(f"Risk score: {risk}/125")
print(f"Priority: {priority}")
