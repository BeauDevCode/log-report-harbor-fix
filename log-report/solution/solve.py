import json
from collections import Counter
from pathlib import Path


LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")


def main() -> None:
    total_requests = 0
    client_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    with LOG_PATH.open("r", encoding="utf-8") as log_file:
        for raw_line in log_file:
            line = raw_line.strip()
            if not line:
                continue

            total_requests += 1
            client_ips.add(line.split()[0])

            request = line.split('"', maxsplit=2)[1]
            request_parts = request.split()
            path_counts[request_parts[1]] += 1

    report = {
        "total_requests": total_requests,
        "unique_ips": len(client_ips),
        "top_path": path_counts.most_common(1)[0][0],
    }

    with REPORT_PATH.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file)
        report_file.write("\n")


if __name__ == "__main__":
    main()
