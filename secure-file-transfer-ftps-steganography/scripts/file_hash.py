#!/usr/bin/env python3
"""Calculate a SHA-256 hash for transfer integrity verification."""
import hashlib
import sys

def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/file_hash.py <file>")
        sys.exit(1)
    print(sha256(sys.argv[1]))
