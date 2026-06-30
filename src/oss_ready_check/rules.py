from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Rule:
    """A single open-source readiness rule."""

    key: str
    label: str
    weight: int
    description: str
    suggestion: str
    check: Callable[[Path], bool]


def exists_any(root: Path, candidates: list[str]) -> bool:
    """Return True when any candidate file or directory exists."""
    return any((root / candidate).exists() for candidate in candidates)


def rule_set() -> list[Rule]:
    """Return the default rule set used by the scanner."""
    return [
        Rule(
            key="readme",
            label="README",
            weight=18,
            description="Project overview exists",
            suggestion="Add a README.md that explains what the project does, installation, usage, and contribution basics.",
            check=lambda root: exists_any(root, ["README.md", "README.rst", "readme.md"]),
        ),
        Rule(
            key="license",
            label="License",
            weight=14,
            description="License file exists",
            suggestion="Add a LICENSE file so users know how they can legally use and modify the project.",
            check=lambda root: exists_any(root, ["LICENSE", "LICENSE.md", "COPYING"]),
        ),
        Rule(
            key="contributing",
            label="Contributing guide",
            weight=12,
            description="Contribution instructions exist",
            suggestion="Add CONTRIBUTING.md with setup steps, coding style, testing instructions, and pull request guidance.",
            check=lambda root: exists_any(root, ["CONTRIBUTING.md", ".github/CONTRIBUTING.md", "docs/CONTRIBUTING.md"]),
        ),
        Rule(
            key="code_of_conduct",
            label="Code of conduct",
            weight=8,
            description="Community behavior expectations exist",
            suggestion="Add CODE_OF_CONDUCT.md to set community expectations for contributors.",
            check=lambda root: exists_any(root, ["CODE_OF_CONDUCT.md", ".github/CODE_OF_CONDUCT.md"]),
        ),
        Rule(
            key="security",
            label="Security policy",
            weight=8,
            description="Security reporting policy exists",
            suggestion="Add SECURITY.md to explain how users should responsibly report vulnerabilities.",
            check=lambda root: exists_any(root, ["SECURITY.md", ".github/SECURITY.md"]),
        ),
        Rule(
            key="changelog",
            label="Changelog",
            weight=6,
            description="Change history exists",
            suggestion="Add CHANGELOG.md so users can see what changed between releases.",
            check=lambda root: exists_any(root, ["CHANGELOG.md", "HISTORY.md", "RELEASES.md"]),
        ),
        Rule(
            key="tests",
            label="Tests",
            weight=10,
            description="Test files or test directory exist",
            suggestion="Add tests so maintainers can review contributions safely.",
            check=lambda root: exists_any(root, ["tests", "test", "spec", "__tests__"]),
        ),
        Rule(
            key="examples",
            label="Examples",
            weight=7,
            description="Examples exist",
            suggestion="Add examples or sample projects so users understand the tool quickly.",
            check=lambda root: exists_any(root, ["examples", "example", "samples", "demo"]),
        ),
        Rule(
            key="package_metadata",
            label="Package metadata",
            weight=7,
            description="Install or package metadata exists",
            suggestion="Add package metadata such as pyproject.toml, package.json, Cargo.toml, go.mod, or similar.",
            check=lambda root: exists_any(root, ["pyproject.toml", "package.json", "Cargo.toml", "go.mod", "setup.py"]),
        ),
        Rule(
            key="issue_templates",
            label="Issue templates",
            weight=5,
            description="GitHub issue templates exist",
            suggestion="Add .github/ISSUE_TEMPLATE files to guide bug reports and feature requests.",
            check=lambda root: exists_any(root, [".github/ISSUE_TEMPLATE", ".gitlab/issue_templates"]),
        ),
        Rule(
            key="ci",
            label="Continuous integration",
            weight=5,
            description="CI workflow exists",
            suggestion="Add a CI workflow to run tests automatically on pull requests.",
            check=lambda root: exists_any(root, [".github/workflows", ".gitlab-ci.yml", "azure-pipelines.yml"]),
        ),
    ]
