from __future__ import annotations

import asyncio
from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.models import ContentItem, SourceType


def _item() -> ContentItem:
    item = ContentItem(
        id="rss:item-1",
        source_type=SourceType.RSS,
        title="Healthcare headline",
        url="https://example.com/healthcare",
        author="tester",
        published_at=datetime.now(timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = "Summary"
    return item


def test_summary_header_includes_industry_name_for_english() -> None:
    summarizer = DailySummarizer()

    result = asyncio.run(
        summarizer.generate_summary(
            [_item()],
            "2026-03-26",
            1,
            language="en",
            industry_name="Healthcare",
        )
    )

    assert result.startswith("# Horizon Healthcare Daily - 2026-03-26")


def test_summary_header_includes_industry_name_for_chinese() -> None:
    summarizer = DailySummarizer()

    result = asyncio.run(
        summarizer.generate_summary(
            [_item()],
            "2026-03-26",
            1,
            language="zh",
            industry_name="医疗",
        )
    )

    assert result.startswith("# Horizon 医疗每日速递 - 2026-03-26")


def test_summary_header_includes_default_ai_tech_label() -> None:
    summarizer = DailySummarizer()

    result = asyncio.run(
        summarizer.generate_summary(
            [_item()],
            "2026-03-26",
            1,
            language="en",
            industry_name="AI 科技",
        )
    )

    assert result.startswith("# Horizon AI 科技 Daily - 2026-03-26")
