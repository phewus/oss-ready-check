from __future__ import annotations

import json
from .scanner import ScanReport


def format_text(report: ScanReport) -> str:
    """Format a report as human-readable text."""
    lines: list[str] = []
    lines.append("OSS Ready Check Report")
    lines.append(f"Target: {report.target}")
    lines.append(f"Score: {report.score}/{report.max_score} ({report.percentage}%)")
    lines.append("")

    for result in report.results:
        status = "PASS" if result.passed else "MISS"
        lines.append(f"{status:<5} {result.label:<24} {result.description}")

    missing = [result for result in report.results if not result.passed]
    if missing:
        lines.append("")
        lines.append("Suggested next actions:")
        for index, result in enumerate(missing, start=1):
            lines.append(f"{index}. {result.suggestion}")
    else:
        lines.append("")
        lines.append("Great job. This repository includes the core open-source readiness files checked by this tool.")

    return "\n".join(lines)


def format_json(report: ScanReport) -> str:
    """Format a report as JSON."""
    return json.dumps(report.to_dict(), indent=2, sort_keys=True)
