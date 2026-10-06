# Configuration Notes

1. Install Suricata on an authorized Linux monitoring host.
2. Identify the correct monitoring interface.
3. Enable EVE JSON output.
4. Load the local rules.
5. Validate the configuration before starting Suricata.
6. Monitor `eve.json`.
7. Forward relevant alerts to your SIEM/SOC workflow.
8. Tune noisy rules after reviewing false positives.

Keep rule IDs unique in your environment and follow the documentation for your installed Suricata release.
