import json
from pathlib import Path
from typing import Any


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}

# Fixed ground truth for the access.log baked into the environment image.
# These values are not recomputed from /app/access.log during verification
# because the agent can modify files under /app and make an incorrect report
# appear consistent with a modified input.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def load_report() -> dict[str, Any]:
    with REPORT_PATH.open("r", encoding="utf-8") as report_file:
        return json.load(report_file)


def test_success_criterion_1_report_schema() -> None:
    """
    Success criterion 1:
    The report exists and has the exact required JSON schema and value types.
    """
    assert REPORT_PATH.is_file(), "/app/report.json does not exist"

    report = load_report()

    assert type(report) is dict, "/app/report.json must contain one JSON object"
    assert set(report) == EXPECTED_KEYS, (
        "report.json must contain exactly total_requests, unique_ips, and top_path"
    )
    assert type(report["total_requests"]) is int, (
        "total_requests must be an integer"
    )
    assert type(report["unique_ips"]) is int, "unique_ips must be an integer"
    assert type(report["top_path"]) is str, "top_path must be a string"


def test_success_criterion_2_total_requests() -> None:
    """
    Success criterion 2:
    total_requests matches the shipped access log.
    """
    report = load_report()

    assert report["total_requests"] == EXPECTED_TOTAL_REQUESTS


def test_success_criterion_3_unique_ips() -> None:
    """
    Success criterion 3:
    unique_ips matches the shipped access log.
    """
    report = load_report()

    assert report["unique_ips"] == EXPECTED_UNIQUE_IPS


def test_success_criterion_4_top_path() -> None:
    """
    Success criterion 4:
    top_path matches the shipped access log.
    """
    report = load_report()

    assert report["top_path"] == EXPECTED_TOP_PATH
