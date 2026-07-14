# Fixed Terminal-Bench 2 Harbor Task: log-report

This repository contains the repaired `dynamo/log-report` Harbor task.

The full task is under [`log-report/`](./log-report).

## Validation targets

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

Expected results:

- Oracle: reward `1.0`
- No-op agent: reward `0.0`
- Deliberately incorrect report: reward `0.0`

See [`EVIDENCE.md`](./EVIDENCE.md) for the recorded Docker-backed Harbor results.

Keep this repository public until the assessment has been reviewed. Make it private only after passing.
