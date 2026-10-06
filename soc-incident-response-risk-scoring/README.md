# SOC Incident Response & Risk Scoring

> Educational/reconstructed portfolio project for SOC alert triage, risk scoring and incident reporting.

## Overview
This project demonstrates a lightweight SOC workflow that converts security alerts into a consistent risk score, prioritizes incidents, and produces structured response information.

## Workflow
```
Security Alert
     ↓
Normalize Alert
     ↓
Score Severity + Confidence + Exposure
     ↓
Risk Score
     ↓
Priority
     ↓
Analyst Investigation
     ↓
Containment / Recovery
     ↓
Incident Report
```

## Risk model
The included model uses three analyst inputs:
- Severity: 1–5
- Confidence: 1–5
- Exposure: 1–5

Risk score = Severity × Confidence × Exposure.

Priority:
- 1–20: LOW
- 21–50: MEDIUM
- 51–80: HIGH
- 81–125: CRITICAL

This is an educational model; production SOCs should calibrate scoring to their environment.

## Included
- `scripts/risk_score.py` - CLI risk-scoring utility.
- `dashboard/app.py` - small local Flask dashboard.
- `reports/incident_report.md` - report template.
- `configuration/README.md` - deployment and tuning notes.
- `screenshots/README.md` - genuine evidence placeholder.

## Run
```bash
pip install -r requirements.txt
python scripts/risk_score.py --severity 4 --confidence 5 --exposure 4
```

For the optional dashboard:
```bash
python dashboard/app.py
```

## Security
Do not place credentials, API keys, real incident data, or personal information in the repository.

## Important note
This is a reconstructed portfolio implementation based on the project concept and is not represented as the user's original source code.
