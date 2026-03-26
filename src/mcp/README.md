# Horizon MCP

Horizon includes a built-in MCP server that exposes the native Horizon pipeline as staged tools and read-only resources.

The MCP layer does not reimplement Horizon business logic. It reuses the existing fetch, score, filter, enrich, and summarize modules from the main codebase.

## Tools

| Tool | Description |
| --- | --- |
| `hz_validate_config` | Validate Horizon config and required environment variables |
| `hz_fetch_items` | Fetch and deduplicate content into the `raw` stage |
| `hz_score_items` | Score items from a stage into `scored` |
| `hz_filter_items` | Filter scored items into `filtered` |
| `hz_enrich_items` | Enrich filtered items into `enriched` |
| `hz_generate_summary` | Generate markdown from a stage |
| `hz_run_pipeline` | Run fetch -> score -> filter -> enrich -> summarize |
| `hz_list_runs` | List recent run artifacts |
| `hz_get_run_meta` | Read metadata for a run |
| `hz_get_run_stage` | Read items from a run stage |
| `hz_get_run_summary` | Read a generated summary |
| `hz_get_metrics` | Read in-memory server metrics |

## Resources

- `horizon://server/info`
- `horizon://metrics`
- `horizon://runs`
- `horizon://runs/{run_id}/meta`
- `horizon://runs/{run_id}/items/{stage}`
- `horizon://runs/{run_id}/summary/{language}`
- `horizon://config/effective`

## Install and Start

```bash
uv sync
uv run horizon-mcp
uv run horizon-mcp --industry healthcare
uv run horizon-mcp --industry gaming --base-config data/config/base.json
```

The server runs over stdio and is intended to be launched by an MCP client. If you pass `--industry`, that layered config becomes the default context for all tool calls unless a tool call explicitly overrides it with `industry`, `base_config_path`, `industry_config_path`, or `config_path`.

## Common Usage Patterns

### Pattern A: Start the server with a default industry

```bash
uv run horizon-mcp --industry healthcare
```

Then tool calls can stay minimal because `healthcare` is already the default context:

```json
{
  "tool": "hz_validate_config",
  "arguments": {
    "check_env": true
  }
}
```

```json
{
  "tool": "hz_run_pipeline",
  "arguments": {
    "hours": 24,
    "save_to_horizon_data": true
  }
}
```

### Pattern B: Override the industry per tool call

Keep the server generic:

```bash
uv run horizon-mcp
```

Then pass the layered config context explicitly:

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

### Pattern C: Use staged calls and let `run_id` carry the config context

First fetch with an explicit industry:

```json
{
  "tool": "hz_fetch_items",
  "arguments": {
    "industry": "healthcare",
    "hours": 24
  }
}
```

Assume the response returns `run_id = "run-20260326-123456"`. The later stages can omit the industry because the service restores it from run metadata:

```json
{
  "tool": "hz_score_items",
  "arguments": {
    "run_id": "run-20260326-123456"
  }
}
```

```json
{
  "tool": "hz_generate_summary",
  "arguments": {
    "run_id": "run-20260326-123456",
    "language": "zh",
    "save_to_horizon_data": true
  }
}
```

### Pattern D: Fall back to the legacy single-file config

```json
{
  "tool": "hz_run_pipeline",
  "arguments": {
    "config_path": "data/config.json",
    "hours": 24
  }
}
```

Do not combine `config_path` with `industry`, `base_config_path`, or `industry_config_path` in the same tool call.

## Run Artifacts

Each run writes artifacts under `data/mcp-runs/<run_id>/`:

- `meta.json`
- `raw_items.json`
- `scored_items.json`
- `filtered_items.json`
- `enriched_items.json`
- `summary-<lang>.md`

## Design Principles

1. Keep Horizon as the single source of business logic.
2. Preserve staged re-entry so a run can continue from intermediate artifacts.
3. Default to no extra side effects unless explicitly requested.

## Client Setup

See [integration.md](integration.md).
