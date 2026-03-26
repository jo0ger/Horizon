from __future__ import annotations

from src.ai.prompts import build_content_analysis_system
from src.models import Config


def _config_with_profile(profile: dict) -> Config:
    return Config.model_validate(
        {
            "ai": {
                "provider": "openai",
                "model": "gpt-4",
                "api_key_env": "OPENAI_API_KEY",
            },
            "sources": {
                "github": [],
                "hackernews": {"enabled": False},
                "rss": [],
                "reddit": {"enabled": False, "subreddits": [], "users": [], "fetch_comments": 0},
                "telegram": {"enabled": False, "channels": []},
            },
            "filtering": {
                "ai_score_threshold": 7.0,
                "time_window_hours": 24,
            },
            "industry": {
                "id": "gaming",
                "name": "游戏",
            },
            "profile": profile,
        }
    )


def test_content_analysis_system_uses_industry_score_bands() -> None:
    config = _config_with_profile(
        {
            "audience": "游戏开发者",
            "score_bands": {
                "9_10": [
                    "头部游戏停运或延期",
                    "平台政策发生重大变化",
                ],
                "0_2": [
                    "无来源传闻",
                    "常规营销节奏内容",
                ],
            },
        }
    )

    prompt = build_content_analysis_system(config)

    assert "头部游戏停运或延期" in prompt
    assert "平台政策发生重大变化" in prompt
    assert "无来源传闻" in prompt
    assert "常规营销节奏内容" in prompt


def test_content_analysis_system_keeps_default_bands_for_missing_keys() -> None:
    config = _config_with_profile(
        {
            "audience": "医疗从业者",
            "score_bands": {
                "9_10": [
                    "重大监管审批",
                    "关键临床证据突破",
                ],
            },
        }
    )

    prompt = build_content_analysis_system(config)

    assert "重大监管审批" in prompt
    assert "关键临床证据突破" in prompt
    assert "值得立即关注的重要报道、深度分析、关键产品/研究/运营变化" in prompt
