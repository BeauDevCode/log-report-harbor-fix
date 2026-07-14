An Apache-style access log is located at `/app/access.log`.

Each non-empty line has this form:

`<client-ip> - - [<timestamp>] "<METHOD> <path> HTTP/1.1" <status> <bytes>`

Analyze the log and write a report to `/app/report.json`.

The report must be one valid JSON object containing exactly these three keys:

- `total_requests` (integer): the number of non-empty request lines in `/app/access.log`.
- `unique_ips` (integer): the number of distinct client IP addresses. The client IP is the first whitespace-separated field of each non-empty line.
- `top_path` (string): the request path that appears most frequently. The request path is the value between the HTTP method and the HTTP version inside the quoted request. The shipped log has one unique most-frequent path, so no tie-breaking rule is required.

Success criteria:

1. `/app/report.json` exists, contains one valid JSON object, has exactly the keys `total_requests`, `unique_ips`, and `top_path`, and uses integer values for `total_requests` and `unique_ips` and a string value for `top_path`.
2. `total_requests` equals the number of non-empty request lines in the shipped `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses in the shipped `/app/access.log`.
4. `top_path` equals the most frequently requested path in the shipped `/app/access.log`.
