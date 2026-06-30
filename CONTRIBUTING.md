# Contributing to OSS Ready Check

Thank you for considering a contribution.

## Ways to help

- Improve documentation
- Add a new readiness rule
- Improve report wording
- Add examples for different project types
- Add tests for existing behavior
- Report bugs or confusing output

## Development setup

```bash
git clone https://github.com/YOUR-USERNAME/oss-ready-check.git
cd oss-ready-check
python -m pip install -e .
python -m pytest
```

## Pull request checklist

Before opening a pull request:

- Explain what changed and why
- Add or update tests when behavior changes
- Keep wording clear for beginners
- Run the test suite locally
- Keep changes focused and small when possible

## Adding a rule

Rules live in `src/oss_ready_check/rules.py`.

A good rule should:

- Check for something broadly useful
- Have a clear label
- Explain why the check matters
- Give an actionable suggestion
- Avoid forcing one ecosystem's style on every project
