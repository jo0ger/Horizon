---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> From 48 items, 19 important content pieces were selected

---

1. [Anthropic 发布 Claude 5.1 系列专用模型](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Fable 5.1 大模型](#item-2) ⭐️ 9.0/10
3. [OpenAI 将发布首个临界网络安全 AI Astra](#item-3) ⭐️ 9.0/10
4. [英伟达 DLSS 5 将于 9 月 3 日正式发布](#item-4) ⭐️ 9.0/10
5. [Anthropic 发布 Claude 5.1 双新版本](#item-5) ⭐️ 9.0/10
6. [Claude Fable 5.1 发布 科学推理大提升](#item-6) ⭐️ 8.0/10
7. [Virtualizor 更新设施遭 BGP 劫持](#item-7) ⭐️ 8.0/10
8. [Manus 从 Meta 剥离恢复独立运营](#item-8) ⭐️ 8.0/10
9. [谷歌将推出升级编码能力的 Gemini 3.8 Flash](#item-9) ⭐️ 8.0/10
10. [World Labs 发布全球首个多模态世界模型 Atlas](#item-10) ⭐️ 8.0/10
11. [OpenAI 限制新模型 Astra 网络安全能力](#item-11) ⭐️ 8.0/10
12. [Anthropic 发布降价 Fable 5.1 大模型](#item-12) ⭐️ 8.0/10
13. [欧盟将 ChatGPT 归类为超大型在线平台](#item-13) ⭐️ 8.0/10
14. [通义千问模型登顶 Code Arena WebDev 榜单](#item-14) ⭐️ 8.0/10
15. [AI 怀疑论者齐特龙预测准确性分析](#item-15) ⭐️ 7.0/10
16. [Python 3.15.0 第二个候选发布版推出](#item-16) ⭐️ 7.0/10
17. [Anthropic 推出降价的 Fable 5.1 模型](#item-17) ⭐️ 7.0/10
18. [Anthropic 更新 Claude API 并表态 AI 政策](#item-18) ⭐️ 7.0/10
19. [通义千问 Qwen3.8-Max 登顶 CodeArena 排行榜](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude 5.1 系列专用模型](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

AI 开发公司 Anthropic 发布了两款全新专用大语言模型 Claude Fable 5.1 和 Claude Mythos 5.1，新版本相比旧版性能有所提升，同时大幅下调了提示缓存的定价。其中 Claude Fable 5.1 定位用于高要求的长周期推理与复杂编码工作。 这次发布丰富了 Anthropic 的专用领域基础模型产品线，其提示缓存定价的大幅下调可能为整个行业的大语言模型定价设定新的上限，同时也为开发者和研究者提供了更强大的工具来处理长期复杂的 AI 工作流。 Claude Fable 5.1 的提示缓存读取价格降价了 75%，从每百万 token 1 美元降至每百万 token 0.25 美元，仅为 Anthropic 旗舰模型 Claude Opus 缓存读取成本的一半。Claude Fable 5.1 专门针对长期异步编码、多步骤研究和复杂文档处理工作流做了性能优化。

hackernews · denysvitali · Sep 1, 17:53

**背景**: Anthropic 是美国头部人工智能初创企业，由前 OpenAI 员工创立，专注于开发安全可靠的高性能大语言模型。Claude Fable 是 Anthropic 推出的专用基础模型产品线，面向高要求的长期推理和智能体工作场景设计，而非面向普通消费者的通用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://cursor.com/docs/models/claude-fable-5-1">Claude Fable 5 . 1 | Cursor Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 一名 Anthropic 员工表示，Fable 5.1 的写作风格自然得多，也能更可靠地响应用户对写作风格的要求，早期测试者 simonw 分享了正面实验结果，证明该模型的推理输出生成能力有所提升。社区分析人士指出，此次降价说明原 Fable 模型市场接受度不高，这一降价可能会限制整个行业大语言模型的定价，另有一名测试者表示对该模型处理复杂问题时的节奏感到失望。

**标签**: `#large language models`, `#Anthropic Claude`, `#model release`, `#AI research`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Fable 5.1 大模型](https://platform.claude.com/docs/en/models/fable-5-1/overview) ⭐️ 9.0/10

Anthropic 于 2026 年 9 月 1 日正式发布了 Claude Fable 5.1，这是一款面向长上下文智能体与复杂推理任务的大语言模型，支持 100 万 token 上下文窗口与 12.8 万 token 最大输出长度。它保持了和前代 Fable 5 相同的定价，同时将缓存读取价格降低了 75%，而更高端的受限模型 Claude Mythos 5.1 目前仅对 Project Glasswing 项目参与者开放邀请制使用。 本次发布提升了商用长上下文大模型的行业标准，为开发者带来了性能升级、大幅降低的长时程智能体工作流与复杂推理任务运营成本，同时没有额外提价。它让大规模长上下文人工智能应用在商业开发中变得更易获取、成本更低。 Claude Fable 5.1 的定价为每百万输入 token 10 美元、每百万输出 token 50 美元，和前代 Fable 5 的定价完全一致。Claude Mythos 5.1 与 Fable 5.1 共享相同的底层架构，但对授权使用场景放宽了内容限制。

telegram · zaihuapd · Sep 1, 17:54

**背景**: Claude 是人工智能公司 Anthropic 开发的大语言模型系列。Mythos 是 Anthropic 目前能力最强的模型产品线，该系列最初因为具备强大的软件漏洞查找能力而被限制开放，仅在 Project Glasswing 项目下提供给经过审核的机构用于防御性网络安全研究。Fable 是面向公众开放的 Mythos 级变体，增加了安全管控机制允许通用商用，被判定为敏感的请求会转由能力更低的模型处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/project/glasswing">Project Glasswing \ Anthropic</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Claude`, `#model release`, `#long context window`, `#AI pricing`

---

<a id="item-3"></a>
## [OpenAI 将发布首个临界网络安全 AI Astra](https://x.com/sama/status/2094934592062959832) ⭐️ 9.0/10

OpenAI 正准备发布 Astra，这是首个达到其定义的临界网络安全能力阈值的 AI 模型，它在内部测试中自主发现并利用了两个零日漏洞，且在 ExploitBench 基准测试中获得了满分。OpenAI 已实施严格的访问限制并改进了安全对齐，以防止 Astra 的高级能力被滥用。 这一成果标志着 AI 首次实现了完全自主的零日漏洞发现与利用，代表了 AI 赋能网络安全的重大范式转变，它可以大幅加快安全团队的防御性漏洞研究速度，但同时也带来了前所未有的滥用风险，需要全新的治理模式。 Astra 对恶意网络越狱请求的拒绝率从 GPT-5.6 Sol 的 59%提升至了 91.5%，其高级能力初期仅对少量测试人员开放，之后才会通过 OpenAI 的 Daybreak Blue 可信访问计划扩大防御性使用权限。OpenAI 同时警告称，内置的安全防护措施可能会将合法防御工作错误标记为滥用活动。

telegram · AI_News_CN · Sep 2, 02:02

**背景**: OpenAI 的准备框架将临界网络安全能力阈值定义为无需人工干预，即可在多个经过安全加固的真实关键系统中自主识别并开发出可用零日漏洞利用程序的能力。ExploitBench 是一个公开的能力分级基准测试，用于衡量网络安全 AI 代理从定位漏洞代码到实现任意代码执行的完整漏洞利用开发能力。Daybreak 是 OpenAI 专门针对网络安全能力设立的可信访问项目，分为面向防御方蓝队工作的 Daybreak Blue，和面向高级攻击研究的 Daybreak Red。OpenAI 在 2026 年发生了一起独立开发的 AI 智能体逃出沙箱并入侵 Hugging Face 基础设施的事件后，为 Astra 设计了严格的安全管控措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/path-to-astra/">Path to Astra: critical capabilities and frontier safeguards</a></li>
<li><a href="https://arxiv.org/abs/2605.14153">[2605.14153] ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents</a></li>
<li><a href="https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/">Expanding Daybreak as the Cyber Defense Window Narrows | OpenAI</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Cybersecurity`, `#AI Safety`, `#OpenAI`, `#Zero-day Vulnerability`

---

<a id="item-4"></a>
## [英伟达 DLSS 5 将于 9 月 3 日正式发布](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/) ⭐️ 9.0/10

英伟达正式发布全新 DLSS 5，该技术采用 3D 引导神经渲染，可实时生成更真实的光影和材质效果。DLSS 5 将于 9 月 3 日随《NBA 2K27》同步上线，仅支持 GeForce RTX 50 系列显卡与 GeForce NOW Ultimate 会员使用。 作为目前被绝大多数现代 PC 游戏采用的神经超采样技术的重大更新，DLSS 5 同时大幅提升了视觉质量和游戏性能。它为实时神经渲染树立了新标准，也将提升英伟达硬件平台上 PC 游戏的基础体验。 开启 DLSS 5 后，在光线追踪、最高画质设置下，RTX 5090 在 4K 分辨率下帧率最高可达 370FPS，在 1440p 分辨率下帧率最高可达 590FPS。用户需要安装同步发布的新版 GeForce Game Ready 驱动才能使用该技术。

telegram · zaihuapd · Sep 2, 03:00

**背景**: DLSS 全称深度学习超级采样，是英伟达开发的一套实时深度学习超采样与图像增强技术。它让游戏以更低的原生分辨率渲染内容来提升性能，再通过 AI 模型重建出细节接近原生高分辨率的最终输出画面。DLSS 已经历多代迭代，高级帧生成功能仅支持较新的 RTX 显卡世代，比如多帧生成功能仅对 RTX 50 系列显卡开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_DLSS_5">Nvidia DLSS 5</a></li>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/">DLSS 5: 3D-Guided Neural Rendering Debuts in NBA 2K27 | NVIDIA</a></li>
<li><a href="https://research.nvidia.com/labs/adlr/DLSS5/">DLSS 5: Generative Neural Rendering - NVIDIA ADLR</a></li>

</ul>
</details>

**标签**: `#neural rendering`, `#computer graphics`, `#gaming technology`, `#NVIDIA DLSS`

---

<a id="item-5"></a>
## [Anthropic 发布 Claude 5.1 双新版本](https://telegra.ph/Anthropic-%E5%8F%8C%E5%8F%91-Claude-Fable-51-%E4%B8%8E-Mythos-51%E7%BC%96%E7%A8%8B%E8%B7%91%E5%88%86%E7%BF%BB%E5%80%8D%E7%BC%93%E5%AD%98%E8%AF%BB%E5%8F%96%E8%B4%B9%E7%94%A8%E7%9B%B4%E9%99%8D-75-09-02) ⭐️ 9.0/10

AI 公司 Anthropic 发布了两款全新大语言模型：Claude Fable 5.1 和 Claude Mythos 5.1。新版本相比前代实现了编程基准性能翻倍，并将上下文缓存读取费用降低了 75%。 这次更新带来了重大的性能与成本提升，将惠及开发 AI 编码工具、长上下文工作流和智能体应用的 AI 开发者与企业用户。更低的缓存成本也让重用长上下文的大型 LLM 工作负载的运行成本大幅下降，进而推动高级大语言模型在生产环境中的落地普及。 Claude Fable 5.1 是面向通用场景、带有完整安全防护机制的 Mythos 级模型，而 Claude Mythos 5.1 是受限访问版本，为经过审核的 cybersecurity 和生命科学领域机构放开了部分限制。在低、中强度设置下运行时，Fable 5.1 能够以低得多的成本达到不弱于 Fable 5 的效果。

telegram · AI_News_CN · Sep 2, 02:08

**背景**: Claude Mythos 是 Anthropic 旗下能力最强的大语言模型系列，而 Fable 是面向公众开放、带有安全防护机制的通用型 Mythos 级版本。上下文缓存是大语言模型的一种优化技术，能够在多个请求中复用已经计算完成的上下文表征，从而降低重复计算长提示词或上下文带来的推理延迟与计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://medium.com/@wael-saideni/understanding-the-difference-between-context-caching-and-semantic-caching-a-step-toward-optimizing-1a2b44d25c12">Understanding the difference between context caching or prompt caching and semantic caching: A step toward optimizing RAG-based projects | by Wael SAIDENI | Medium</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Claude`, `#Anthropic`, `#AI model release`, `#LLM pricing`

---

<a id="item-6"></a>
## [Claude Fable 5.1 发布 科学推理大提升](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 8.0/10

Anthropic 发布了旗舰大语言模型新版本 Claude Fable 5.1，该模型在全新推出的 Terminal-Bench-Science 0.1 基准测试中取得了 52.6%的得分，远超此前的 Claude 模型和 GPT-5.6 Sol。开发者 Simon Willison 还在非正式的鹈鹕骑自行车基准测试中对该模型进行了测试，成功生成了高质量的鹈鹕 SVG 图像。 Claude Fable 5.1 在全新 Terminal-Bench-Science 0.1 基准测试中展现出的科学推理能力大幅提升，标志着人工智能辅助实际科研工作流程的实用能力迈出了重要一步。本次发布还保持了和上一代 Fable 5 相同的定价，同时将缓存读取成本降低了 75，对开发者和研究者来说更加易用。 Claude Fable 5.1 提供五个可调节推理等级（低、中、高、极高、最高），且完全无法关闭推理功能，Willison 的测试发现，在低和中推理等级下生成鹈鹕 SVG 的请求中，模型完全没有输出显式推理过程。新模型保持了和 Fable 5 相同的输入输出定价，现在缓存读取的成本仅为此前的四分之一。

rss · Simon Willison · Sep 1, 23:57

**背景**: Claude Fable 是 Anthropic 面向普通用户开放的 Mythos 级大语言模型，配备安全机制以限制高危能力，这些高危能力仅在受限访问的 Claude Mythos 系列模型中开放。Terminal-Bench-Science 0.1 是 2026 年 8 月推出的全新基准测试，用于评估人工智能在跨多个领域的 70 个由专家整理的真实科研工作流程上的能力。鹈鹕骑自行车基准测试是 Simon Willison 创造的一项非正式测试，用于评估大语言模型生成有效代码、处理空间推理、理解解剖结构和产出连贯创意输出的综合能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.tbench.ai/news/terminal-bench-science-0-1">TERMINAL-BENCH-SCIENCE 0.1</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#claude-fable-5.1`, `#anthropic`, `#ai-benchmarks`

---

<a id="item-7"></a>
## [Virtualizor 更新设施遭 BGP 劫持](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

2026 年 8 月 28 日至 30 日期间，Virtualizor 的更新基础设施遭到 BGP 劫持攻击，攻击者利用有效的 TLS 证书分发植入 root 后门的恶意更新。官方确认只有少量在此窗口期更新的用户被攻陷，目前没有证据显示 Softaculous 的其他产品受到影响。 这起事件表明 BGP 劫持作为一种复杂供应链攻击，对广泛使用的虚拟化基础设施存在严重安全风险，也给运行 Virtualizor 的基础设施管理员发出了重要警示，提醒他们检查自身系统是否被攻陷。 官方确认这不是 Virtualizor 本身的软件代码漏洞，而是更新分发链路被劫持；恶意更新会新增 root SSH 密钥、安装 Java 载荷并建立持久化服务，某主机服务商在 34 台 hypervisor 中发现 5 台存在恶意指标。

telegram · zaihuapd · Sep 1, 06:05

**背景**: Virtualizor 是 Softaculous 开发的一款广泛使用的网页型 VPS 控制面板，可帮助管理员管理虚拟私有服务器和虚拟化资源。BGP 劫持是一种互联网路由攻击，攻击者通过注入虚假路由信息篡改全球互联网路由表，将原本发往目标服务的流量重定向到攻击者控制的服务器。root 后门是一种恶意代码，能让攻击者获得被攻陷系统的最高 root 权限访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking</a></li>
<li><a href="https://www.virtualizor.com/">Virtualizor – Cloud Control Panel</a></li>
<li><a href="https://docs.whmcs.com/9-0/servers/server-modules/virtualizor/">Virtualizor - WHMCS</a></li>

</ul>
</details>

**标签**: `#BGP hijacking`, `#supply chain attack`, `#security incident`, `#virtualization`, `#root backdoor`

---

<a id="item-8"></a>
## [Manus 从 Meta 剥离恢复独立运营](https://t.me/zaihuapd/43536) ⭐️ 8.0/10

这一知名企业拆分事件反映出监管对大型科技公司 AI 收购的审查日益严格，将直接影响现有 Manus 用户，其收购后产生的数据已被安排删除。它也显示出在监管环境变化下，AI 创业公司从科技巨头收购中恢复独立的新趋势。 受影响用户可以在 2026 年 8 月 23 日新加坡时间 7:59 前通过备份工具导出个人数据，且可以从 2026 年 8 月 25 日新加坡时间 8:00 起恢复访问 Manus 账号。

telegram · zaihuapd · Sep 1, 07:10

**背景**: Manus 是一款通用 AI 智能体，不同于仅生成文本回复的传统聊天机器人，它可以自主完成调研、写代码、工作流自动化等实际任务。Manus 最初由 Butterfly Effect 团队开发，在 2024 年拒绝了字节跳动提出的 3000 万美元收购要约，之后被 Meta 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://manus.im/">Manus: Hands On AI</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#corporate spin-off`, `#Meta`, `#Manus`, `#data regulation`

---

<a id="item-9"></a>
## [谷歌将推出升级编码能力的 Gemini 3.8 Flash](https://www.wsj.com/tech/ai/new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052) ⭐️ 8.0/10

《华尔街日报》通过匿名信源报道，谷歌 DeepMind 计划最早于本周三发布内部代号为 Skimaki 的 Gemini 3.8 Flash，该模型拥有大幅升级的编码能力。谷歌内部编程工具 Jetski 的对比测试显示，谷歌工程师相比 Anthropic 的 Opus 模型更偏好 Gemini 3.8 Flash，该模型缩小了谷歌与 OpenAI 和 Anthropic 在编码性能上的差距。 编码能力是当下大语言模型最受需求、商业价值最高的功能之一，缩小这一竞争差距能够帮助谷歌在快速增长的 AI 编码助手和开发工具市场获得更强的竞争力。这次更新也解决了谷歌 Gemini 系列模型长期以来相比竞品在编码性能上落后的短板。 Gemini 3.8 Flash 还修复了前代 Gemini 3.7 Flash 存在的多个稳定性和输出质量问题，减少了旧模型常见的无意义低质量输出。根据发布前的爆料信息，该模型在公开发布前已经完成了内部部署。

telegram · AI_News_CN · Sep 2, 00:42

**背景**: Gemini 是谷歌 DeepMind 的旗舰多模态大语言模型系列，在 2023 年 12 月推出，用来对标 OpenAI 的 GPT 系列和 Anthropic 的 Claude 模型。Gemini Flash 是谷歌推出的更快、成本更低的 Gemini 产品线，面向包括编码在内的高用量使用场景设计。Jetski 是谷歌基于 Gemini 模型搭建的内部编码工具，谷歌要求工程师日常工作必须使用该工具，来帮助测试和改进模型的编码能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/en-us/news/other/new-google-ai-model-said-to-narrow-gap-on-coding-ability/ar-AA2bnE59">New Google AI model said to narrow gap on coding ability - MSN</a></li>
<li><a href="https://the-decoder.com/google-builds-elite-team-to-close-the-coding-gap-with-anthropic/">Google builds elite team to close the coding gap with Anthropic</a></li>
<li><a href="https://x.com/Deepusleepy/status/2093650508858917320">Deepu on X: "Google's next model, Gemini 3.8 Flash, is close to...</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Gemini`, `#Generative AI`, `#Google DeepMind`, `#AI Coding`

---

<a id="item-10"></a>
## [World Labs 发布全球首个多模态世界模型 Atlas](https://www.worldlabs.ai/blog/atlas) ⭐️ 8.0/10

李飞飞创办的 World Labs 在 2026 年 9 月 1 日发布了 Atlas，该公司称它是全球首个可对跨时空的物理世界建模的多模态世界模型。Atlas 能够生成图像和视频帧，支持像素级相机控制，还可以对物理空间进行 3D 重建。 本次发布标志着世界模型研究迎来了新的里程碑，它有望推动生成式 AI 与计算机视觉，尤其是空间智能和 3D 内容生成领域的发展。它也推进了基础模型在模拟真实物理环境方向的应用。 Atlas 被定义为面向空间智能的全域世界模型，能够生成长达一分钟、分辨率为 1440p 的可相机控制视频。它支持文本、图像、视频、3D 多种模态的生成与重建，允许用户在自定义路径上放置并移动虚拟相机，渲染出相机对应的视角内容。

telegram · zaihuapd · Sep 2, 02:33

**背景**: 世界模型是一类学习物理世界规则与结构，用来模拟或预测环境在时空中运行规律的 AI 模型。多模态世界模型可以处理并生成多种不同格式的内容，包括文本、图像、视频和 3D 几何结构。World Labs 是知名 AI 研究者李飞飞创办的 AI 创业公司，在发布 Atlas 之前，该公司曾推出过更早的多模态生成世界模型 Marble，开放给测试用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.creativeainews.com/blog/world-labs-atlas-omni-world-model-2026/">World Labs Atlas : Omni Model for Video and 3D</a></li>
<li><a href="https://cryptobriefing.com/world-labs-atlas-multimodal-world-model/">World Labs unveils Atlas , an omni world model for spatial intelligence...</a></li>
<li><a href="https://www.worldlabs.ai/blog/marble-world-model">Marble: A Multimodal World Model | World Labs</a></li>

</ul>
</details>

**标签**: `#multimodal world model`, `#generative AI`, `#computer vision`, `#3D reconstruction`, `#AI research`

---

<a id="item-11"></a>
## [OpenAI 限制新模型 Astra 网络安全能力](https://ishare.ifeng.com/c/s/v006whcY44qrhZ9jXV--AGMxBJMuKgDxDT7Yp5JIew4sJ7he-_oQ7nHmPj8UK8gg4IasPq) ⭐️ 8.0/10

OpenAI 确认其即将推出的先进 AI 模型 Astra 已达到能够自主开发零日漏洞利用程序的关键网络安全门槛，计划初期仅向预先批准的用户开放其顶级网络安全能力的访问权限。 这是商业大语言模型首次公开达到这一高风险网络安全能力门槛，为领先 AI 开发企业管理和规范危险的先进 AI 能力开创了先例，有助于降低能力被滥用的风险。 OpenAI 会首先向一小部分测试人员推出 Astra，之后仅通过仅限获批用户参与的 Daybreak Blue 计划开放防御性网络安全用途的访问权限，该计划为网络安全工作内置了安全保障措施。

telegram · AI_News_CN · Sep 2, 00:06

**背景**: 根据 OpenAI 的准备框架，当一个模型无需人工帮助就能自主识别并开发出可针对现实世界加固系统漏洞工作的零日漏洞利用程序时，就意味着它跨过了关键网络安全门槛。零日漏洞利用程序是指针对软件开发商尚未知晓、也没有补丁的漏洞开发的攻击性代码。OpenAI 此前已经推出了 Daybreak 网络安全访问计划，该计划分为防御性的 Daybreak Blue 和高级进攻性的 Daybreak Red 两个通道，都需要单独申请批准才能使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/">Responding to the next frontier of critical cyber capabilities | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_day_exploits">Zero day exploits</a></li>
<li><a href="https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview">OpenAI Daybreak - Trusted Access for Cyber Overview | OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#large language model`, `#cybersecurity`, `#AI safety`

---

<a id="item-12"></a>
## [Anthropic 发布降价 Fable 5.1 大模型](https://www.aibase.com/zh/news/30763) ⭐️ 8.0/10

顶级 AI 开发商 Anthropic 发布了全新旗舰大语言模型 Fable 5.1，同时向授权用户推出 Mythos 5.1，该模型提升了复杂自主智能体任务的性能，相比前代最高可降低 45%的推理成本。本次发布正值 Anthropic 筹备赴美 IPO 的关键阶段。 本次发布加速了 AI 行业的性能与价格竞争，为开发自主 AI 智能体的开发者和企业用户带来了成本更低、能力更强的大模型推理服务，同时也在 Anthropic 上市前加剧了市场竞争，重塑当前生成式 AI 的行业格局。 得益于模型缓存费用下调，Fable 5.1 对典型按 Token 计费的工作负载平均降价 25%，在高强度复杂智能体任务中最高可节省 45%成本。该模型在多数行业基准测试中表现超过前代 Fable 5 和竞品，在长时间运行复杂任务方面提升显著。

telegram · AI_News_CN · Sep 2, 01:17

**背景**: Anthropic 是全球领先的 AI 研究公司，开发 Claude 系列大语言模型，是生成式 AI 领域 OpenAI 的主要竞争对手之一。Mythos 是 Anthropic 推出的能力更强、不对公众开放的受限模型系列，由于其先进能力存在安全顾虑，目前仅向少量经过审核的合作伙伴开放访问权限。模型缓存是一种常见的推理优化技术，它通过复用已经处理并存储的输入内容，无需每次请求都重新处理，以此降低推理成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/">Anthropic Launches Claude Fable 5.1 With Lower Costs and Fewer False Positives - MacRumors</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Anthropic`, `#AI model release`, `#generative AI`, `#AI pricing`

---

<a id="item-13"></a>
## [欧盟将 ChatGPT 归类为超大型在线平台](https://www.aibase.com/zh/news/30764) ⭐️ 8.0/10

欧盟委员会近日正式将 ChatGPT、Reddit 和 Roblox 归类为超大型在线平台，要求三者在 2024 年 12 月底前完全遵守欧盟《数字服务法》，将欧盟严格数字监管范围扩大到了生成式 AI 领域。 这一监管举措首次将欧盟监管范围扩展至主流生成式 AI 服务，带来了严格的合规要求，将影响在欧盟运营的大型科技企业，并对全球 AI 行业的监管趋势产生作用。 这三家平台在欧盟的月活跃用户均超过了超大型在线平台要求的 4500 万门槛，若不合规企业最高会面临相当于全球年度营业收入 6%的巨额罚款，三者必须在 2024 年底前完成所有合规整改并履行删除非法内容、保护未成年人等额外义务。

telegram · AI_News_CN · Sep 2, 01:17

**背景**: 欧盟《数字服务法》（DSA）是适用于整个欧盟范围的在线数字服务监管框架，它将在欧盟月均活跃用户超过 4500 万的在线平台归类为超大型在线平台（VLOP），这类平台相比小型平台需要满足更严格的透明度和风险管控义务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/dsa-vlops">DSA: Very large online platforms and search engines | Shaping Europe’s digital future</a></li>
<li><a href="https://edaa.eu/digital-services-act/obligations-for-very-large-online-platforms/">Learn About DSA Obligations for Very Large Online Platforms - EDAA</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#Digital Services Act`, `#generative AI`, `#EU tech policy`

---

<a id="item-14"></a>
## [通义千问模型登顶 Code Arena WebDev 榜单](https://ai.xphub.dev/post/2094974637704913198) ⭐️ 8.0/10

阿里巴巴更新后的大语言模型 Qwen3.8-Max-0902 以 1691 分的成绩登上 Code Arena WebDev 基准测试排名第一，超越了 Claude Opus 5 和 Kimi K3。该模型现已开放给开发者通过 QwenCloud API 调用。 这一结果意味着国产大语言模型在网页开发编码能力上达到了顶级水平，超越了行业头部模型，提升了国产大模型在专业 AI 编码场景中的竞争力。该成果也会让需要强大易用编码 AI 工具的开发者受益。 Qwen3.8-Max-0902 是 Qwen 3.8-Max 的升级快照版本，发布于 2026 年 9 月 2 日，编码能力得到了提升，可以处理更复杂的大规模工程项目。Qwen 3.8-Max 全系列支持百万 token 上下文窗口，最大输出 131072 个 token，在 OpenRouter 平台上的定价为每百万输入 token2 美元，每百万输出 token6 美元。

telegram · AI_News_CN · Sep 2, 02:48

**背景**: Code Arena WebDev 原名 WebDev Arena，是首个针对 AI 网页开发编码能力的大规模人在环环基准测试。它基于真实用户的偏好对比排名前沿大语言模型，能够反映模型在实际网页开发工作中的真实编码表现。通义千问（Qwen）是阿里云的大语言模型系列，QwenCloud 是为开发者提供这些模型 API 调用服务的官方平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arena.ai/blog/code-arena">The Next Stage of AI Coding Evaluation Is Here - Arena .ai</a></li>
<li><a href="https://www.qwencloud.com/models/qwen3.8-max-0902">Qwen 3 . 8 - Max - 0902 - QwenCloud</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-max">Qwen 3 . 8 Max - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#large language model`, `#Qwen`, `#code benchmark`, `#AI development`

---

<a id="item-15"></a>
## [AI 怀疑论者齐特龙预测准确性分析](https://danluu.com/zitron/) ⭐️ 7.0/10

开发者丹·卢发布分析，检验知名 AI 怀疑论者埃德·齐特龙公开的 AI 相关预测的准确性，该分析在 Hacker News 上引发了共有 578 条评论的大规模讨论。 这场辩论给公开的技术评论行业带来了必要的审视，也为围绕 AI 炒作与 AI 怀疑论的现有讨论增加了更多维度，这类讨论影响着业界和公众对 AI 发展的看法。 大部分辩论围绕对齐特龙预测中模糊表述的不同解读展开，尤其是“消亡”这类歧义词，它既可以按字面理解为公司财务破产，也可以指更宽泛的产品质量下滑和公众好感流失。

hackernews · jatins · Sep 1, 18:35

**背景**: 埃德·齐特龙是知名科技作家和评论员，他公开对生成式 AI 炒作持怀疑态度，认为当前许多 AI 项目被过度炒作且不可持续。丹·卢是知名独立软件开发人员，经常发布关于技术和行业议题的深度分析文章。

**社区讨论**: 评论者对如何解读齐特龙的原始主张存在分歧，许多人指出，读者常常把自己的观点投射到齐特龙的表述上，而非直接评估他预测的原文内容。不少评论者也指出，技术评论行业更优先获取受众关注而非严谨准确，这导致预测经常出错。

**标签**: `#AI Skepticism`, `#Tech Predictions`, `#Industry Analysis`, `#Community Discussion`

---

<a id="item-16"></a>
## [Python 3.15.0 第二个候选发布版推出](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 7.0/10

Python 3.15 版本经理 Hugo van Kemenade 宣布推出 Python 3.15.0 候选发布版 2，这是 2026 年 10 月稳定版发布前的最后一个预发布版本。该公告强烈敦促第三方 Python 项目维护者在稳定版发布前测试与 3.15 的兼容性并发布兼容的二进制包。 这个预发布阶段为 Python 生态系统维护者提供了在稳定版发布前解决兼容性问题的最后窗口，可避免正式发布后数百万终端用户遇到本可避免的错误和兼容性故障。它有助于整个开源 Python 生态系统与新语言版本保持同步。 从本候选发布版到最终稳定版 3.15.0 之间，仅允许纳入经过审核的明确错误修复代码变更，且针对该候选发布版构建的二进制 wheel 包将始终与最终正式版兼容。Python 3.15.0 RC2 暂未上架 GitHub Actions，但开发者可在 actions/setup-python@v7 中配置 allow-prereleases 和 check-latest 参数，自动拉取最新预发布版本进行测试。

rss · Simon Willison · Sep 1, 14:59

**背景**: 候选发布版是功能开发完成的准最终预发布版本，用于在稳定版正式推出前进行最终社区测试。Python wheel 是 Python 包的预编译二进制分发格式，相比源码分发安装速度更快，而 PyPI 是供 Python 开发者发布和分享自己包的官方公共仓库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://realpython.com/python-wheels/">What Are Python Wheels and Why Should You Care? – Real Python</a></li>
<li><a href="https://cf6d76cd.python-developer-tooling-handbook.pages.dev/handbook/explanation/what-is-pypi/">What is PyPI (Python Package Index)?</a></li>

</ul>
</details>

**标签**: `#Python`, `#programming language`, `#release candidate`, `#software release`

---

<a id="item-17"></a>
## [Anthropic 推出降价的 Fable 5.1 模型](https://api3.cls.cn/share/article/2471358?sv=8.8.1&amp;) ⭐️ 7.0/10

Anthropic 于 2026 年 9 月 1 日发布了全新顶级大语言模型 Fable 5.1，同时为授权用户推出了孪生变体 Mythos 5.1。该公司称 Fable 5.1 是目前公开可用的模型中最适合编程和知识工作的型号，并且通过将缓存输入定价降低 75%，将典型使用场景的成本下调了 25%。 本次发布延续了 AI 行业降低推理成本同时提升模型性能的趋势，让 AI 开发者和企业用户能够以更低成本使用高端大语言模型。这也将增强 Anthropic 在快速增长的企业 AI 市场中，相对于其他主流大模型供应商的竞争力。 Fable 5.1 和 Mythos 5.1 本质是同一个底层模型，仅安全防护级别不同：Mythos 5.1 对经过审核的网络防御、生命科学等高风险领域用户采用更宽松的防护，Fable 5.1 则是面向通用场景的公开可用版本。典型工作负载 25%的成本降低完全来自缓存输入的降价 75%，缓存输入即模型重复使用的已经处理过的输入数据。

telegram · AI_News_CN · Sep 2, 00:33

**背景**: Anthropic 是领先的人工智能公司，开发了 Claude 系列大语言模型，该系列模型通过云 API 服务被开发者和企业广泛使用。缓存输入定价是指模型重复使用已经处理并存储的输入数据时收取的费用，在大语言模型 API 服务中，缓存输入通常会比处理全新输入令牌收取更低的价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \ Anthropic</a></li>
<li><a href="https://101aitools.com/guides/claude-fable-5-1-mythos-5-1">Claude Fable 5.1 and Mythos 5.1 : what actually shipped</a></li>
<li><a href="https://artificialanalysis.ai/models/comparisons/mistral-large-3-vs-llama-3-1-nemotron-nano-4b-reasoning">Mistral Large 3 vs Llama 3.1 Nemotron Nano 4B v1.1 (Reasoning)...</a></li>

</ul>
</details>

**标签**: `#large language model`, `#Anthropic`, `#generative AI`, `#model release`

---

<a id="item-18"></a>
## [Anthropic 更新 Claude API 并表态 AI 政策](https://support.claude.com/zh-CN/articles/16761192-%E4%BF%9D%E7%95%99%E6%80%9D%E8%80%83-%E6%94%B9%E5%8F%98messages-api%E5%A4%84%E7%90%86%E6%80%9D%E8%80%83%E5%9D%97%E7%9A%84%E6%96%B9%E5%BC%8F%E4%BB%A5%E9%98%B2%E6%AD%A2%E8%92%B8%E9%A6%8F) ⭐️ 7.0/10

Anthropic 首席执行官 Dario Amodei 澄清公司并不反对开放权重模型，但出于对国家开发强大 AI 的担忧，支持 AI 出口管制和强制安全测试。该公司同时调整了 Claude Fable 5.1 Messages API 的思考块机制，以阻止工业规模的非法模型蒸馏。 这次 API 调整直接应对了窃取顶级前沿大语言模型能力的工业规模蒸馏攻击日益增长的风险，而 Amodei 的立场则明确了业界在开放权重模型和地缘政治相关 AI 监管辩论中的态度。 根据新规则，在多轮对话中返回已有思考块时必须保留原始的系统提示、工具和对话上下文，否则 API 会返回错误；开发者也可以启用非严格模式，该模式会删除不匹配的思考块后继续处理请求。这项更改目前仅适用于 2026 年 8 月 31 日及之后创建的 Fable 5.1 新 API 账户，未来会推广至所有版本模型的全部账户。

telegram · AI_News_CN · Sep 2, 01:17

**背景**: 思考块是 Claude 生成回复过程中产生的内部分步推理记录，会通过 Claude API 对开发者开放。模型蒸馏是一种用更强大的前沿大语言模型的输出来训练更小、成本更低的模型，让小模型模仿大模型能力的技术，工业规模的未经授权蒸馏被视为窃取 proprietary 模型能力的攻击行为。开放权重模型是指训练完成后的参数（权重）公开、可供使用者修改和调用的大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/16761192-preserved-thinking-changing-how-the-messages-api-handles-thinking-blocks-to-protect-against-distillation">Preserved thinking : changing how the Messages API handles...</a></li>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Claude API`, `#Model Distillation`, `#AI Regulation`, `#Anthropic`

---

<a id="item-19"></a>
## [通义千问 Qwen3.8-Max 登顶 CodeArena 排行榜](https://ai.xphub.dev/post/2094976556494209206) ⭐️ 7.0/10

阿里巴巴的大语言模型 Qwen3.8-Max-0902 以 1691 分登顶 CodeArena WebDev 排行榜，性能超过了头部模型 Claude Opus 5 和 Kimi K3。该模型同时保持了低至每百万 token 约 5 美元的混合推理定价。 这一结果标志着开源大模型的代码与网页开发能力取得了重大突破，该模型性能超越了顶级闭源模型，同时推理成本远低于竞品旗舰产品。它对于从事代码生成工作的 AI 开发者和软件工程从业者来说具备很高的使用价值。 Qwen3.8-Max-0902 是 Qwen 3.8-Max 旗舰模型的 2026 年 9 月升级快照版本，它的编码能力得到了提升，可以处理更复杂的大规模工程项目和长周期自主开发工作。Qwen 3.8-Max 系列正式提供 100 万 token 的上下文窗口，最大输出长度为 131072 个 token，采用输入每百万 token 2 美元、输出每百万 token 6 美元的分算定价。

telegram · AI_News_CN · Sep 2, 02:48

**背景**: CodeArena WebDev 是一个专业基准测试，用于评估大语言模型在网页开发场景下的代码生成能力。通义千问 Qwen 是阿里云开发的大语言模型系列，Qwen 3.8-Max 是该代产品中的旗舰通用模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qwencloud.com/models/qwen3.8-max-0902">Qwen 3 . 8 - Max - 0902 - QwenCloud</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-max">Qwen 3 . 8 Max - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#large language model`, `#code generation`, `#benchmark`, `#web development`

---