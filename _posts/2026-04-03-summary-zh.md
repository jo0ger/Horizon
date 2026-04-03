---
layout: default
title: "Horizon Summary: 2026-04-03 (ZH)"
date: 2026-04-03
lang: zh
---

> From 47 items, 24 important content pieces were selected

---

1. [Google DeepMind 发布开源 Gemma 4 模型](#item-1) ⭐️ 9.0/10
2. [谷歌 DeepMind 发布开源 Gemma 4 大模型](#item-2) ⭐️ 9.0/10
3. [微软发布三款自研人工智能基础模型](#item-3) ⭐️ 9.0/10
4. [Google 发布开放模型 Gemma 4 系列](#item-4) ⭐️ 9.0/10
5. [谷歌正式发布开源大模型 Gemma 4](#item-5) ⭐️ 9.0/10
6. [谷歌发布 Apache 2.0 许可的 Gemma4 开源模型](#item-6) ⭐️ 9.0/10
7. [vLLM v0.19.0 正式发布](#item-7) ⭐️ 8.0/10
8. [AMD 发布开源 Lemonade 本地大语言模型服务器](#item-8) ⭐️ 8.0/10
9. [阿里发布千问 Qwen3.6-Plus 大模型](#item-9) ⭐️ 8.0/10
10. [Nekogram 12.5.2 被曝存在窃取手机号后门](#item-10) ⭐️ 8.0/10
11. [Arm 将在中国销售 AGI 服务器 CPU](#item-11) ⭐️ 8.0/10
12. [微软加速自研 AI 模型 目标 2027 年自主](#item-12) ⭐️ 8.0/10
13. [中国发布首个原生物理 AI 平台 ORCA Lab 1.0](#item-13) ⭐️ 8.0/10
14. [苹果 LGTM 让 Vision Pro 实现 4K 3D 渲染](#item-14) ⭐️ 8.0/10
15. [微软推出全球最高精度语音转写模型](#item-15) ⭐️ 8.0/10
16. [前 Azure 工程师发文批评侵蚀信任的决策](#item-16) ⭐️ 7.0/10
17. [Hacker News 讨论新版 Cursor 3 AI 编辑器](#item-17) ⭐️ 7.0/10
18. [阿里发布闭源千问 Qwen3.6-Plus 大模型](#item-18) ⭐️ 7.0/10
19. [2025 年英伟达中国 AI 芯片份额降至 55%](#item-19) ⭐️ 7.0/10
20. [ElevenLabs 推出 ElevenMusic AI 音乐应用](#item-20) ⭐️ 7.0/10
21. [Claude Code 泄露后 GitHub 出现钓鱼陷阱](#item-21) ⭐️ 7.0/10
22. [OpenAI 关停 Sora 后收购 TBPN](#item-22) ⭐️ 7.0/10
23. [谷歌 Vids 集成 Veo3.1 支持 AI 虚拟形象互动](#item-23) ⭐️ 7.0/10
24. [谷歌拟建天然气电厂供 AI 数据中心](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google DeepMind 发布开源 Gemma 4 模型](https://deepmind.google/models/gemma/gemma-4/) ⭐️ 9.0/10

Google DeepMind 发布了全新的开源 Gemma 4 大语言模型系列，相比前代新增了对推理、多模态和工具调用的原生支持。一个高热度的 Hacker News 讨论串汇集了社区测试结果、基准测试对比，以及用户分享的量化版本模型和运行指南。 作为最受欢迎的开源大语言模型系列之一的重大更新，Gemma 4 拥有出色的基准性能和更丰富的能力，能够让开发者和个人用户更易获得高性能的开源 AI。本次发布延续了行业打造更强大、可在消费级硬件本地运行的开源模型的趋势。 Gemma 4 系列包含从 2B 到 31B 的多个参数规格，其中 26B-a4b 这类混合专家模型变体拥有出色性能，适合在笔记本电脑本地运行。有用户反馈 31B 参数的 checkpoint 存在漏洞，无论输入什么提示词都只会输出重复分隔符，不过托管在 AI Studio API 的版本可以正常运行。

hackernews · jeffmcjunkin · Apr 2, 16:10

**背景**: Gemma 是 Google DeepMind 推出的开源大语言模型系列，旨在方便开发者进行开发和部署，其技术源自支持谷歌闭源 Gemini 模型的相同研究。开源大语言模型会以宽松许可证公开发布，允许开发者本地运行、修改和部署模型，无需依赖第三方 API 服务。

**社区讨论**: 大多数参与测试的社区用户都称赞 Gemma 4 的性能，有用户指出 26B-a4b 变体在笔记本本地运行就能输出他见过的质量最好的图像生成结果，社区成员已经提前分享了预量化版本来简化本地运行流程。有用户分享了 Gemma 4 和 Qwen 3.5 等竞品的基准测试对比，指出入门级 Gemma 4 E4B 的性能可以和其他系列的 8B 至 9B 模型竞争，同时也有人反馈用于本地部署的 31B 模型检查点存在故障。

**标签**: `#large language models`, `#open AI`, `#Google DeepMind`, `#Gemma 4`, `#machine learning releases`

---

<a id="item-2"></a>
## [谷歌 DeepMind 发布开源 Gemma 4 大模型](https://simonwillison.net/2026/Apr/2/gemma-4/#atom-everything) ⭐️ 9.0/10

谷歌 DeepMind 发布了 Gemma 4，这是四款采用宽松 Apache 2.0 许可的全新开源多模态大语言模型系列，针对端侧设备使用优化，拥有突破性的参数效率。该系列包含 2B、4B、31B 稠密模型变体和一个 26B-A4B 混合专家变体，原生支持视觉、视频处理，较小尺寸的模型还原生支持音频输入。 这次发布推动了小型高能力端侧 AI 这个快速发展领域的进步，它以极低参数规模实现了高智能水平，还采用完全宽松的开源许可，支持广泛的商业和非商业使用。它让开发者可以在消费设备上部署强大的多模态推理 AI，无需依赖云端连接。 较小的 2B 和 4B 模型采用分层嵌入（PLE）技术，减少推理过程中载入内存的有效参数量，而目前 31B 稠密模型的 GGUF 构建存在问题，无法生成有效输出。LM Studio 和 Ollama 这类常见的本地大模型运行工具目前还不支持小模型的原生音频输入功能。

rss · Simon Willison · Apr 2, 18:28

**背景**: 参数效率指的是在不提升单次推理所需计算量的前提下提升模型性能的技术路线。混合专家（Mixture-of-Experts，MoE）是一种神经网络架构，它会将每个输入令牌路由到一小部分称为专家的专用子网络，在保持总参数量更高以获得更好知识容量的同时，维持每个令牌的计算量处于较低水平。分层嵌入（Per-Layer Embeddings，PLE）是一种优化技术，通过为每层添加小型令牌嵌入来提升模型性能，同时不会增加端侧推理过程中需要载入内存的激活参数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Mixture of Experts (MoE) | Sebastian Raschka, PhD What Is Mixture of Experts (MoE)? How It Works (2026) How Mixture-of-Experts LLMs Work. An innovative approach to ... What Is Mixture of Experts (MoE)? How Modern LLMs Get ...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/gemma-3n">Gemma 3n model overview | Google AI for Developers</a></li>
<li><a href="https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/">Introducing Gemma 3n: The developer guide - Google Developers Blog</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#open-ai`, `#google-deepmind`, `#on-device-ai`, `#parameter-efficient-models`

---

<a id="item-3"></a>
## [微软发布三款自研人工智能基础模型](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) ⭐️ 9.0/10

微软在 4 月 2 日发布了三款完全自研的基础 AI 模型，分别是 MAI-Transcribe-1、MAI-Voice-1 和 MAI-Image-2，分别覆盖语音转写、语音生成和图像生成领域。这三款模型现已通过 Microsoft Foundry 和全新的 MAI Playground 向用户开放使用。 这次发布标志着微软在打造自有竞争力基础 AI 阵容上迈出重要一步，能够降低其对外部模型合作方的依赖，同时加剧生成式 AI 市场的竞争。这些模型面向高商业价值的企业场景，还可以提升微软自身 C 端和 B 端产品的 AI 能力。 MAI-Transcribe-1 在 FLEURS 基准测试的 25 种主流语言上表现均超过 OpenAI 的 Whisper-large-v3，平均词错误率仅为 3.8%。MAI-Voice-1 可在 1 秒内生成 60 秒长度的语音，还支持用数秒样本音频定制音色，MAI-Image-2 的生成速度相比前代至少提升两倍，已经开始向 Bing 和 PowerPoint 推送。

telegram · zaihuapd · Apr 2, 11:31

**背景**: Microsoft Foundry 前身为 Azure AI Studio，是微软 Azure 上的统一 AI 开发平台，允许开发者构建、部署和扩缩 AI 应用，内置企业级安全与治理工具。MAI Playground 是供开发者和用户直接测试微软新款 MAI 模型的公开测试空间，目前仅对美国地区用户开放。FLEURS 是用于评估自动语音识别模型跨语言性能的标准多语言基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://azure.microsoft.com/en-us/products/ai-foundry/">Microsoft Foundry | Microsoft Azure</a></li>
<li><a href="https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/">Today we're announcing 3 new world class MAI models, available in Foundry | Microsoft AI</a></li>
<li><a href="https://blog.csdn.net/gitblog_00009/article/details/150778442">Voxtral-Mini-3B-2507性能 基 准 测 试 -CSDN博客</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#foundation models`, `#microsoft`, `#speech ai`, `#image generation`

---

<a id="item-4"></a>
## [Google 发布开放模型 Gemma 4 系列](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) ⭐️ 9.0/10

Google 正式发布了开放大语言模型系列 Gemma 4，该系列共有四种不同规格，覆盖从手机到高端工作站的各类设备，且以宽松的 Apache 2.0 许可证开放。新模型系列支持多模态输入和高级 AI Agent 工作流，小规格版本专门针对端侧离线运行优化。 本次发布将 Google 级别的模型能力带到了端侧设备，扩大了高性能开放 AI 的可及范围，同时通过允许商业使用和自定义修改的宽松许可证，巩固了 Google 在快速发展的开放 AI 生态中的地位。它满足了开发者和企业对可在不同硬件上部署的灵活开放模型选项日益增长的需求。 四个型号分别为 2B E2B、4B E4B、26B MoE 和 31B Dense，其中 2B 和 4B 版本除图像和视频处理外，还原生支持音频输入。31B dense 模型目前在 Arena AI 文本榜单的开放模型中排名第三，26B MoE 模型排名第六，而初代 Gemma 家族累计下载量已经超过 4 亿次，衍生版本超过 10 万个。

telegram · zaihuapd · Apr 2, 16:12

**背景**: Gemma 是 Google 推出的开放大语言模型系列，基于 Google 闭源 Gemini 模型的相同底层技术构建，旨在为开发者提供可自定义修改的开源替代方案。MoE 是混合专家模型的缩写，是一种神经网络架构，它将模型计算拆分到多个称为专家的小型专用子网络中，能够在不按比例提升推理成本的前提下实现更高的整体性能。端侧 AI 指直接在手机、笔记本电脑这类本地用户硬件上运行的 AI 模型，不需要依赖云服务器，因此支持离线使用，也能更好地保护数据隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Gemma 4 : Our most capable open models to date</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/On-device_artificial_intelligence">On-device artificial intelligence</a></li>

</ul>
</details>

**标签**: `#large language models`, `#open AI`, `#Gemma 4`, `#on-device AI`, `#Google`

---

<a id="item-5"></a>
## [谷歌正式发布开源大模型 Gemma 4](https://www.aibase.com/zh/news/26812) ⭐️ 9.0/10

北京时间 2025 年 4 月 3 日，谷歌正式发布新一代开源大模型 Gemma 4，该模型包含四种不同规格，支持多模态输入与端侧部署。其中 31B 稠密版本在 Arena AI 文本榜单中位列全球开源模型第三，在逻辑推理和函数调用上拥有领先性能。 作为谷歌推出的重量级新一代开源大模型，Gemma 4 采用宽松的 Apache 2.0 许可开放，降低了开发者搭建前沿本地化隐私 AI 应用的门槛，将对全球开源 AI 生态产生深远影响。它还为开源模型赋能自主智能体工作流设立了新标准，推动了端侧 AI 技术的发展。 Gemma 4 基于 Gemini 3 技术栈构建，共包含四个规格：2.3B E2B、4.5B E4B、26B MoE 和 31B 稠密模型；其中 31B 非量化版本可在单块 80GB H100 显卡上运行，量化版本兼容消费级显卡。小型的 E2B 和 E4B 原生支持语音输入，通过 PLE 嵌入技术可在树莓派和智能手机上实现低延迟运行，还支持 128K 长上下文窗口。

telegram · AI_News_CN · Apr 3, 01:02

**背景**: Apache 2.0 是由 Apache 软件基金会推出的宽松自由软件许可证，允许用户出于任何目的使用、修改、分发和再分发修改后的代码，对商业和非商业开源项目都十分友好。混合专家架构（MoE）是一种大语言模型架构，它通过只为每个输入激活小部分模型参数（称为专家），在提升模型性能的同时控制计算开销。嵌入是文本等数据的向量表示，是检索增强生成、AI 智能体记忆等核心 AI 功能的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>

</ul>
</details>

**标签**: `#large language model`, `#open-source AI`, `#Gemma 4`, `#Google AI`, `#end-side AI`

---

<a id="item-6"></a>
## [谷歌发布 Apache 2.0 许可的 Gemma4 开源模型](https://www.aibase.com/zh/news/26816) ⭐️ 9.0/10

谷歌正式推出新一代开源大语言模型 Gemma4，采用宽松的 Apache 2.0 许可证，一改此前 Gemma 版本使用的限制性自定义许可协议。新模型在多项基准测试中取得了更好的性能，同时对现有开发生态的兼容性也得到了提升。 这次协议变更消除了基于 Gemma 进行商业开发和开源开发的主要法律障碍，让更多开发者和中小企业都可以使用谷歌开发的高质量 AI 技术。这也标志着谷歌在开放 AI 发展方向上的重大战略转向，将影响全球开源大模型生态的竞争格局。 Gemma4 支持在服务器、手机、树莓派等多种设备上离线本地部署，还能无缝融入 Android 等同样采用 Apache 2.0 许可的现有生态，大幅降低了开发者的部署门槛。

telegram · AI_News_CN · Apr 3, 01:10

**背景**: Gemma 是由 Google DeepMind 和谷歌其他团队联合开发的开源大语言模型系列，名称源自拉丁语中意为宝石的词汇。Apache 2.0 许可证是业界广泛认可的宽松自由软件许可，允许用户出于任何目的（包括商业用途）自由使用、修改和分发被授权的软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/">Google announces Gemma 4 open AI models, switches to Apache 2 ...</a></li>
<li><a href="https://www.zdnet.com/article/google-gemma-4-fully-open-source-powerful-local-ai/">Google's Gemma 4 model goes fully open-source and ... - ZDNET</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License - Wikipedia</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#large language model`, `#Google Gemma`, `#Apache 2.0 license`

---

<a id="item-7"></a>
## [vLLM v0.19.0 正式发布](https://github.com/vllm-project/vllm/releases/tag/v0.19.0) ⭐️ 8.0/10

vllm 项目在 GitHub 上发布了开源大语言模型推理引擎 vLLM 的 0.19.0 版本。这是一个功能丰富的小版本更新，为该工具带来了重要的增量改进。 vLLM 是全球 AI/ML 社区中使用最广泛、影响力最大的开源大语言模型推理与服务工具之一。对这个核心工具的改进将惠及数千个在研究或生产场景中部署大语言模型的开发者和机构。 作为一个功能小版本，v0.19.0 专注于对现有 vLLM 代码库进行增量改进，而非大规模架构改动，在该项目已经领先行业的吞吐量和内存效率基础上继续优化。

github · khluu · Apr 3, 02:19

**背景**: vLLM 是一款开源的高吞吐量、内存高效的大语言模型推理与服务引擎，最初由加州大学伯克利分校的 Sky 计算实验室开发。它的核心创新是 PagedAttention 内存管理算法，相比标准 HuggingFace 流水线可提供高达 24 倍的推理吞吐量提升。它现在是一个由社区驱动的项目，可用于研究和大规模生产部署，截至 2026 年已经在 GitHub 获得了超过 7.49 万星标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory ...</a></li>
<li><a href="https://vllm.ai/">vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/">vLLM</a></li>

</ul>
</details>

**标签**: `#large language models`, `#machine learning inference`, `#open source software`, `#release announcement`

---

<a id="item-8"></a>
## [AMD 发布开源 Lemonade 本地大语言模型服务器](https://lemonade-server.ai/) ⭐️ 8.0/10

AMD 正式推出了 Lemonade，这是一款支持在 AMD CPU、GPU 和 NPU 硬件上运行推理的开源本地多模态大语言模型推理服务器。该项目统一了 AMD 消费级和企业级硬件上对文本、图像和音频 AI 模型的推理支持。 该发布解决了 AMD 硬件长期以来 ROCm 本地推理体验存在的痛点，提供了官方一站式方案，简化了本地 AI 的依赖和驱动配置。它还能利用 AMD 集成 NPU 在现代锐龙系统上实现更低功耗、更快的本地 AI 推理，推动端侧本地 AI 生态发展。 Lemonade 支持 ROCm、Vulkan、CPU、GPU 和 NPU 等多种后端，覆盖了语音合成、语音识别、文本生成、图像生成和图像编辑等功能。Lemonade 使用的 NPU 专属内核和模型仍然是专有的，并未以开源形式发布。

hackernews · AbuAssar · Apr 2, 11:04

**背景**: NPU 即神经网络处理单元，是专用硬件加速器，它针对神经网络推理运算进行加速，功耗比通用 CPU 和 GPU 更低。多模态大语言模型服务器可以处理并运行多种 AI 数据的推理，包括文本、图像和音频，支持一体化的本地 AI 工作流。ROCm 是 AMD 针对 GPU 加速高性能计算和机器学习推理打造的开源软件平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/lemonade-for-local-ai.html">Lemonade by AMD: A Unified API for Local AI Developers</a></li>
<li><a href="https://medium.com/@waranmadesh826/what-is-an-npu-and-why-it-matters-in-the-ai-era-36b83590323b">What Is an NPU and Why It Matters in the AI Era | Medium</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-llm">What is a multimodal LLM (MLLM)? - IBM</a></li>

</ul>
</details>

**社区讨论**: 长期用户称赞 Lemonade 稳定的开发节奏和面向 AMD 硬件的丰富功能，指出它已经支持现代 AMD 系统上大多数常见本地 AI 工作负载。许多评论者欢迎这款官方工具解决 ROCm 糟糕的用户体验，但目前对于 NPU 实际推理性能相比 AMD 独立 GPU 表现仍有疑问。部分社区成员已经注意到 NPU 组件是专有的，并表达了对完全开源 NPU 支持的诉求。

**标签**: `#local LLMs`, `#AMD`, `#open source`, `#inference server`, `#AI runtime`

---

<a id="item-9"></a>
## [阿里发布千问 Qwen3.6-Plus 大模型](https://t.me/zaihuapd/40658) ⭐️ 8.0/10

阿里巴巴发布了新一代千问大语言模型 Qwen3.6-Plus，整体性能相比前代获得大幅提升。该模型的编程能力表现已经接近顶级的 Claude 系列模型，并且实现了可用的「氛围编程」，只需自然语言提示即可让 AI 自主完成端到端编码工作。 本次发布代表着开放能力大模型在实用化 AI 软件工程领域取得了实质性进展，让端到端自主 AI 编码距离实际落地应用更进一步。它缩小了中国本土大模型与全球顶级编程大模型之间的性能差距，可为开发者提供能力更强的本土化 AI 辅助开发选项。 Qwen3.6-Plus 具备原生多模态理解与推理能力，在智能体编程评测 SWE-bench 和真实世界智能体任务评测 Claw-Eval 两项权威测试中，编程表现接近 Claude 系列模型。在前端网页开发、仓库级复杂任务等实测场景中，该模型可以自主拆解任务、规划路径、测试修改直至完成全部任务。

telegram · zaihuapd · Apr 2, 05:02

**背景**: SWE-bench 是一个标准评测基准，用于测试大语言模型修复来自 GitHub 的真实编程问题的能力，统计模型能通过生成补丁解决的问题占比。Claw-Eval 是专门用于评测 AI 智能体完成真实世界任务能力的端到端基准，所有测试任务都经过人工验证，可以准确衡量智能体完成完整任务的能力。本文中的「氛围编程」和已有的 Java 实时应用 Atmosphere 框架无关，它指的是用简单自然语言提示驱动 AI 自主完成完整编码项目的开发工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/swe-bench-verified">SWE-Bench Verified Leaderboard</a></li>
<li><a href="https://dev.to/sky_05/new-benchmark-for-open-source-agents-what-is-claw-eval-how-step-35-flash-secured-the-2-spot-592d">New Benchmark for Open-Source Agents: What is Claw-Eval? How ...</a></li>
<li><a href="https://github.com/Atmosphere/atmosphere">GitHub - Atmosphere/atmosphere: Real-time transport layer for ...</a></li>

</ul>
</details>

**标签**: `#large language model`, `#Qwen`, `#AI coding`, `#multimodal AI`, `#model release`

---

<a id="item-10"></a>
## [Nekogram 12.5.2 被曝存在窃取手机号后门](https://thebadinteger.github.io/nekogram-phone-exfiltration/) ⭐️ 8.0/10

安全研究人员发现第三方 Telegram 客户端 Nekogram 12.5.2 的 Google Play 版本中存在经过混淆的后门，会静默窃取已登录用户的手机号并将其发送至开发者控制的 Telegram 机器人。这段恶意代码没有出现在项目公开的 GitHub 源码中，开发者对机器人用途的解释与代码实际行为不符。 这是一起针对广泛分发的开源移动应用用户的已确认供应链攻击，意味着信任该项目开源模式的用户无法保证分发版本和公开源码一致。该事件会让应用的大量用户面临身份和账号泄露风险，同时也凸显了即使是开源项目，信任预编译应用分发版本也存在风险。 后门位于经过混淆的 Extra.java 文件中，会从最多 8 个已登录账号中提取手机号，并通过加密的 Telegram 内联查询将数据泄露给机器人@nekonotificationbot。只有 Google Play 分发的预编译 APK 包含该后门，从公开 GitHub 源码自行编译的版本不包含这段恶意代码。

telegram · zaihuapd · Apr 2, 12:58

**背景**: Nekogram 是面向 Telegram 即时通讯平台的开源第三方客户端，提供官方客户端没有的额外自定义功能。第三方 Telegram 客户端受到想要更多掌控应用体验的用户欢迎，许多用户因为它们开源就对其放下戒心。混淆是恶意软件常用来隐藏恶意代码、躲避安全工具检测的技术。Telegram 内联查询是允许机器人在任意聊天的输入框直接接收用户请求的功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Nekogram/Nekogram?search=1">Nekogram / at main · Nekogram / Nekogram · GitHub</a></li>
<li><a href="https://core.telegram.org/bots/inline">Inline Bots</a></li>
<li><a href="https://attack.mitre.org/techniques/T1027/">Obfuscated Files or Information, Technique T1027 - MITRE ATT&CK®</a></li>

</ul>
</details>

**标签**: `#security vulnerability`, `#malware`, `#telegram client`, `#supply chain attack`

---

<a id="item-11"></a>
## [Arm 将在中国销售 AGI 服务器 CPU](https://www.tomshardware.com/pc-components/cpus/arm-to-sell-its-new-agi-cpu-in-china-we-would-expect-the-demand-for-this-product-to-be-just-as-strong-in-china-as-it-is-in-the-rest-of-the-world) ⭐️ 8.0/10

Arm 宣布将把其最新发布的、基于 Neoverse V3 架构的 136 核 AGI 服务器 CPU 销往中国市场，并且确认这款成品处理器符合现行出口管制规定，而 Neoverse V3 IP 核心目前无法向中国开发者授权。 这一决定为现有的半导体出口限制找到了变通方案，既帮助 Arm 维持在中国的市场份额，又能满足中国对 AI 基础设施硬件日益增长的需求，同时会对全球 AI 硬件供应链和出口管制格局产生影响。 这款 136 核 AGI 服务器 CPU 是 Arm35 年来推出的首款自有数据中心芯片，面向基础设施与超算领域的通用人工智能 workload 设计，成品处理器适用的出口管制规则与 IP 核心授权不同。

telegram · zaihuapd · Apr 3, 02:30

**背景**: Neoverse 是 Arm 推出的一系列 64 位处理器核心，专门面向数据中心、边缘计算和高性能计算场景设计，Neoverse V3 是该系列面向高级 AI 和高性能系统的最新一代产品。半导体 IP 核是预先设计好的可重复使用逻辑单元，开发者可以购买 IP 授权来自行设计芯片，而成品服务器 CPU 是已经制造完成、可直接安装在服务器中使用的完整处理器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_Neoverse">ARM Neoverse - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_intellectual_property_core">Semiconductor intellectual property core - Wikipedia</a></li>
<li><a href="https://awesomeagents.ai/news/arm-agi-cpu-first-chip-35-years/">Arm Launches AGI CPU , Its First Chip in 35 Years | Awesome Agents</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#AI Hardware`, `#Export Control`, `#Server CPU`

---

<a id="item-12"></a>
## [微软加速自研 AI 模型 目标 2027 年自主](https://www.aibase.com/zh/news/26817) ⭐️ 8.0/10

在与 OpenAI 的合作协议松绑后，微软正在加速自研大模型战略，目标是在 2027 年前实现世界领先的图文音频处理能力和完全 AI 技术自主。微软已经取得了早期成果，在 4 月 2 日发布的全新语音转录模型，在测试的 25 种主流语言中有 11 种的表现超过了现有同类产品。 微软通过大规模部署英伟达最新的 GB200 算力集群为这项研发提供支撑，还计划在未来 12 至 18 个月内将底层算力提升至全球领先规模。该计划的核心目标是打造能与 OpenAI 和 Anthropic 模型竞争的前沿 AI 系统。

telegram · AI_News_CN · Apr 3, 01:22

**背景**: 微软多年来一直是 OpenAI 的核心合作伙伴和主要投资方，旗下 Copilot 等现有生成式 AI 产品长期依赖 OpenAI 的模型技术。双方原本的合作协议对微软自主研发通用大模型设置了诸多限制，去年的协议调整解除了这些限制。

**标签**: `#Large Language Models`, `#Microsoft`, `#AI Strategy`, `#Self-developed AI`, `#Generative AI`

---

<a id="item-13"></a>
## [中国发布首个原生物理 AI 平台 ORCA Lab 1.0](https://www.aibase.com/zh/news/26820) ⭐️ 8.0/10

上海松应科技正式发布了 ORCA Lab 1.0，这是中国首个专门面向个人开发者和小型轻量化团队打造的原生物理 AI 开发者平台。该平台通过零代码流程、低成本和单机运行等核心特性，降低了具身智能研发的门槛。 此次发布让物理 AI 与具身智能研究实现普惠化，该领域此前因成本高昂、硬件要求高，仅大型科技公司和顶尖科研机构能够参与。它向更多个人创作者开放了该领域，推动了中国具身智能产业的发展与商用落地。 ORCA Lab 1.0 打破了以往机器人训练对高性能算力集群的依赖，开发者仅用一台普通笔记本电脑就可以流畅运行全流程。它支持覆盖机器人设计、仿真训练到真机部署的全生命周期开发，还提供开放接口鼓励开发者共建开放生态。

telegram · AI_News_CN · Apr 3, 01:35

**背景**: 物理 AI 与具身智能高度相关，指的是能够和物理世界交互的 AI 系统，传统上这类研究需要复杂的动力学模拟和海量计算，因此研发成本极高。数字孪生机器人是实体机器人的虚拟镜像副本，开发者可以在仿真环境中测试训练模型，减少对昂贵实体硬件的依赖和损耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/delltechnologies/2025/12/17/the-ai-native-factory-remaking-manufacturing-with-physical-ai/">Dell Technologies BrandVoice: The AI-Native Factory: Remaking Manufacturing With Physical AI</a></li>
<li><a href="https://eureka.patsnap.com/article/what-is-a-digital-twin-in-robotics">What is a digital twin in robotics? - eureka.patsnap.com</a></li>

</ul>
</details>

**标签**: `#Physical AI`, `#Embodied Intelligence`, `#Developer Platform`, `#AI Tools`

---

<a id="item-14"></a>
## [苹果 LGTM 让 Vision Pro 实现 4K 3D 渲染](https://www.aibase.com/zh/news/26822) ⭐️ 8.0/10

苹果研究团队与香港大学合作推出了 LGTM（Less Gaussians, Texture More）技术框架，解决了 3D 高斯喷溅在高分辨率下的计算瓶颈，让 Apple Vision Pro 能够以更低的计算负载实现 4K 实时 3D 渲染。 这一突破打破了 Vision Pro 这类空间计算设备运行高保真实时 3D 内容的主要障碍，能够为终端用户带来更沉浸式、更逼真的体验，还能推动空间计算产业的实际落地发展。 LGTM 采用两步式工作流程：它先从低分辨率图像中学习场景的基础几何结构，再通过专门的外观网络从高分辨率原图提取精细细节作为纹理，叠加在简单几何结构之上，同时它还可以对 NoPoSplat、DepthSplat 等现有 3D 高斯喷溅模型进行升级。

telegram · AI_News_CN · Apr 3, 02:18

**背景**: 3D 高斯喷溅是 2023 年兴起的热门 3D 重建与渲染技术，它可以将多张 2D 图像转换为 3D 场景表示，实现快速的实时渲染，在速度和质量上都优于 NeRF 等传统方法。传统前馈式 3D 高斯喷溅的计算需求会随着渲染分辨率提升呈二次方增长，这让算力有限的移动设备无法在高分辨率头显上运行 4K 实时渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.25745v1">LGTM enables feed-forward 4K textured Gaussian splatting.</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>
<li><a href="https://alanhou.org/blog/arxiv-less-gaussians-texture-more-4k-feed/">LGTM: Breaking the 4K Barrier in Feed-Forward 3D Gaussian Splatting / LGTM：突破前馈式3D高斯泼溅的4K分辨率瓶颈 | Alan Hou</a></li>

</ul>
</details>

**标签**: `#3D Gaussian Splatting`, `#3D Rendering`, `#Spatial Computing`, `#Apple Vision Pro`, `#Computer Graphics`

---

<a id="item-15"></a>
## [微软推出全球最高精度语音转写模型](https://www.aibase.com/zh/news/26823) ⭐️ 8.0/10

微软推出了全新语音转文字模型 MAI-Transcribe-1，该模型在 25 种语言上的平均词错误率仅为 3.9%，性能超过 OpenAI Whisper-large-v3 和 Google Gemini 3.1 Flash。该模型现已通过 Microsoft Foundry 平台开放批量转写服务，定价为每小时音频 0.36 美元。 该新模型为多语种自动语音识别树立了全新的精度标杆，推动了为众多商用 AI 应用提供支撑的转写技术进步。它为开发者和企业提供了比 OpenAI 和谷歌现有领先模型精度更高、价格更具竞争力的新选择。 MAI-Transcribe-1 在 FLEURS 标准基准测试中，在其支持的 25 种语言里有 11 种的转写精度排名第一，批量转写速度是现有 Microsoft Azure Fast 产品的 2.5 倍，但当前版本暂不支持实时转写和说话人分离功能，微软计划在后续更新中添加这些能力。

telegram · AI_News_CN · Apr 3, 02:30

**背景**: MAI-Transcribe-1 是微软自研 MAI 系列模型的第三款产品，该系列此前已经推出了语音合成模型 MAI-Voice-1 和图像生成模型 MAI-Image-2。FLEURS 是行业内广泛认可的、用于评估多语种自动语音识别模型性能的标准基准测试。Microsoft Foundry 是微软提供的统一平台，供开发者构建、编排和运行 AI 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/">State of the Art Speech Recognition with MAI-Transcribe-1 | Microsoft AI</a></li>
<li><a href="https://arxiv.org/abs/2205.12446">[2205.12446] FLEURS : Few-shot Learning Evaluation of Universal...</a></li>
<li><a href="https://www.logicintelligence.com/microsoft-foundry/">Microsoft Foundry - Logic Intelligence</a></li>

</ul>
</details>

**标签**: `#speech recognition`, `#large language model`, `#automatic speech transcription`, `#Microsoft`, `#multimodal AI`

---

<a id="item-16"></a>
## [前 Azure 工程师发文批评侵蚀信任的决策](https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion) ⭐️ 7.0/10

一名前 Azure 核心工程师公开发文批评微软的内部决策，称这些决策侵蚀了客户和开发者对 Azure 的信任，这篇文章在 Hacker News 上引发了广泛的印证性讨论。 这篇内部爆料为全球三大公有云平台之一的组织问题提供了罕见无过滤的视角，会影响全球数百万依赖 Azure 的云开发者和企业客户。 作者表示，他们在 2025 年 1 月先向微软首席执行官发送了 concerns，在未收到回应后向公司董事会升级反映，随后才发布了这篇公开批评。

hackernews · axelriet · Apr 2, 16:00

**背景**: Azure Core 是微软 Azure 的基础组件，既可以指代 Azure 云平台的核心底层基础设施，也可以指代支撑所有官方 Azure 客户端开发包的共享核心库。微软 Azure 是全球最大的公有云服务提供商之一，与亚马逊 AWS 和谷歌云并列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/overview/azure/core-readme?view=azure-dotnet">Azure Core shared client library for .NET - Azure for .NET Developers | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/">Describe the core architectural components of Azure - Training | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 许多当前和曾经的 Azure 用户与开发者认同这一批评，分享了自己的糟糕使用体验，包括粗糙 UI、过时文档，以及 Azure OpenAI 在高负载下泄露其他用户响应的问题。部分评论者质疑作者是真正的举报人还是心怀不满的前员工，另一名前 Azure 工程师则认为作者戏剧化的写作削弱了其核心观点的可信度。

**标签**: `#Azure`, `#Cloud Computing`, `#Microsoft`, `#Software Engineering`, `#Industry Insider`

---

<a id="item-17"></a>
## [Hacker News 讨论新版 Cursor 3 AI 编辑器](https://cursor.com/blog/cursor-3) ⭐️ 7.0/10

Anysphere 推出了其 AI 代码编辑器的主要新版本 Cursor 3，在 Hacker News 引发了广泛讨论，用户分享了自己将 Cursor 与竞品 Claude Code 对比的实际使用体验。 作为一款广受欢迎的 AI 辅助开发工具，Cursor 3 全新的智能体优先设计方向影响着 AI 开发工具的发展格局，社区反馈也反映了开发者对 AI 编码工作流的实际需求。 Cursor 3 是 Visual Studio Code 的分支，增加了专属 AI 功能，本次重大更新新增了智能体窗口和设计模式，聚焦智能体驱动的开发工作流，同时支持本地设备和远程 SSH 环境。

hackernews · adamfeldman · Apr 2, 18:13

**背景**: Cursor 是由旧金山初创公司 Anysphere 开发的专有 AI 代码编辑器，该公司成立于 2022 年。Claude Code 是 Anthropic 推出的独立智能体编码工具，能够理解整个代码库、编辑文件并运行终端命令，帮助开发者更快交付代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor) - Wikipedia</a></li>
<li><a href="https://cursor.com/blog/cursor-3">Meet the new Cursor · Cursor</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 用户观点出现分歧：部分长期用户认为，即使使用新的默认 Composer 2 模型，Cursor 仍比 Claude Code 效率更高，另一些用户则将免费版 Cursor 的自动补全功能与 Claude Code 结合使用，质疑 Cursor 付费订阅的价值。多名用户对 Cursor 3 转向智能体优先、以聊天为核心的设计方向表示担忧，认为该方向弱化了代码本身的核心地位，这是许多开发者不喜欢的。

**标签**: `#AI code editor`, `#developer tools`, `#Cursor`, `#AI-assisted development`

---

<a id="item-18"></a>
## [阿里发布闭源千问 Qwen3.6-Plus 大模型](https://qwen.ai/blog?id=qwen3.6) ⭐️ 7.0/10

阿里巴巴发布了面向真实世界 AI 智能体优化的新型闭源托管大语言模型 Qwen3.6-Plus。本次发布标志着千问偏离其以往为人熟知的开放权重发布路线，做出了战略转向。 这个曾经受欢迎的开放权重大模型提供商转向闭源托管服务，标志着更广泛的行业趋势：AI 厂商通过开放发布建立品牌知名度后，开始转向模型开发商业化。它影响了依赖千问开放权限进行实验和定制开发的 AI 开发者与研究者。 Qwen3.6-Plus 未公开披露参数量，其官方基准测试对比使用的是竞品的旧版本模型（使用 Anthropic Claude Opus 4.5 而非 4.6，使用 Google Gemini Pro 3.0 而非 3.1）。目前 OpenRouter 的 API 提供该模型的免费预览版本。

hackernews · pretext · Apr 2, 14:28

**背景**: 开放权重大语言模型会向公众公开训练完成的模型参数，允许开发者在本地运行、修改和部署模型。闭源托管大语言模型将模型权重和核心代码作为专有技术保留，仅通过开发公司管理的云端 API 提供访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3.6-plus-preview:free">Qwen3.6 Plus Preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.metriccoders.com/post/closed-source-large-language-models">Closed Source Large Language Models - metriccoders.com</a></li>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>

</ul>
</details>

**社区讨论**: 许多社区成员对千问的战略转向表示愤怒，指出该品牌正是依靠开放小型模型发布积累的好感才建立起来。部分用户认为，考虑到 AI 行业新版本模型发布频率很高，针对千问基准测试对比方法的批评有些言过其实。其他测试过模型的用户指出，OpenRouter 上的免费推理选项可以产出可用的输出，在零价格的优势下很难被替代。

**标签**: `#large language models`, `#Qwen`, `#AI agents`, `#open AI`, `#machine learning`

---

<a id="item-19"></a>
## [2025 年英伟达中国 AI 芯片份额降至 55%](https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips) ⭐️ 7.0/10

2025 年，英伟达在中国 AI 芯片市场的份额从美国出口制裁前的 95%降至 55%，中国本土厂商合计拿下了 41%的市场份额，其中华为以近 20%的占比成为本土第一。华为近期还发布了 Atlas 350 AI 加速器，号称性能接近英伟达 H20 的三倍。 这一重大市场变化表明，美国出口管制和中国半导体本土化政策正在快速重塑全球 AI 芯片供应链，将对全球芯片厂商和中国 AI 行业参与者的发展战略都产生影响。 2025 年英伟达向中国出货约 220 万块 AI 芯片，本土厂商合计出货 165 万块；本土厂商中华为之后排名靠前的依次是阿里平头哥、百度昆仑芯和寒武纪。H20 是目前在美国出口管制下英伟达能够合法向中国出口的最先进 AI 芯片。

telegram · zaihuapd · Apr 2, 06:08

**背景**: 美国从 2022 年 10 月开始对中国实施多轮出口制裁，限制先进 AI 芯片及相关半导体技术对华出口，打乱了英伟达向中国供应高端 AI 芯片的节奏。中国政府随后推动国内数据中心优先使用国产芯片，以扶持本土半导体产业发展。H20 是英伟达专门针对中国市场设计、符合现行美国出口管制规定的 AI 芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/opinion/articles/2025-04-14/could-nvidia-ceo-s-mar-a-lago-meal-cost-the-west-its-ai-lead">Nvidia 's Mar-a-Lago Dinner Could Be a Raw Deal for US AI - Bloomberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced Computing ... - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#semiconductor market`, `#Nvidia`, `#domestic chips`, `#trade policy`

---

<a id="item-20"></a>
## [ElevenLabs 推出 ElevenMusic AI 音乐应用](https://www.aibase.com/zh/news/26811) ⭐️ 7.0/10

领先的生成式语音 AI 企业 ElevenLabs 于 2025 年 4 月 1 日推出 iOS 应用 ElevenMusic，正式进军 AI 音乐创作市场，与 Suno 和 Udio 等平台展开竞争。本次发布标志着该公司从单一语音 AI 服务商向全栈创意平台的战略转型。 这次入场加剧了快速增长的 AI 音乐生成市场的竞争，将重塑生成音频领域的创作者经济，同时帮助 ElevenLabs 拓展业务范围，降低音频模型商品化的风险。它也为寻求易用 AI 创作工具的普通创作者和消费者带来了更多选择。 ElevenMusic 支持通过自然语言提示词生成定制音乐，可调整曲目长度、歌词和艺术风格，还整合了实时电台、基于情绪维度的歌单等流媒体社交功能。它采用免费增值订阅模式：免费用户每日可生成 7 首作品，每月 9.99 美元的专业版则提供每月 500 首创作额度和 500GB 存储空间。

telegram · AI_News_CN · Apr 3, 01:02

**背景**: ElevenLabs 原本是生成式 AI 语音领域的领先先驱，专注于为内容创作提供自然富有表现力的 AI 语音解决方案。Suno 和 Udio 是 AI 音乐生成领域现有的两家领先平台，都支持用户通过简单的文本提示生成定制化的高质量音乐。ElevenLabs 在 2025 年 2 月完成了 C 轮融资，估值达到 110 亿美元，获得了拓展新生成音频赛道的资金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elevenlabscn.com/about.html">ElevenLabs - 关于我们</a></li>
<li><a href="https://suno.com/">Suno | AI Music Generator</a></li>
<li><a href="https://www.udio.com/">Udio | AI Music Generator - Official Website</a></li>

</ul>
</details>

**标签**: `#AI music generation`, `#generative AI`, `#product launch`, `#ElevenLabs`

---

<a id="item-21"></a>
## [Claude Code 泄露后 GitHub 出现钓鱼陷阱](https://www.aibase.com/zh/news/26813) ⭐️ 7.0/10

在 Anthropic 因人为失误意外泄露 Claude Code 源码后，黑客建立了经过 SEO 优化的虚假 GitHub 仓库，以提供解锁企业版泄露源码为诱饵，传播针对开发者的 Vidar 信息窃取恶意软件。 本次攻击瞄准主动寻找泄露 Claude Code 源码的开发者，展示了攻击者可以如何快速利用近期公开的安全事件发起次生钓鱼攻击，威胁开发者的敏感数据安全。 感染设备后植入的恶意程序包含成熟的 Vidar 信息窃取木马，会窃取浏览器凭证、加密货币钱包数据和其他敏感信息，同时还会部署 GhostSocks 代理工具，为远程控制和数据回传搭建秘密通道。目前已经发现至少两个手法类似的虚假仓库，恶意压缩包更新频率极高，可绕过基础安全检测。

telegram · AI_News_CN · Apr 3, 01:02

**背景**: Claude Code 是 Anthropic 开发的面向开发者的智能 AI 编码工具。Vidar 是一款成熟的信息窃取恶意软件，自 2018 年起就以恶意软件即服务的形式在暗网流通，而 GhostSocks 是攻击者常用来维持对被入侵网络隐蔽访问的代理工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/what-is-vidar-malware/">What is Vidar Malware? - Check Point Software</a></li>
<li><a href="https://www.darktrace.com/blog/phantom-footprints-tracking-ghostsocks-malware">Tracking & Detecting GhostSocks Malware - Darktrace</a></li>

</ul>
</details>

**标签**: `#AI security`, `#phishing`, `#cybersecurity`, `#Claude Code`, `#malware`

---

<a id="item-22"></a>
## [OpenAI 关停 Sora 后收购 TBPN](https://www.aibase.com/zh/news/26815) ⭐️ 7.0/10

OpenAI 在关停旗下 Sora 人工智能视频应用一个月后，宣布完成对知名科技商业播客 TBPN 的收购。这场收购标志着 OpenAI 从开发 AI 工具转向把控 AI 发展相关公众叙事的战略转变。 这一动向代表了 AI 企业进入媒体领域、塑造 AGI 发展相关公众舆论和监管叙事的新趋势，给监管层和公众带来了全新挑战。如果该趋势延续，可能会重塑公众对通用人工智能的认知和监管方式。 OpenAI 承诺将保留 TBPN 的编辑独立性，允许播客继续自主做出编辑决策、独立选择嘉宾。行业分析指出，Sora 被关停主要是因为它日均运营成本达 100 万美元，同时用户数量腰斩，无法实现盈利。

telegram · AI_News_CN · Apr 3, 01:10

**背景**: TBPN 是一款知名的日常科技播客，在硅谷拥有大量忠实受众，曾采访马克·扎克伯格、马克·库班等多位顶尖科技行业领袖。在本文的语境中，AGI 指通用人工智能，也就是理论上具备人类所能完成的所有智力任务学习与执行能力的人工智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inc.com/ben-sherry/openai-acquires-tbpn-the-irreverent-tech-podcast-with-a-cult-following/91326232">OpenAI Acquires TBPN, the Irreverent Tech Podcast With a Cult ...</a></li>
<li><a href="https://podcast.app/tbpn-p6101625">TBPN podcast - Free on The Podcast App OpenAI acquires popular tech podcast TBPN - CNBC TBPN - Podcast - Apple Podcasts TBPN podcast - Free on The Podcast App TBPN podcast - Free on The Podcast App TBPN podcast - Free on The Podcast App OpenAI acquires TBPN, the buzzy founder-led business talk ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI industry`, `#corporate strategy`, `#media acquisition`, `#AGI`

---

<a id="item-23"></a>
## [谷歌 Vids 集成 Veo3.1 支持 AI 虚拟形象互动](https://www.aibase.com/zh/news/26818) ⭐️ 7.0/10

谷歌于 4 月 2 日宣布为企业级视频创作应用 Vids 推出重大升级，集成 Veo3.1AI 视频生成模型，实现了文字提示词控制的 AI 虚拟形象互动功能，还新增了直接导出到 YouTube 和全新 Chrome 录屏扩展等工作流功能。微软也在同日发布了三款 competing 的 MAI 多模态基础模型。 本次更新标志着可控 AI 视频生成领域取得了阶段性进展，推动 AI 视频工具从简单内容生成转向具备专业深度的自动化创作阶段，将重塑企业内容生产的成本结构与创意边界。竞品模型同日发布也凸显了生成式 AI 行业的竞争正在持续升级。 新功能允许用户通过文字提示指挥 AI 虚拟形象完成和产品、道具的特定互动，同时保持角色视觉一致性，本次集成支持生成长度为 8 秒的视频片段。普通用户每月可生成 10 次视频，企业高级版账户每月最多可生成 1000 次。

telegram · AI_News_CN · Apr 3, 01:22

**背景**: Google Vids 是谷歌在 2024 年推出的企业级 AI 视频创作工具，经过快速迭代已经陆续加入了 3D 卡通形象和多语言支持功能。Veo3.1 是谷歌 DeepMind 推出的最新 AI 视频生成模型，能够根据文字或图像提示生成高质量影片，拥有出色的角色一致性表现。Lyria3 是谷歌 DeepMind 目前最先进的音乐生成模型，可以根据提示生成高质量立体声音频，在本次升级前已经完成了和 Vids 的集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yolly.ai/veo-3.1">Google Veo 3 . 1 — AI Video Generator | Yolly AI</a></li>
<li><a href="https://deepmind.google/models/lyria/">Lyria 3 — Google DeepMind</a></li>
<li><a href="https://www.forbes.com/sites/janakirammsv/2026/04/02/microsoft-builds-its-own-ai-model-stack-to-reduce-openai-dependence/">Microsoft Builds Its Own AI Model Stack To Reduce OpenAI ...</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#Google Vids`, `#generative AI`, `#AI avatars`

---

<a id="item-24"></a>
## [谷歌拟建天然气电厂供 AI 数据中心](https://www.aibase.com/zh/news/26821) ⭐️ 7.0/10

谷歌与能源公司 Crusoe Energy 在美国得克萨斯州阿姆斯特朗县启动建设一座 933 兆瓦的天然气发电厂，专门为谷歌古德奈特 AI 数据中心园区供电，项目许可已于 2026 年 1 月提交。该电厂预计每年排放 450 万吨二氧化碳，受 AI 业务扩张推动，谷歌整体温室气体排放量较 2019 年已增长 48%。 这一事件暴露了 AI 行业爆发式增长的能源需求与大型科技公司公开做出的净零碳承诺之间日益加剧的矛盾，点明了行业尚未解决的系统性挑战。它清晰展现了当可再生能源无法满足即时电力需求时，科技巨头如何将 AI 扩张置于气候目标之前。 谷歌表示仍在推进风电合作，且尚未就该电厂签署正式购电合同，但同时指出稳定的基荷电力是当前大型 AI 数据中心运行必不可少的刚需。谷歌的选择并非个例，已有多家科技巨头因清洁能源增长无法填补电力缺口转而使用天然气。

telegram · AI_News_CN · Apr 3, 01:45

**背景**: 基荷电力是电力系统需要持续稳定供应的基础电力负荷，提供基荷电力的发电厂被称为基荷电厂，这类电厂通常要求运行稳定，传统上多由天然气、煤炭或核能电厂担任。装机容量是衡量发电厂建设规模和发电能力的核心指标，指电厂内所有发电机组额定功率的总和，单位为瓦。Crusoe Energy 是一家专注于提供能源导向型 AI 基础设施和云计算服务的私营企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/基荷电厂/5158241">基荷电厂_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/装机容量/10782194">装机容量_百度百科</a></li>
<li><a href="https://www.crusoe.ai/">Crusoe | The AI factory company | Renewable-powered AI ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#carbon emissions`, `#energy`, `#big tech`

---