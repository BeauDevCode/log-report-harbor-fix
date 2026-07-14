# Harbor validation evidence

The repaired task is in [`log-report/`](./log-report).

Validation ran with Harbor 0.18.0 on a GitHub-hosted Ubuntu runner with Docker:

https://github.com/BeauDevCode/log-report-harbor-fix/actions/runs/29376153356

## Oracle

Command:

```bash
harbor run -p log-report -a oracle
```

Harbor result:

```text
1/1 Mean: 1.000
adhoc • oracle
Trials: 1
Exceptions: 0
Mean: 1.000
Reward 1.0: 1
```

Verifier artifacts:

```text
reward.txt: 1
ctrf.json summary: tests=4, passed=4, failed=0, skipped=0, pending=0, other=0
```

## No-op agent

Command:

```bash
harbor run -p log-report --agent nop
```

Harbor result:

```text
1/1 Mean: 0.000
adhoc • nop
Trials: 1
Exceptions: 0
Mean: 0.000
Reward 0.0: 1
```

Verifier artifacts:

```text
reward.txt: 0
ctrf.json summary: tests=4, passed=0, failed=4, skipped=0, pending=0, other=0
```

## Deliberately wrong solution

For the negative test, `solution/solve.sh` was temporarily replaced in a copy of the task with:

```bash
#!/bin/bash
set -euo pipefail

cat > /app/report.json <<'JSON'
{"total_requests": 5, "unique_ips": 3, "top_path": "/index.html"}
JSON
```

Harbor result:

```text
1/1 Mean: 0.000
adhoc • oracle
Trials: 1
Exceptions: 0
Mean: 0.000
Reward 0.0: 1
```

Verifier artifacts:

```text
reward.txt: 0
ctrf.json summary: tests=4, passed=3, failed=1, skipped=0, pending=0, other=0
```

Relevant failure:

```text
FAILED test_outputs.py::test_success_criterion_2_total_requests
E assert 5 == 6
```
