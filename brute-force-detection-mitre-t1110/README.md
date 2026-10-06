# Brute Force Detection & MITRE ATT&CK T1110 Analysis

> Educational/reconstructed portfolio project for detecting repeated authentication failures and mapping the activity to MITRE ATT&CK.

## Overview
This project demonstrates a defensive workflow for identifying possible brute-force authentication activity, enriching the alert with context, and mapping the behavior to **MITRE ATT&CK T1110 — Brute Force**.

## Detection workflow
```
Authentication Logs
       ↓
Failed-login aggregation
       ↓
Threshold / anomaly detection
       ↓
Source & account analysis
       ↓
MITRE ATT&CK T1110 mapping
       ↓
SOC triage
       ↓
Containment + credential review
```

## Detection logic
The included script groups failed authentication events by source IP. When the number of failures reaches the configured threshold, it raises a potential brute-force finding.

This is a simple educational detector and should be tuned for real environments to account for normal authentication failures and distributed attacks.

## Included
- `scripts/brute_force_detector.py` - CSV-based detector.
- `detection-rules/README.md` - detection and tuning guidance.
- `reports/incident_report.md` - investigation report template.
- `mitre/t1110.md` - ATT&CK mapping notes.
- `screenshots/README.md` - genuine lab evidence placeholder.

## Run
```bash
python scripts/brute_force_detector.py sample_auth_events.csv --threshold 5
```

## Defensive controls
- MFA
- Account lockout/rate limiting
- Strong authentication policies
- Centralized logging
- SIEM correlation
- Source reputation and network controls
- Monitoring successful logins following repeated failures

## Important note
This is a reconstructed portfolio implementation based on the project concept and is not represented as the user's original source code.
