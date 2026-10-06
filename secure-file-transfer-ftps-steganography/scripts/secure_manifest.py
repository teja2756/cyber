#!/usr/bin/env python3
"""Create a simple JSON manifest containing file integrity metadata."""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/secure_manifest.py <file>")
        sys.exit(1)

    path = sys.argv[1]
    manifest = {
        "filename": os.path.basename(path),
        "size_bytes": os.path.getsize(path),
        "sha256": sha256(path),
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    print(json.dumps(manifest, indent=2))
