# Wazuh SOC Monitoring Lab

> Educational/reconstructed portfolio project for a Security Operations Center (SOC) workflow using Wazuh concepts.

## Overview
This project demonstrates a beginner-friendly SOC monitoring workflow: collecting security events, analyzing authentication activity, identifying suspicious patterns, assigning severity, and documenting incidents.

## Objectives
- Understand SIEM/SOC monitoring concepts.
- Analyze Linux authentication logs.
- Detect repeated failed authentication attempts.
- Map suspicious activity to defensive investigation steps.
- Produce structured incident information.

## Architecture
```
Linux Endpoint -> Authentication/System Logs -> Wazuh Agent -> Wazuh Manager
-> Wazuh Dashboard/Alerts -> SOC Analyst -> Triage -> Investigation -> Response -> Report
```

## Included
- `scripts/log_analyzer.py` - local educational log analyzer.
- `detection-rules/custom_rules.xml` - example Wazuh-style custom rule.
- `configuration/README.md` - deployment notes.
- `reports/README.md` - incident reporting template.
- `screenshots/README.md` - placeholders for real lab screenshots.

## Security
Never commit passwords, API keys, private keys, .env files, real credentials, or sensitive IP information.

## Important note
This repository is a reconstructed portfolio implementation based on the project concept and workflow, not a claim that these files are the user's original source code.
