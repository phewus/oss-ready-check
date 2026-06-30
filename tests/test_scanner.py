from pathlib import Path

from oss_ready_check.scanner import scan_project


def test_scan_project_scores_existing_files(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Example", encoding="utf-8")
    (tmp_path / "LICENSE").write_text("MIT", encoding="utf-8")
    (tmp_path / "tests").mkdir()

    report = scan_project(tmp_path)

    passed_keys = {result.key for result in report.results if result.passed}
    assert "readme" in passed_keys
    assert "license" in passed_keys
    assert "tests" in passed_keys
    assert report.score > 0
    assert report.max_score == 100


def test_scan_project_rejects_missing_path(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    try:
        scan_project(missing)
    except FileNotFoundError as exc:
        assert "does not exist" in str(exc)
    else:
        raise AssertionError("Expected FileNotFoundError")
