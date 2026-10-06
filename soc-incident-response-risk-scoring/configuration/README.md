# Configuration Notes

## Recommended SOC process
1. Ingest alert.
2. Validate the detection.
3. Record severity, confidence and exposure.
4. Calculate risk.
5. Prioritize investigation.
6. Correlate related events.
7. Contain confirmed threats.
8. Document actions and evidence.
9. Close or escalate the incident.

## Production considerations
- Use authentication and authorization.
- Store secrets outside source control.
- Add audit logging.
- Connect to a real SIEM only through approved APIs.
- Protect incident data and apply retention policies.
- Tune thresholds using historical incident data.
