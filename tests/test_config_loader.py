from __future__ import annotations

import json
from pathlib import Path

from src.config_loader import load_legacy_config, load_layered_config
from src.storage.manager import StorageManager


def test_load_layered_config_merges_base_and_industry(tmp_path: Path) -> None:
    repo_root = tmp_path
    (repo_root / "data" / "config" / "industries").mkdir(parents=True)

    (repo_root / "data" / "config" / "base.json").write_text(
        json.dumps(
            {
                "ai": {
                    "provider": "openai",
                    "model": "gpt-4",
                    "api_key_env": "OPENAI_API_KEY",
                    "languages": ["en"],
                },
                "filtering": {
                    "ai_score_threshold": 6.5,
                    "time_window_hours": 24,
                },
                "output": {
                    "summaries_dir": "var/summaries",
                    "publish_to_docs": False,
                    "include_industry_in_filename": True,
                },
            }
        ),
        encoding="utf-8",
    )
    (repo_root / "data" / "config" / "industries" / "healthcare.json").write_text(
        json.dumps(
            {
                "industry": {
                    "id": "healthcare",
                    "name": "Healthcare",
                },
                "sources": {
                    "github": [],
                    "hackernews": {"enabled": False},
                    "rss": [
                        {
                            "name": "STAT",
                            "url": "https://www.statnews.com/feed/",
                            "enabled": True,
                        }
                    ],
                    "reddit": {"enabled": False, "subreddits": [], "users": [], "fetch_comments": 0},
                    "telegram": {"enabled": False, "channels": []},
                },
                "filtering": {
                    "ai_score_threshold": 7.5,
                },
                "profile": {
                    "audience": "healthcare operators",
                    "search_hints": ["FDA"],
                },
            }
        ),
        encoding="utf-8",
    )

    loaded = load_layered_config(repo_root, industry="healthcare")

    assert loaded.mode == "layered"
    assert loaded.config.filtering.ai_score_threshold == 7.5
    assert loaded.config.filtering.time_window_hours == 24
    assert loaded.config.output.summaries_dir == "var/summaries"
    assert loaded.config.output.include_industry_in_filename is True
    assert loaded.config.industry.slug == "healthcare"
    assert loaded.config.profile.search_hints == ["FDA"]
    assert loaded.storage_data_dir == (repo_root / "data").resolve()


def test_load_legacy_config_keeps_single_file_compatibility(tmp_path: Path) -> None:
    config_path = tmp_path / "data" / "config.json"
    config_path.parent.mkdir(parents=True)
    config_path.write_text(
        json.dumps(
            {
                "version": "1.0",
                "ai": {
                    "provider": "openai",
                    "model": "gpt-4",
                    "api_key_env": "OPENAI_API_KEY",
                },
                "sources": {
                    "github": [],
                    "hackernews": {"enabled": True, "fetch_top_stories": 10, "min_score": 50},
                    "rss": [],
                    "reddit": {"enabled": False, "subreddits": [], "users": [], "fetch_comments": 0},
                    "telegram": {"enabled": False, "channels": []},
                },
                "filtering": {
                    "ai_score_threshold": 6.0,
                    "time_window_hours": 24,
                },
            }
        ),
        encoding="utf-8",
    )

    loaded = load_legacy_config(tmp_path)

    assert loaded.mode == "legacy"
    assert loaded.config.output.summaries_dir == "data/summaries"
    assert loaded.config.industry.slug == "ai-tech"
    assert loaded.storage_data_dir == config_path.parent.resolve()


def test_storage_manager_uses_industry_slug_in_summary_filename(tmp_path: Path) -> None:
    storage = StorageManager(
        data_dir=tmp_path / "data",
        root_dir=tmp_path,
        summaries_dir="exports/summaries",
    )

    path = storage.save_daily_summary("2026-03-25", "# Demo", language="zh", industry_slug="gaming")

    assert path == (tmp_path / "exports" / "summaries" / "horizon-gaming-2026-03-25-zh.md").resolve()
    assert path.read_text(encoding="utf-8") == "# Demo"
