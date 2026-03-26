# Horizon MCP Integration

## Recommended Command

Start the built-in MCP server from the Horizon repository root:

```bash
uv run horizon-mcp
uv run horizon-mcp --industry healthcare
```

If you need a Python module fallback:

```bash
uv run python -m src.mcp.server
uv run python -m src.mcp.server --industry healthcare
```

## Two Setup Modes

### Option A: Client Config With Explicit `cwd`

Some MCP clients need a fixed working directory in their config. In that case, the absolute path is only used in the client-side `cwd` field, not in Horizon's code.

Example:

```json
{
  "mcpServers": {
    "horizon": {
      "command": "uv",
      "args": ["run", "horizon-mcp", "--industry", "healthcare"],
      "cwd": "/absolute/path/to/Horizon"
    }
  }
}
```

Restart the client after saving the config.

### Option B: Local Start Without Any Path In Config

If your workflow allows you to start the MCP server manually, no absolute path is needed at all:

```bash
cd /absolute/path/to/Horizon
uv run horizon-mcp
uv run horizon-mcp --industry healthcare
```

This is the cleanest way to avoid path values in client configuration.

## Config Resolution

Horizon MCP now supports both config modes:

- Legacy single-file config via `config_path`
- Layered config via `industry`, `base_config_path`, and `industry_config_path`

Resolution priority is:

1. Explicit tool call arguments
2. MCP server startup defaults such as `uv run horizon-mcp --industry healthcare`
3. Run metadata from earlier staged calls on the same `run_id`
4. Legacy fallback to `data/config.json`

## Tool Call Examples

### Validate the effective healthcare config

If the server was started with `--industry healthcare`, the tool call can stay short:

```json
{
  "tool": "hz_validate_config",
  "arguments": {
    "check_env": true
  }
}
```

If the server was started without a default industry, pass it explicitly:

```json
{
  "tool": "hz_validate_config",
  "arguments": {
    "industry": "healthcare",
    "check_env": true
  }
}
```

### Run the full pipeline for one industry

```json
{
  "tool": "hz_run_pipeline",
  "arguments": {
    "industry": "gaming",
    "hours": 48,
    "sources": ["rss", "reddit"],
    "save_to_horizon_data": true
  }
}
```

### Run staged calls with `run_id` inheritance

Step 1:

```json
{
  "tool": "hz_fetch_items",
  "arguments": {
    "industry": "healthcare",
    "hours": 24
  }
}
```

Step 2:

```json
{
  "tool": "hz_score_items",
  "arguments": {
    "run_id": "run-20260326-123456"
  }
}
```

Step 3:

```json
{
  "tool": "hz_filter_items",
  "arguments": {
    "run_id": "run-20260326-123456",
    "topic_dedup": true
  }
}
```

Step 4:

```json
{
  "tool": "hz_generate_summary",
  "arguments": {
    "run_id": "run-20260326-123456",
    "language": "en",
    "save_to_horizon_data": true
  }
}
```

### Override the config file paths explicitly

```json
{
  "tool": "hz_run_pipeline",
  "arguments": {
    "industry": "healthcare",
    "base_config_path": "data/config/base.json",
    "industry_config_path": "data/config/industries/healthcare.json",
    "hours": 24
  }
}
```

### Use the old single-file config

```json
{
  "tool": "hz_run_pipeline",
  "arguments": {
    "config_path": "data/config.json",
    "hours": 24
  }
}
```

Do not mix `config_path` with `industry`, `base_config_path`, or `industry_config_path`.

## Secret Files

Instead of exporting environment variables manually, you can place a JSON file in one of these locations:

- `.cursor/mcp.secrets.json`
- `.cursor/mcp.secrets.local.json`
- `config/mcp.secrets.json`
- `config/mcp.secrets.local.json`
- `<horizon_path>/data/mcp.secrets.json`
- `<horizon_path>/data/mcp-secrets.json`

Supported formats:

```json
{
  "OPENAI_API_KEY": "sk-xxxx",
  "ANTHROPIC_API_KEY": "sk-ant-xxxx",
  "GOOGLE_API_KEY": "xxxx",
  "GITHUB_TOKEN": "ghp_xxxx"
}
```

```json
{
  "env": {
    "OPENAI_API_KEY": "sk-xxxx",
    "ANTHROPIC_API_KEY": "sk-ant-xxxx",
    "GOOGLE_API_KEY": "xxxx",
    "GITHUB_TOKEN": "ghp_xxxx"
  }
}
```

You can also point to a custom secrets file with:

```json
{
  "HORIZON_MCP_SECRETS_PATH": "/absolute/path/to/mcp.secrets.json"
}
```

## Smoke Check

Run the local smoke check from the repository root:

```bash
uv run python scripts/check_mcp.py
```

It verifies module import, path resolution, config loading, and metrics access.
