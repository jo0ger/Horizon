"""Content analysis using AI."""

import json
import re
from typing import List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import CONTENT_ANALYSIS_USER, build_content_analysis_system
from .utils import parse_json_response
from ..models import Config, ContentItem


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(self, ai_client: AIClient, config: Config | None = None):
        self.client = ai_client
        self.config = config

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    async def analyze_batch(
        self,
        items: List[ContentItem],
        batch_size: int = 10
    ) -> List[ContentItem]:
        analyzed_items = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))

            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                for item in batch:
                    try:
                        await self._analyze_item(item)
                        analyzed_items.append(item)
                    except Exception as e:
                        print(f"Error analyzing item {item.id}: {e}")
                        item.ai_score = 0.0
                        item.ai_reason = "Analysis failed"
                        item.ai_summary = item.title
                        analyzed_items.append(item)
                    progress.advance(task)

        return analyzed_items

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item.

        Args:
            item: Content item to analyze (modified in-place)
        """
        # Prepare content section
        content_section = ""
        if item.content:
            # Split off comments if present
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, comments_part = content_text.split("--- Top Comments ---", 1)
                content_section = f"正文: {main.strip()[:800]}"
            else:
                content_section = f"正文: {content_text[:1000]}"

        # Prepare discussion section (comments, engagement)
        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"社区评论：\n{comments_part[:1500]}")

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"热度分: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} 条评论")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} 个赞")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} 次转发")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} 条回复")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} 次浏览")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} 次收藏")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"赞同比率: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"互动数据: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"讨论链接: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"社区备注: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        # Generate user prompt
        user_prompt = CONTENT_ANALYSIS_USER.format(
            title=item.title,
            source=f"{item.source_type.value}",
            author=item.author or "未知",
            url=str(item.url),
            content_section=content_section,
            discussion_section=discussion_section
        )
        
        # Get AI completion
        response = await self.client.complete(
            system=build_content_analysis_system(self.config),
            user=user_prompt,
            temperature=0.3
        )

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            print(f"Warning: could not parse analysis response for {item.id}, using defaults")
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return

        # Update item with analysis results
        item.ai_score = float(result.get("score", 0))
        item.ai_reason = result.get("reason", "")
        item.ai_summary = result.get("summary", item.title)
        item.ai_tags = result.get("tags", [])
