---
layout: default
title: Configuration Guide
---

# Configuration Guide

Horizon is configured through two files: a `.env` file for API keys and a `data/config.json` file for sources, AI provider, and filtering options.

## AI Providers

Configure which AI model scores and summarizes your content.

**Anthropic Claude**:

```json
{
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY"
  }
}
```

**OpenAI**:

```json
{
  "ai": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key_env": "OPENAI_API_KEY"
  }
}
```

**MiniMax**:

```json
{
  "ai": {
    "provider": "minimax",
    "model": "MiniMax-M2.7",
    "api_key_env": "MINIMAX_API_KEY"
  }
}
```

Available models: `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`, `MiniMax-M2.5`, `MiniMax-M2.5-highspeed`

**Aliyun DashScope** (OpenAI-compatible):

```json
{
  "ai": {
    "provider": "ali",
    "model": "qwen-plus",
    "api_key_env": "DASHSCOPE_API_KEY"
  }
}
```

Use the [DashScope compatible-mode](https://help.aliyun.com/zh/dashscope/developer-reference/use-dashscope-by-calling-openai-api) endpoint. Set `DASHSCOPE_API_KEY` in your `.env`. Optional: set `base_url` to override the default `https://dashscope.aliyuncs.com/compatible-mode/v1`.

**Custom Base URL** (for proxies):

```json
{
  "ai": {
    "provider": "anthropic",
    "base_url": "https://your-proxy.com/v1",
    ...
  }
}
```

## Information Sources

All sources are configured under the top-level `sources` key in `config.json`.

### GitHub

```json
{
  "sources": {
    "github": [
      {
        "type": "user_events",
        "username": "gvanrossum",
        "enabled": true
      },
      {
        "type": "repo_releases",
        "owner": "python",
        "repo": "cpython",
        "enabled": true
      }
    ]
  }
}
```

### Hacker News

```json
{
  "sources": {
    "hackernews": {
      "enabled": true,
      "fetch_top_stories": 30,
      "min_score": 100
    }
  }
}
```

### RSS Feeds

```json
{
  "sources": {
    "rss": [
      {
        "name": "Blog Name",
        "url": "https://example.com/feed.xml",
        "enabled": true,
        "category": "ai-ml"
      }
    ]
  }
}
```

### Reddit

```json
{
  "sources": {
    "reddit": {
      "enabled": true,
      "fetch_comments": 5,
      "subreddits": [
        {
          "subreddit": "MachineLearning",
          "sort": "hot",
          "fetch_limit": 25,
          "min_score": 10
        }
      ],
      "users": [
        {
          "username": "spez",
          "sort": "new",
          "fetch_limit": 10
        }
      ]
    }
  }
}
```

## Filtering

Content is scored 0-10:

- **9-10**: Groundbreaking - Major breakthroughs, paradigm shifts
- **7-8**: High Value - Important developments, deep technical content
- **5-6**: Interesting - Worth knowing but not urgent
- **3-4**: Low Priority - Generic or routine content
- **0-2**: Noise - Spam, off-topic, or trivial

```json
{
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24
  }
}
```

- `ai_score_threshold`: Only include content scoring >= this value
- `time_window_hours`: Fetch content from last N hours

## Industry Prompt Profile

Use `profile` to steer how the AI scores, downranks, and explains content for a specific industry.

```json
{
  "profile": {
    "audience": "Healthcare operators, investors, and researchers",
    "score_bands": {
      "9_10": [
        "Major regulatory approvals or strong late-stage clinical evidence",
        "Events that materially change treatment decisions or market structure"
      ],
      "0_2": [
        "Promotional claims with weak evidence",
        "Low-signal items with little operational relevance"
      ]
    },
    "scoring_focus": [
      "Evidence quality, sample size, and decision relevance"
    ],
    "downrank_if": [
      "The piece overstates impact without strong support"
    ],
    "concept_focus": "Trial phases, drug targets, reimbursement terms, and workflow concepts",
    "search_hints": ["FDA", "PubMed", "NEJM"]
  }
}
```

- `audience`: who the summary is written for
- `score_bands`: per-score-range examples inserted into the scoring prompt; supported keys are `9_10`, `7_8`, `5_6`, `3_4`, `0_2`
- `scoring_focus`: what high-value items should emphasize
- `downrank_if`: what should be penalized
- `concept_focus`: what kinds of terms should trigger background lookups
- `search_hints`: preferred sources when grounding background context

## Environment Variable Substitution

RSS feed URLs support `${VAR_NAME}` syntax for secrets. The variable is expanded at runtime from environment variables (or `.env` file):

```json
{
  "name": "LWN.net",
  "url": "https://lwn.net/headlines/full_text?key=${LWN_KEY}",
  "enabled": true
}
```

This way `config.json` can be committed to a public repo without leaking tokens.
