# Detection Rules & Tuning

## Baseline
Start with a small threshold in a controlled lab and review normal authentication behavior.

## Useful correlations
- Multiple failures from one source against one account.
- Multiple accounts targeted from one source.
- Successful authentication after repeated failures.
- Geographically or temporally unusual authentication.
- Endpoint/network alerts occurring at the same time.

## False positives
Potential benign causes include:
- Forgotten passwords
- Misconfigured services
- Expired credentials
- Automated jobs using outdated credentials

Tune thresholds and exceptions based on real environment baselines.
