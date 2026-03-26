"""AI prompts for content analysis and summarization."""

from __future__ import annotations

from ..models import Config, IndustryConfig, ProfileConfig


SCORE_BAND_LABELS = {
    "9_10": "9-10 分：突破性",
    "7_8": "7-8 分：高价值",
    "5_6": "5-6 分：有一定价值",
    "3_4": "3-4 分：低优先级",
    "0_2": "0-2 分：噪音",
}


def _industry(config: Config | None) -> IndustryConfig:
    if config and getattr(config, "industry", None):
        return config.industry
    return IndustryConfig()


def _profile(config: Config | None) -> ProfileConfig:
    if config and getattr(config, "profile", None):
        return config.profile
    return ProfileConfig()


def _render_score_bands(profile: ProfileConfig) -> str:
    merged_bands = ProfileConfig().score_bands
    for key, value in (profile.score_bands or {}).items():
        if value:
            merged_bands[key] = value

    sections = []
    for key, label in SCORE_BAND_LABELS.items():
        bullet_lines = "\n".join(f"- {item}" for item in merged_bands.get(key, []))
        sections.append(f"{label}\n{bullet_lines}")

    return "\n\n".join(sections)


def build_content_analysis_system(config: Config | None = None) -> str:
    industry = _industry(config)
    profile = _profile(config)
    score_bands = _render_score_bands(profile)
    scoring_focus = "\n".join(f"- {item}" for item in profile.scoring_focus) or "- 重大变化"
    downrank = "\n".join(f"- {item}" for item in profile.downrank_if) or "- 纯噪音"

    return f"""你是一名资深的「{industry.name}」行业内容编辑，面向 {profile.audience}，负责从海量信息中筛出真正重要的内容。

请按 0-10 分对新闻的重要性进行评分：

{score_bands}

请重点关注：
{scoring_focus}

以下情况应明显降权：
{downrank}

同时考虑：
- 信息源可信度与表达质量
- 社区讨论质量：有洞见、有争议、有补充信息会提高价值
- 互动数据是否反映出社区验证过的重要性
"""


CONTENT_ANALYSIS_USER = """请分析下面这条内容，并返回 JSON：
- score (0-10): 重要性评分
- reason: 简短说明评分原因；如果提供了评论，也请考虑讨论质量
- summary: 一句话总结
- tags: 3-5 个主题标签

内容如下：
标题: {title}
来源: {source}
作者: {author}
链接: {url}
{content_section}
{discussion_section}

只返回合法 JSON：
{{
  "score": <number>,
  "reason": "<简短说明评分原因>",
  "summary": "<一句话总结>",
  "tags": ["<标签1>", "<标签2>", "..."]
}}"""


def build_concept_extraction_system(config: Config | None = None) -> str:
    industry = _industry(config)
    profile = _profile(config)

    return f"""你负责识别「{industry.name}」新闻中，读者可能不熟悉、需要补充解释的概念。
给定一条新闻，请返回 1-3 个适合搜索的查询词，用于补充背景知识。
重点关注：{profile.concept_focus}。
不要返回过于宽泛、人人都知道的常识词，也不要只返回泛泛的公司名，除非新闻的理解确实依赖某个具体子概念。
如果这条新闻本身已经足够清楚，返回空列表。"""


CONCEPT_EXTRACTION_USER = """这条新闻里有哪些概念值得补充解释？

标题: {title}
摘要: {summary}
标签: {tags}
内容: {content}

只返回合法 JSON：
{{
  "queries": ["<检索词1>", "<检索词2>"]
}}"""


def build_content_enrichment_system(config: Config | None = None) -> str:
    industry = _industry(config)
    profile = _profile(config)
    trusted_sources = "、".join(profile.search_hints) if profile.search_hints else "官方或一手来源"

    return f"""你是一名熟悉「{industry.name}」的资深分析写作者，任务是帮助读者理解重要新闻的上下文。

给定一条高分新闻、原始内容和搜索结果，请生成结构化分析。
如果搜索结果中出现 {trusted_sources} 这类来源，优先使用它们作为事实依据。

请同时输出英文和中文字段，字段名固定如下：
- title_en / title_zh
- whats_new_en / whats_new_zh
- why_it_matters_en / why_it_matters_zh
- key_details_en / key_details_zh
- background_en / background_zh
- community_discussion_en / community_discussion_zh

字段要求：
0. title：简短标题，不超过 15 个词。
1. whats_new：1-2 句，明确说明到底发生了什么、有什么变化。
2. why_it_matters：1-2 句，说明为什么重要、会影响谁、会带来什么后果。
3. key_details：1-2 句，补充重要细节、限制条件、注意点或背景信息。
4. background：2-4 句，解释理解这条新闻所需的背景知识。
5. community_discussion：1-3 句，总结评论区的主要观点、争议点或补充信息；如果没有评论可为空。

语言规则：
- 所有 *_en 字段必须用英文书写。
- 所有 *_zh 字段必须用简体中文书写。只有技术缩写、专有名词、产品名等可以保留英文原文。

其他要求：
- 除 community_discussion 在无评论时可为空外，其余字段都必须是完整句子
- 只能基于提供的内容和搜索结果，不要编造信息
- 只解释新闻标题、摘要或正文中确实出现过的概念
- 优先利用搜索结果校验近期事件和专有名词
- 如果新闻足够直白、不需要补充背景，则 background_en / background_zh 返回空字符串
- sources 字段只能填写你实际使用过、且出现在搜索结果中的 URL
"""


CONTENT_ENRICHMENT_USER = """请基于下面的新闻内容，生成结构化的双语分析。

新闻信息：
- 标题: {title}
- 链接: {url}
- 一句话摘要: {summary}
- 分数: {score}/10
- 评分理由: {reason}
- 标签: {tags}

正文：
{content}
{comments_section}

检索结果（用于事实校验与补充背景）：
{web_context}

只返回合法 JSON。字段名必须保持不变；其中 *_en 用英文，*_zh 用简体中文。除 community_discussion 在无评论时可为空外，其余字段都必须是完整句子：
{{
  "title_en": "<英文短标题，不超过15个词>",
  "title_zh": "<用中文写一个简短标题，不超过15个词>",
  "whats_new_en": "<用英文写1-2句话>",
  "whats_new_zh": "<用中文写1-2句话>",
  "why_it_matters_en": "<用英文写1-2句话>",
  "why_it_matters_zh": "<用中文写1-2句话>",
  "key_details_en": "<用英文写1-2句话>",
  "key_details_zh": "<用中文写1-2句话>",
  "background_en": "<用英文写2-4句话，或空字符串>",
  "background_zh": "<用中文写2-4句话，或空字符串>",
  "community_discussion_en": "<用英文写1-3句话，或空字符串>",
  "community_discussion_zh": "<用中文写1-3句话，或空字符串>",
  "sources": ["<检索结果中的URL>", "..."]
}}"""
