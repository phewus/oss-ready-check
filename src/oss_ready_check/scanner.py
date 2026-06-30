from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

from .rules import Rule, rule_set


@dataclass(frozen=True)
class CheckResult:
    key: str
    label: str
    passed: bool
    weight: int
    description: str
    suggestion: str


@dataclass(frozen=True)
class ScanReport:
    target: str
    score: int
    max_score: int
    percentage: int
    results: list[CheckResult]

    def to_dict(self) -> dict[str, Any]:
        return {
            "target": self.target,
            "score": self.score,
            "max_score": self.max_score,
            "percentage": self.percentage,
            "results": [asdict(result) for result in self.results],
            "missing": [asdict(result) for result in self.results if not result.passed],
        }


def scan_project(target: str | Path, rules: list[Rule] | None = None) -> ScanReport:
    """Scan a project folder and return an open-source readiness report."""
    root = Path(target).expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"Target path does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Target path is not a directory: {root}")

    active_rules = rules or rule_set()
    results: list[CheckResult] = []

    for rule in active_rules:
        passed = bool(rule.check(root))
        results.append(
            CheckResult(
                key=rule.key,
                label=rule.label,
                passed=passed,
                weight=rule.weight,
                description=rule.description,
                suggestion=rule.suggestion,
            )
        )

    max_score = sum(rule.weight for rule in active_rules)
    score = sum(result.weight for result in results if result.passed)
    percentage = round((score / max_score) * 100) if max_score else 0

    return ScanReport(
        target=str(root),
        score=score,
        max_score=max_score,
        percentage=percentage,
        results=results,
    )
