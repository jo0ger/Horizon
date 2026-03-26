---
layout: default
title: "Horizon Summary: 2026-03-26 (ZH)"
date: 2026-03-26
lang: zh
---

> From 54 items, 24 important content pieces were selected

---

1. [Swift 6.3 正式发布 支持原生 Android 开发](#item-1) ⭐️ 9.0/10
2. [Apifox 桌面端遭供应链投毒攻击](#item-2) ⭐️ 9.0/10
3. [中国计算机学会抵制 NeurIPS 投稿限制政策](#item-3) ⭐️ 9.0/10
4. [苹果谷歌合作，Gemini 支持 Siri AI](#item-4) ⭐️ 9.0/10
5. [AI2 发布全开源视觉驱动 MolmoWeb 网络代理](#item-5) ⭐️ 9.0/10
6. [GitHub 将用 Copilot 用户数据训练 AI](#item-6) ⭐️ 9.0/10
7. [DeepMind 发布 Lyria 3 Pro AI 音乐模型](#item-7) ⭐️ 9.0/10
8. [Hacker News 热议 ARC-AGI-3 基准](#item-8) ⭐️ 8.0/10
9. [最高法院在考克斯音乐版权案中胜诉](#item-9) ⭐️ 8.0/10
10. [遭入侵 LiteLLM 在 PyPI 被下载近 4.7 万次](#item-10) ⭐️ 8.0/10
11. [谷歌推出 TurboQuant 压缩大模型 KV 缓存](#item-11) ⭐️ 8.0/10
12. [英特尔 AMD 延长中国客户服务器 CPU 交付期](#item-12) ⭐️ 8.0/10
13. [特朗普组建科技领袖 AI 政策顾问委员会](#item-13) ⭐️ 8.0/10
14. [苹果蒸馏谷歌 Gemini 实现 iPhone 端侧 AI](#item-14) ⭐️ 8.0/10
15. [黑客用报废车零件在桌面运行 Model 3 电脑](#item-15) ⭐️ 7.0/10
16. [黑客社区讨论欧盟推送聊天监控法案](#item-16) ⭐️ 7.0/10
17. [对 AI 代理代码生成赶工的批评](#item-17) ⭐️ 7.0/10
18. [NASA 调整阿耳忒弥斯计划，暂停 Gateway 建月基地](#item-18) ⭐️ 7.0/10
19. [AI 短剧冲击横店 群演集体失业](#item-19) ⭐️ 7.0/10
20. [Sora 停摆后快手可灵冲击收入翻倍](#item-20) ⭐️ 7.0/10
21. [高德开放平台发布适配 OpenClaw 的技能](#item-21) ⭐️ 7.0/10
22. [通义千问落地红旗量产智能座舱](#item-22) ⭐️ 7.0/10
23. [OpenAI 投资 AI 智能体初创公司 Isara](#item-23) ⭐️ 7.0/10
24. [Apifox 公网 SaaS 版 JS 被篡改安全公告](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Swift 6.3 正式发布 支持原生 Android 开发](https://swift.org/blog/swift-6.3-released/) ⭐️ 9.0/10

Swift 6.3 于 2026 年 3 月 25 日正式发布，首次推出官方 Android 版 Swift SDK。开发者现在可以使用 Swift 编写原生 Android 程序，也可以通过 Swift Java 插件将 Swift 代码集成到现有的 Kotlin/Java Android 项目中。 本次发布标志着 Swift 在跨平台开发领域取得了重大里程碑，它允许开发者在苹果平台和 Android 之间共享同一套代码库，无需维护多套独立原生代码。它将 Swift 的使用场景扩展到了苹果生态之外，为跨平台原生应用开发提供了新的选择。 官方 Android 版 Swift SDK 包含了为 Android 目标生成和运行 Swift 代码所需的全部库、头文件和其他资源，而 Swift Java 插件可以通过将 Java 类封装为对应的 Swift 类型，让 Swift 代码调用现有的 Java/Kotlin API。根据 2025 年预发布版本测试时的反馈，Android 社区开发者指出目前 Swift 覆盖的 Android API 仍然有限。

telegram · zaihuapd · Mar 25, 03:45

**背景**: Swift 是由苹果公司最初开发的通用编程语言，主要用于 iOS、macOS 等苹果平台开发，自推出后已经完全开源。在本次正式发布之前，自 2025 年 10 月起就已经向开发者提供 Android 版 Swift SDK 的实验性夜间构建版本，供测试和移植工作使用。跨平台开发允许开发者用共享代码构建可在多个操作系统上运行的应用，降低整体开发和维护的工作量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swift.org/documentation/articles/swift-sdk-for-android-getting-started.html">Getting Started with the Swift SDK for Android | Swift.org</a></li>
<li><a href="https://www.swift.org/blog/nightly-swift-sdk-for-android/">Announcing the Swift SDK for Android | Swift.org</a></li>
<li><a href="https://github.com/swiftlang/swift-java">GitHub - swiftlang/swift-java: Java interopability support for Swift · GitHub</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 安卓开发者社区对预览版 SDK 的讨论中，部分开发者担忧 Swift 目前提供的 Android API 支持仍然十分有限，而且面对 Jetpack Compose 这类官方 Android API 的快速迭代，Swift 的支持很可能会滞后。skip.tools 这类第三方工具已经基于该 SDK 构建了额外功能，通过桥接到 Jetpack Compose 帮助开发者将 SwiftUI 应用移植到 Android。

**标签**: `#Swift`, `#cross-platform development`, `#Android development`, `#programming language release`

---

<a id="item-2"></a>
## [Apifox 桌面端遭供应链投毒攻击](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 9.0/10

攻击者篡改了 Apifox 桌面端存放在 CDN 的统计脚本，注入恶意代码窃取 SSH 密钥与 Git 凭证等开发者敏感信息，该攻击自 3 月 4 日起开始活跃，影响 Windows、macOS 和 Linux 全平台用户。安全研究者 phith0n 已经独立还原了恶意载荷并公开了分析代码，Apifox 官方已在最新版本中移除了该恶意脚本。 这次攻击是一起影响广泛的供应链安全事件，针对一款常用的 API 开发工具，致使大量开发者的核心敏感 credentials 面临极高的泄露风险。它也凸显了桌面应用依赖的第三方 CDN 资源被篡改后带来的严峻安全威胁。 用户可通过检查本地 Apifox 的 Network Persistent State 文件或 LevelDB 数据库中是否包含 apifox.it.com 等可疑域名来确认是否受影响，缓解措施包括通过防火墙或 DNS 封禁可疑域名，以及重新安装最新版 Apifox。截至消息披露时，Apifox 官方尚未就该事件发布正式声明。

telegram · zaihuapd · Mar 25, 11:10

**背景**: Apifox 是一款流行的一体化 API 开发协作平台，整合了 Postman、Swagger、Mock 和 JMeter 等工具的功能，被大量开发者使用。供应链投毒攻击是一种复杂网络攻击，攻击者会入侵软件分发链中可信任的第三方组件来注入恶意代码，而 CDN 即内容分发网络，是常用于托管和分发软件静态脚本与资源的服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apifox">Apifox · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://www.idmanagement.gov/experiments/cdns/paper2/">CDN Attack Vectors and Mitigation - IDManagement</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#cybersecurity`, `#software security`, `#credential theft`

---

<a id="item-3"></a>
## [中国计算机学会抵制 NeurIPS 投稿限制政策](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 9.0/10

中国计算机学会于 2026 年 3 月 25 日发表官方声明，反对 NeurIPS 2026 禁止受美国制裁机构投稿的新政策。该学会呼吁中国学者抵制本次会议，并威胁若政策不撤回就会将 NeurIPS 移出中国计算机学会推荐国际学术会议和期刊目录。 这是全球顶尖人工智能学术会议日益政治化以来，学界做出的最强烈的机构回应之一，它可能会显著改变这一极具影响力的领域顶会的参与格局，对计算机和人工智能领域的国际学术交流产生深远影响。 中国计算机学会的声明明确呼吁中国计算机领域的科研人员拒绝为 NeurIPS 提供任何学术服务，也拒绝向该会议投稿，而将 NeurIPS 移出推荐目录的措施仅会在 NeurIPS 不撤回政策的情况下生效。

telegram · zaihuapd · Mar 25, 14:07

**背景**: NeurIPS 全称神经信息处理系统大会，是与 ICML、ICML 并列的人工智能与机器学习领域三大最具影响力的年度顶级学术会议之一。中国计算机学会推荐国际学术会议和期刊目录是中国学界广泛参考的排名，会影响很多中国计算机领域科研人员的学术评价、职称评审和研究生毕业要求。不受政治干预、开放包容的学术交流是全球学界广泛认可的核心准则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeurIPS">NeurIPS</a></li>
<li><a href="https://ccf.atom.im/">中国计算机学会推荐国际学术会议和期刊目录（2026）</a></li>

</ul>
</details>

**标签**: `#AI research`, `#academic conferences`, `# NeurIPS`, `#academic policy`, `#scholarly exchange`

---

<a id="item-4"></a>
## [苹果谷歌合作，Gemini 支持 Siri AI](https://t.me/zaihuapd/40506) ⭐️ 9.0/10

苹果和谷歌宣布达成多年合作，谷歌的 Gemini 模型与云技术将为苹果今年推出的全新 AI 功能提供支持，其中包括更个性化的 Siri。苹果将维持现有的隐私标准，所有 AI 计算都运行在设备端或私有云上。 这次合作将重塑全球 AI 助手市场，打破全球两大科技公司之间长期的竞争格局。它将直接提升长期在生成式功能上落后于对手的 Siri 的 AI 能力，为 iPhone 用户带来更智能的助手体验。 苹果下一代 Apple Foundation Models 将基于谷歌 Gemini 技术构建，为全新 Siri 功能提供支持。苹果仍保留对自身隐私框架的控制权，用户数据不会因和谷歌的合作受到损害。

telegram · zaihuapd · Mar 25, 16:32

**背景**: Gemini 是谷歌最新的生成式大语言模型系列，其中 Gemini 3 是目前谷歌能力最强的版本，支持先进的推理任务。Apple Foundation Models 是苹果的端侧大语言模型框架，为苹果设备的 AI 功能 Apple Intelligence 提供支持。端侧 AI 指直接运行在用户本地硬件而非外部云服务器的 AI 计算，这种方式有助于提升响应速度并保护用户隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/">Gemini 3 — Google DeepMind</a></li>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>
<li><a href="https://www.articsledge.com/post/on-device-ai">What Is On-Device AI? How It Works in 2026 - articsledge.com</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#apple`, `#google`, `# Gemini`, `#siri`

---

<a id="item-5"></a>
## [AI2 发布全开源视觉驱动 MolmoWeb 网络代理](https://www.aibase.com/zh/news/26564) ⭐️ 9.0/10

艾伦人工智能研究所（AI2）发布了全开源的视觉驱动网络代理 MolmoWeb，该代理仅依靠浏览器截图就能做出导航决策。AI2 同时还发布了目前规模最大的开放网页导航数据集 MolmoWebMix，包含人类标注与合成导航数据。 这次发布改变了网络代理依赖网页 DOM 结构的开发范式，实现了更鲁棒的网页自动化，可在绝大多数网站上正常运行，不受底层代码变动的影响。它以较小模型规模实现了优秀性能，且采用完全开放许可，也推动了网络代理研究的普及化，挑战了大型科技公司的数据垄断。 8B 参数版本的 MolmoWeb 在 WebVoyager 基准测试中得分达到 78.2%，接近 OpenAI 闭源模型 o3 的 79.3%，还在 UI 元素定位任务中超过了 Anthropic 的 Claude 3.7；通过多次运行任务筛选最优结果可将成功率提升至 94.7%。模型和数据集已在 GitHub 和 Hugging Face 以宽松的 Apache 2.0 协议开放，但它目前仍在处理复杂指令、登录验证和法律合规方面存在挑战。

telegram · AI_News_CN · Mar 26, 01:28

**背景**: 传统网络代理依赖访问网页的底层代码结构文档对象模型（DOM）来识别元素并做出决策。当网站更新时，DOM 结构经常发生变化，会导致传统代理无法正常工作，而且并非所有网络平台都开放 DOM 访问权限。视觉驱动的设计让代理像人类一样通过视觉观察网页来运作，而不需要解析原始代码，因此具备更强的通用性。WebVoyager 是一项标准基准测试，用于衡量网络代理在各类常用网站上完成真实导航任务的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allenai.org/blog/molmoweb">MolmoWeb: An open agent for automating web tasks | Ai2</a></li>
<li><a href="https://www.researchgate.net/publication/384207409_WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models">WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | Request PDF</a></li>
<li><a href="https://arxiv.org/html/2401.13919v3">WebVoyager : Building an End-to-End Web Agent with Large...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open-source AI`, `#web automation`, `#computer vision`, `#machine learning`

---

<a id="item-6"></a>
## [GitHub 将用 Copilot 用户数据训练 AI](https://www.aibase.com/zh/news/26566) ⭐️ 9.0/10

GitHub 宣布从 2026 年 4 月 24 日起，将默认使用 Copilot 免费版、Pro 版和 Pro+版用户的交互数据训练 AI 模型，采用用户可手动在隐私设置中关闭的选择退出机制，Cop 商业版、企业版和教育版用户暂不受此变更影响。 这一政策变动影响数百万开发者，引发了关于数据隐私、知识产权归属和私有代码定义的关键争议，标志着在公开高质量代码数据逐渐枯竭的背景下，头部 AI 企业转向挖掘私有用户交互数据提升模型性能的行业大趋势，也体现了 GitHub 从开源代码托管平台向闭环 AI 训练生态的重大战略转向。 本次采集的数据涵盖模型输入输出、代码片段、上下文信息、仓库结构、聊天记录、光标上下文、注释文档、文件名和用户对代码建议的反馈，数据可共享给包括微软在内的关联公司，但不会提供给第三方 AI 服务商，该政策采用默认启用、用户主动退出的机制，这是引发社区争议的核心点。

telegram · AI_News_CN · Mar 26, 01:45

**背景**: GitHub Copilot 是 GitHub 与 OpenAI 合作开发的 AI 代码助手，可根据现有代码上下文为开发者自动生成代码建议，此前该模型一直依赖公开代码仓库中的训练数据提升性能。生成式 AI 模型的性能高度依赖训练数据的规模和质量，而 AI 训练的数据合规性近年来已经成为全球范围内核心的行业和监管议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oschina.net/news/290253/github-copilot-workspace">GitHub 发布 AI 原生开发工具 GitHub Copilot Workspace - OSCHINA - 中文开源技术交流社区</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1888887013358404123">AI大模型训练数据合规法律风险及应对 - 知乎</a></li>
<li><a href="https://blog.csdn.net/w605283073/article/details/141014372">浅析 GitHub Copilot 工作原理帮你更高效使用-CSDN博客</a></li>

</ul>
</details>

**社区讨论**: 这一政策变动已经在开发者社区引发广泛讨论，多数讨论围绕 GitHub 默认将用户的私有代码片段和仓库数据用于 AI 训练是否合理，以及该政策如何重新定义传统私有仓库的概念展开。

**标签**: `#GitHub Copilot`, `#AI policy`, `#data privacy`, `#software development`

---

<a id="item-7"></a>
## [DeepMind 发布 Lyria 3 Pro AI 音乐模型](https://www.aibase.com/zh/news/26569) ⭐️ 9.0/10

谷歌 DeepMind 发布了先进 AI 音乐生成模型 Lyria 3 Pro，该模型能够根据文本提示生成完整结构化的全长高保真歌曲，将 AI 音乐生成的能力从 30 秒的短片段提升到了全新水平。该模型可以独立创作包含前奏、主歌、副歌、桥段等标准结构的完整歌曲。 这是音频生成式 AI 的一次重大飞跃，将 AI 音乐工具从辅助创作工具推向了能够自主完成全曲创作的阶段，有望重塑整个数字音乐生产行业。它为内容创作者带来了更高效低成本的音乐创作方案，同时也推动人类音乐人将创作重心转向更深层次的情感表达与艺术定义。 Lyria 3 Pro 支持 24-bit 高保真音频输出，满足专业音频制作的基础要求，并且依托谷歌多模态技术，允许用户直接通过描述风格、情绪、节奏的自然文本来生成歌曲。该模型目前也已接入谷歌 Gemini 应用，可用于为各类内容项目创建自定义音轨。

telegram · AI_News_CN · Mar 26, 02:02

**背景**: 在 Lyria 3 Pro 推出之前，大多数现有的 AI 音乐生成模型只能创作 30 秒左右的短旋律片段，无法生成结构完整的全长歌曲。谷歌 DeepMind 在 2025 年 2 月推出了 Lyria 3 的初版，随后在 AI 音乐赛道加快了开发迭代，仅数月后就推出了这个升级 Pro 版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/lyria-3-pro/">Lyria 3 Pro: Create longer tracks in more Google products</a></li>
<li><a href="https://workspaceupdates.googleblog.com/2026/03/create-longer-musical-tracks-in-gemini-app-with-Lyria-3-Pro.html">Create longer musical tracks in the Gemini app with Lyria 3 Pro</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#AI music`, `#DeepMind`, `#large language model`, `#audio generation`

---

<a id="item-8"></a>
## [Hacker News 热议 ARC-AGI-3 基准](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

ARC Prize 团队公开发布了 ARC-AGI-3 基准测试及配套技术报告，在 Hacker News 上引发了高参与度的批判性讨论。讨论焦点包括基准测试人类基线方法的缺陷，以及 ARC 挑战能否真正测量通用智能。 作为最受关注的通用人工智能进度测量公开基准之一，围绕 ARC-AGI-3 设计的争议会影响研究人员评估下一代 AI 系统、衡量 AGI 发展进度的方式。这场讨论也凸显了 AI 领域内部在如何定义和测试通用智能方面长期存在的分歧。 批评者指出，ARC-AGI-3 将人类基线定义为自愿报名解谜的参与者中表现第二好的首次测试成绩，而非采用具有代表性样本的人类平均得分。该基准以每关的操作效率为核心评分指标，批评者称它没有清晰报告模型完整通过了多少挑战关卡。

hackernews · lairv · Mar 25, 18:16

**背景**: ARC-AGI 是一个知名的 AI 基准测试，旨在测量机器对全新未知问题的推理、抽象和泛化能力，这些能力被认为是通用人工智能的核心特质。ARC Prize 是一项奖金超百万美元的非营利公开竞赛，要求参赛者开发能够通过 ARC-AGI 测试的开源解决方案。包括 ARC-AGI-2 在内的前身版本于 2025 年之前发布，相比早期版本进行了升级，以规避记忆训练数据、过拟合等常见基准测试问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>
<li><a href="https://spectrum.ieee.org/arc-prize-agi-test">ARC Prize Challenge: AI's Struggle With Simple Puzzles - IEEE ...</a></li>
<li><a href="https://www.adaline.ai/blog/what-is-the-arc-agi-benchmark-and-its-significance-in-evaluating-llm-capabilities-in-2025">What is the ARC AGI Benchmark and its significance in... | Adaline</a></li>

</ul>
</details>

**社区讨论**: 大多数评论者对该基准提出批评，部分人认为它无法真正测量通用智能，因为测试表现在很大程度上取决于解谜经验，并非所有人类都具备这类经验。社区对 ARC-AGI 测量智能的思路是否合理也存在分歧，有人用“飞机不需要像鸟类振翅也能飞”的观点支持该测试的合理性，而支持者认为让人类和 AI 解决同样问题，是评估智能的公平方式。

**标签**: `#AGI`, `#AI Benchmarking`, `#ARC Challenge`, `#AI Evaluation`

---

<a id="item-9"></a>
## [最高法院在考克斯音乐版权案中胜诉](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html) ⭐️ 8.0/10

2026 年 3 月，美国最高法院在音乐版权侵权诉讼中裁定互联网服务提供商考克斯通信胜诉，该案由各大唱片公司提起，针对考克斯的用户分享盗版音乐的行为追究考克斯的责任。最高法院推翻了此前认定考克斯负有侵权责任的陪审团裁决。 这一标志性裁决重塑了美国互联网服务提供商第三方版权责任的规则，确立了重要先例，减轻了要求 ISP 全面监控用户在线活动的压力。它将影响版权方、互联网中介机构和普通网民在线隐私之间的权力平衡。 最高法院的多数意见援引了 1984 年索尼 Betamax 案，该案已经确立《版权法》不会自动要求第三方服务提供商为用户实施的侵权行为承担责任。唱片方此前主张，考克斯从用户的盗版行为中获利，且未采取足够行动制止侵权。

hackernews · oj2828 · Mar 25, 15:02

**背景**: 根据美国版权法，只要满足处理侵权活动的相关要求，互联网服务提供商长期以来受《数字千年版权法》的避风港条款保护，无需为用户的侵权行为承担次级责任。本案的核心争议点是，当避风港保护不适用时，ISP 是否仍会因为未能遏制用户的大规模盗版行为而被认定为直接承担责任。

**社区讨论**: 大多数 Hacker News 评论者对裁决反应积极，称赞这是一场小小的胜利，它减少了促使 ISP 监控用户在线活动的动机。部分评论者使用类比梳理裁决的逻辑，也有评论者批评现行的现代版权制度过于严苛且有害。还有一名评论者指出，本次裁决合理援引了更早的 Betamax 版权案先例。

**标签**: `#copyright law`, `#internet policy`, `#supreme court`, `#internet service provider`

---

<a id="item-10"></a>
## [遭入侵 LiteLLM 在 PyPI 被下载近 4.7 万次](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 8.0/10

Daniel Hnyk 分析发现，遭篡改的 LiteLLM 版本 1.82.7 和 1.82.8 在 PyPI 上线的 46 分钟内被下载了 46996 次，且 88%依赖该库的包都未固定版本，因此容易受到攻击。 这起事件暴露了 Python AI 供应链中普遍存在的依赖版本固定风险，会影响成千上万使用 LiteLLM 连接多种大语言模型的开发者和机构。 本次分析借助记录 PyPI 官方下载统计数据的公开 BigQuery PyPI 数据集完成，这两个恶意版本被下架前仅在 PyPI 上线不到一小时。

rss · Simon Willison · Mar 25, 17:21

**背景**: LiteLLM 是一款流行的开源 Python 库，它提供统一接口来访问来自不同服务商的 100 多种大语言模型。PyPI 是 Python 编程语言的官方公共软件包仓库。版本固定是指为依赖项指定精确版本的开发实践，可以避免自动安装未经验证或恶意的新版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://stackoverflow.com/questions/28509481/should-i-pin-my-python-dependencies-versions">Should I pin my Python dependencies versions? - Stack Overflow</a></li>
<li><a href="https://docs.pypi.org/api/bigquery/">BigQuery Datasets - PyPI Docs</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#pypi`, `#software packaging`, `#llm`

---

<a id="item-11"></a>
## [谷歌推出 TurboQuant 压缩大模型 KV 缓存](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) ⭐️ 8.0/10

谷歌研究院推出了向量量化算法 TurboQuant，该算法无需对模型进行重新训练或微调，就能将大语言模型的 KV 缓存压缩至 3 比特。该方法可实现最高 6 倍的内存缩减，在 H100 GPU 上注意力计算速度最高提升 8 倍，同时保持原模型性能不变。 这一进展解决了大语言模型长上下文推理过程中，KV 缓存体积增长带来的关键内存瓶颈，让消费级和数据中心硬件都能高效部署更长的上下文窗口。它的性能优于现有量化方法，在不牺牲准确率的前提下拓展了可实现的压缩水平边界。 TurboQuant 将于 ICLR 2026 展示，另外两款相关压缩方法 QJL 和 PolarQuant 将于 AISTATS 2026 展示。在高维向量搜索任务中，TurboQuant 的召回率也优于现有方法 PQ 和 RabbiQ。

telegram · zaihuapd · Mar 25, 05:15

**背景**: KV 缓存是一种在大语言模型推理过程中存储中间键、值计算结果来加速文本生成的技术，但它的体积会随上下文长度和批次大小线性增长，给长上下文推理带来严重的内存瓶颈。向量量化是经典的有损压缩技术，它将相似的高维向量分组，用一个原型向量代表整个分组，从而减少存储数据集所需的总内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant : Redefining AI efficiency with extreme compression</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vector_quantization">Vector quantization</a></li>

</ul>
</details>

**标签**: `#large language models`, `#model quantization`, `#KV cache compression`, `#AI efficiency`

---

<a id="item-12"></a>
## [英特尔 AMD 延长中国客户服务器 CPU 交付期](https://t.me/zaihuapd/40507) ⭐️ 8.0/10

路透社报道，英特尔和 AMD 已通知中国客户，受供应紧张影响服务器 CPU 交付周期将延长。英特尔对其在中国销售的第四代、第五代至强（Xeon）处理器实施限量供货，同时将服务器产品整体涨价超 10%，而 AMD 部分产品的交付周期也被拉长至 8 到 10 周。 这一事件会影响全球半导体供应链以及中国国内云计算和人工智能基础设施的部署，将直接影响国内硬件采购的成本和供货可得性。由人工智能需求拉动的服务器 CPU 短缺也反映出全球人工智能基础设施投资热潮正在重塑半导体市场格局。 英特尔将供应紧张归因于人工智能的快速普及带动了需求增长，该公司预计其库存将在 2026 年第一季度降至最低点，当年第二季度开始改善。对中国客户而言，英特尔部分服务器 CPU 型号的交付周期目前最长已达到 6 个月。

telegram · zaihuapd · Mar 26, 00:03

**背景**: 服务器 CPU 是专门为服务器硬件设计的处理器，负责为云平台、数据中心以及人工智能模型的训练和推理提供计算资源和服务。第四代和第五代英特尔至强是英特尔最新推出的服务器级 CPU，广泛应用于全球各地的企业数据中心和人工智能基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon/5th-gen-xeon-scalable-processors.html">5th Gen Intel® Xeon® Processors – Intel</a></li>
<li><a href="https://en.wikipedia.org/wiki/Server_(computing)">Server (computing)</a></li>
<li><a href="https://www.serversimply.com/blog/intels-5th-generation-vs-4th-generation-xeon-cpus-advancements-and-integrations">Intel Xeon 4th Gen Vs 5th Gen Scalable Processors | Server Simply</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply chain`, `#server CPU`, `#hardware industry`

---

<a id="item-13"></a>
## [特朗普组建科技领袖 AI 政策顾问委员会](https://www.aibase.com/zh/news/26565) ⭐️ 8.0/10

美国前总统唐纳德·特朗普计划组建名为 PCAST 的 AI 政策顾问委员会，首批 13 名成员包括黄仁勋、马克·扎克伯格和谢尔盖·布林等顶级科技领袖。该委员会将围绕放松监管、维持全球 AI 领导地位、经济影响和国家安全为美国 AI 战略提供白宫咨询建议。 该委员会汇聚了全球 AI 行业最具影响力的人物直接参与制定美国国家 AI 政策，其政策建议很可能对全球 AI 发展、监管趋势和国际 AI 竞争力产生深远影响。这一动向标志着美国 AI 政策将向更贴近产业的方向转变，优先降低创新面临的监管壁垒。 首批 13 名成员覆盖了 AI 硬件基础设施、互联网应用和企业技术等领域，该委员会由白宫 AI 与加密货币事务官员大卫·萨克斯共同主持。其核心工作重点还包括应对 AI 对美国劳动力市场带来的影响。

telegram · AI_News_CN · Mar 26, 01:45

**背景**: PCAST 全称是美国总统科学技术顾问委员会，是一个起源于 1933 年的长期存在的美国官方顾问机构。它的职责是汇聚顶尖科技专家，就紧迫的全国性科技相关问题直接向美国总统提供政策建议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/President's_Council_of_Advisors_on_Science_and_Technology">President's Council of Advisors on Science and Technology - Wikipedia</a></li>
<li><a href="https://kyma.com/decision-2024/national-politics/2026/03/25/president-trump-appoints-first-members-of-pcast/">President Trump appoints first members of PCAST - KYMA</a></li>
<li><a href="https://obamawhitehouse.archives.gov/administration/eop/ostp/pcast/about">About PCAST | The White House</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#artificial intelligence`, `#regulation`, `#technology policy`, `#U.S. politics`

---

<a id="item-14"></a>
## [苹果蒸馏谷歌 Gemini 实现 iPhone 端侧 AI](https://www.aibase.com/zh/news/26568) ⭐️ 8.0/10

根据 2026 年 3 月 25 日披露的消息，苹果通过深度合作协议获得了谷歌全量 Gemini 模型的完整访问权限，并使用知识蒸馏技术将 Gemini 的能力迁移到可在 iPhone 本地运行的轻量小型模型中。该蒸馏模型将在未来的 iOS 更新中用于优化 Siri 等 iOS 原生 AI 应用。 这一布局将移动 AI 竞争的重心从云端参数规模竞赛转向端侧执行效率，能为移动端用户在前沿 AI 能力、更高隐私保障和更快响应速度之间实现平衡，同时也为利用第三方大模型加速端侧 AI 落地开创了新先例。 苹果采取了短期借力蒸馏 Gemini 快速升级端侧 AI、长期继续独立自研 Apple Foundation Models 掌握 AI 自主权的双重战略。经过蒸馏的小型模型在保持接近全量 Gemini 性能的同时，只需要低得多的算力就可以本地运行。

telegram · AI_News_CN · Mar 26, 02:02

**背景**: 知识蒸馏是一种 AI 模型压缩技术，遵循教师-学生框架：大型高性能的教师模型将学到的知识迁移给更小的学生模型，让小模型以小得多的体积保留原模型的大部分能力。端侧 AI 指直接在手机这类终端用户硬件上运行的 AI 计算，不需要将数据发送到云端服务器处理，因此能提供更快的响应速度和更好的用户隐私保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/weixin_43694096/article/details/127505946">一文搞懂【知识蒸馏】【Knowledge Distillation】算法原理_知识蒸馏算... 让小模型也能深度思考：推理知识蒸馏（Knowledge Distillation for Re... 知识蒸馏_百度百科 知识蒸馏原理分类方法及Hinton经典算法解读-开发者社区-阿里云 知识蒸馏研究综述 - ict.ac.cn 【AI系统】知识蒸馏原理 - ZOMI酱酱 - 博客园</a></li>
<li><a href="https://ssshooter.com/kitten-large-language-model-6/">小猫都能懂的 大 模 型 原 理 6 - 模 型 优化 • Usubeni Fantasy</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1935796159261148086">知识蒸馏（Knowledge Distillation）：一篇从核心原理到前沿应用的完...</a></li>

</ul>
</details>

**标签**: `#On-device AI`, `#Knowledge Distillation`, `#Large Language Model`, `#Apple`, `#Gemini`

---

<a id="item-15"></a>
## [黑客用报废车零件在桌面运行 Model 3 电脑](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 7.0/10

一篇 2026 年 3 月 23 日发布的技术博客详细介绍了一名研究者如何逆向工程，并使用从事故报废特斯拉车辆上回收的零件，在桌面成功启动了特斯拉 Model 3 的车机电脑。该项目在 Hacker News 上引发了超过 120 条社区讨论，内容覆盖汽车电子等相关话题。 该项目拓展了公众对特斯拉汽车软硬件的公开认知，推动了开放逆向工程工作，有助于提升汽车 cybersecurity 研究水平，也能让售后改装更加 accessible。它还让大众开始关注特斯拉针对 root 权限研究的漏洞赏金计划架构。 特斯拉在漏洞赏金计划中为研究者提供个人车辆的永久 SSH root 证书，只要研究者提交至少一个有效的 root 漏洞即可获得，该机制类似苹果的安全研究设备计划。已有社区成员表示，只要有对应固件，就能在 QEMU 模拟器中运行特斯拉基于 Qt 开发的 QtCar 界面软件。

hackernews · driesdep · Mar 25, 21:11

**背景**: 汽车电子逆向工程指拆解并研究车辆内部计算机系统的运行原理，是汽车安全研究和售后车辆改装领域的核心工作。特斯拉在 Bugcrowd 平台运营公开漏洞赏金计划，向报告其系统有效安全漏洞的安全研究者提供奖金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bugcrowd.com/tesla">Bug Bounty: Tesla | Bugcrowd</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Model_3">Tesla Model 3 - Wikipedia</a></li>
<li><a href="https://undercodetesting.com/unlock-hardware-hacking-secrets-free-uart-course-essential-tool-guide-video/">Unlock Hardware Hacking Secrets: Free UART... - Undercode Testing</a></li>

</ul>
</details>

**社区讨论**: 社区评论者认为特斯拉的 root 权限资质项目很有意思，指出该项目类似苹果的项目，在开放研究和管控访问权限之间取得了不错的平衡。多名评论者分享了自身的相关经历，包括离线测试 ECU、改装特斯拉，以及指出 LVDS 这类通用硬件接口的跨场景应用。

**标签**: `#reverse engineering`, `#automotive electronics`, `#Tesla`, `#hardware hacking`

---

<a id="item-16"></a>
## [黑客社区讨论欧盟推送聊天监控法案](https://fightchatcontrol.eu/?foo=bar) ⭐️ 7.0/10

欧盟正在持续推进允许扫描用户私人消息和照片的新立法，这在 Hacker News 引发了高参与度讨论，其中包括反对该法案的倡导运动 Fight Chat Control 创始人的发言。 该法案将从根本上改变所有欧盟居民的数字隐私保护框架，因为它要求消息服务商为内容扫描绕过端到端加密，这会为政府强制要求的大规模数字监控开创重大先例。 当前的推进发生在欧盟机构间的三方谈判失败之后，欧盟理事会拒绝就用经司法批准的针对性嫌疑人监控替代全面大规模监控方案做出妥协，这一度让原临时法规面临失效风险。

hackernews · MrBruh · Mar 25, 20:27

**背景**: 该欧盟官方名称为《防止和打击儿童性虐待条例》（CSAR）的法案被批评者俗称为“聊天监控”（Chat Control）。它最早由欧盟委员会在 2022 年提出，批评者将更新版本称为 Chat Control 2.0，而 Fight Chat Control 是一个反对该法案的草根倡导运动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.politico.eu/article/one-man-spam-campaign-ravages-eu-chat-control-bill-fight-chat-control/">One-man spam campaign ravages EU 'Chat Control' bill</a></li>
<li><a href="https://edri.org/our-work/chat-control-what-is-actually-going-on/">Chat Control: What is actually going on? - European Digital ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论大体上反对这项拟议的监控法规，一名参与者提问为何没有主动立法来明确保护私人通信的权利，其他人则分享了评估该提案的经验法则，并对欧盟日益增加的监控提出了更广泛的批评。

**标签**: `#digital privacy`, `#EU regulation`, `#mass surveillance`, `#chat control`

---

<a id="item-17"></a>
## [对 AI 代理代码生成赶工的批评](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Pi 代理框架开发者、资深工程师 Mario Zechner 对现代智能体 AI 代码生成趋势提出批评，该观点被开发者 Simon Willison 在 2026 年 3 月 25 日的博客中分享推广。Zechner 认为，消除人工编码瓶颈会让 AI 智能体的错误以不可持续的速度累积，他呼吁放缓开发速度以维持工程纪律。 这一评论点出了当前行业争相采用自主 AI 编码智能体过程中一个被忽视的风险，指出了错漏丛生、难以维护的代码库会给所有使用生成式 AI 的软件开发团队带来长期问题。随着 AI 编码成为主流，它推动行业重新评估开发速度和代码质量之间的权衡。 Zechner 建议将每日 AI 生成代码的量限制在人工可 review 的范围内，并手动编写所有核心架构和 API 代码，而 Simon Willison 不认可必须手写代码的要求，但他同意需要建立新的工程纪律来平衡速度和思考的周全性。

rss · Simon Willison · Mar 25, 21:47

**背景**: 智能体 AI 指能够在极少人工持续监督的情况下自主规划、完成任务和编写代码的人工智能系统。智能体工程是借助这类自主 AI 编码智能体开发软件的新兴学科，随着大语言模型能力提升，该领域普及度迅速增长。认知债务指因赶工开发、简化清晰合理的代码设计而产生的未来维护和理解成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>
<li><a href="https://db0.ai/docs/pi">Persistent memory extension for the Pi coding agent . | db0.ai</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#AI code generation`, `#industry commentary`

---

<a id="item-18"></a>
## [NASA 调整阿耳忒弥斯计划，暂停 Gateway 建月基地](https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/) ⭐️ 7.0/10

NASA 宣布对阿耳忒弥斯探月计划进行重大战略调整，暂停原有的 Gateway 月球轨道空间站项目，将重心转向在 2029 年前建成永久月球表面基地。NASA 还计划在 2028 年开展前往火星的核动力推进技术演示任务，并加速商业登月任务的推进。 这次重大调整改变了 NASA 阿耳忒弥斯计划的核心方向，加快了人类重返月球表面的进度，将影响全球探月活动的发展走向。同时它也推动了对未来火星及更远深空探索至关重要的核推进技术的研发进程。 在新规划下，NASA 此后每年至少实施一次月面着陆，在 Artemis V 任务之后，NASA 将增加商业采购并采用可重复使用硬件，目标是每 6 个月完成一次载人登月任务。NASA 还计划在加速商业月球载荷服务的框架下，从 2027 年开始实施 30 次机器人登月任务。

telegram · zaihuapd · Mar 25, 04:30

**背景**: 阿耳忒弥斯计划是 NASA 正在执行的载人探月项目，Artemis V 是该计划的第四次载人任务，原规划负责向 Gateway 月球轨道空间站运送组件。Gateway 原本是计划建在月球轨道的多国合作小型空间站，作为阿耳忒弥斯月面任务和深空探索的枢纽。核电推进是一种深空推进技术，依靠核反应堆发电驱动电推进器，在长距离任务中比传统化学推进的能量效率高得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/月球门户">月球门户 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/wiki/核电火箭">核电火箭 - 维基百科，自由的百科全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artemis_V">Artemis V</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#NASA`, `#lunar program`, `#aerospace engineering`

---

<a id="item-19"></a>
## [AI 短剧冲击横店 群演集体失业](https://www.aibase.com/zh/news/26559) ⭐️ 7.0/10

低成本 AI 生成短剧越来越普及，导致包括横店在内的中国大型影视基地大量群众演员和特约演员失业，顶级短剧演员的片酬也被腰斩。截至 2026 年 1 月，AI 生成短剧在中国百强漫剧中的占比已从一年前的 7%飙升至 38%。 这一行业颠覆是生成式 AI 对基层创意劳动力产生的首批大规模影响之一，正在快速重塑全球短视频内容行业的经济模式和生产流程。低成本 AI 内容的爆发式增长也向更多创作者开放了短剧市场，大幅降低了入行门槛。 制作一部同等质量的精品 AI 短剧总成本可控制在 20 万元以内，而传统真人精品短剧的成本为 150 万至 300 万元，且 AI 短剧单集制作成本可低至 500 元。某头部平台预计到 2026 年 3 月底，其 AI 短剧月产能可达到 150 部，这一速度是传统真人剧组无法实现的。

telegram · AI_News_CN · Mar 26, 01:21

**背景**: 横店影视城是中国最大的影视拍摄基地，长期依赖大量群众演员和特约演员支撑国内庞大的影视制作产业。短剧是近年流行的高速增长垂直短视频内容形式，单集通常时长 1 到 3 分钟，面向移动端用户 binge 观看。AI 生成短剧借助生成式 AI 工具自动生成人物形象、口型同步和场景画面，取代了大部分实地拍摄和人类演员的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://variety.com/2026/digital/news/short-form-video-ai-generated-dramas-filmart-1236692132/">How Short-Form Video, AI-Generated Dramas Power Global Content</a></li>
<li><a href="https://ktla.com/business/press-releases/globenewswire/9361091/skyreels-open-sources-the-worlds-first-human-centric-video-foundation-model-for-ai-short-drama-creation-skyreels-v1-reshaping-the-ai-short-drama-landscape">SkyReels Open Sources the World's First Human-Centric Video ...</a></li>
<li><a href="https://news.futunn.com/en/post/69843567/the-ai-short-drama-huo-qubing-has-gained-popularity-discussions">The AI short drama 'Huo Qubing' has gained popularity! Discussions arise over production costs and viewership. How far along is the industrialization of AI manga dramas?</a></li>

</ul>
</details>

**标签**: `#AI for content creation`, `#industry disruption`, `#AI impact on labor`, `#digital media`, `#generative AI`

---

<a id="item-20"></a>
## [Sora 停摆后快手可灵冲击收入翻倍](https://www.aibase.com/zh/news/26560) ⭐️ 7.0/10

2026 年 3 月 25 日 OpenAI 关停 Sora 文本生成视频模型当天，快手宣布旗下国产可灵 AI 视频生成模型已取得亮眼早期商业化成绩，并定下了 2026 年可灵 AI 年收入同比翻倍的目标。快手还计划将 2026 年集团总资本支出提升至 260 亿元，其中大部分资金将投入可灵的 AI 基础设施建设。 这一进展证明生成式 AI 视频大模型除了 OpenAI 的高成本开发路线外，还存在可实现盈利商业化的其他路径，也将全球生成式 AI 视频赛道的竞争从技术展示转向了可持续盈利比拼。它同时也是中国大模型商业化进程中的重要里程碑。 2025 年第四季度可灵 AI 贡献营收 3.4 亿元，2025 年 12 月单月收入突破 2000 万美元，截至 2026 年 1 月其年化收入运行率已超过 3 亿美元。和深陷高成本困境难以为继的 Sora 不同，可灵走的是低门槛、多场景快速渗透的路线，确保收入增速超过成本增速。

telegram · AI_News_CN · Mar 26, 01:21

**背景**: Sora 是 OpenAI 开发的知名文本生成视频模型，推出不到两年便于 2026 年 3 月关停，主要原因是开发运营成本过高难以为继，同时 OpenAI 也在精简内部产品线。可灵是快手开发的国产文本生成视频大模型，能够生成 1080p 分辨率、30 帧每秒的视频，动态流畅度相比早期版本有明显提升。年化收入运行率（ARR）是一种财务指标，通过当前短期营收推算出全年的预计总收入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c3w3e467ewqo">Sora: OpenAI closes AI video app and cancels $1bn Disney deal</a></li>
<li><a href="https://skywork.ai/blog/keling-ai-2-5-turbo-hands-on-test-40-improvement-in-smoothness-realistic-light-and-shadow-even-ordinary-users-can-create-cinematic-grade-ai-videos/">Keling AI 2.5 Turbo Hands-On Test: 40% Improvement in... - Skywork ai</a></li>
<li><a href="https://www.linkedin.com/posts/mikelingle_whats-the-difference-between-run-rate-and-activity-7170760249753210880-J4La">What's the difference between Run Rate and ARR ? Both Run Rate ...</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#text-to-video model`, `#AI commercialization`, `#large language model`, `#Chinese AI`

---

<a id="item-21"></a>
## [高德开放平台发布适配 OpenClaw 的技能](https://www.aibase.com/zh/news/26567) ⭐️ 7.0/10

2026 年 3 月 25 日，高德开放平台宣布已将自身地图能力封装为适配 OpenClaw 的标准化技能，并发布到 ClawHub 对所有开发者和普通用户开放。 这次整合标志着地理信息服务从传统 API 调用模式转向自然语言驱动的 AI 智能体交互模式，降低了开发门槛，同时加速了地理信息产业融入 AI 智能体生态的进程。 本次上线的技能涵盖地理信息相关的生活办公助手和高德地图网站生成助手，可将 POI 应用开发时间从数天压缩至分钟级，还能让 AI 根据自然语言指令在数秒内生成定制化行程路书。

telegram · AI_News_CN · Mar 26, 01:45

**背景**: OpenClaw 是一款免费开源的 AI 智能体框架，允许开发者在自有基础设施上搭建 AI 驱动的自动化工作流。ClawHub 是 OpenClaw 的开放技能注册表与市场，支持智能体技能的版本管理和向量搜索。AI 智能体技能是预封装的可复用能力，无需重新训练底层大语言模型就能让智能体获得新功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw-ai.dev/">OpenClaw AI — Skills, Templates & Agent Showcase</a></li>
<li><a href="https://grokipedia.com/page/ClawHub">ClawHub</a></li>
<li><a href="https://github.com/heilcheng/awesome-agent-skills">GitHub - heilcheng/awesome-agent-skills: A curated list of ...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Geographic Information Service`, `#Location-Based Services`, `#Large Language Models`

---

<a id="item-22"></a>
## [通义千问落地红旗量产智能座舱](https://www.aibase.com/zh/news/26570) ⭐️ 7.0/10

2025 年 3 月 26 日，阿里巴巴的通义千问通用 AI 助手已正式接入红旗汽车智能座舱，并将首发搭载于红旗 HS6 PHEV。本次整合是完整形态的通用 AI 助手首次进入量产汽车场景。 这次落地推动车载智能从单点功能响应升级为端到端主动出行服务，为通用大语言模型开辟了新的实用落地场景。它也推进了阿里巴巴打造跨设备全场景通用 AI 助手的战略布局。 该系统可以从单条自然语音指令中识别多个模糊用户意图，通过云端多 Agent 协同决策完成任务拆解与编排，再联动车端应用执行方案。未来还将接入即时零售、票务预订等更多阿里生态服务，拓展车内服务边界。

telegram · AI_News_CN · Mar 26, 02:13

**背景**: 通义千问（Qwen）是阿里云开发的开源大语言模型系列，在多达 3 万亿标记的多领域多语言语料上完成了预训练训练。多智能体协同决策是一种 AI 框架，可让多个独立 AI 智能体共同完成单个模型难以处理的复杂任务，目前已在汽车和出行场景得到广泛探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2503.13415">[2503.13415] A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives</a></li>
<li><a href="https://github.com/QwenLM/Qwen">GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#In-vehicle AI`, `#Smart Cockpit`, `#AI Assistant`, `#Large Language Model`

---

<a id="item-23"></a>
## [OpenAI 投资 AI 智能体初创公司 Isara](https://www.aibase.com/zh/news/26572) ⭐️ 7.0/10

OpenAI 秘密投资了总部位于旧金山的初创公司 Isara，该公司由两名 23 岁的 AI 研究员张 Eddie 和 Henry Gasztowtt 于 2024 年 6 月创立。Isara 正在开发能够协调数千个 AI 智能体协同工作的软件架构，用于解决大型复杂工业问题。 这笔投资代表行业对多智能体协作技术路线的认可，该路线被普遍认为是推动通用人工智能发展、在重工业领域解锁全新 AI 应用的关键一步。它可能为 AI 发展开辟新方向，即发展重心转向智能体协同工作，而非单纯扩大单个模型的规模。 根据公开报道，Isara 目前融资总额为 9400 万美元，估值达到 6.5 亿美元，而该公司成立不到一年就已经从谷歌、Meta 和 OpenAI 挖来了十余名顶尖研究人员。

telegram · AI_News_CN · Mar 26, 02:26

**背景**: AI 智能体是能够感知环境、自主采取行动完成目标的人工智能实体，而多智能体系统则是协调多个 AI 智能体协同完成共同任务的技术框架。大规模多智能体系统背后的分布式人工智能研究方向，专门研究分散的智能体群体如何协作解决单个大模型难以处理的复杂问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techmeme.com/260325/p44">Isara, which aims to build software that can coordinate the ...</a></li>
<li><a href="https://www.ibm.com/think/topics/multiagent-system">What is a Multi-Agent System? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_agent">Intelligent agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#OpenAI`, `#startup funding`, `#artificial general intelligence`

---

<a id="item-24"></a>
## [Apifox 公网 SaaS 版 JS 被篡改安全公告](https://mp.weixin.qq.com/s/GpACQdnhVNsMn51cm4hZig?scene=0&subscene=90) ⭐️ 7.0/10

Apifox 发布了官方风险提示与升级公告，确认其公网 SaaS 版桌面客户端动态加载的一个外部 JavaScript 文件在供应链攻击中被恶意篡改。本次攻击影响了 2026 年 3 月 4 日至 2026 年 3 月 22 日期间使用该服务的用户，官方敦促所有受影响用户进行升级修复问题。 Apifox 是一款被广泛使用的 API 开发协作平台，本次事件暴露了威胁开发者和企业敏感数据的关键供应链攻击载体。该公告需要所有 Apifox 公有云 SaaS 版用户立即关注，以避免信息泄露或进一步的恶意活动。 本次事件仅影响 Apifox 公网 SaaS 版本，独立私有部署等其他部署版本不受影响。在 2026 年 3 月 4 日至 3 月 22 日期间使用该服务的用户存在敏感信息泄露的潜在风险。

telegram · AI_News_CN · Mar 26, 02:43

**背景**: Apifox 是集 API 文档、调试、Mock、自动化测试能力于一体的一体化协作 API 开发平台，在全球开发者群体中被广泛使用。SaaS 是一种云端软件交付模式，由服务提供商将服务托管在公有云基础设施上，用户通过互联网访问使用，无需自行管理底层基础设施。JavaScript 文件篡改类供应链攻击针对合法软件加载的第三方外部资源，攻击者可以借此注入恶意代码窃取数据或执行其他有害操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.v2ex.com/t/1201146">Apifox 遭受供应链攻击 - V2EX</a></li>
<li><a href="https://github.com/apifox/apifox">GitHub - apifox/apifox: Apifox = Postman + Swagger + Mock + JMeter。Apifox 官网：https://www.apifox.cn/</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/328295460">了解一下，什么是SaaS部署?什么又是独立部署呢? - 知乎</a></li>

</ul>
</details>

**标签**: `#Security Alert`, `#JavaScript Tampering`, `#Supply Chain Security`, `#Apifox`, `#SaaS`

---