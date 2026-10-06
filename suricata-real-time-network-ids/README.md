# Real-Time Network IDS Using Suricata

> Educational/reconstructed portfolio implementation for a SOC network-monitoring project.

## Overview
This project demonstrates how Suricata can inspect network traffic, generate IDS alerts, and support SOC investigation.

## Workflow
```
Network Traffic
      ↓
Suricata IDS
      ↓
Rules / Signatures
      ↓
eve.json Alerts
      ↓
SOC Analyst
      ↓
Triage → Investigate → Contain → Report
```

## Objectives
- Understand network IDS concepts.
- Monitor traffic using Suricata.
- Create and tune detection rules.
- Analyze structured JSON alerts.
- Support incident triage with source/destination context.

## Included
- `rules/local.rules` - example educational detection rules.
- `scripts/eve_alert_summary.py` - summarizes Suricata EVE JSON alerts.
- `configuration/README.md` - deployment notes.
- `reports/README.md` - investigation template.
- `screenshots/README.md` - location for genuine lab screenshots.

## Example
```bash
python scripts/eve_alert_summary.py eve.json
```

## Security
Use this project only on networks and systems you own or are authorized to monitor.

## Important note
This is a reconstructed portfolio implementation based on the project concept, not a claim that these files are the user's original source code.
