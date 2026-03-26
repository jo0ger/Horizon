"""Core data models for Horizon."""

from datetime import datetime
from enum import Enum
import re
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, HttpUrl, Field


class SourceType(str, Enum):
    """Supported information source types."""
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    RSS = "rss"
    REDDIT = "reddit"
    TELEGRAM = "telegram"


class ContentItem(BaseModel):
    """Unified content item model from any source."""

    id: str  # Format: {source}:{subtype}:{native_id}
    source_type: SourceType
    title: str
    url: HttpUrl
    content: Optional[str] = None
    author: Optional[str] = None
    published_at: datetime
    fetched_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    # AI analysis results
    ai_score: Optional[float] = None  # 0-10 importance score
    ai_reason: Optional[str] = None
    ai_summary: Optional[str] = None
    ai_tags: List[str] = Field(default_factory=list)


class AIProvider(str, Enum):
    """Supported AI providers."""
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    ALI = "ali"
    GEMINI = "gemini"
    DOUBAO = "doubao"
    MINIMAX = "minimax"


class AIConfig(BaseModel):
    """AI client configuration."""

    provider: AIProvider
    model: str
    base_url: Optional[str] = None
    api_key_env: str
    temperature: float = 0.3
    max_tokens: int = 4096
    languages: List[str] = Field(default_factory=lambda: ["en"])


class GitHubSourceConfig(BaseModel):
    """GitHub source configuration."""

    type: str  # "user_events", "repo_releases", etc.
    username: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    enabled: bool = True


class HackerNewsConfig(BaseModel):
    """Hacker News configuration."""

    enabled: bool = True
    fetch_top_stories: int = 30
    min_score: int = 100


class RSSSourceConfig(BaseModel):
    """RSS feed source configuration."""

    name: str
    url: HttpUrl
    enabled: bool = True
    category: Optional[str] = None


class RedditSubredditConfig(BaseModel):
    """Configuration for monitoring a specific subreddit."""
    subreddit: str
    enabled: bool = True
    sort: str = "hot"           # hot, new, top, rising
    time_filter: str = "day"    # hour, day, week, month, year, all (only for top/controversial)
    fetch_limit: int = 25
    min_score: int = 10


class RedditUserConfig(BaseModel):
    """Configuration for monitoring a specific Reddit user."""
    username: str               # without u/ prefix
    enabled: bool = True
    sort: str = "new"
    fetch_limit: int = 10


class RedditConfig(BaseModel):
    """Reddit source configuration."""
    enabled: bool = True
    subreddits: List[RedditSubredditConfig] = Field(default_factory=list)
    users: List[RedditUserConfig] = Field(default_factory=list)
    fetch_comments: int = 5     # top comments per post, 0 to disable


class TelegramChannelConfig(BaseModel):
    """Configuration for monitoring a specific Telegram channel."""
    channel: str            # channel username, e.g. "zaihuapd"
    enabled: bool = True
    fetch_limit: int = 20


class TelegramConfig(BaseModel):
    """Telegram source configuration."""
    enabled: bool = True
    channels: List[TelegramChannelConfig] = Field(default_factory=list)


class SourcesConfig(BaseModel):
    """All sources configuration."""

    github: List[GitHubSourceConfig] = Field(default_factory=list)
    hackernews: HackerNewsConfig = Field(default_factory=HackerNewsConfig)
    rss: List[RSSSourceConfig] = Field(default_factory=list)
    reddit: RedditConfig = Field(default_factory=RedditConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)


class EmailConfig(BaseModel):
    """Email configuration for updates/subscriptions."""
    imap_server: str
    imap_port: int = 993
    smtp_server: str
    smtp_port: int = 465
    email_address: str
    password_env: str = "EMAIL_PASSWORD"
    sender_name: str = "Horizon Daily"
    subscribe_keyword: str = "SUBSCRIBE"
    unsubscribe_keyword: str = "UNSUBSCRIBE"
    enabled: bool = False


class FilteringConfig(BaseModel):
    """Content filtering configuration."""

    ai_score_threshold: float = 7.0
    time_window_hours: int = 24


class IndustryConfig(BaseModel):
    """Industry metadata for a single pipeline run."""

    id: str = "ai-tech"
    name: str = "AI 科技"
    slug: Optional[str] = None

    def model_post_init(self, __context: Any) -> None:
        if not self.slug:
            normalized = self.id or self.name
            self.slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-") or "ai-tech"


def _default_score_bands() -> Dict[str, List[str]]:
    return {
        "9_10": [
            "行业格局变化、监管重大进展、关键产品发布、重要科研突破",
            "对行业参与者产生直接、深远影响的事件",
        ],
        "7_8": [
            "值得立即关注的重要报道、深度分析、关键产品/研究/运营变化",
            "对行业判断、业务决策、技术路线有明显参考价值",
        ],
        "5_6": [
            "增量更新、一般性教程、普通行业动态",
            "了解即可，但不一定需要优先阅读",
        ],
        "3_4": [
            "常规更新、泛泛而谈、信息量较低",
            "对目标读者帮助有限",
        ],
        "0_2": [
            "纯营销、无关内容、标题党、低质量搬运",
            "缺少事实支撑或几乎没有有效信息",
        ],
    }


class ProfileConfig(BaseModel):
    """Industry-specific scoring and enrichment guidance."""

    audience: str = "关注 AI、软件工程、开源基础设施与技术趋势的读者"
    score_bands: Dict[str, List[str]] = Field(default_factory=_default_score_bands)
    scoring_focus: List[str] = Field(
        default_factory=lambda: [
            "技术深度、原创性与信息密度",
            "对 AI、开发者生态或产业趋势的潜在影响",
            "信息源的可信度与表达质量",
            "社区讨论是否提供了额外有效信号",
        ]
    )
    downrank_if: List[str] = Field(
        default_factory=lambda: [
            "纯营销软文或缺乏事实支撑的宣传",
            "对用户和行业影响极小的琐碎更新",
            "与目标领域无关或信息密度过低的内容",
        ]
    )
    concept_focus: str = (
        "新闻中出现、但普通读者未必熟悉的技术名词、模型、协议、项目、框架、公司、产品或行业概念"
    )
    search_hints: List[str] = Field(default_factory=list)


class OutputConfig(BaseModel):
    """Output paths and publishing behavior."""

    summaries_dir: str = "data/summaries"
    docs_posts_dir: str = "docs/_posts"
    publish_to_docs: bool = True
    include_industry_in_filename: bool = False


class Config(BaseModel):
    """Main configuration model."""

    version: str = "1.0"
    ai: AIConfig
    sources: SourcesConfig
    filtering: FilteringConfig
    industry: IndustryConfig = Field(default_factory=IndustryConfig)
    profile: ProfileConfig = Field(default_factory=ProfileConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    email: Optional[EmailConfig] = None
