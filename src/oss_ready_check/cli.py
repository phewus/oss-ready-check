from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .formatters import format_json, format_text
from .scanner import scan_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="oss-ready-check",
        description="Check whether a repository has common open-source readiness files.",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Project directory to scan. Defaults to current directory.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the report as JSON instead of text.",
    )
    parser.add_argument(
        "--fail-under",
        type=int,
        default=None,
        metavar="PERCENT",
        help="Exit with code 2 when the score percentage is below this value.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        report = scan_project(Path(args.target))
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    output = format_json(report) if args.json else format_text(report)
    print(output)

    if args.fail_under is not None and report.percentage < args.fail_under:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
