# OSS Ready Check

**OSS Ready Check** is a small command-line tool that helps developers review whether a project is ready to be published as a healthy open-source repository.

It scans a project folder and checks for common open-source essentials such as a README, license, contributing guide, code of conduct, security policy, tests, examples, changelog, package metadata, and GitHub issue templates.

The goal is simple: help maintainers and new contributors improve open-source project quality before asking people to use or contribute to their code.

## Why this project exists

Many projects are useful but difficult to contribute to because they are missing basic community and maintenance files. New contributors often do not know where to start, and maintainers may not notice gaps until users begin opening issues.

OSS Ready Check gives a quick, local, human-readable report so a maintainer can improve a repository before publishing, sharing, or requesting contributions.

## Features

- Scans any local project directory
- Checks for common open-source readiness files
- Gives a score out of 100
- Explains what is missing and why it matters
- Supports JSON output for automation
- Works without external dependencies
- Beginner-friendly Python codebase

## Quick start

```bash
python -m oss_ready_check .
```

Or after installation:

```bash
oss-ready-check .
```

## Example output

```text
OSS Ready Check Report
Target: /path/to/project
Score: 78/100

PASS  README.md                 Project overview exists
PASS  LICENSE                   License file exists
MISS  CONTRIBUTING.md            Contribution instructions are missing
PASS  tests/                    Test directory exists
MISS  SECURITY.md                Security policy is missing

Suggested next actions:
1. Add CONTRIBUTING.md so contributors know how to help.
2. Add SECURITY.md so users know how to report vulnerabilities.
```

## JSON output

```bash
oss-ready-check . --json
```

## What it checks

| Check | Why it matters |
|---|---|
| README | Explains what the project does and how to use it |
| LICENSE | Clarifies legal reuse rights |
| CONTRIBUTING | Helps contributors submit useful changes |
| CODE_OF_CONDUCT | Sets community expectations |
| SECURITY | Provides a responsible disclosure path |
| CHANGELOG | Tracks project changes |
| Tests | Gives confidence that changes do not break behavior |
| Examples | Helps new users understand the project quickly |
| GitHub issue templates | Improves issue quality |
| Package metadata | Helps installation and distribution |

## Installation from source

```bash
git clone https://github.com/YOUR-USERNAME/oss-ready-check.git
cd oss-ready-check
python -m pip install -e .
oss-ready-check .
```

## Roadmap

- Add more ecosystem-specific checks for Python, Node.js, Rust, and Go
- Add GitHub Actions compatibility mode
- Add a Markdown report export option
- Add severity levels for missing items
- Add a web version for non-technical users
- Add multilingual documentation

## Contributing

Contributions are welcome. Start with `CONTRIBUTING.md`, then open an issue or pull request.

Good first contributions include:

- Improving documentation
- Adding more check rules
- Adding tests
- Improving report wording
- Adding examples for different project types

## License

MIT License. See `LICENSE` for details.
