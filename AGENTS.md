# Repository Guidelines

## Project Structure & Module Organization
`src/` contains the application code. Key areas are `src/ai/` for scoring and summarization, `src/scrapers/` for source collectors, `src/storage/` for config and artifact handling, and `src/mcp/` for the MCP server layer. CLI entry points live in `src/main.py` and `src/setup/wizard.py`.

`tests/` covers the MCP adapter, service layer, and provider clients. Runtime data lives under `data/` (`config.example.json`, `presets.json`, generated summaries). Documentation and screenshots are in `docs/`, and `scripts/check_mcp.py` supports local validation.

## Build, Test, and Development Commands
- `uv sync --dev`: install runtime and test dependencies from `pyproject.toml` and `uv.lock`.
- `uv run horizon`: run the pipeline with `data/config.json`.
- `uv run horizon --hours 48 --source rss,github`: run a narrower fetch window or source set.
- `uv run horizon-wizard`: generate or update `data/config.json` interactively.
- `uv run horizon-mcp`: start the stdio MCP server.
- `uv run pytest`: run the full test suite.
- `uv run pytest --cov=src`: run tests with coverage.
- `uv run python scripts/check_mcp.py`: smoke test MCP wiring.
- `docker-compose run --rm horizon`: run the app in the repo’s container setup.

## Coding Style & Naming Conventions
Target Python 3.11+ with 4-space indentation and type hints on new or changed code. Follow existing naming patterns: `snake_case` for modules, functions, and variables, `PascalCase` for classes, and `SCREAMING_SNAKE_CASE` for constants. Prefer extending existing modules over introducing parallel abstractions.

No repo-wide formatter or linter is configured in `pyproject.toml`, so match the surrounding style and keep imports ordered consistently.

## Testing Guidelines
Tests use `pytest`; discovery is configured for `tests/` in `pyproject.toml`. Name files `test_*.py` and keep shared fixtures in `tests/conftest.py`. Add targeted tests for new MCP tools, config handling, and provider edge cases. There is no enforced coverage gate, but new features should ship with regression tests.

## Commit & Pull Request Guidelines
Recent history uses concise Conventional Commit prefixes such as `feat(RSS): ...`, `feat(page): ...`, and `chore: ...`. Keep commits focused, imperative, and scoped when the change is isolated.

PRs should explain the behavior change, note config or environment impacts, and link related issues. Include screenshots for `docs/` or UI output changes, plus sample commands or test results for pipeline or MCP changes.

## Configuration & Security Notes
Copy `.env.example` to `.env` and `data/config.example.json` to `data/config.json` for local setup. Never commit secrets or private feed credentials. If you add config fields or MCP tools, update the README and example config in the same change.
