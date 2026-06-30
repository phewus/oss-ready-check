from pathlib import Path

from oss_ready_check.formatters import format_json, format_text
from oss_ready_check.scanner import scan_project


def test_format_text_contains_score(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Example", encoding="utf-8")
    report = scan_project(tmp_path)
    text = format_text(report)
    assert "OSS Ready Check Report" in text
    assert "Score:" in text


def test_format_json_contains_missing(tmp_path: Path) -> None:
    report = scan_project(tmp_path)
    data = format_json(report)
    assert '"missing"' in data
    assert '"percentage"' in data
