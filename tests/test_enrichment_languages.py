from __future__ import annotations

from datetime import datetime, timezone
import sys
import types

ddgs_stub = types.ModuleType("ddgs")


class _DDGSStub:
    pass


ddgs_stub.DDGS = _DDGSStub
sys.modules.setdefault("ddgs", ddgs_stub)


anthropic_stub = types.ModuleType("anthropic")
anthropic_stub.AsyncAnthropic = object
sys.modules.setdefault("anthropic", anthropic_stub)

openai_stub = types.ModuleType("openai")
openai_stub.AsyncOpenAI = object
sys.modules.setdefault("openai", openai_stub)

google_stub = types.ModuleType("google")
google_genai_stub = types.ModuleType("google.genai")
google_genai_stub.Client = object
google_genai_types_stub = types.ModuleType("google.genai.types")
google_genai_stub.types = google_genai_types_stub
google_stub.genai = google_genai_stub
sys.modules.setdefault("google", google_stub)
sys.modules.setdefault("google.genai", google_genai_stub)
sys.modules.setdefault("google.genai.types", google_genai_types_stub)

from src.ai.enricher import ContentEnricher
from src.ai.prompts import (
    build_content_enrichment_system,
    build_content_enrichment_user,
    get_output_languages,
)
from src.models import Config, ContentItem, SourceType


def _config(languages: list[str]) -> Config:
    return Config.model_validate(
        {
            "ai": {
                "provider": "openai",
                "model": "gpt-4",
                "api_key_env": "OPENAI_API_KEY",
                "languages": languages,
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
                "id": "ai-tech",
                "name": "AI 科技",
            },
        }
    )


def _item() -> ContentItem:
    return ContentItem(
        id="rss:item-1",
        source_type=SourceType.RSS,
        title="Test title",
        url="https://example.com/item",
        author="tester",
        published_at=datetime.now(timezone.utc),
    )


def test_get_output_languages_filters_and_preserves_order() -> None:
    config = _config(["zh", "fr", "en", "zh"])

    assert get_output_languages(config) == ["zh", "en"]


def test_build_content_enrichment_system_respects_zh_only() -> None:
    prompt = build_content_enrichment_system(_config(["zh"]))

    assert "请只输出中文字段" in prompt
    assert "- title_zh" in prompt
    assert "title_en" not in prompt


def test_build_content_enrichment_user_respects_en_only() -> None:
    prompt = build_content_enrichment_user(_config(["en"]))

    assert '"title_en"' in prompt
    assert '"title_zh"' not in prompt
    assert "所有字段内容用英文书写" in prompt


def test_build_content_enrichment_user_preserves_language_order() -> None:
    prompt = build_content_enrichment_user(_config(["zh", "en"]))

    assert prompt.index('"title_zh"') < prompt.index('"title_en"')
    assert prompt.index('"whats_new_zh"') < prompt.index('"whats_new_en"')


def test_build_content_enrichment_user_supports_runtime_formatting() -> None:
    prompt = build_content_enrichment_user(_config(["zh"]))

    rendered = prompt.format(
        title="标题",
        url="https://example.com",
        summary="摘要",
        score=8,
        reason="原因",
        tags="标签1, 标签2",
        content="正文",
        comments_section="",
        web_context="检索结果",
    )

    assert '"title_zh": "<用中文写一个简短标题，不超过15个词>"' in rendered
    assert "标题: 标题" in rendered


def test_store_enrichment_result_uses_primary_language_fallback_for_zh() -> None:
    enricher = ContentEnricher(ai_client=None, config=_config(["zh"]))  # type: ignore[arg-type]
    item = _item()
    result = {
        "title_zh": "中文标题",
        "whats_new_zh": "发生了新的变化。",
        "why_it_matters_zh": "这很重要。",
        "key_details_zh": "这里有关键细节。",
        "background_zh": "这里是背景信息。",
        "community_discussion_zh": "社区讨论集中在执行难度。",
        "sources": ["https://example.com/context"],
    }

    enricher._store_enrichment_result(
        item,
        result,
        {"https://example.com/context": "Context source"},
    )

    assert item.metadata["title_zh"] == "中文标题"
    assert item.metadata["detailed_summary_zh"] == "发生了新的变化。 这很重要。 这里有关键细节。"
    assert item.metadata["detailed_summary"] == item.metadata["detailed_summary_zh"]
    assert item.metadata["background"] == "这里是背景信息。"
    assert item.metadata["community_discussion"] == "社区讨论集中在执行难度。"
    assert "title_en" not in item.metadata


def test_store_enrichment_result_uses_first_language_for_legacy_fallback() -> None:
    enricher = ContentEnricher(ai_client=None, config=_config(["en", "zh"]))  # type: ignore[arg-type]
    item = _item()
    result = {
        "title_en": "English title",
        "whats_new_en": "Something changed.",
        "why_it_matters_en": "It matters.",
        "key_details_en": "More details.",
        "background_en": "Background in English.",
        "community_discussion_en": "English discussion.",
        "title_zh": "中文标题",
        "whats_new_zh": "有新变化。",
        "why_it_matters_zh": "这很重要。",
        "key_details_zh": "更多细节。",
        "background_zh": "中文背景。",
        "community_discussion_zh": "中文讨论。",
    }

    enricher._store_enrichment_result(item, result, {})

    assert item.metadata["detailed_summary"] == item.metadata["detailed_summary_en"]
    assert item.metadata["background"] == "Background in English."
    assert item.metadata["community_discussion"] == "English discussion."
