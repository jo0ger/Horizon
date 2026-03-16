---
layout: default
title: "Horizon Summary: 2026-03-16 (ZH)"
date: 2026-03-16
lang: zh
---

> From 39 items, 22 important content pieces were selected

---

1. [Claude 推出百万 Token 上下文窗口](#item-1) ⭐️ 9.0/10
2. [谷歌推出 Chrome DevTools MCP 集成](#item-2) ⭐️ 8.0/10
3. [塞巴斯蒂安的 LLM 架构图库](#item-3) ⭐️ 8.0/10
4. [成年小鼠大脑玻璃化冷冻及功能恢复](#item-4) ⭐️ 8.0/10
5. [谷歌地图十年来最大 Gemini AI 升级](#item-5) ⭐️ 8.0/10
6. [智谱 AI 发布 GLM-5-Turbo 大模型](#item-6) ⭐️ 8.0/10
7. [特斯拉下周启动 Terafab AI 芯片工厂项目](#item-7) ⭐️ 8.0/10
8. [加拿大 2026 年 C-22 法案扩大大规模监控](#item-8) ⭐️ 7.0/10
9. [Hacker News 讨论 49MB 臃肿新闻网页问题](#item-9) ⭐️ 7.0/10
10. [River 拆分 Wayland 合成器与窗口管理器](#item-10) ⭐️ 7.0/10
11. [Simon Willison 定义智能体工程](#item-11) ⭐️ 7.0/10
12. [苹果发布全新 M5 系列笔记本芯片](#item-12) ⭐️ 7.0/10
13. [ImageGlass 10 Beta 1 发布 新增跨平台支持](#item-13) ⭐️ 7.0/10
14. [OpenAI 在 ChatGPT 测试广告](#item-14) ⭐️ 7.0/10
15. [绿联 MiniMax 推龙虾应用 让 NAS 变智脑](#item-15) ⭐️ 7.0/10
16. [阅文作家助手 Claw 开启创作内测](#item-16) ⭐️ 7.0/10
17. [企业微信 OpenClaw 接入重大升级](#item-17) ⭐️ 7.0/10
18. [多国预警 AI 深度伪造语音诈骗](#item-18) ⭐️ 7.0/10
19. [万兴推出国内首个全链路 AI 漫剧平台](#item-19) ⭐️ 7.0/10
20. [马斯克 xAI 重组 推出数字擎天柱项目](#item-20) ⭐️ 7.0/10
21. [马斯克诉 OpenAI 天价官司定档 4 月开庭](#item-21) ⭐️ 7.0/10
22. [AI 设计方案使犬肿瘤缩小 75%](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude 推出百万 Token 上下文窗口](https://www.aibase.com/zh/news/26226) ⭐️ 9.0/10

Anthropic 正式为旗下 Claude 大语言模型全面上线 100 万 Token 上下文窗口，Claude Opus 4.6 和 Claude Sonnet 4.6 均支持该能力，且全窗口采用一口价定价。这项新能力让 Claude 可以在单次提问中处理整个代码库、超大型文档和多本全本图书。 这一突破是长上下文大语言模型技术的重大飞跃，重塑了 AI 辅助开发工作流，还可能颠覆众多处理大量文本或代码的行业。不溢价的平价一口价模式也让长上下文 AI 相比竞品能覆盖更广泛的开发者群体。 100 万 Token 的上下文大约可以容纳 750 万个英文单词，相当于整整 7 套完整的《哈利·波特》系列小说。Claude Opus 4.6 在大海捞针长上下文检索测试中取得 78.3%的得分，是所有现有同类模型中的最高分。

telegram · AI_News_CN · Mar 16, 01:27

**背景**: Token 是大语言模型处理输入、生成输出所用的基本文本单位，上下文窗口则定义了模型单次交互中能够处理和参考的最大 Token 数量。大海捞针测试是一项标准评估，用来衡量长上下文大语言模型从大量输入文本中找出隐藏的特定细小信息的能力。在这次发布之前，多数主流大模型的上下文窗口限制小得多，开发者不得不手动将完整代码库这类大型输入分割为更小的块才能使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/">Tokens and Context Windows in LLMs - GeeksforGeeks</a></li>
<li><a href="https://arize.com/blog-course/the-needle-in-a-haystack-test-evaluating-the-performance-of-llm-rag-systems/">The Needle In a Haystack Test : Evaluating the Performance... - Arize AI</a></li>

</ul>
</details>

**社区讨论**: OpenAI 总裁 Greg Brockman 称赞了这一新能力，他表示无需手动编写大量代码的自由为开发者减轻了沉重的脑力负担。原新闻报道未收录更多广泛的社区讨论内容。

**标签**: `#Large Language Models`, `#Claude`, `#Long Context AI`, `#AI Programming`, `#Anthropic`

---

<a id="item-2"></a>
## [谷歌推出 Chrome DevTools MCP 集成](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) ⭐️ 8.0/10

谷歌正式发布了 Chrome DevTools MCP，该功能允许 AI 代理与实时 Chrome 浏览器会话交互并对其进行调试。该项目最新的 v0.20.0 版本已经推出了尚未正式官宣的独立命令行界面（CLI）。 该集成将基于 MCP 的标准化 AI 工具访问能力带入全球最常用的开发工具之一，加速了 AI 驱动的 Web 调试和自动化工作流的发展。它为 AI 代理自动化需要浏览器检查和交互的复杂 Web 任务创造了新机会。 Chrome DevTools MCP 作为 MCP 服务器运行，可为 AI 编码助手提供对 Chrome DevTools 原生功能的完整访问权限。MCP 处理完整 DOM 快照这类大型数据时会产生很高的 token 用量，新增的独立 CLI 则为直接访问提供了更低成本的选择。

hackernews · xnx · Mar 15, 19:12

**背景**: Model Context Protocol（MCP）是 Anthropic 在 2024 年 11 月推出的开源标准，用于统一大语言模型和 AI 代理连接外部工具、系统和数据源的方式。Chrome DevTools 是谷歌官方内置的开发工具套件，用于直接在 Chrome 浏览器中构建、测试和调试 Web 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">ChromeDevTools/chrome-devtools-mcp - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/tutorial/chrome-devtools-mcp">Chrome DevTools MCP: AI-Powered Browser Automation and Debugging | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 社区参与者围绕 MCP 和直接 CLI 访问的优缺点展开讨论，多数人同意两者适用于不同场景：MCP 提供统一的跨工具集成能力，而直接 CLI 速度更快、成本更低。一位曾（且仍）参与 DevTools 团队的成员确认了 v0.20.0 版本中未官宣的独立 CLI 推出，回应了人们对 MCP token 成本的担忧。多位用户分享了基于 Chrome DevTools MCP 的实际自动化用例和第三方工具，他们已经在日常使用这些工具。

**标签**: `#Chrome DevTools`, `#Model Context Protocol`, `#AI Agents`, `#Debugging`, `#Web Development`

---

<a id="item-3"></a>
## [塞巴斯蒂安的 LLM 架构图库](https://sebastianraschka.com/llm-architecture-gallery/) ⭐️ 8.0/10

研究者塞巴斯蒂安·拉施卡（Sebastian Raschka）推出了全新整理的 LLM Architecture Gallery，这是一份现代大语言模型架构的可视化概览资源，在 Hacker News 上引发了大量富有洞见的讨论。 这份整理后的参考资源对机器学习从业者和研究者而言极具价值，围绕它展开的讨论也凸显了当代开源权重 LLM 领域架构趋同的核心行业趋势。 该图库将过往 LLM 对比研究中的架构图整合为一份便于访问的参考资源，社区观察者指出，当前具备竞争力的顶尖开源权重 LLM 已经收敛到狭窄的设计空间，核心是带有 RMSNorm、旋转位置编码、SwiGLU 激活函数等标准组件的仅解码器稠密 Transformer。

hackernews · tzury · Mar 15, 16:01

**背景**: 大语言模型（LLM）是在海量文本语料上训练、用于处理自然语言任务的人工智能模型，自七年前 GPT-2 发布以来，LLM 的架构一直在持续发展。研究者已经测试了多种不同的架构方案，包括混合专家模型（MoE）、状态空间模型和线性注意力等，以此提升 LLM 的性能和效率。与科技公司持有的闭源专有模型不同，开源权重 LLM 的权重完全公开，可供人们自由使用和修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/blog/2026/llm-architecture-gallery.html">New LLM Architecture Gallery | Sebastian Raschka, PhD</a></li>
<li><a href="https://github.com/rasbt/llm-architecture-gallery">rasbt/llm-architecture-gallery - GitHub</a></li>
<li><a href="https://maxpool.dev/llm-design/">LLM Architecture Design Guide | MaxPool</a></li>

</ul>
</details>

**社区讨论**: 大多数社区成员称赞该图库是高质量的实用资源，很多人都认同自 GPT-2 推出以来 LLM 领域没有出现根本性架构创新、整个领域已经收敛到一套共享核心设计的观点。有评论者将该图库与经典的「神经网络动物园」可视化项目对比，还有人建议为资源增加演化排序和尺寸缩放功能来进一步优化。

**标签**: `#Large Language Models`, `#LLM Architecture`, `#Machine Learning`, `#Curated Resources`

---

<a id="item-4"></a>
## [成年小鼠大脑玻璃化冷冻及功能恢复](https://www.pnas.org/doi/10.1073/pnas.2516848123) ⭐️ 8.0/10

研究人员在《美国国家科学院院刊》（PNAS）发表研究成果，开发出 V3 玻璃化保护剂，成功实现成年小鼠脑片和原位完整全脑的玻璃化冷冻，且复温后神经功能得以恢复。 这项成果是完整成年哺乳动物大脑功能冷冻保存领域的重要里程碑，同时推动了神经科学研究和整体器官保存领域的发展，为复杂全神经器官的长期功能保存提供了新的可行路径。 V3 保护剂通过优化冷却流程有效避免了冰晶损伤，实验证实复温后的脑片恢复了细胞代谢，同时保留了电生理活性和突触可塑性；针对全脑保存，研究人员采用血管灌注技术平衡脱水与保护剂渗透，初步实现了原位全脑的功能保留。

telegram · zaihuapd · Mar 15, 08:30

**背景**: 玻璃化冷冻又称玻璃态冷冻保存，是一种将样本转化为非晶态无定形玻璃固体而非结晶冰的冷冻保存技术，可避免冰晶对活细胞和组织造成损伤。实现玻璃化需要冷冻保护剂（CPA），保护剂可以减少细胞脱水损伤，帮助整个样本在冷却过程中形成稳定的玻璃态。在这项研究之前，尚未有成功对完整成年哺乳动物全脑进行功能冷冻保存的报道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vitrification">Vitrification - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8162897/">Mathematical modeling of protectant transport in tissues - PMC</a></li>
<li><a href="https://www.21cm.com/vm3.html">VM3 Cryoprotectant for Successful Tissue Preservation</a></li>

</ul>
</details>

**标签**: `#cryopreservation`, `#neuroscience`, `#biotechnology research`, `#vitrification`

---

<a id="item-5"></a>
## [谷歌地图十年来最大 Gemini AI 升级](https://www.aibase.com/zh/news/26233) ⭐️ 8.0/10

谷歌首席执行官桑达尔·皮查伊宣布 Google 地图推出十年来最大规模升级，接入 Gemini AI 模型新增两项 AI 驱动功能：对话式定制地点推荐工具 Ask Maps 和 3D 实时渲染沉浸式导航，目前已开始在部分地区向 iOS 和安卓用户推送。 作为全球使用最广泛的消费级导航应用之一，这次生成式 AI 深度整合标志着地图行业的转型变革，也将加速 AI 在日常消费软件中的普及应用。 Ask Maps 目前已率先在美国和印度上线，它可以分析海量用户数据回答复杂自然语言查询，甚至能帮用户预订座位。沉浸式导航利用 Gemini 实时渲染数亿张街景和航拍照片，清晰呈现道路细节，降低用户在复杂立交桥走错路的概率。

telegram · AI_News_CN · Mar 16, 02:19

**背景**: Gemini 是谷歌 DeepMind 开发的多模态大语言模型系列，于 2023 年 12 月首次发布，是谷歌的旗舰生成式 AI，接替了此前的 PaLM 2 等模型。Google 地图是全球最受欢迎的消费级地图导航应用，全球数十亿用户使用它提供的出行和地点服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/">Ask Maps and Immersive Navigation: New AI features in Google Maps</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**标签**: `#Google Maps`, `#Gemini`, `#Generative AI`, `#AI Integration`, `#Navigation Technology`

---

<a id="item-6"></a>
## [智谱 AI 发布 GLM-5-Turbo 大模型](https://autoglm.zhipuai.cn/autoclaw) ⭐️ 8.0/10

智谱 AI 正式发布针对复杂 AI Agent 场景深度优化的 GLM-5-Turbo 基座模型，这是首款龙虾（OpenClaw）场景原生大模型，在智谱自研 ZClawBench 基准测试中位居国产大模型首位。智谱同步为 OpenClaw AI Agent 生态推出了“龙虾套餐”订阅体系和企业级安全管理体系。 此次发布将大模型竞争的焦点从单一语义理解转向端到端执行效率，加速了 AI Agent 的大规模商业化落地，推动大模型从提效工具向企业数字劳动力转型，为国内 AI Agent 产业发展提供了标准范式。 GLM-5-Turbo 从训练阶段就针对工具调用、复杂指令拆解、定时触发和高吞吐持续执行等 AI Agent 核心能力优化，在开发者盲测中获得 90%的优胜认可率。该模型现已率先接入全球首款原生 AI Agent 终端“龙虾盒子”，开发者从 2026 年 3 月 16 日起可通过智谱开放平台 BigModel.cn 调用相关 API。

telegram · AI_News_CN · Mar 16, 02:45

**背景**: AI Agent 是能够独立完成长链路多步骤复杂任务的自主 AI 系统，近年来是大语言模型行业的核心发展方向之一。通用大模型往往存在长链路任务执行中容易失速失效的痛点，无法满足复杂 AI Agent 场景的需求。OpenClaw 是一个开源自主 AI Agent 框架，支持大模型通过模块化技能执行任务、扩展能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/26235">Zhipu Launches GLM-5-Turbo: The First Lobster-Specific Scene ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://open-claw.org/">OpenClaw | The Open -Source Personal AI Assistant & Autonomous...</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Agent`, `#Model Release`, `#GLM-5-Turbo`, `#Zhipu AI`

---

<a id="item-7"></a>
## [特斯拉下周启动 Terafab AI 芯片工厂项目](https://www.aibase.com/zh/news/26236) ⭐️ 8.0/10

埃隆·马斯克于 2026 年 3 月 14 日宣布，特斯拉自研巨型 AI 芯片工厂项目 Terafab 将在七天后（即下周）正式启动。该项目启动是因为特斯拉全自动驾驶（FSD）项目的 AI 芯片需求未得到满足，且外部代工厂出现了生产延误。 这一进展标志着特斯拉正向 AI 芯片生产全链路垂直整合迈进，有望重塑全球车载 AI 芯片市场格局，并降低特斯拉自动驾驶业务面临的半导体供应链风险。如果项目成功，将为汽车企业全面掌控核心 AI 硬件供应链开创全新先例。 特斯拉第五代 AI 芯片 AI5 预计将成为 Terafab 首批生产的产品之一，计划 2026 年小批量生产，2027 年实现量产。受三星 2 纳米工艺流片延期影响，特斯拉下一代 AI6 芯片量产已推迟至 2027 年底，这一情况也加速了特斯拉自建工厂的进度。

telegram · AI_News_CN · Mar 16, 02:53

**背景**: 长期以来，特斯拉一直依赖台积电、三星等外部代工厂生产自动驾驶系统所用的 AI 芯片。马斯克此前多次表示，即便供应商满负荷生产，也无法满足 FSD 项目不断增长的 AI 芯片需求。流片是集成电路设计交付生产前的最后一个步骤，因此流片延期会直接推迟芯片量产的时间线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/autos-transportation/musk-says-teslas-gigantic-chip-fab-project-launch-seven-days-2026-03-14/">Musk says Tesla's mega AI chip fab project to launch in seven days | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tape-out">Tape - out - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Tesla`, `#Autonomous Driving`, `#Semiconductor Manufacturing`, `#Supply Chain`

---

<a id="item-8"></a>
## [加拿大 2026 年 C-22 法案扩大大规模监控](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/) ⭐️ 7.0/10

2026 年 3 月加拿大提出新的 C-22 法案，该法案扩大了警方和安全机构的监控权力，要求电子服务提供商留存用户元数据并配合政府的数据调取请求。 该法案威胁所有加拿大居民而非仅犯罪嫌疑人的数字隐私权，为政府大规模监控开创了令人担忧的先例，会影响所有向加拿大市场提供服务的国内外科技公司。 该法案设立了强制性大规模元数据留存制度，要求企业存储所有加拿大人的位置数据、设备信息和其他敏感元数据，同时允许法官免除要求告知当事人其数据已被令状调取的规则。

hackernews · opengrass · Mar 15, 21:22

**背景**: 元数据是描述其他数字信息的数据，就像数字通信的信封，即使通信内容被加密，它也能暴露发送方、接收方、位置和时间信息。大规模元数据监控指为执法和情报机构使用，收集存储全体民众而非仅犯罪嫌疑人元数据的做法。加拿大此前曾尝试通过类似的广泛监控法案，已被隐私倡导组织否决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ssd.eff.org/module/why-metadata-matters">Why Communication Metadata Matters | Surveillance Self-Defense</a></li>
<li><a href="https://reclaimthenet.org/canada-bill-c22-lawful-access-act-metadata-retention-surveillance">Canada's Bill C-22 Mandates Mass Metadata Surveillance of Canadians</a></li>
<li><a href="https://www.canada.ca/en/public-safety-canada/news/2026/03/backgrounder--securing-access-to-information-in-bill-c-22.html">Backgrounder – Securing Access to Information (Bill C-22 – Part 2) - Canada.ca</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区参与者指出，虽然该法案要求数据调取需要令状，但它包含可以免除告知目标用户数据被调取的条款，同时批评该法案是五眼联盟监控合作不透明的扩张。社区成员还分享了反对该法案的实际行动步骤，包括联系民选代表和支持成熟的隐私倡导组织。

**标签**: `#digital privacy`, `#surveillance`, `#public policy`, `#technology regulation`

---

<a id="item-9"></a>
## [Hacker News 讨论 49MB 臃肿新闻网页问题](https://thatshubham.com/blog/news-audit) ⭐️ 7.0/10

一项审计发现单个新闻网页大小达 49MB，由此在 Hacker News 上引发了高参与度讨论，收集了用户对现代商业与新闻网站极端资源臃肿问题的投诉和亲身经历。 这个问题会损害终端用户体验，浪费有限的带宽和设备资源，还会导致用户离开传统新闻媒体，突显了现代网络生态中的系统性问题。 这场讨论共有 177 条实质性评论，来自开发者和终端用户，分享的经历包括单页资源占用达到 750MB，以及主流新闻网站因过多 JavaScript 和追踪脚本逼走资深用户。

hackernews · kermatt · Mar 15, 19:25

**背景**: 软件臃肿（software bloat）指软件或网页为实现核心功能却占用了远超出必要水平的系统资源与带宽的现象，通常不会给用户体验带来对应的明显提升。网页资源臃肿会迫使访客消耗更多不必要的数据，拖慢页面加载速度，还会消耗设备的处理能力和电量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software_bloat">Software bloat - Wikipedia</a></li>
<li><a href="https://www.curotec.com/insights/how-to-improve-website-performance/">Getting the Fast Website Load Times - A Web Performance... - Curotec</a></li>

</ul>
</details>

**社区讨论**: 评论者一致对网页臃肿问题表达不满，分享了多个关于主流新闻网站资源占用过多、性能糟糕、未经授权隐私追踪的个人经历。不少评论者提到，臃肿问题已经让他们彻底停止访问热门新闻媒体。

**标签**: `#web performance`, `#web development`, `#software bloat`, `#community discussion`

---

<a id="item-10"></a>
## [River 拆分 Wayland 合成器与窗口管理器](https://isaacfreund.com/blog/river-window-management/) ⭐️ 7.0/10

River Wayland 合成器实现了 Wayland 合成器核心与窗口管理器的全新架构分离，该方案由开发者在近期博客中详细介绍。这一开发在 Hacker News 上引发了一个参与度很高的讨论帖。 这一改动解决了 Wayland 长期以来饱受批评的默认设计选择，为 Linux 桌面 Wayland 生态带来了更模块化、灵活的窗口管理和更清晰的代码。它也推动了围绕减少多年来困扰 Wayland 开发的协议碎片化问题的重要讨论。 新设计在避免每帧往返开销的同时仍能实现帧完美的窗口重排，还为分离后的窗口管理器引入了名为 river-window-management-v1 的新协议。与大多数同时整合两项功能的现有 Wayland 合成器不同，River 现在明确采用非整体式架构。

hackernews · dpassens · Mar 15, 15:09

**背景**: Wayland 是面向 Linux 桌面的现代显示协议，旨在替代老旧的 X11 协议，核心目标是实现更流畅、更安全的硬件加速图形。传统上 Wayland 合成器一直将两个不同角色（负责屏幕合成和图形输出的合成器、负责窗口排列和用户输入的窗口管理器）整合在同一个程序中。River 是一款基于 wlroots 的开源动态平铺 Wayland 合成器，灵感来自 Xmonad 等流行的平铺窗口管理器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayland_(protocol)">Wayland (protocol) - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/River">river - ArchWiki</a></li>
<li><a href="https://github.com/riverwm/river">GitHub - riverwm/ river : [mirror] A non-monolithic Wayland compositor</a></li>

</ul>
</details>

**社区讨论**: 大多数评论者对这一改动反应积极，不少人认为它修复了 Wayland 长期存在的缺陷，让 Wayland 变得好用得多。讨论中最普遍的担忧是，新的 river-window-management-v1 协议能否成为跨合成器标准，还是会加剧 Wayland 当前因各合成器自定义扩展导致的碎片化问题。有评论者幽默地表示 Wayland 正在逐个重新发明 X11 已有的功能，而 River 的现有用户对这一更新表示兴奋，并向曾经的 Xmonad 用户推荐了该项目。

**标签**: `#Wayland`, `#window management`, `#software architecture`, `#Linux desktop`

---

<a id="item-11"></a>
## [Simon Willison 定义智能体工程](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/#atom-everything) ⭐️ 7.0/10

知名行业评论员 Simon Willison 在他持续更新的《智能体工程模式》指南中，正式定义了新兴术语 agentic engineering，同时也对 LLM 智能体、编码智能体等相关概念给出了清晰界定。 这个清晰的定义为快速发展的 AI 辅助软件开发领域建立了通用词汇，帮助从业者就使用 AI 编码工具的实践达成共识。它还明确了人类工程师和 AI 编码智能体的互补角色，消除了围绕 AI 增强软件开发的认知困惑。 Willison 在此语境中将 LLM 智能体定义为循环运行工具以实现用户既定目标的系统，他指出直接执行代码的能力是让 agentic engineering 成为可能的核心特性。这份指南本身仍在开发完善中，他计划随着智能体工程的新模式和新技术出现不断更新内容。

rss · Simon Willison · Mar 15, 22:41

**背景**: Agentic engineering（智能体工程）是聚焦 AI 增强软件开发的新兴学科，随着大语言模型的代码生成能力不断提升，该领域受到越来越多的关注。在 Willison 给出正式定义之前，该术语在科技行业的使用并不统一，不同技术领袖对其有着不同的解读。基于 LLM 的编码智能体是为辅助软件开发设计的 AI 工具，能够直接与代码库和开发环境交互完成任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://addyosmani.com/blog/agentic-engineering/">AddyOsmani.com - Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Claude Code overview - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#agentic engineering`, `#AI-assisted development`, `#LLM agents`, `#software engineering`

---

<a id="item-12"></a>
## [苹果发布全新 M5 系列笔记本芯片](https://t.me/zaihuapd/40272) ⭐️ 7.0/10

苹果于 2026 年 3 月宣布推出面向新款 MacBook Pro 的 M5 Pro 和 M5 Max 芯片，同时为更新后的 MacBook Air 配备基础版 M5 芯片。新款专业级 M5 芯片采用苹果全新 Fusion Architecture 设计，搭载含 6 颗超级核心和 12 颗性能核心的 18 核 CPU。 这是应用广泛的苹果 M 系列笔记本芯片的一次重要跨代更新，推出的全新架构进一步提升了专业笔记本的性能上限。此次更新将影响专业内容创作者、普通消费者以及全球个人计算和半导体行业。 不同于采用单裸片设计的基础版 M5 和前几代 Apple Silicon 芯片，Fusion Architecture 通过先进封装将两颗裸片整合为一颗单一 SoC。全新的“超级核心”是苹果目前性能最高的 CPU 核心设计，专为高要求专业工作负载优化性能。

telegram · zaihuapd · Mar 15, 07:20

**背景**: Apple Silicon 是苹果为自有设备开发的自研 ARM 架构系统级芯片产品线，从 2020 年开始逐步替代 Mac 电脑中的 Intel 处理器。M 系列是苹果目前用于 Mac 笔记本和台式机的 Apple Silicon 芯片系列，每一代都在性能和能效上实现提升。在 M5 推出之前，所有高端 M 系列 Pro 和 Max 芯片都采用传统单裸片设计来整合所有处理组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/">Apple debuts M5 Pro and M5 Max to supercharge the most ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://dev.to/tyson_cung/apple-m5-fusion-architecture-explained-two-dies-one-chip-infinite-possibilities-o9e">Apple M 5 Fusion Architecture Explained - Two Dies, One Chip ...</a></li>

</ul>
</details>

**标签**: `#Apple Silicon`, `#Semiconductors`, `#Laptop Hardware`, `#Apple M5`

---

<a id="item-13"></a>
## [ImageGlass 10 Beta 1 发布 新增跨平台支持](https://imageglass.org/news/imageglass-10-beta-1-is-here-99) ⭐️ 7.0/10

知名免费开源看图软件 ImageGlass 推出了 ImageGlass 10 Beta 1 版本，该版本基于.NET 和 Avalonia 完全重写，在原有的 Windows 支持之外新增了原生 macOS 与 Linux 支持。旧版本 ImageGlass 9 已转入维护模式，后续所有开发重心都转移到 ImageGlass 10。 本次更新满足了 ImageGlass 用户社区期待已久的跨平台需求，将一款广受欢迎的 Windows 专属看图工具变成了可适配所有主流桌面系统的选择。它为 macOS 和 Linux 用户提供了一个全新的免费开源轻量看图替代方案。 本次 beta 版本包含多项性能优化，包括更快的启动速度、更迅捷的切图体验以及大图流畅缩放，但本次测试版的二进制安装文件暂未提供数字签名。

telegram · zaihuapd · Mar 15, 11:40

**背景**: ImageGlass 是一款免费开源看图工具，支持常见格式与多种专业图片格式，个人和商业使用都可免费获取。Avalonia 是为.NET 生态打造的开源跨平台 UI 框架，允许开发者通过单一共享代码库构建可在多平台运行的应用。当软件进入维护模式后，开发团队会停止添加新的大功能，仅修复关键漏洞来维持现有版本的正常运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Avalonia_(software_framework)">Avalonia (software framework) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Maintenance_mode">Maintenance mode - Wikipedia</a></li>
<li><a href="https://avaloniaui.net/">Avalonia UI – Open-Source .NET XAML Framework | WPF & MAUI ...</a></li>

</ul>
</details>

**标签**: `#open source`, `#software release`, `#cross-platform`, `#image viewer`, `#.NET`

---

<a id="item-14"></a>
## [OpenAI 在 ChatGPT 测试广告](https://t.me/zaihuapd/40282) ⭐️ 7.0/10

OpenAI 于 2 月 9 日开始在 ChatGPT 中测试广告，预计长期来看广告收入将贡献公司近一半的总营收。该公司同时确认 ChatGPT 的月增长率已重回 10%以上，并计划于本周发布更新版聊天模型。 这一公告披露了 OpenAI 为其旗舰产品制定的核心商业化变现战略，为整个生成式 AI 行业的变现探索树立了重要参考。该举措将影响未来 AI 企业如何平衡营收目标与用户隐私保护。 本次测试的广告放置在对话框下方的独立区域，免费用户和 ChatGPT Go 订阅用户都能看到，广告不会访问用户的私人对话，广告商也无法干预 ChatGPT 生成的回答内容。OpenAI 首席执行官 Sam Altman 确认，长期来看广告收入占公司总营收的比例不到 50%。

telegram · zaihuapd · Mar 16, 01:23

**背景**: ChatGPT Go 是 OpenAI 推出的 ChatGPT 低价订阅档位，经过初期测试后已在全球上线，在美国的定价为每月 8 美元。生成式 AI 行业在初期热潮后一直在探索多样化的变现方式，在现有的订阅模式之外，广告被认为是一大重要的潜在营收来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-go/">Introducing ChatGPT Go , now available worldwide | OpenAI</a></li>
<li><a href="https://www.marketingdive.com/news/chatgpt-to-begin-testing-ads-as-generative-ai-competition-heats-up/809964/">ChatGPT to begin testing ads as generative AI competition heats up | Marketing Dive</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#Generative AI`, `#AI Monetization`, `#Digital Advertising`

---

<a id="item-15"></a>
## [绿联 MiniMax 推龙虾应用 让 NAS 变智脑](https://www.aibase.com/zh/news/26221) ⭐️ 7.0/10

领先 NAS 品牌绿联与 AI 企业 MiniMax 达成深度战略合作，推出一键部署的 OpenClaw（龙虾）应用，将 MiniMax 大模型原生内嵌到绿联 NAS 中，把消费级私有云转变为本地私有 AI 大脑。即日起至 2026 年 4 月 12 日，所有绿联 NAS 用户都可享受该应用 30 天的全功能免费试用。 这次合作极大简化了此前为消费级私有云添加大模型能力的复杂流程，让普通消费者和小微企业都能更便捷地获得私有本地 AI 能力。它也为 2026 年消费级私有云产品的智能化升级指明了新方向。 不同于以往需要极客手动调试 Docker 环境、配置复杂 API 的 DIY 部署方案，OpenClaw 可直接在绿联 UGOS Pro 应用中心一键安装完成。该 AI 功能将率先适配绿联 DXP 系列和即将推出的 iDX 系列 NAS 设备。

telegram · AI_News_CN · Mar 16, 01:16

**背景**: NAS 即网络附加存储，是一种本地存储用户数据的私有云设备，相比公有云能为用户提供更好的数据隐私控制。UGOS Pro 是绿联专为自家 NAS 产品线开发的专有 Linux 操作系统。MiniMax 是一家领先的通用人工智能公司，开发了适用于推理、编码和长上下文任务的高性能大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://needtoknowit.com.au/blog/ugreen-ugos-pro-review-nas-software-and-ecosystem-explained/">UGREEN UGOS Pro Review — NAS Software and Ecosystem Explained — Need to Know IT</a></li>
<li><a href="https://github.com/openclaw/lobster">GitHub - openclaw/lobster: Lobster is a Openclaw-native workflow shell: a typed, local-first “macro engine” that turns skills/tools into composable pipelines and safe automations—and lets Openclaw call those workflows in one step.</a></li>
<li><a href="https://github.com/MiniMax-AI/MiniMax-M1">GitHub - MiniMax-AI/MiniMax-M1: MiniMax-M1, the world's first open-weight, large-scale hybrid-attention reasoning model. · GitHub</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Private AI`, `#NAS`, `#AI Deployment`

---

<a id="item-16"></a>
## [阅文作家助手 Claw 开启创作内测](https://www.aibase.com/zh/news/26223) ⭐️ 7.0/10

3 月 15 日，阅文集团推出的国内首个网文创作专属 AI 智能体“作家助手 Claw”正式开启内测，该产品基于阅文自研的垂类大模型“阅文妙笔”打造。它可为网文创作者提供多角色全流程创作辅助，并且采用了隐私优先的本地数据存储方案。 本次落地标志着 AI 在网文垂直行业的应用从基础通用内容生成阶段迈入端到端流程治理阶段，是行业发展的关键里程碑。它将降低网文创作门槛，实现更高效的工业化协同创作，提升整个网文产业的 IP 运营效率。 Claw 基于阅文集团 2023 年发布的国内首个网文垂类大模型“阅文妙笔”打造，目前已支持 QQ 机器人交互，所有用户数据均存储在本地以保障创作者隐私安全。产品计划通过持续灰度测试和数据喂养，最终进化为集编辑、运营、经纪人等多角色于一体的全能创作助理。

telegram · AI_News_CN · Mar 16, 01:16

**背景**: 阅文集团是中国最大的网络文学平台，在 2023 年 7 月正式发布了国内首个网文行业专属大语言模型“阅文妙笔”。垂类领域大模型是指针对特定行业数据训练得到的 AI 模型，相比通用大模型能更好适配具体场景需求，输出更贴合行业要求的结果。面向内容创作的 AI 智能体是可以为创作者提供全流程多任务支持的 AI 系统，而非仅能提供单次内容生成服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://m.nbdpress.com/a/49062">China Literature releases first large-scale model for webnovel</a></li>
<li><a href="https://kr-asia.com/tencents-china-literature-unveils-industrys-first-large-language-model-for-writers">Tencent’s China Literature unveils industry's first large ...</a></li>
<li><a href="https://hellotars.com/ai-agents/novel-writer-ai-agent">Novel Writer AI Agent For Creative Fiction Writing by Tars</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Vertical Large Model`, `#AI Writing`, `#Content Creation`, `#Product Launch`

---

<a id="item-17"></a>
## [企业微信 OpenClaw 接入重大升级](https://www.aibase.com/zh/news/26224) ⭐️ 7.0/10

企业微信为其 OpenClaw AI 接入推出了重大升级，为企业 AI 智能体新增了扫码一键部署和自动化文档操作能力。目前已有多家主流云服务商与模型生态厂商完成了对本次新版本的适配工作。 本次升级大幅降低了企业 AI 智能体的应用门槛，推动实用 AI 更深地融入企业办公流程。它也反映了大模型开发从参数竞争转向实际工程落地的整体行业趋势。 AI 智能体现在可根据简单的文字指令自动创建文档并写入内容，平台配备了严格的权限隔离机制，仅允许 AI 智能体编辑自身创建的文档，方便员工后续精调 AI 生成的内容。管理员可通过腾讯云后台完成一键扫码授权部署，无需进行复杂的底层开发。

telegram · AI_News_CN · Mar 16, 01:27

**背景**: OpenClaw 是一款免费开源的自主 AI 智能体，可通过大语言模型执行任务，以消息平台作为主要用户界面。KimiClaw 是面向专业人士、支持低门槛工作流自动化的 AI 工作空间，智谱 AI 推出的 AutoClaw 则是面向中国用户的可一键安装的本地版 OpenClaw 产品。企业微信是腾讯推出的、被企业广泛使用的企业级办公协同平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw</a></li>
<li><a href="https://autoglm.zhipuai.cn/autoclaw/">AutoClaw（澳龙）- OpenClaw一键安装 | 飞书集成 | AI助手下载</a></li>
<li><a href="https://www.linkedin.com/pulse/kimiclaw-ai-workspace-structured-environment-where-scales-goldie-qkcyc">KimiClaw AI Workspace: Structured Environment Where Automation...</a></li>

</ul>
</details>

**标签**: `#Enterprise AI`, `#AI Agents`, `#Digital Transformation`, `#Workflow Automation`

---

<a id="item-18"></a>
## [多国预警 AI 深度伪造语音诈骗](https://www.aibase.com/zh/news/26225) ⭐️ 7.0/10

Techradar 一项覆盖六国的最新大规模调查显示，冒充熟人实施诈骗的 AI 深度伪造语音诈骗正在全球激增，有 24%的消费者无法从听感上区分真假人声。调查指出 55 岁以上人群人均经济损失是年轻受害者的三倍，此类诈骗的年复合增长率达到 16%。 这是一种快速蔓延的新兴公共安全与网络安全威胁，对老年人等弱势群体的伤害尤为严重，同时它也凸显了业界和政府亟需采取协同行动，应对 AI 赋能诈骗带来的日益增长的风险。 本次调查覆盖了美、英、加、法、德、西六国超过 1.2 万名消费者，安全专家提出不能仅依靠普通用户识别诈骗，呼吁运营商加快部署“AI 盾牌”系统，用技术手段过滤非法合成语音。

telegram · AI_News_CN · Mar 16, 01:27

**背景**: AI 深度伪造语音又称语音克隆，是生成式人工智能的一种应用，可以生成足以以假乱真、模仿特定个人的语音，甚至能生成原说话者从未说过的内容。低成本生成式 AI 工具的普及让不法分子很容易获取这项技术，而当前的检测技术往往难以可靠区分深度伪造语音和真实人声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Audio_deepfake">Audio deepfake - Wikipedia</a></li>
<li><a href="https://www.nbcnews.com/tech/security/ai-voice-cloning-software-flimsy-guardrails-report-finds-rcna195131">AI can steal your voice, and there's not much you can do about it Beyond Cybersecurity: Deepfake Audio Is An Evidence Crisis AI Voice Cloning: What It Is & the Technology Behind It Top 7 AI Voice Cloning Tools for Realistic Speech 2026 (PDF) A Systematic Literature Review on AI Voice Cloning ...</a></li>

</ul>
</details>

**标签**: `#AI Deepfake`, `#Voice Fraud`, `#Cybersecurity`, `#Generative AI`

---

<a id="item-19"></a>
## [万兴推出国内首个全链路 AI 漫剧平台](http://reelmate.cn/) ⭐️ 7.0/10

2026 年 3 月 13 日，万兴科技联手生数科技 Vidu 推出了国内首个精品 AI 漫剧全链路创作平台万兴剧厂（Reelmate）。该平台产出的一部漫剧作品上线仅 29 小时，播放量就突破了 2 亿次。 本次发布标志着 AI 漫剧制作从小作坊式摸索正式迈入工业化量产阶段，开启了 AIGC 在短剧内容领域的大规模商业化周期。它有望重构整个网络短剧行业的生产逻辑与成本结构。 该平台深度整合了生数科技领先的 ViduQ3 漫剧大模型，解决了 AI 生成视频中长期存在的跨集角色不一致核心痛点，分镜一抽可用率达到 80%。它还为真人剧的 Agent 分镜创作带来了 6 倍效率提升，一个 3 人团队使用该平台仅用 5 天就能交付整整 75 集成片漫剧。

telegram · AI_News_CN · Mar 16, 01:27

**背景**: AI 漫剧是 AIGC 内容创作中增长快速、潜力巨大的细分赛道，行业预测未来三年全球 AI 漫剧市场规模将突破千亿元。在本次平台发布前，已有 AI 生成工具始终无法解决跨集角色形象不一致等核心问题，导致 AI 漫剧无法实现工业化大规模量产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.3dmgame.com/news/202602/3937037.html">国产AI视频 模 型 ViduQ 3 火出圈 复刻高燃动 漫 战斗_3DM单机</a></li>
<li><a href="https://www.ithome.com/0/927/864.htm">绘梦工坊全链路 AI 漫剧创作平台：单项目制作周期压缩至 3 天，入局千...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2000469156861089713">AI漫剧制作工具大集合：11款漫剧制作软件，免费付费都有 - 知乎</a></li>

</ul>
</details>

**标签**: `#AIGC`, `#Generative AI`, `#AI Video Generation`, `#Content Creation`

---

<a id="item-20"></a>
## [马斯克 xAI 重组 推出数字擎天柱项目](https://www.aibase.com/zh/news/26228) ⭐️ 7.0/10

埃隆·马斯克承认其 AI 公司 xAI 的大多数创始成员已经离职，为公司早期管理不当道歉，目前正通过重新联系过往合格候选人、招聘 AI 编程工具初创公司 Cursor 的新高管来重组团队。他同时宣布 xAI 与特斯拉合作的“数字擎天柱”AI 项目将在 6 个月后开放用户测试。 作为全球最受关注的高估值 AI 初创公司之一，xAI 的大规模人才流失和重组凸显了当前全球 AI 行业对顶尖人才的激烈争夺。即将推出的数字擎天柱联合项目将 AI 智能体的应用场景拓展到了消费汽车和生产力领域，将会影响面向消费者的 AI 产品的发展方向。 xAI 最初的创始团队目前仅剩下两名成员留在公司，在与 SpaceX 合并后，xAI 的估值已经达到 2500 亿美元。数字擎天柱是一款旨在帮助车主处理办公任务的实时智能 AI 系统，未来将部署在特斯拉的全球超级充电网络中，提供强大的分布式计算能力。

telegram · AI_News_CN · Mar 16, 01:46

**背景**: xAI 是埃隆·马斯克创立的人工智能初创公司，近期被 SpaceX 收购并完成合并。Cursor 是总部位于旧金山的初创公司 Anysphere 开发的热门 AI 辅助代码编辑器，在开发者群体中积累了大量用户，与 GitHub Copilot 等产品直接竞争。数字擎天柱是 xAI 和特斯拉合作的联合 AI 项目，也被戏称为 Macrohard 来调侃微软，定位为可以为用户自动化处理办公工作的 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/03/13/elon-musk-xai-co-founders-spacex-ipo.html">Musk says xAI must be 'rebuilt' amid co-founder exodus ...</a></li>
<li><a href="https://www.teslarati.com/tesla-xai-digital-optimus-explained/">What is Digital Optimus? The new Tesla and xAI project explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#xAI`, `#Industry News`, `#Digital Optimus`, `#Team Restructuring`

---

<a id="item-21"></a>
## [马斯克诉 OpenAI 天价官司定档 4 月开庭](https://www.aibase.com/zh/news/26232) ⭐️ 7.0/10

马斯克起诉 OpenAI 及其合作伙伴微软的 1340 亿美元天价索赔案，在近期的法庭听证会结束后已正式定于 2026 年 4 月 28 日开庭审理。法官驳回了 OpenAI 要求剔除马斯克方核心专家证词的动议，同时对马斯克方的赔偿计算逻辑提出了质疑。 这场涉及 AI 行业头部参与者的高风险纠纷是 AI 领域最受关注的法律案件之一，其判决结果很可能会为未来大型 AI 企业围绕创始使命和商业化的冲突树立重要先例。由于马斯克的竞争 AI 创业公司 xAI 是本案背后的核心相关方，该案也将直接影响全球生成式 AI 行业的竞争格局。 马斯克主张 OpenAI 背弃了最初的非营利创始使命，并指控 OpenAI 首席执行官山姆·奥尔特曼存在欺诈行为，而 OpenAI 则反驳称该诉讼是出于商业动机的骚扰，意在为马斯克旗下的 xAI 获取竞争优势。法官将马斯克 1340 亿美元的赔偿计算逻辑称为近乎“凭空捏造”，但仍裁定应由陪审团而非法院来决定专家证词的最终有效性。

telegram · AI_News_CN · Mar 16, 02:03

**背景**: 马斯克是 OpenAI 的早期创始贡献者，在推出自己的竞争 AI 企业前曾向 OpenAI 提供了 3800 万美元的早期资金。xAI 是马斯克在 2023 年 7 月成立的人工智能创业公司，是 SpaceX 旗下的全资子公司，直接在生成式 AI 市场与 OpenAI 展开竞争。驳回动议是美国法院的标准法律程序，指被告以原告诉讼存在法律缺陷为由，正式要求法官剔除部分或全部诉讼请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">xAI (company) - Wikipedia</a></li>
<li><a href="https://www.reuters.com/technology/elon-musks-ai-firm-xai-launches-website-2023-07-12/">Elon Musk launches AI firm xAI as he looks to take on OpenAI | Reuters</a></li>
<li><a href="https://legalterms.net/what-is-a-motion-to-dismiss/">What Is a Motion to Dismiss? - Legal Terms</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#OpenAI`, `#legal dispute`, `#Elon Musk`, `#Microsoft`

---

<a id="item-22"></a>
## [AI 设计方案使犬肿瘤缩小 75%](https://www.aibase.com/zh/news/26234) ⭐️ 7.0/10

澳大利亚 AI 专家 Paul Conyngham 联合使用 ChatGPT、AlphaFold 和 Grok 等多款 AI 模型，为患有晚期肥大细胞癌的爱犬开发了实验性个性化癌症治疗方案，报道显示爱犬的肿瘤已经缩小了 75%。独立专家提醒，由于爱犬同时接受了传统治疗，AI 设计方案的实际贡献目前仍未得到证实。 该案例是结合多款 AI 工具开发个性化癌症治疗方案的典型早期真实应用展示，表明 AI 甚至能够让非医学专业人士处理复杂生物信息来开发个性化治疗方案。它也推动 AI 驱动的个性化医疗从实验室更快走向实际应用，预示着未来医疗研发效率有望获得根本性提升。 该项目始于 2024 年 11 月，由 ChatGPT 建议对肿瘤进行基因组测序，AI 识别靶蛋白并筛选已获 FDA 批准的药物，关键的疫苗设计工作由 Grok 完成。这类 AI 设计的个性化治疗方案预估总成本在 2 万到 5 万美元之间，要证明其长期安全性和有效性仍存在诸多巨大挑战。

telegram · AI_News_CN · Mar 16, 02:45

**背景**: AlphaFold 是谷歌 DeepMind 开发的人工智能系统，能够从氨基酸序列出发高精度预测蛋白质的三维结构，这项技术突破让其核心开发者获得了 2024 年诺贝尔化学奖的一半奖项。Grok 是 xAI 开发的生成式 AI 聊天机器人，于 2023 年 11 月推出，支持实时获取网络信息完成多种任务。癌症个性化治疗会根据个体特定的肿瘤特征调整干预方案，普遍认为相比通用统一治疗能带来更好的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI in healthcare`, `#personalized medicine`, `#generative AI`, `#AlphaFold`, `#cancer research`

---