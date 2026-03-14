---
layout: default
title: "Horizon Summary: 2026-03-14 (ZH)"
date: 2026-03-14
lang: zh
---

> From 47 items, 21 important content pieces were selected

---

1. [Anthropic 发布 Claude Opus 4.6 大模型](#item-1) ⭐️ 9.0/10
2. [Claude 4.6 系列 100 万上下文正式可用](#item-2) ⭐️ 8.0/10
3. [AI 助力 Liquid 模板引擎获性能提升](#item-3) ⭐️ 8.0/10
4. [字节跳动拟海外部署 3.6 万枚 B200 芯片](#item-4) ⭐️ 8.0/10
5. [上海首例脑机接口手术获新进展](#item-5) ⭐️ 8.0/10
6. [OpenAI Sora2 视频 API 重大更新](#item-6) ⭐️ 8.0/10
7. [Google Maps 集成 Gemini AI](#item-7) ⭐️ 8.0/10
8. [Claude 1M 上下文窗口全面开放](#item-8) ⭐️ 8.0/10
9. [亚马逊与 Cerebras 合作部署 AI 推理芯片](#item-9) ⭐️ 8.0/10
10. [Hacker News 讨论 canirun.ai 本地 AI 工具](#item-10) ⭐️ 7.0/10
11. [开源 Mouser 替代 Logi Options Plus](#item-11) ⭐️ 7.0/10
12. [卡塔尔氦气停产威胁芯片供应链](#item-12) ⭐️ 7.0/10
13. [Hammerspoon v2 将从 Lua 切换至 JS](#item-13) ⭐️ 7.0/10
14. [Meta 因性能落后推迟 Avocado 模型发布](#item-14) ⭐️ 7.0/10
15. [支付宝 DeepLink 被指可致信息泄露](#item-15) ⭐️ 7.0/10
16. [马斯克 xAI 架构失误将推倒重构](#item-16) ⭐️ 7.0/10
17. [格力自研 AI 芯片出货量破 800 万颗](#item-17) ⭐️ 7.0/10
18. [Meta 推迟 Llama4 发布至 5 月](#item-18) ⭐️ 7.0/10
19. [美团推出 AI 搜索产品问小团](#item-19) ⭐️ 7.0/10
20. [绿联 MiniMax 推 NAS 原生大模型服务](#item-20) ⭐️ 7.0/10
21. [马斯克宣布推出数字擎天柱 AI 项目](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 4.6 大模型](https://t.me/zaihuapd/40251) ⭐️ 9.0/10

AI 开发商 Anthropic 推出了更新后的 Claude Opus 4.6 大语言模型，带来多项重大能力升级。新模型默认具备 200K 上下文窗口（测试版支持 100 万 token），最大输出 token 数相比前代翻倍至 128K，新增自适应思考模式和自动上下文压缩功能，可支持近乎无限长度的对话。 这是 Anthropic 旗舰前沿大语言模型的一次重大更新，提升了长上下文处理和复杂推理能力，既增强了 Anthropic 在高端大模型市场的竞争力，也推动了整个行业对长上下文 AI 技术的发展。本次升级能直接让处理长文档、长对话和复杂任务的终端用户与开发者受益。 新增的自适应思考模式可根据问题复杂度动态调整推理深度，并新增了最高级的 max effort 参数，允许用户在回答完整度和 token 使用效率之间进行权衡。自动上下文压缩功能会在对话接近窗口限制时自动总结早期内容，在保留核心信息的同时避免上下文溢出。

telegram · zaihuapd · Mar 14, 01:19

**背景**: 大语言模型（LLM）是在海量文本语料上训练得到的 AI 系统，能够生成类人文本并完成各类语言任务。模型的上下文窗口指模型生成回答时，能够处理和参考的最大输入文本量，单位为 token。Anthropic 推出的 effort 参数允许用户控制模型生成回答时投入的计算量，调整结果质量和 token 成本之间的平衡。长上下文能力是当前顶尖大语言模型的核心竞争维度，因为它支持需要处理大量连续文本的更高级场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://colab.research.google.com/github/ashishpatel26/context_engineering/blob/main/context_engineering/3_compress_context.ipynb">3_ compress _ context .ipynb - Colab</a></li>
<li><a href="https://docs.litellm.ai/docs/providers/anthropic_effort">Anthropic Effort Parameter | liteLLM</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Model Release`, `#Claude Opus`, `#Anthropic`, `#Long Context AI`

---

<a id="item-2"></a>
## [Claude 4.6 系列 100 万上下文正式可用](https://claude.com/blog/1m-context-ga) ⭐️ 8.0/10

Anthropic 宣布，Claude Opus 4.6 和 Claude Sonnet 4.6 大语言模型的 100 万 token 上下文窗口现已正式可用。本次更新还将媒体处理上限提升至 600 张图片或 PDF 页面，且不对长上下文使用收取额外溢价。 本次更新消除了长上下文处理的定价壁垒，为需要处理大文档、维持长对话会话的开发者和 AI 代理用户带来了重大利好。它还通过低价策略冲击了其他对大上下文访问收取额外费用的竞品，加剧了高端大语言模型市场的竞争。 Claude Code 已将基础版 Opus 和支持 1M 上下文的 Opus 合并为同一个模型入口，早期用户测试未发现旧版 Claude 常见的、在接近 1M token 上限时性能大幅下降的问题。1M 上下文功能目前仅对 Anthropic Max+计划用户开放，Pro 计划用户仍会遇到原有上下文限制。

hackernews · meetpateltech · Mar 13, 17:19

**背景**: 上下文窗口是大语言模型单次请求可处理的最大内容量，以 token 为单位衡量，平均 1000 个 token 约等于 750 个单词，提示词、对话历史和模型输出都需要容纳在窗口内。AI 代理是能够在长交互中完成复杂多步骤任务的自主人工智能系统，这类应用需要大上下文窗口来保留历史信息，维持稳定性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devtk.ai/en/blog/llm-context-window-explained/">LLM Context Windows Explained: 4K to 1M Tokens (2026)</a></li>
<li><a href="https://ailunex.com/blog/large-language-models-understanding-context-windows-and-tokens">LLM Context Windows: 4K to 1M Tokens Explained 2025</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_agent">Intelligent agent - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 大多数 Hacker News 评论者对本次更新持积极态度，许多人指出无额外溢价的定价对于在 Claude Code 上进行长时编码工作来说是重大改变。用户普遍关心的开放问题包括 1M 上下文窗口实际可用的大小是多少、接近上限时性能下降幅度有多大，以及长会话会如何影响 token 预算消耗。有一位评论者认为本次更新是 Anthropic 针对 OpenAI GPT 5.4 收费 1M 上下文功能做出的竞争回应。

**标签**: `#Large Language Models`, `#Claude AI`, `#Context Window`, `#AI Agents`

---

<a id="item-3"></a>
## [AI 助力 Liquid 模板引擎获性能提升](https://simonwillison.net/2026/Mar/13/liquid/#atom-everything) ⭐️ 8.0/10

Shopify 首席执行官 Tobias Lütke 利用 Andrej Karpathy 的 AI 驱动 autoresearch 系统，为开源 Liquid Ruby 模板引擎找到了数百项性能优化，最终实现解析加渲染速度提升 53%、内存分配减少 61%。最终生成的合并请求包含 93 次提交，来自 AI 编码代理开展的约 120 次自动化实验。 这项工作展示了新兴 AI 辅助自动化开发技术一个极具吸引力的实际应用场景，证明 AI 可以为已经经过人类开发者数十年优化的成熟代码库带来大幅改进。它也凸显了完善的现有测试套件如何为安全高效的 AI 驱动代码优化提供基础。 整体性能提升来自数十项小型微优化，包括将 StringScanner 分词器替换为`String#byteindex`（仅这一项就减少了 12%的解析时间）、标签解析使用手动字节扫描、以及预缓存小整数的字符串转换以减少不必要的分配。所有变更都通过 Liquid 项目现有 974 个单元测试的验证。

rss · Simon Willison · Mar 13, 03:44

**背景**: Liquid 是 Shopify 于 2005 年创建的开源 Ruby 模板语言，被广泛用于构建灵活的面向客户网页应用。Autoresearch 是 Andrej Karpathy 推出的新型开源 AI 系统，它允许 AI 代理自动运行数百次半自主代码实验，识别出有效的改进方案。Nanochat 是 Karpathy 开发的最小化开源全栈管线，用于训练和运行类似 ChatGPT 的小型大语言模型，是一个面向 LLM 学习的教育项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai">Andrej Karpathy's new open source 'autoresearch' lets you run ...</a></li>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can buy. · GitHub</a></li>
<li><a href="https://shopify.github.io/liquid/">Documentation for the Liquid template language, created by Shopify.</a></li>

</ul>
</details>

**标签**: `#Performance Optimization`, `#AI-Assisted Development`, `#Open Source`, `#Liquid Template Engine`, `#Ruby`

---

<a id="item-4"></a>
## [字节跳动拟海外部署 3.6 万枚 B200 芯片](https://www.wsj.com/tech/chinas-bytedance-gets-access-to-top-nvidia-ai-chips-d68bce3a) ⭐️ 8.0/10

据《华尔街日报》3 月 13 日报道，字节跳动计划与东南亚云服务商 Aolani Cloud 合作，在马来西亚部署总计 3.6 万枚英伟达 B200 AI 芯片。该项目总硬件投入预计超过 250 亿美元，这批算力将用于支持字节跳动的海外 AI 研发，满足全球 AI 服务需求。 这次尖端 AI 芯片的大规模部署是字节跳动全球 AI 基础设施的重大扩张，将大幅提升其 AI 研发能力，同时重塑全球 AI 行业的竞争格局。 3.6 万枚 B200 芯片将被配置为约 500 套英伟达 Blackwell 计算系统，合作方 Aolani Cloud 是东南亚专注 AI 领域的云基础设施服务商，主打高性能 GPU 云服务。

telegram · zaihuapd · Mar 13, 08:45

**背景**: 英伟达 B200 是基于英伟达 Blackwell 微架构的新一代数据中心 AI 加速芯片，由英伟达在 2024 年 3 月正式发布。它专为大模型训练、微调、推理等端到端 AI 工作负载提供高性能算力支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.aolanicloud.com/">AOLANI</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing">NVIDIA Blackwell Platform Arrives to Power a New Era of Computing | NVIDIA Newsroom</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#ByteDance`, `#Nvidia B200`, `#AI R&D`, `#semiconductor industry`

---

<a id="item-5"></a>
## [上海首例脑机接口手术获新进展](https://t.me/zaihuapd/40242) ⭐️ 8.0/10

复旦大学附属华山医院完成了上海首例临床脑机接口手术，帮助瘫痪四年的患者实现了意念控制喝水。团队在世界脑机接口联合会议上披露了这一进展，明确新型术中功能定位技术大幅缩短了手术时长。 这是脑机接口转化研究领域具有高影响力的重要临床进展，证明改良手术技术能够帮助长期瘫痪患者恢复运动功能。它推动了植入式脑机接口技术针对神经损伤导致重度运动障碍患者的临床转化进程。 植入的脑机接口装置大小如一枚硬币，放置在患者颅骨外以采集大脑感觉运动区域的神经信号，整套系统还配套了可由患者解码后脑电信号控制的外置手套。本例患者四年前因车祸导致颈椎错位，进而瘫痪。

telegram · zaihuapd · Mar 13, 09:30

**背景**: 植入式脑机接口是一种记录解码大脑神经信号、将人类意念转化为外部设备动作的技术，目前被广泛研究用于帮助瘫痪患者恢复运动功能。术中功能定位是帮助手术过程中精准定位目标脑区的技术，有助于缩短手术时间、提升手术精准度。全球已有多个研究团队在针对瘫痪患者的运动功能恢复临床试验中初步验证了植入式脑机接口的有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/33770760/">Novel intraoperative online functional mapping of somatosensory...</a></li>
<li><a href="https://neuralink.com/">Neuralink — Pioneering Brain Computer Interfaces</a></li>
<li><a href="https://spj.science.org/doi/10.34133/cbsystems.0044">Neural Decoding for Intracortical Brain–Computer Interfaces</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#medical technology`, `#clinical neurosurgery`, `#translational research`

---

<a id="item-6"></a>
## [OpenAI Sora2 视频 API 重大更新](https://developers.openai.com/api/docs/guides/video-generation) ⭐️ 8.0/10

OpenAI 近日为基于 Sora2 模型的 Sora 视频生成 API 推送了重大更新，新增五项核心能力升级，解决了批量视频生产中的一致性、时长和多格式适配痛点。更新内容包括跨场景角色一致性、20 秒最长时长、横竖屏双输出、视频延伸和增强批量处理。 本次更新推出了市场高度期待的功能，解决了规模化商业视频生产的核心痛点，对 AI 开发者和内容创作者来说都是重要进展。它推动生成式 AI 视频进一步适配多平台大规模商用的实际需求。 为实现跨场景角色一致性，开发者可以预先上传或定义包含外观、服装、配件信息的角色档案，模型会在生成多个片段时自动复用该参考，避免视觉漂移。视频时长上限从此前的 12-16 秒提升至 20 秒，一次生成任务即可输出两种分辨率的横竖屏素材，无需二次裁剪或重渲染。

telegram · AI_News_CN · Mar 13, 07:05

**背景**: Sora 是 OpenAI 推出的前沿生成式 AI 视频模型，能够根据自然语言提示或图像输入生成细节丰富的动态视频片段。在本次更新前，生成式视频 API 普遍存在多场景角色特征不一致、片段时长短、适配不同平台宽高比需要额外工作量等问题。OpenAI 的 Batch API 专为处理大规模生成请求设计，符合专业工作室工作流和自动化内容生产的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/video-generation">Video generation with Sora | OpenAI API</a></li>
<li><a href="https://openai.com/index/sora-2/">Sora 2 is here | OpenAI</a></li>
<li><a href="https://www.vo3ai.com/blog/openai-opens-sora-2-video-api-to-all-developers-what-this-means-for-ai-filmmakin-2026-03-13">OpenAI Sora 2 Video API Now Open to All Developers</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Video Generation`, `#OpenAI Sora`, `#API Updates`

---

<a id="item-7"></a>
## [Google Maps 集成 Gemini AI](https://www.solidot.org/story?sid=83757) ⭐️ 8.0/10

谷歌已将自家 Gemini 大语言模型集成到 Google Maps 中，新增了两款 AI 驱动功能：支持对话交互的 Ask Maps 和升级后的 3D 沉浸式导航。这些新功能将首先向 Android 和 iOS 平台用户推出。 这是谷歌 Gemini 生成式 AI 面向消费者的一次重大集成，落地到全球最常用的日常应用之一，推动了生成式 AI 在日常消费工具中的主流普及。它将为全球数十亿 Google Maps 用户带来更直观、更具交互性的使用体验。 由 Gemini 驱动的 Ask Maps 功能允许用户直接在 Google Maps 应用内通过自然对话交互规划行程、询问出行相关问题并优化出行建议。全新 3D 沉浸式导航利用街景和航拍图像数据，渲染出精确详细的立交桥、人行横道、地标和路标的 3D 视觉效果，提供更直观的路线引导。

telegram · AI_News_CN · Mar 13, 10:15

**背景**: Gemini 是谷歌推出的多模态大语言模型系列，能够处理和生成文本、图像、音频、代码、视频等多种类型的数据。Google Maps 是全球最受欢迎的消费者地图导航服务，在全球拥有数十亿月活用户。最新的 Gemini 2.0 Flash 模型支持原生多模态处理，非常适合集成到 Google Maps 这类对视觉要求高的服务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>
<li><a href="https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/">Ask Maps and Immersive Navigation: New AI features in Google Maps</a></li>
<li><a href="https://9to5google.com/2026/03/12/google-maps-immersive-navigation/">‘Immersive Navigation’ is the biggest Google Maps driving update in a decade</a></li>

</ul>
</details>

**标签**: `#Gemini AI`, `#Google Maps`, `#AI integration`, `#generative AI`, `#navigation technology`

---

<a id="item-8"></a>
## [Claude 1M 上下文窗口全面开放](https://telegra.ph/Claude-1M%E4%B8%8A%E4%B8%8B%E6%96%87%E7%AA%97%E5%8F%A3%E5%85%A8%E9%9D%A2%E5%BC%80%E6%94%BE-%E5%AE%9A%E4%BB%B7%E7%BB%9F%E4%B8%80%E5%AA%92%E4%BD%93%E9%85%8D%E9%A2%9D%E5%A4%A7%E5%B9%85%E6%8F%90%E5%8D%87-03-13-2) ⭐️ 8.0/10

截至 2025 年 3 月 13 日，Anthropic 已向所有用户全面开放 Claude 的 1M-token 上下文窗口，实行统一定价并大幅提升了媒体使用配额。 这一调整让广受欢迎的 Claude 大语言模型中备受追捧的 1M-token 大上下文能力面向所有 AI 开发者和普通用户开放可用。它推动了生成式 AI 领域扩大上下文窗口尺寸的行业趋势，解锁了更多高级使用场景。 此前 Claude 的 1M-token 上下文窗口仅对第 4 层级组织和拥有自定义速率限制的团队开放测试。本次更新统一了所有用户群体的定价，并大幅提高了媒体客户的使用上限。

telegram · AI_News_CN · Mar 13, 19:53

**背景**: Claude 是 AI 公司 Anthropic 开发的生成式预训练大语言模型系列，通过人类反馈强化学习和宪法 AI 微调来遵循伦理准则。上下文窗口定义了大语言模型生成输出时能够处理和参考的最大输入文本量，1M-token 的上下文窗口大约可容纳 75 万字，足够在单个提示词中处理整本书籍或完整代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/context-windows">Context windows - Claude API Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Claude`, `#Generative AI`, `#AI Announcement`

---

<a id="item-9"></a>
## [亚马逊与 Cerebras 合作部署 AI 推理芯片](https://api3.cls.cn/share/article/2312801?sv=8.5.9) ⭐️ 8.0/10

本周五亚马逊与 Cerebras Systems 宣布达成新合作协议，将在 AWS 数据中心内部署 Cerebras AI 推理芯片，并搭配亚马逊 Trainium3 AI 芯片，为各类加速型生成式 AI 应用提供算力支持。今年早些时候，Cerebras 已经与 OpenAI 签署了价值 100 亿美元的芯片供应协议。 这项合作扩展了 AWS 的生成式 AI 基础设施服务，强化了对英伟达全球 AI 芯片市场主导地位的竞争，同时也能让 AWS 的全球客户获得速度更快、容量更高的 AI 推理能力，用于聊天机器人、编程助手等常见 AI 工具。 这套整合方案将优化推理预填充处理的 Trainium3，与优化解码处理的 Cerebras CS-3 芯片结合，可实现每秒 3000 tokens 的推理速度，高速推理容量比现有方案高出 5 倍。新服务将在未来几个月内通过 Amazon Bedrock 推出，芯片通过亚马逊定制网络技术实现互联。

telegram · AI_News_CN · Mar 13, 23:03

**背景**: AI 推理是预训练好的生成式 AI 模型响应用户请求生成输出的过程，低延迟的高速推理对保障交互式 AI 应用的流畅用户体验至关重要。AWS 是亚马逊旗下的云计算部门，是全球最大的云服务提供商，为企业客户提供各类 AI 基础设施与服务。Cerebras Systems 是一家高估值 AI 芯片初创企业，它研发和英伟达旗舰产品不同的专用芯片，以此参与 AI 加速芯片市场的竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/cerebras-is-coming-to-aws">Cerebras is coming to AWS</a></li>
<li><a href="https://www.aboutamazon.com/news/aws/aws-cerebras-ai-inference">AWS and Cerebras collaboration aims to set a new standard for ...</a></li>
<li><a href="https://www.wsj.com/tech/amazon-announces-inference-chips-deal-with-cerebras-109ecd31">Amazon Announces Inference Chips Deal With Cerebras</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#cloud computing`, `#AI inference`, `#AI infrastructure`, `#Amazon AWS`

---

<a id="item-10"></a>
## [Hacker News 讨论 canirun.ai 本地 AI 工具](https://www.canirun.ai/) ⭐️ 7.0/10

一个高参与度的热门 Hacker News 讨论串正在讨论 canirun.ai 工具，该工具可在用户下载模型前检测本地硬件能否运行 AI 大语言模型。社区贡献者分享了实用运行技巧、实验经验，还对该工具的内存需求估算进行了修正。 随着开源大语言模型本地运行在开发者和注重隐私的用户中越来越普及，该工具可以帮助用户避免浪费时间下载不兼容的大模型文件。社区汇总的集体经验也降低了新手入门本地 AI 的门槛。 社区用户指出 canirun.ai 的内存估算存在误导性：它标注 4 位量化的 Llama 3.1 8B 仅需 4.1GB 内存，而原始未量化模型的权重就超过了 16GB。该工具的估算方法适用于稠密模型，但没有考虑混合专家（MoE）模型不同的性能特性。

hackernews · ricardbejarano · Mar 13, 12:46

**背景**: 本地大语言模型（local LLM）指完全运行在用户自有本地硬件、而非远程云端服务器的大语言模型。和云端大语言模型服务相比，本地运行 LLM 拥有更好的数据隐私性和离线可用性。canirun.ai 是一款免费工具，旨在帮助用户在下载体积庞大的 LLM 文件前提前检测硬件兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PythonicVarun/canirun">GitHub - PythonicVarun/canirun: A lightweight CLI to ...</a></li>
<li><a href="https://www.sigmabrowser.com/blog/what-local-llms-really-are-and-how-they-work">What Local LLMs Really Are and How They Work</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 大多数贡献者在指出 canirun.ai 缺陷、分享实用见解的同时，也肯定了该工具背后的开发尝试。一名经验丰富的用户分享了自己两年本地 LLM 实验得出的经验，指出 Qwen 3.5 9B 这类小模型非常适合本地嵌入式用例。许多用户表示，目前仍缺乏明确指南帮助用户根据硬件匹配满足特定速度和上下文窗口要求的大语言模型，对此他们感到困扰。

**标签**: `#local ai`, `#large language models`, `#developer tools`, `#community discussion`

---

<a id="item-11"></a>
## [开源 Mouser 替代 Logi Options Plus](https://github.com/TomBadash/MouseControl) ⭐️ 7.0/10

开源项目 Mouser 的一位贡献者推出了这款工具，作为罗技专有软件 Logi Options Plus 的免费开源替代品，解决了官方软件常见的高 CPU 占用和不必要遥测收集问题。 该项目为罗技鼠标用户提供了一个轻量、注重隐私的臃肿官方软件替代方案，满足了对专有输入设备配置工具的糟糕性能和隐私问题感到不满的用户需求。 人们观察到官方 Logi Options Plus 更新程序在英特尔芯片 MacBook Pro 上会占用 40%到 60%的 CPU，这促使开发者寻找替代方案，Mouser 项目目前托管在 GitHub 上，正在招募更多开源贡献者。

hackernews · avionics-guy · Mar 13, 18:42

**背景**: Logi Options Plus 是罗技官方推出的专有软件，用于自定义旗下鼠标和键盘的按键映射、滚动速度和其他偏好设置。长期以来，许多用户都抱怨这款官方软件充斥不必要功能、资源占用过高，还会收集不必要的使用遥测数据，引发隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hn.nuxt.dev/item/47368033">Nuxt HN | Mouser : An open source alternative to Logi-Plus mouse ...</a></li>
<li><a href="https://www.logitech.com/en-us/software/logi-options-plus">Logi Options+ Software | Logitech</a></li>

</ul>
</details>

**社区讨论**: 大多数社区成员都认可 Logi Options Plus 质量差、问题多，并分享了适用于 macOS、Linux 等不同平台的多款替代鼠标配置工具。评论者普遍青睐开源方案的隐私性和透明度，许多人都分享了自己经过测试的个人推荐。

**标签**: `#open source`, `#utility software`, `#privacy`, `#macOS`, `#input devices`

---

<a id="item-12"></a>
## [卡塔尔氦气停产威胁芯片供应链](https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock) ⭐️ 7.0/10

卡塔尔即将暂停氦气生产，这一事件在 Hacker News 引发了高赞的大规模讨论，话题围绕其对全球半导体供应链的潜在影响，同时涉及美国战略储备、通胀以及更广泛的大宗商品供应问题。 氦气是半导体生产中不可替代的原材料，因此突发供应中断可能引发生产延误和价格上涨，影响将波及整个全球科技行业。这一事件也凸显了支撑关键科技领域的战略大宗商品供应存在系统性风险。 此次停产让全球芯片供应链仅有约两周时间来适应氦气供应减少，美国已根据 2013 年《氦气管理法案》在 2024 年完成了对国家战略氦储备的全部撤资。由于独特的低温和导热特性，氦气在半导体制造的晶圆冷却环节目前没有可行的商业替代方案。

hackernews · johnbarron · Mar 13, 12:31

**背景**: 氦气是一种化学惰性的稀有气体，拥有出色的导热性和低温特性，因此是半导体制造多个核心工序必不可少的原材料。美国曾保有全球最大的战略氦储备，为依赖氦气的关键产业提供供应缓冲。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.innovationnewsnetwork.com/why-helium-is-essential-to-the-future-of-semiconductor-manufacturing/64493/">Why helium is essential to the future of semiconductor manufacturing</a></li>
<li><a href="https://www.idtechex.com/en/research-article/helium-conservation-needed-to-support-a-growing-semiconductor-industry/31674">Helium Conservation Needed to Support a Growing Semiconductor Industry | IDTechEx Research Article</a></li>
<li><a href="https://en.wikipedia.org/wiki/National_Helium_Reserve">National Helium Reserve - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区参与者提出了一系列相关担忧，许多人谈到多种大宗商品普遍涨价，并对官方通胀数据提出质疑。一名用户指出美国卖掉战略氦储备、如今却持有战略比特币储备这一讽刺现象，还有用户提问为什么不能用储量更丰富的氩气等其他稀有气体替代氦气。

**标签**: `#semiconductor supply chain`, `#helium`, `#supply chain risk`, `#tech industry`

---

<a id="item-13"></a>
## [Hammerspoon v2 将从 Lua 切换至 JS](https://github.com/Hammerspoon/hammerspoon) ⭐️ 7.0/10

在开源 Mac 自动化工具 Hammerspoon 的高热度 Hacker News 讨论中，项目维护者宣布即将推出的 v2 版本将把脚本语言从 Lua 切换为 JavaScript，用户同时分享了实际用例和第三方扩展。 切换到 JavaScript 将让 Hammerspoon 面向更多已经掌握 JavaScript 的开发者开放，有望扩大该工具的用户群，同时为这个开源项目带来更多未来社区贡献。 Hammerspoon 当前稳定版是 macOS 系统 API 和 Lua 脚本引擎之间的桥梁，所有自定义自动化配置都用 Lua 编写，而 v2 的重写目前正处于积极开发阶段。

hackernews · tosh · Mar 13, 18:34

**背景**: Hammerspoon 是一款热门开源 macOS 桌面自动化工具，允许用户编写自定义脚本来自动化 macOS 工作流的几乎任何部分。它是从最小化自动化工具 Mjolnir 分叉而来，目的是为用户提供更集成、开箱即用的友好体验。迄今为止所有版本的 Hammerspoon 都使用 Lua 作为用户配置的默认脚本语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Hammerspoon/hammerspoon">GitHub - Hammerspoon/hammerspoon: Staggeringly powerful macOS desktop automation with Lua · GitHub</a></li>
<li><a href="http://www.hammerspoon.org/">Hammerspoon</a></li>
<li><a href="https://aibit.im/blog/post/hammerspoon-automate-macos-via-lua-an-open-source-power-tool">Hammerspoon: Automate macOS via Lua – an Open‑Source Power Tool</a></li>

</ul>
</details>

**社区讨论**: 大多数社区参与者都分享了对 Hammerspoon 的正面体验，许多人表示他们依赖该工具完成日常核心生产力工作流，包括自定义窗口平铺、自定义快捷键、导出标签页到笔记应用、个人活动追踪等。多名用户还分享了自己为 Hammerspoon 开发的自定义第三方扩展和工具集。

**标签**: `#macOS automation`, `#open source`, `#developer tools`, `#Hammerspoon`

---

<a id="item-14"></a>
## [Meta 因性能落后推迟 Avocado 模型发布](https://www.reuters.com/technology/meta-delays-rollout-new-ai-model-nyt-reports-2026-03-12/) ⭐️ 7.0/10

在投入数十亿美元研发数个月后，Meta 仍因性能落后于竞品，将代号为 Avocado 的新型大 AI 模型原定于 3 月的发布时间推迟到了 5 月之后，Meta 计划在 2026 年投入 1150 亿至 1350 亿美元用于 AI 研发。 此次推迟发布凸显了全球顶级科技公司在大模型领域竞争的白热化程度，体现出新 AI 模型发布的性能门槛已经大幅提升，也表明当前 AI 赛道中保持竞争力需要投入极高的资本成本。 据透露，Avocado 当前的性能介于谷歌 Gemini 2.5 和 Gemini 3 之间，尚未达到 Meta 的发布标准，而 Meta 发言人表示公司相信新模型最终会展现出快速发展轨迹，对其发布充满信心。

telegram · zaihuapd · Mar 13, 05:55

**背景**: 基础大模型是现代生成式 AI 产品的核心底层技术，各大顶级科技公司都在竞相研发性能更强的模型以抢占市场份额。谷歌已于 2026 年 1 月发布最新旗舰模型 Gemini 3，创下了新的行业性能标杆。作为全球头部科技巨头，Meta 近年一直在大举投入 AI 研发，希望追赶大模型领域的领先者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/03/12/technology/meta-avocado-ai-model-delayed.html">Meta Delays Rollout of New A.I. Model After Performance ...</a></li>
<li><a href="https://www.reuters.com/technology/meta-delays-rollout-new-ai-model-nyt-reports-2026-03-12/">Meta pushes AI model 'Avocado' rollout to May or later, NYT ...</a></li>
<li><a href="https://blog.google/products-and-platforms/products/gemini/gemini-3/">Gemini 3: Introducing the latest Gemini AI model from Google</a></li>

</ul>
</details>

**标签**: `#large AI models`, `#AI competition`, `#Meta`, `#generative AI`

---

<a id="item-15"></a>
## [支付宝 DeepLink 被指可致信息泄露](https://innora.ai/zfb/) ⭐️ 7.0/10

安全研究机构 Innora AI 发布报告称，支付宝 v10.8.26.7000 和 v10.8.30.8000 两个版本存在 DeepLink 与 WebView JSBridge 结合的可利用攻击链，可让外部页面获取用户敏感隐私信息。研究团队按负责任披露流程提交问题后，蚂蚁集团在 2026 年 3 月回应称相关能力属于正常功能，发布方附带的编辑注也指出该研究主张可能存在夸大。 支付宝是全球拥有数亿活跃用户的最常用移动支付应用之一，如果报告中的隐私漏洞被确认可利用，将导致大量用户个人信息面临高泄露风险。这一事件也引发了行业对多数混合移动应用使用的 JSBridge 架构普遍存在的潜在安全风险的关注。 该攻击需要用户主动点击恶意链接才会触发，报告指出 iOS 端有 18 个敏感 API 可被调用，安卓端则有 13 个，其中包含位置获取和支付相关接口。根据编辑注，原报告仅明确展示了获取用户定位权限和触发直达支付弹窗这两个影响。

telegram · zaihuapd · Mar 13, 11:43

**背景**: DeepLink 是一项移动技术，允许用户点击链接后直接打开应用内的特定页面，而非被重定向到应用主页或外部浏览器。JSBridge 是混合移动应用开发中常用的通信机制，它实现了运行在应用内置 WebView 组件中的 JavaScript 代码与应用原生代码之间的双向通信。该机制让托管在应用内的网页内容可以访问普通网页无法使用的原生应用能力和 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mobile_deep_linking">Mobile deep linking - Wikipedia</a></li>
<li><a href="https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges">WebView – Native bridges | Security | Android Developers</a></li>
<li><a href="https://javascript.plainenglish.io/what-is-jsbridge-f72f3c0987f1">What is JSBridge. What are its advantages and… | by Brandon Evans | JavaScript in Plain English</a></li>

</ul>
</details>

**标签**: `#mobile security`, `#vulnerability disclosure`, `#jsbridge`, `#alipay`

---

<a id="item-16"></a>
## [马斯克 xAI 架构失误将推倒重构](https://futurism.com/artificial-intelligence/elon-musk-screwed-up-xai-rebuilding) ⭐️ 7.0/10

埃隆·马斯克于 3 月 13 日证实，他的人工智能初创公司 xAI 原始核心架构设计错误，将从零开始进行全面重构。截至公告发布时，xAI 最初 12 名联合创始人中已有 9 人离职，公司正采取措施应对人才流失并调整投资结构。 作为一家参与全球生成式 AI 市场竞争的高知名度 AI 初创公司，这一重大挫折将放缓 xAI 的开发进度，重塑当前 AI 行业的竞争格局。这一事件也凸显了初创企业从零构建前沿大模型面临的高风险和不确定性。 离职的联合创始人包括近期宣布辞职的 xAI 图像生成产品负责人张国栋。为填补人才缺口，马斯克从 AI 编程初创公司 Cursor 聘请了两名资深员工，同时重新联系此前被拒绝的候选人；特斯拉已获准将其持有的 xAI 投资转换为 SpaceX 的少量股权，SpaceX 预计将于今年晚些时候以 1.25 万亿美元的估值上市。

telegram · zaihuapd · Mar 14, 02:21

**背景**: xAI 是埃隆·马斯克于 2023 年 3 月创立的人工智能初创公司，创立初衷是应对马斯克所称现有生成式 AI 模型中的政治正确和自由派偏见问题。该公司最知名的产品是 Grok 系列大语言模型，已集成到马斯克的社交媒体平台 X，由 xAI 自研的 Colossus 超级计算机提供算力支持。Cursor 是一家快速增长的 AI 编程工具初创公司，近期获得了高额融资，也得到了英伟达 CEO 黄仁勋等行业领袖的认可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">xAI (company) - Wikipedia</a></li>
<li><a href="https://builtin.com/artificial-intelligence/what-is-xai">What Is xAI? The Company Behind Grok | Built In</a></li>
<li><a href="https://cursor.com/">Cursor : The best way to code with AI</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#xAI`, `#Startup News`, `#AI Industry`

---

<a id="item-17"></a>
## [格力自研 AI 芯片出货量破 800 万颗](https://www.aibase.com/zh/news/26205) ⭐️ 7.0/10

在 3 月 12 日举办的 AWE 2026 展会上，中国家电巨头格力电器宣布，其自研的 EAi AI 芯片累计出货量已突破 800 万颗，工业级 MCU 芯片出货量逼近 2 亿颗。这些新型芯片将赋能新一代智能家电，实现主动 AI 服务而非仅响应用户指令。 这一里程碑证实格力已成功实现消费级 AI 芯片和工业级 MCU 的大规模量产，解决了企业面临的潜在供应链风险，也推动其向主动式 AI 智能家居生态转型。它同时也是中国家电行业自主半导体发展的一项关键突破。 EAi 系列 AI 芯片结合了高性能 AI 算力与嵌入式 MCU 的低功耗、易用性特性，支持 HMI、智能视觉和智能语音功能，可应用于智能家居、工业、医疗等多类场景。格力在展会上推出了多款搭载 EAi 芯片的家电新品，同时展示了其在工业制品和智能装备领域的技术成果。

telegram · AI_News_CN · Mar 13, 08:03

**背景**: 格力六年前启动了自研芯片项目，该项目长期以来一直受到业内争议。微控制单元（MCU）是一种紧凑型集成电路，用于管控从家电到工业设备各类嵌入式设备的特定运行功能。工业级 MCU 相比消费级产品能够承受更恶劣的运行环境，因此适用于工业自动化等性能要求更高的应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/26205">Shipment Exceeds 8 Million Units! Dong Mingzhu's Chip ...</a></li>
<li><a href="https://inf.news/en/tech/283690e0d825456dd142b36bb6c28d67.html">Gree has been "making chips" for 6 years: cumulative ...</a></li>
<li><a href="https://www.reuters.com/technology/chinas-gree-can-now-make-its-own-chips-local-media-reports-2024-12-16/">China's Gree can now make its own chips, local media reports</a></li>

</ul>
</details>

**标签**: `#self-developed chips`, `#AI smart home`, `#semiconductor industry`, `#supply chain security`

---

<a id="item-18"></a>
## [Meta 推迟 Llama4 发布至 5 月](https://www.aibase.com/zh/news/26207) ⭐️ 7.0/10

由于在性能微调与逻辑推理优化过程中遇到技术挑战，Meta 已将其新一代开源大语言模型 Llama4 的发布时间推迟至今年 5 月。Meta 确认仍将坚持开源 Llama4 战略，该模型将推出多个不同参数规模的版本，以满足不同场景的部署需求。 这一动态反映出开发高性能顶级大语言模型的难度正在不断提升，此次推迟也会影响 Meta 在全球 AI 竞赛中相对 OpenAI、谷歌等对手的竞争位置。Llama4 的发布是会影响整个开源 AI 生态、改变全球 AI 开发者和研究者工作节奏的重大事件。 Meta 正利用推迟带来的额外时间对 Llama4 开展更深度的安全压力测试，该模型在多模态理解和长文本处理能力方面的整体研发进度仍符合预期。Llama4 通过推出多个参数规模版本，可支持从移动端设备到企业级服务器的全场景部署需求。

telegram · AI_News_CN · Mar 13, 08:41

**背景**: Llama4 是 Meta AI 开发的新一代开源大语言模型系列，定位为 Meta 核心人工智能战略的基石。对于大语言模型而言，不同的参数规模对应不同的能力等级和算力需求，因此不同版本可以适配不同的部署场景。性能微调是模型训练完成后的优化流程，用于提升模型的推理能力、输出质量以及对用户需求的适配性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hub.researchgraph.org/what-is-llama-4/">What is Llama 4? - hub.researchgraph.org</a></li>
<li><a href="https://web.dev/articles/llm-sizes">Understand LLM sizes | web.dev</a></li>
<li><a href="https://www.geeksforgeeks.org/deep-learning/fine-tuning-large-language-model-llm/">Fine Tuning Large Language Model (LLM) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Meta`, `#Llama4`, `#open source AI`, `#AI industry`

---

<a id="item-19"></a>
## [美团推出 AI 搜索产品问小团](https://www.aibase.com/zh/news/26208) ⭐️ 7.0/10

在 3 月 13 日举办的美团 2026 年管理层沟通会上，CEO 王兴提出物理世界数字化是 AI 落地的核心战略底座，并宣布美团已于 2026 年春节期间推出面向本地生活的 AI 搜索产品“问小团”，推进其 AI Agent 战略落地。 这一来自头部本地生活科技企业的战略发布，反映了大模型竞争正从通用智能转向深度融合真实物理世界信息的行业专属应用这一核心新兴趋势，有望影响整个本地生活服务科技领域的 AI 发展与竞争方向。 “问小团”基于美团覆盖全国的本地生活信息基建打造，美团自 2025 年起就显著加大了对该领域基建的投入，先后推出多款 AI 应用和自研大模型。王兴强调，单纯的通用智力提升无法填补餐厅位次等物理世界场景的即时信息缺口，因此物理世界数字化是 AI 落地应用必不可少的基础。

telegram · AI_News_CN · Mar 13, 08:41

**背景**: 美团是中国领先的本地生活服务科技巨头，从 2023 年开始布局扩展 AI 业务，当年收购了一家 AI 初创公司，后续又推出了多个自研大语言模型。AI Agent 是一种能够感知环境、代表用户自主完成任务以实现目标的 AI 系统，通常以大语言模型为核心驱动。问小团是专门为处理复杂本地生活服务查询打造的 AI 搜索助手，可以直接将推荐结果对接用户交易环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meituan">Meituan - Wikipedia</a></li>
<li><a href="https://pandaily.com/meituan-launches-ask-xiaotuan-ai-search-bringing-the-local-services-battle-into-the-ai-era">Meituan Launches “Ask Xiaotuan” AI Search, Bringing the Local Services Battle Into the AI Era - Pandaily</a></li>

</ul>
</details>

**标签**: `#AI Product Launch`, `#Meituan`, `#AI Agent`, `#Physical World Digitalization`

---

<a id="item-20"></a>
## [绿联 MiniMax 推 NAS 原生大模型服务](https://www.aibase.com/zh/news/26211) ⭐️ 7.0/10

中国 NAS 厂商绿联与国内 AI 公司 MiniMax 达成深度战略合作，推出业内首款面向消费级 NAS 的原生内嵌大模型服务。用户只需在绿联私有云一键安装，就能获得开箱即用的私有 AI 助手。 这次整合消除了此前劝退非技术用户的复杂手动配置流程，是面向 C 端的本地 AI 落地的重要一步。它也推动消费级 NAS 从单纯的数据存储库进化为个人家庭智脑。 该服务通过绿联 UGOS Pro 系统上的 OpenClaw 龙虾应用提供，首发支持绿联 DXP 系列及即将上市的 iDX 系列 NAS 设备。从发布日到 2026 年 4 月 12 日，所有用户可享受 30 天内置大模型全功能免费使用权，大模型支持文档总结、创意写作、智能问答等功能。

telegram · AI_News_CN · Mar 13, 09:55

**背景**: 网络附加存储（NAS）是一种私有本地存储设备，和公有云存储不同，它让用户完全掌控自己的个人数据。在个人 NAS 上运行大语言模型可以让用户在使用 AI 服务的同时不向第三方平台分享隐私数据，但过去这需要复杂的技术配置，多数非技术用户无法实现。UGOS Pro 是绿专为自家 NAS 设备开发的基于 Linux 的专有操作系统，MiniMax 则是中国领先的开发高性能大语言模型的人工智能企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nas.ugreen.com/pages/solution-software">UGOS PRO System Applications - Ugreen NAS</a></li>
<li><a href="https://github.com/MiniMax-AI/MiniMax-01">GitHub - MiniMax-AI/MiniMax-01: The official repo of MiniMax ...</a></li>
<li><a href="https://openclaws.io/">OpenClaw | The AI That Actually Does Things</a></li>

</ul>
</details>

**标签**: `#Network-Attached Storage (NAS)`, `#Large Language Model`, `#Private AI`, `#Consumer AI`, `#Product Integration`

---

<a id="item-21"></a>
## [马斯克宣布推出数字擎天柱 AI 项目](https://www.cnbeta.com.tw/articles/tech/1553384.htm) ⭐️ 7.0/10

埃隆·马斯克宣布，其旗下 xAI 与特斯拉将联合开发名为数字擎天柱（又称 Macrohard/巨硬）的新项目。该项目旨在打造可独立运行整家公司的自主 AI 数字员工，依托特斯拉自研 AI4 芯片运行，该芯片单颗售价 650 美元，功耗仅为英伟达 H100 的四分之一。 这个备受关注的雄心勃勃的项目有望降低全球 AI 行业对昂贵英伟达 AI 硬件的高度依赖，同时推动可处理端到端企业工作的自主 AI 智能体发展。它有可能重塑 AI 硬件市场和企业自动化行业格局。 数字擎天柱由 xAI 的 Grok 大语言模型提供核心动力，该模型赋予其强大推理能力，可自动化所有依赖键盘、鼠标和屏幕操作的计算机工作流程。该项目仅少量采用英伟达硬件，大部分工作负载由特斯拉自研 AI4 芯片承担。

telegram · AI_News_CN · Mar 13, 12:32

**背景**: xAI 是埃隆·马斯克创立的独立人工智能初创公司，于 2023 年 11 月推出了基于自研大语言模型的生成式 AI 聊天机器人 Grok。特斯拉近期向 xAI 注资 20 亿美元，数字擎天柱是双方达成投资合作后首个重大联合项目。特斯拉在面向自动驾驶的自研 AI 芯片领域拥有多年研发经验，而可独立完成完整工作任务的自主 AI 智能体是当前 AI 行业增长最快的发展方向之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/autos-transportation/musk-unveils-joint-tesla-xai-project-macrohard-eyes-software-disruption-2026-03-11/">Musk unveils joint Tesla-xAI project 'Macrohard', eyes ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://www.notateslaapp.com/news/3777/tesla-announces-joint-digital-optimus-project-with-xai">Tesla Announces Joint 'Digital Optimus' Project With xAI ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Large Language Models`, `#AI Hardware`, `#Tesla`, `#xAI`

---