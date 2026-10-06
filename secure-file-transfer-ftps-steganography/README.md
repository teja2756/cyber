# Secure File Transfer via FTPS & Steganography

> Educational/reconstructed portfolio implementation based on a secure file-transfer project concept.

## Overview
This project demonstrates a layered approach to protecting files during transfer: secure transport with FTPS, optional steganographic hiding, integrity verification, and malware scanning before delivery.

## Security Architecture
```
Sender
  |
  +--> File Validation
  |
  +--> Optional Steganography
  |
  +--> SHA-256 Integrity Hash
  |
  +--> FTPS/TLS Transfer
  |
  v
Receiver
  |
  +--> Integrity Verification
  |
  +--> VirusTotal / approved malware-scanning workflow
  |
  +--> Extraction / Delivery
```

## Security concepts
- **FTPS/TLS:** protects data in transit.
- **Steganography:** hides data inside a carrier file; it is not encryption.
- **Hashing:** verifies file integrity.
- **RSA:** can be used for key exchange/signing workflows; never publish private keys.
- **Malware scanning:** adds a defensive inspection layer.

## Included
- `scripts/file_hash.py` - SHA-256 integrity utility.
- `scripts/secure_manifest.py` - creates a transfer manifest.
- `configuration/README.md` - secure deployment notes.
- `reports/README.md` - transfer/security report template.
- `screenshots/README.md` - genuine lab evidence placeholder.

## Important
Do not commit passwords, FTPS credentials, API keys, RSA private keys, SSH keys, or real confidential files.

This is a reconstructed portfolio implementation and does not claim to be the user's original source code.
