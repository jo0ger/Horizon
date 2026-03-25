---
layout: default
title: "Horizon Summary: 2026-03-25 (ZH)"
date: 2026-03-25
lang: zh
---

> From 51 items, 24 important content pieces were selected

---

1. [Litellm 1.82.7/1.82.8 版本遭植入恶意代码](#item-1) ⭐️ 9.0/10
2. [PyPI 上 litellm 遭植入窃密木马](#item-2) ⭐️ 9.0/10
3. [阿里达摩院发布破纪录 RISC-V CPU 玄铁 C950](#item-3) ⭐️ 9.0/10
4. [创始人重写 Video.js 体积缩减 88%](#item-4) ⭐️ 8.0/10
5. [Anthropic 为 Claude Code 推出自动模式](#item-5) ⭐️ 8.0/10
6. [流式专家技术让消费设备运行万亿参数大模型](#item-6) ⭐️ 8.0/10
7. [DarkSword iOS Safari 零点击漏洞披露](#item-7) ⭐️ 8.0/10
8. [Google 推出 Gemini 暗网安全 AI 代理](#item-8) ⭐️ 8.0/10
9. [OpenAI 将停用 AI 视频工具 Sora](#item-9) ⭐️ 8.0/10
10. [Anthropic 为 Claude Code 推出自动模式](#item-10) ⭐️ 8.0/10
11. [OpenAI 为 ChatGPT 推出 AI 购物协议](#item-11) ⭐️ 8.0/10
12. [OpenAI 计划关停 AI 视频平台 Sora](#item-12) ⭐️ 8.0/10
13. [OpenAI 终止文生视频项目 Sora](#item-13) ⭐️ 8.0/10
14. [谷歌发布轻量大模型 Gemini 3.1 Flash-Lite](#item-14) ⭐️ 8.0/10
15. [法官质疑美国报复 Anthropic](#item-15) ⭐️ 8.0/10
16. [热门 AI 库 litellm 遭供应链投毒](#item-16) ⭐️ 8.0/10
17. [Litellm 遭供应链投毒 凭证疑泄露](#item-17) ⭐️ 8.0/10
18. [OpenAI 关闭消费者 AI 视频应用 Sora](#item-18) ⭐️ 7.0/10
19. [LiteLLM 攻击后的依赖冷却支持](#item-19) ⭐️ 7.0/10
20. [英伟达投资策略遭反垄断审查](#item-20) ⭐️ 7.0/10
21. [中国日均 AI 词元调用量两年涨超千倍](#item-21) ⭐️ 7.0/10
22. [微软发布开源 Rust 培训教材](#item-22) ⭐️ 7.0/10
23. [Anthropic 为 Claude Code 推出自动模式](#item-23) ⭐️ 7.0/10
24. [OpenAI 调整电商战略 放弃即时结账功能](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Litellm 1.82.7/1.82.8 版本遭植入恶意代码](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

流行的 PyPI 包 Litellm 近期发布的 1.82.7 和 1.82.8 版本被证实遭植入 fork 炸弹恶意代码，该事件与针对项目 Trivy 依赖的 ongoing CI/CD 供应链攻击有关。 恶意代码在 Litellm 源码中添加了一段 base64 编码的恶意数据块，可解码并执行额外恶意程序，1.82.8 版本还新增了可执行的_init.pth 文件，会在 Python 解释器启动时运行恶意代码。只有安装了被污染 PyPI 版本的用户会受影响，项目固定版本的代理 Docker 镜像未受影响，PyPI 已经将恶意包隔离，阻止进一步下载。

hackernews · dot_treo · Mar 24, 12:06

**背景**: LitellM 是一个开源 Python 库，可为开发者提供统一接口，调用来自百余种不同提供商的大语言模型。分叉炸弹是一种拒绝服务攻击，通过不断复制自身进程耗尽系统内存与算力，导致目标系统变慢或崩溃。CI/CD 供应链攻击是指攻击者入侵软件项目的自动化构建发布流程，将恶意代码植入对外分发的软件包中，最终传递给所有下游用户的网络攻击类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.penligent.ai/hackinglabs/litellm-on-pypi-was-compromised-what-the-attack-changed-and-what-defenders-should-do-now/">LiteLLM on PyPI Was Compromised, What the Attack Changed and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fork_bomb">Fork bomb - Wikipedia</a></li>
<li><a href="https://www.darkreading.com/application-security/trivy-supply-chain-attack-targets-ci-cd-secrets">Trivy Supply Chain Attack Targets CI/CD Secrets</a></li>

</ul>
</details>

**社区讨论**: LitellM 维护者确认事件仍在发展中，并将源头追溯到项目 CI/CD 工作流中被入侵的 Trivy 依赖。社区成员对软件依赖和开发环境的信任问题表达了普遍担忧，部分成员分享了可帮助用户检测恶意包活动的新安全工具，也有人指出事件议题串中存在大量垃圾评论。

**标签**: `#supply chain security`, `#malicious package`, `#software security`, `#pypi`

---

<a id="item-2"></a>
## [PyPI 上 litellm 遭植入窃密木马](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

发布在 PyPI 上的热门 Python 包 litellm 的 1.82.7 和 1.82.8 版本被植入了窃取凭据的恶意软件。漏洞被发现后，PyPI 已对 litellm 项目进行了隔离处理。 这是一起影响广泛使用的 LLM 工具包的高影响力供应链攻击，它可以在安装完成后自动窃取用户凭据。任何在攻击窗口期内安装了这两个版本的开发者和组织都面临凭据泄露的直接风险。 1.82.8 版本将恶意软件隐藏在 litellm_init.pth 文件中，该文件会在包安装后的 Python 启动阶段自动运行，即使用户从未在代码中导入过 litellm 也会触发攻击。本次攻击源于 LiteLLM 的 CI 流水线中使用的安全扫描工具 Trivy 此前被攻破，攻击者借此窃取了项目的 PyPI 发布凭据。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一款热门的开源 Python 库，它提供了统一接口，可以调用来自不同提供商的上百种大语言模型。.pth 文件是 Python 包中的特殊文件，会在 Python 启动时被自动解析执行，原本的用途是修改模块搜索路径。PyPI 是 Python 编程语言的官方公共软件包仓库，它会隔离被攻陷的项目，阻止恶意版本继续被分发下载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://runebook.dev/en/docs/python/library/sys_path_init/pth-files">The Hidden Power and Problems of Python .pth Files</a></li>
<li><a href="https://www.penligent.ai/hackinglabs/litellm-on-pypi-was-compromised-what-the-attack-changed-and-what-defenders-should-do-now/">LiteLLM on PyPI Was Compromised, What the Attack Changed and What Defenders Should Do Now - Penligent</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#python`, `#malware`, `#pypi`, `#litellm`

---

<a id="item-3"></a>
## [阿里达摩院发布破纪录 RISC-V CPU 玄铁 C950](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 9.0/10

2026 年 3 月 24 日，阿里巴巴达摩院在上海举办的 2026 玄铁 RISC-V 生态大会上发布了全新旗舰 RISC-V CPU 玄铁 C950。这款新芯片在 SPECint2006 单核测试中得分超过 70 分，创下了所有公开披露的 RISC-V 处理器的性能新纪录。 这一突破将开源 RISC-V 处理器的性能上限推进到高端算力区间，让 RISC-V 芯片得以进入此前被封闭专有 CPU 架构主导的高要求场景。它将加速开放 RISC-V 生态的发展，拓展云计算和生成式 AI 基础设施的应用可能性。 玄铁 C950 面向云计算、生成式 AI、高端机器人和边缘计算等高端算力场景，它集成了达摩院自研的 AI 加速引擎，可原生运行通义千问 3、DeepSeek V3 等千亿参数级大模型。

telegram · zaihuapd · Mar 24, 06:01

**背景**: RISC-V 是开源的 CPU 指令集架构，开发者可以免费使用和修改该架构，近年来在全球获得了越来越广泛的应用。SPECint2006 是行业通用的基准测试套件，用于衡量 CPU 的整数计算性能，方便对不同处理器设计进行公平对比。达摩院是阿里巴巴集团在 2017 年成立的全球前沿技术研究机构，研究范围涵盖半导体、人工智能和基础科学等多个领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://pandaily.com/alibaba-damo-academy-launches-xuan-tie-c950-cpu-for-large-ai-models">Alibaba DAMO Academy Launches XuanTie C950 CPU for Large AI Models - Pandaily</a></li>
<li><a href="https://damo.alibaba.com/about?language=en">About Us - Damo - Alibaba</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#CPU`, `#Semiconductors`, `#AI Accelerator`, `#Cloud Computing`

---

<a id="item-4"></a>
## [创始人重写 Video.js 体积缩减 88%](https://videojs.org/blog/videojs-v10-beta-hello-world-again) ⭐️ 8.0/10

在原 Video.js 项目被收购、新维护方疏于维护后，其创始人重新夺回了项目控制权，发布了彻底重写的 v10 测试版，新版本体积比旧版缩小了 88%。 Video.js 每月有数十亿用户，被亚马逊、领英、Dropbox 等主流网站使用，这款体积更小的现代化重写版本可以提升大量现有生产部署的网页性能，同时让这个关键的热门开源项目重新焕发活力。 本次重写得到了来自 Plyr、Vidstack 和 Media Chrome 四个开源媒体项目开发者的共同贡献，v10 版本新增了一流的 React 和 TypeScript 支持，还采用了全新的可组合模块化架构。

hackernews · Heff · Mar 24, 18:03

**背景**: Video.js 是一款历史悠久的开源 HTML5 网页播放器，诞生至今已有 16 年。在该项目被私募股权公司收购后，新拥有者削减了维护人员，导致项目维护不足，一直停留在过时臃肿的代码架构上。Media Chrome 是一个使用网页组件构建的可定制化媒体播放器控件开源项目，而 Plyr 是一款广受欢迎的轻量可定制 HTML5 媒体播放器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videojs.org/blog/videojs-v10-beta-hello-world-again">Video.js v10 Beta: Hello, World (again) | Blog | Video.js | Open Source Video Player</a></li>
<li><a href="https://github.com/muxinc/media-chrome">GitHub - muxinc/media-chrome: Custom elements (web components ... media-chrome - npm Get Started - Media Chrome Docs Media Chrome Examples Building the next generation of video players with Media Chrome Best of JS • media-chrome</a></li>
<li><a href="https://github.com/sampotts/plyr">sampotts/plyr: A simple HTML5, YouTube and Vimeo player plyr - npm Using Plyr Player for Lightweight, Accessible Video UI Plyr: CSS Styleable Video Player - CSS-Tricks Plyr download | SourceForge.net Plyr download | SourceForge.net Plyr : CSS Styleable Video Player - CSS-Tricks Using Plyr Player for Lightweight, Accessible Video UI Using Plyr Player for Lightweight, Accessible Video UI Plyr: The Ultimate HTML5, YouTube & Vimeo Player for Modern ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员向创始人表示祝贺，表达了对测试小体积版本的期待，还就架构选择提出了技术问题，包括为何不将其发布为网页组件，以及如何处理跨功能的状态依赖。还有评论者询问了 HLS 和 DASH 两种流媒体协议之间的取舍问题。

**标签**: `#open source`, `#web development`, `#video player`, `#javascript`

---

<a id="item-5"></a>
## [Anthropic 为 Claude Code 推出自动模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 8.0/10

Anthropic 为 Claude Code 推出了全新的自动模式，这是一种自主权限模式，允许 Claude 自行做出操作批准决定，同时由专门的安全分类器模型提供防护。该新功能替代了原有的全有或全无的`--dangerously-skip-permissions`参数，该参数原本会完全禁用权限检查。 该功能解决了开发人员使用 Claude Code 时重复收到权限提示的常见痛点，在保留内置安全防护的同时支持完全自主的 AI 辅助编码。它比之前不受监管的全权限选项更好地平衡了便利性和风险控制，是 AI 辅助软件工程的一项重要进步。 无论会话使用的主模型是什么，安全分类器都运行在 Claude Sonnet 4.6 上，它会拦截超出任务范围的操作、不受信任的基础设施目标以及由恶意内容驱动的操作。自动模式自带大量默认放行和拦截规则，用户也可以添加自定义规则进一步定制。

rss · Simon Willison · Mar 24, 23:57

**背景**: Claude Code 是 Anthropic 推出的智能 AI 编码工具，旨在帮助开发人员处理代码库、编辑文件、运行终端命令，更快交付软件。在自动模式推出之前，避免重复权限提示的唯一方法是使用`--dangerously-skip-permissions`参数，该参数会完全禁用所有权限检查，让用户面临意外或风险操作的威胁。Anthropic 长期专注于 AI 安全，在其宪法 AI 对齐方案中，使用专门训练的分类器模型实时检测违规行为和风险操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://blog.promptlayer.com/claude-dangerously-skip-permissions/">claude --dangerously-skip-permissions</a></li>
<li><a href="https://www.anthropic.com/news/building-safeguards-for-claude">Building safeguards for Claude</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI assisted development`, `#autonomous coding`, `#Anthropic`

---

<a id="item-6"></a>
## [流式专家技术让消费设备运行万亿参数大模型](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

流式专家推理技术的最新实验已经实现让 1 万亿参数的 Kimi K2.5 大语言模型在配备 96GB 内存的 M2 Max MacBook Pro 上运行，也让 3970 亿参数的 Qwen3.5-397B-A17B 模型在 iPhone 上运行。 这一突破使得本身没有足够内存容纳完整大模型的消费级硬件，也能在设备上运行超大规模混合专家大语言模型，让用户无需依赖云服务器就能使用强大的大型 AI 模型，拓展了这类模型的可及性。 Kimi K2.5 在推理过程中任何时刻仅激活 320 亿参数，iPhone 运行的 Qwen 模型速度为每秒 0.6 个词元，而 128GB 内存的 M4 Max 运行 Kimi K2.5 的速度约为每秒 1.7 个词元。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家（Mixture-of-Experts，MoE）是一种大语言模型架构，它对每个输入仅激活小部分专家参数，因此模型总参数规模可以变得非常大，同时单次推理的计算量保持在较低水平。流式专家推理技术通过仅在生成每个词元时从存储中加载当前需要的专家权重，而非一次性将整个模型加载进内存，解决了设备内存不足的问题。Kimi K2.5 是月之暗面 AI 发布的开源多模态大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/ Kimi - K 2 . 5 · Hugging Face</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Sparse Mixture-of-Experts Transformers for Efficient Scaling ... Applying Mixture of Experts in LLM Architectures | NVIDIA ... Mixture of Experts in Large Language Models: Intuition ... Mixture of experts approach for Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 该话题在全球 AI 社区引发了大量关注和跟进实验，独立开发者们正在持续迭代优化方案以提升性能。

**标签**: `#large language models`, `#mixture-of-experts`, `#on-device AI`, `#inference optimization`

---

<a id="item-7"></a>
## [DarkSword iOS Safari 零点击漏洞披露](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

可通过 Safari 恶意网页感染设备的 iOS 零点击漏洞利用链 DarkSword 已被公开披露。该漏洞自 2025 年 11 月起就被多名攻击者用于在沙特阿拉伯、土耳其、马来西亚和乌克兰发动攻击，所有相关漏洞如今都已在最新的 iOS 更新中修复。 该漏洞会影响 iOS 18 从 18.4 到 18.7 的所有版本，覆盖全球数百万活跃的苹果 iPhone 用户。由于它仅需要用户打开恶意网页即可触发，不需要额外用户交互，因此对未打补丁的设备构成了严重安全威胁，本次披露也会推动受影响用户立即安装官方安全更新。 DarkSword 串联了 6 个独立漏洞以投放恶意载荷，其中包括针对 iOS 设备加密钱包数据的窃密木马 GHOSTBLADE。虽然所有漏洞都已经在 iOS 26.3 中完成完整修补，但其中大多数漏洞早已被苹果分批在更早的更新中修复，例如 CVE-2025-43529 就已经在 iOS 18.7.3 和 iOS 26.2 中被修复。

telegram · zaihuapd · Mar 24, 11:45

**背景**: 零点击漏洞利用是一类安全漏洞，它允许攻击者在不需要目标用户进行任何交互的情况下安装恶意软件并入侵设备。DarkSword 是一款基于网页的漏洞利用工具包，当用户通过 Safari 浏览器访问被入侵或恶意构造的网站时，它就可以向存在漏洞的 iOS 设备投放不同的恶意载荷。通过 DarkSword 部署的 GHOSTBLADE 是一款专门的窃密加密货币恶意软件，它会扫描受感染设备上的加密货币交易所和钱包应用以窃取用户资金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.darkreading.com/threat-intelligence/darksword-iphone-exploit-spies-thieves">DarkSword: iPhone Exploit Kit Serves Spies & Thieves Alike - Dark Reading</a></li>
<li><a href="https://grokipedia.com/page/Zero-click_exploit">Zero-click exploit</a></li>
<li><a href="https://www.mexc.com/news/969892">DarkSword Malware Strikes iOS: Crypto Wallets Under... | MEXC News</a></li>

</ul>
</details>

**标签**: `#iOS security`, `#zero-click exploit`, `#Safari vulnerability`, `#cyber security`

---

<a id="item-8"></a>
## [Google 推出 Gemini 暗网安全 AI 代理](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

Google 推出了基于 Gemini 的暗网情报安全运营 AI 代理，目前已作为 Google Threat Intelligence 的一部分开放公开预览。该工具每天扫描 800 万至 1000 万条暗网帖子，定位和特定组织相关的安全风险，在内部测试中达到了 98%的准确率。 这次发布将大模型 AI 能力引入暗网威胁监控，而这项任务传统上需要安全团队投入大量人力完成。它可以大幅提升企业的威胁检测效率，同时也是头部云服务商在 AI 网络安全领域推出的一项重要新品。 该 AI 代理会先为每个客户构建定制的组织画像，再将暗网内容和画像交叉比对，识别包括初始访问中介活动、数据泄露和内部威胁在内的各类风险。目前 98%的准确率仅来自 Google 内部测试，尚未公开第三方独立验证结果。

telegram · zaihuapd · Mar 24, 13:15

**背景**: 暗网情报是指监控暗网论坛与交易平台、收集和组织相关威胁信息的工作。Google Threat Intelligence 是 Google Cloud 推出的威胁情报平台，本身已经拥有包含超过 500 亿份文件的大规模威胁情报资源库。网络安全 AI 代理是一类自主 AI 工具，可以独立识别和处理安全任务，减轻安全团队的人工工作量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era">Bringing dark web intelligence into the AI era - Google Cloud</a></li>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web</a></li>
<li><a href="https://cloud.google.com/transform/how-google-does-it-building-ai-agents-cybersecurity-defense/">How Google Does It: Building AI agents for cybersecurity and ...</a></li>

</ul>
</details>

**标签**: `#Gemini AI`, `#cybersecurity`, `#dark web intelligence`, `#Google Cloud`, `#AI agent`

---

<a id="item-9"></a>
## [OpenAI 将停用 AI 视频工具 Sora](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 8.0/10

彭博社报道，OpenAI 计划在高调推出仅 6 个月后停用其 Sora AI 视频生成工具，关闭面向开发者的 Sora API，并逐步收尾与迪士尼的相关合作。这次调整属于产品线精简工作的一部分，公司将把资源转向 AI 智能体和名为 Spud 的新模型。 这个备受关注的生成式 AI 项目即将被停用，标志着 OpenAI 在传闻中的 IPO 筹备阶段发生了重大战略转向，将重塑生成式 AI 视频行业的竞争格局以及相关开发者生态。它也反映出 OpenAI 越发重视面向企业的 AI 工具和通用基础模型，而非面向消费者的生成式视频业务。 OpenAI 还将重组部分安全保障团队，把相关工作更紧密地融入核心开发流程中，而根据对内部员工的公告，新模型 Spud 的初始开发已经完成。本次调整发生在 OpenAI 筹备潜在首次公开募股的阶段。

telegram · AI_News_CN · Mar 25, 00:32

**背景**: Sora 是 OpenAI 推出的知名文本生成视频 AI 模型，能够根据文本提示生成长达一分钟的高清视频。AI 智能体是一种目标驱动的自主运行 AI 系统，可以独立规划步骤、调用所需工具，在极少人工输入的情况下完成指定任务。Spud 是 OpenAI 下一代主流基础 AI 模型的代号，截至 2026 年 3 月，该模型已经完成初始开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomsguide.com/ai/openai-just-killed-sora-as-company-readies-ipo-and-new-spud-model">OpenAI just killed Sora as company readies IPO and new 'Spud ...</a></li>
<li><a href="https://www.tipranks.com/news/the-fly/openai-finished-initial-development-of-next-major-ai-model-the-information-says-thefly-news">OpenAI finished initial development of next major AI model ...</a></li>
<li><a href="https://medium.com/@kalumbalighton/is-everyone-sleeping-on-ai-agents-533d5ec93026">Is Everyone Sleeping on AI Agents ? | by Lighton N. Kalumba | Medium</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#OpenAI Sora`, `#AI Video Generation`, `#Industry Strategy`

---

<a id="item-10"></a>
## [Anthropic 为 Claude Code 推出自动模式](https://claude.com/blog/auto-mode) ⭐️ 8.0/10

Anthropic 为旗下 AI 编码助手 Claude Code 推出了全新的自动模式（Auto Mode），该功能内置工具调用前的安全分类机制，可自动放行安全操作并拦截高风险行为，目前以研究预览形式向 Claude Team 计划用户开放。 这次发布解决了 AI 编码工具长期存在的自主工作流效率与操作安全性之间的核心矛盾，让开发者可以减少人工审批带来的流程打断，同时避免完全关闭权限检查带来的重大安全风险，推动了实用自主 AI 编码助手的行业发展。 自动模式支持 Claude Sonnet 4.6 与 Opus 4.6 模型，未来数日内会向 Enterprise 计划用户和 API 用户开放；开发者可通过`claude --enable-auto-mode`命令启用，或是在桌面端应用和 VS Code 的设置中开启。Anthropic 提示，尽管该功能比现有的`--dangerously-skip-permissions`参数更安全，但仍并非零风险，且可能略微增加 Token 消耗和延迟。

telegram · AI_News_CN · Mar 25, 01:31

**背景**: Claude Code 是 Anthropic 推出的智能 AI 编码工具，能够理解整个代码库、编辑文件并运行终端命令，帮助开发者完成完整的编码工作流。AI 编码助手是一类专门设计用来自主完成编写、编辑、重构代码等常见编码任务的人工智能系统。完全自主的 AI 编码长期以来面临的最大挑战，就是在流畅的工作流程和防止意外批量删除文件、敏感数据泄露等有害操作之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI coding agent`, `#Claude Code`, `#software development`, `#AI safety`, `#autonomous AI`

---

<a id="item-11"></a>
## [OpenAI 为 ChatGPT 推出 AI 购物协议](https://www.aibase.com/zh/news/26519) ⭐️ 8.0/10

3 月 24 日，OpenAI 正式宣布推出智能体商业协议（Agentic Commerce Protocol），该协议支持所有层级的 ChatGPT 用户直接在聊天界面内完成从商品搜索、比价到一键结账的全流程购物。 这次发布标志着 OpenAI 从问答引擎向执行智能体进化的关键一步，预计将重塑线上商品分发与搜索优化格局，正式开启 AI 智能体电商时代。 该功能向从免费版到 Pro 版的所有 ChatGPT 用户开放，OpenA 尚未和任何特定商家签署独家协议，初期展示位对所有接入协议的电商开放，结账功能通过与 Stripe 的合作实现。

telegram · AI_News_CN · Mar 25, 00:58

**背景**: 智能体商业协议是一套开放标准，允许电商平台将自身库存数据直接接入 OpenAI 的接口，让 AI 智能体可以获取实时商品信息并直接在聊天界面内完成购买。传统搜索引擎优化主要针对普通搜索结果的网页排名进行优化，而 AI 搜索和 AI 智能体电商的兴起，正在推动营销从业者开发全新的优化策略，让商品能获得 AI 的优先推荐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/future-shopping-what-chatgpts-agentic-ecommerce-protocol-means-rnwve">The Future of Shopping: What ChatGPT’s Agentic eCommerce...</a></li>
<li><a href="https://departmentofproduct.substack.com/p/what-is-acp-agentic-commerce-protocol">What is ACP? Agentic Commerce Protocol from Stripe and OpenAI...</a></li>
<li><a href="https://www.reddit.com/r/digital_marketing/comments/1s1k3bb/ai_search_is_quietly_changing_how_seo_works/">AI search is quietly changing how SEO works. : r/digital_marketing - Reddit</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#AI commerce`, `#agentic AI`, `#e-commerce`

---

<a id="item-12"></a>
## [OpenAI 计划关停 AI 视频平台 Sora](https://ishare.ifeng.com/c/s/v006ltpxjezzcbv4UGiPup56TxU--voijLEBXhsV4nEsyHvtGuncunDkNIBKx04IOyBP2) ⭐️ 8.0/10

OpenAI 本周宣布计划关停推出仅六个月的 AI 视频生成平台与社交应用 Sora，公司将把原 Sora 团队重新调配至企业业务、编程工具和长期机器人研究领域，为计划中 2024 年第四季度的 IPO 做准备。 此次关停标志着这家全球最具影响力 AI 企业的重大战略转向，它将把资源重新集中在高价值的企业级与生产力导向 AI，而非消费者社交产品。这也暴露了在当前监管和技术条件下，完全开放的面向消费者生成式 AI 视频平台仍存在大量未解决的挑战。 Sora 消费者应用、面向开发者的版本以及 ChatGPT 内置的视频生成功能都将停止服务，最先进的 Sora2 模型仍会保留在 ChatGPT 付费墙后作为生产力工具提供。关停的原因包括用户下载量暴跌、平台普遍存在未经审核的侵权和深伪内容，以及与迪士尼潜在的 1 亿美元 IP 授权交易告吹。

telegram · AI_News_CN · Mar 25, 01:02

**背景**: Agentic AI 系统是一类生成式 AI 系统，能够半自主或全自主运行，自主感知、推理并完成任务，而非仅响应用户直接指令生成内容。恐怖谷效应是一种心理学现象，指当人造物体和人类的相似程度达到很高但不完全逼真的水平时，人类观察者会对其产生强烈的不适和反感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/恐怖谷理论">恐怖谷理论 - 维基百科，自由的百科全书</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Generative AI`, `#Sora`, `#AI Industry`, `#Corporate Strategy`

---

<a id="item-13"></a>
## [OpenAI 终止文生视频项目 Sora](https://www.aibase.com/zh/news/26521) ⭐️ 8.0/10

2026 年 3 月 24 日，OpenAI 正式宣布终止其领先文生视频模型 Sora 的所有后续开发与服务，此举属于业务重组的一部分。该变动终结了 OpenAI 与迪士尼计划中的 10 亿美元合作项目，OpenAI 将把资源转向 GPT-5 和 AI Agent 开发，为 2026 年的资本市场活动做准备。 这次 abrupt 退出重塑了生成式 AI 视频行业的竞争格局，给其他文生视频赛道的竞争者带来了新的机遇与不确定性。它也标志着 OpenAI 的重大战略转向，同时凸显了 OpenAI 与其最大投资方微软之间不断加剧的分歧。 OpenAI 并未公布终止 Sora 项目的具体技术原因，但外界普遍将此次调整解读为业务瘦身，目的是在资本市场动作前向投资者展示更清晰、更具盈利能力的业务版图。Sora 团队已经确认将逐步关闭相关服务，后续会公布接口下线时间表和用户内容保存方案。

telegram · AI_News_CN · Mar 25, 01:07

**背景**: Sora 是 OpenAI 开发的文生视频生成式 AI 模型，于 2024 年 2 月首次对外公开，能够根据文本提示生成长达 60 秒的 1080p 视频。GPT-5 是 OpenAI 推出的第五代生成式预训练 Transformer 大模型，于 2025 年 8 月正式公开上线。AI Agent 是能够通过自主推理和规划为用户完成目标型任务的自主 AI 系统，在 2026 年已经成为生成式 AI 行业的核心发展方向之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to-video model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5">GPT-5 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#generative AI`, `#Sora`, `#text-to-video`, `#AI industry`

---

<a id="item-14"></a>
## [谷歌发布轻量大模型 Gemini 3.1 Flash-Lite](https://www.aibase.com/zh/news/26527) ⭐️ 8.0/10

Google DeepMind 公开发布了轻量化大语言模型 Gemini 3.1 Flash-Lite，该模型实现了 2.5 倍的首响应速度提升，吞吐量超过每秒 360 个 token，还能完成近实时的动态 UI 生成。在第三方多模态任务测试中，它的表现超过了 Claude Opus 4.6 等更大体量的竞品模型。 这项低延迟生成式 AI 的突破催生了快速 UI 原型设计、动态交互界面生成等全新的实时 AI 应用场景，拓展了轻量化大语言模型的实用范围。它也为轻量大模型领域树立了速度与性能的新标杆，推动行业探索更快速度的 AI 落地应用。 Gemini 3.1 Flash-Lite 的输出成本从每百万 token 0.40 美元上涨至 1.50 美元，且现有演示在处理复杂网页逻辑时仍存在不稳定性，内容可能随时间变得混乱。该模型目前已经在 Google AI Studio 和 Vertex AI 平台开放公开使用。

telegram · AI_News_CN · Mar 25, 01:41

**背景**: Gemini 3.1 Flash-Lite 是谷歌 Gemini 3 系列大模型的一员，于 2026 年 3 月推出，针对高吞吐量、低延迟的工作负载进行了优化。Google AI Studio 是谷歌在 2023 年推出的免费网页端开发环境，支持开发者和非技术用户使用 Gemini 模型快速搭建生成式 AI 应用原型。Vertex AI 是谷歌云推出的托管企业级平台，用于规模化构建、训练和部署机器学习与生成式 AI 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/">Gemini 3.1 Flash Lite: Our most cost-effective AI model yet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Studio">Google AI Studio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vertex_AI">Vertex AI</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#Large Language Models`, `#Generative AI`, `#Low-latency AI`

---

<a id="item-15"></a>
## [法官质疑美国报复 Anthropic](https://www.aibase.com/zh/news/26528) ⭐️ 8.0/10

美国联邦法官林丽婷（Rita Lin）公开质疑，拜登政府将头部 AI 公司 Anthropic 列入供应链风险黑名单，是否是针对 Anthropic 首席执行官因滥用风险拒绝向美国国防部开放 Claude 模型无限制访问权限的政治报复。 本案将为私营 AI 企业面对政府要求时的自主权开创关键先例，其结果会塑造未来 AI 治理和政府获取私有 AI 模型的规则；包括微软在内的硅谷巨头都在密切关注此案，如果政府胜诉，可能会开启随意 targeting 任何拒绝政府要求的 AI 企业的大门。 这个原本用于打击外国敌对势力的黑名单认定，首次被用于美国本土顶尖 AI 公司，且这份行政命令范围极广，甚至禁止美国国家艺术基金会这类非敏感机构使用 Claude。Anthropic 表示，由于国防承包商因政策不确定性不敢使用其产品，该认定已经危及数亿美元的短期潜在收入。

telegram · AI_News_CN · Mar 25, 02:03

**背景**: Anthropic 是美国头部人工智能公司，开发了 Claude 系列大语言模型，该系列模型最早于 2023 年公开发布。美国国防部的供应链风险黑名单是一种监管工具，原本用于标记对美国国家安全构成潜在威胁的企业，被列入黑名单后联邦政府实体将被限制与该企业开展业务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/anthropic-supply-chain-risk-shockwaves-silicon-valley/">Anthropic Hits Back After US Military Labels It a ‘Supply ...</a></li>
<li><a href="https://www.msn.com/en-us/money/companies/pentagon-blacklisting-anthropic-ai-as-supply-chain-risk-was-retaliatory-elizabeth-warren-suggests/ar-AA1ZdX4S">Pentagon blacklisting Anthropic AI as 'supply chain risk' was ...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#AI governance`, `#politics of AI`, `#AI industry`, `#government policy`

---

<a id="item-16"></a>
## [热门 AI 库 litellm 遭供应链投毒](https://www.aibase.com/zh/news/26529) ⭐️ 8.0/10

攻击者窃取发布权限后，将携带恶意程序的热门 Python AI 库 litellm 的 1.82.7 和 1.82.8 版本上传到 PyPI，这次攻击仅因攻击者的编码错误引发系统崩溃才被提早发现，知名 AI 研究者 Andrej Karpathy 公开向开发者发出了预警。 litellm 每月下载量接近 1 亿次，被超过 2000 个常用 AI 工具依赖，因此这次攻击导致大量 AI 开发者的大模型 API 密钥、云访问密钥、SSH 密钥等敏感凭证面临被盗风险，同时也暴露出开源 AI 生态普遍存在的软件供应链安全隐患。 恶意程序通过恶意.pth 文件植入，会在每次 Python 解释器启动时自动运行，即使用户从未在代码中显式导入 litellm 也会触发，它会窃取系统内所有敏感信息并加密发送到攻击者服务器。本次攻击源于攻击者攻陷漏洞扫描工具 Trivy 后，盗取了 litellm 的发布凭证。

telegram · AI_News_CN · Mar 25, 02:20

**背景**: LiteLLM 是一款流行的开源 Python 库，它提供统一接口用来调用 100 多种不同的大语言模型 API，是很多 AI 开发项目依赖的核心基础工具。PyPI 是 Python 编程语言的官方公共软件包仓库，往合法流行的 PyPI 包中注入恶意程序的软件供应链攻击，近年来已经成为越来越常见的安全威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack: Malicious PyPI Packages ...</a></li>
<li><a href="https://www.litellm.ai/">LiteLLM</a></li>
<li><a href="https://www.xda-developers.com/popular-python-library-backdoor-machine/">A popular Python library just became a backdoor to your ...</a></li>

</ul>
</details>

**标签**: `#software supply chain security`, `#AI infrastructure`, `#malware`, `#open source security`, `#Python packages`

---

<a id="item-17"></a>
## [Litellm 遭供应链投毒 凭证疑泄露](https://telegra.ph/Karpathy-%E7%B4%A7%E6%80%A5%E9%A2%84%E8%AD%A6AI-%E5%BC%80%E5%8F%91%E8%80%85%E7%A5%9E%E5%99%A8litellm-%E9%81%AD%E6%95%99%E7%A7%91%E4%B9%A6%E7%BA%A7%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E6%95%B0%E4%B8%87%E5%87%AD%E8%AF%81%E6%88%96%E5%B7%B2%E5%85%A8%E6%B3%84%E9%9C%B2-03-25) ⭐️ 8.0/10

广泛使用的 AI 开发工具 Litellm 遭到了疑似教科书级别的供应链投毒攻击，可能有数万用户凭证已经完全泄露，该预警最初是安德烈·卡帕西发布的紧急警告。 这起事件影响了数千名依赖 Litellm 连接多种大语言模型服务的 AI 开发者，是一个需要用户立即采取行动的关键网络安全问题，可防止他人未经授权访问他们的大模型账号。 本次预警将这起事件标记为供应链投毒的典型案例，并且估计攻击中可能已经有多达数万条用户凭证被泄露。

telegram · AI_News_CN · Mar 25, 02:20

**背景**: Litellm 是一款流行的开源开发库，可为开发者提供统一接口，用来调用 OpenAI、Anthropic 和谷歌等供应商提供的一百多种不同大语言模型。软件供应链投毒攻击是指攻击者将恶意代码注入受信任的常用开发工具，从而感染所有安装使用该受感染软件的下游用户的网络攻击方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/supply-chain-attack/">What Is a Supply Chain Attack? - CrowdStrike</a></li>
<li><a href="https://www.twingate.com/blog/glossary/supply-chain-poisoning-attack">What Is Supply Chain Poisoning ? How It Works & Examples | Twingate</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#AI development tools`, `#cybersecurity`, `#software supply chain`

---

<a id="item-18"></a>
## [OpenAI 关闭消费者 AI 视频应用 Sora](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 7.0/10

OpenAI 宣布将在面向消费者的短视频 AI 应用 Sora 推出仅六个月后关闭该服务。公司表示将重新把重心转向包括实体世界物理任务机器人技术在内的其他优先项目。 这次突然关闭标志着 OpenAI 的重大战略转变，也引发了业内对独立消费者级生成式 AI 娱乐应用商业可行性的质疑。这也反映出 OpenAI 在生成式 AI 竞争激烈的格局下控制成本的需求。 OpenAI 在宣布关闭 Sora 仅一天前才发布了该服务的安全使用指南，这一突发且沟通不足的决定遭到了批评。Sora 此前曾与迪士尼达成内容合作，允许用户生成包含迪士尼角色的 AI 视频。

hackernews · mikeocool · Mar 24, 20:01

**背景**: Sora 是一款生成式 AI 驱动的消费者应用，允许用户通过简单文本提示生成定制短视频，在推出后很快获得了大量关注。生成式 AI 视频技术利用训练好的机器学习模型从文本或图像输入生成原创视频内容，在过去两年中普及度快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/03/24/technology/openai-shutting-down-sora.html">OpenAI Is Shutting Down Sora, Its A.I. Video Generator Top Stories OpenAI shutting down Sora video-creation app - NBC News OpenAI is shutting down its Sora video app just months after ... OpenAI pulls the plug on Sora video generator | AP News OpenAI shutters video app Sora as company reels in costs - CNBC OpenAI is scrapping the Sora app to chase bigger AI goals OpenAI Discontinues AI Video Gen App Sora - Forbes</a></li>
<li><a href="https://edition.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down">OpenAI is shutting down its Sora video app just months after ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论出现分歧，部分批评者认为 Sora 是有害的例子，属于企业控制的成瘾性 AI 娱乐，会传播低质量的“AI 垃圾”，而另一些喜欢该应用的用户也承认，它的新鲜感在推出后很快消退，几乎没有能留住用户的长期粘性。许多评论者还批评，关闭决定时机过于突然，就在新安全指南发布后立刻发生。

**标签**: `#generative ai`, `#openai`, `#ai video`, `#product shutdown`

---

<a id="item-19"></a>
## [LiteLLM 攻击后的依赖冷却支持](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

在 2026 年 3 月发生恶意 LiteLLM 供应链攻击后，Simon Willison 发布评论文章，介绍了 Andrew Nesbitt 对主流包管理器依赖冷却功能的调研结果。该调研显示，多数流行包管理器已经在 2025 年 9 月至 2026 年 2 月间的新版本中加入了原生依赖冷却支持。 这篇评论让业界重视起这个可阻挡约 80%开源供应链攻击的简单有效防护手段，帮助技术团队在备受关注的 LiteLLM 事件后快速采取防护措施。它也记录了原生依赖冷却支持在整个包管理生态中取得的快速进展，提高了这个未被充分利用的安全功能的知名度。 已经加入原生依赖冷却支持的包管理器包括 pnpm 10.16、Yarn 4.10.0、Bun 1.3、Deno 2.6、uv 0.9.17 和 npm 11.10.0，它们都支持设置最小发布时间规则，并为可信包设置例外；pip 26.0 仅支持使用绝对时间戳进行冷却过滤，目前已有现成的基于 cron 的变通方案实现相对时长过滤。

rss · Simon Willison · Mar 24, 21:11

**背景**: 依赖冷却是一种供应链安全实践，它会阻止安装刚发布的新版本依赖，直到该版本已经公开一段时间，让开源社区有机会在大多数用户安装更新前发现恶意代码。据估算，7 天的依赖冷却可以阻挡 80%的典型开源供应链攻击，包括由维护者账号被泄露引发的攻击。2026 年 3 月的 LiteLLM 供应链攻击由威胁组织 TeamPCP 实施，该组织攻破了一名维护者的 PyPI 账号，向用户推送了被植入后门的热门 AI 代理软件包版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/dependency-cooldowns-supply-chain-security/">Dependency Cooldowns Block 80% of Supply Chain Attacks</a></li>
<li><a href="https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html">TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via ...</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns - blog.yossarian.net</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#package managers`, `#dependency management`, `#software security`

---

<a id="item-20"></a>
## [英伟达投资策略遭反垄断审查](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 7.0/10

自 2022 年以来，英伟达已向 OpenAI、CoreWeave 和 Reflection 等人工智能初创公司投入数十亿美元，并通过与芯片初创公司 Groq 达成的 200 亿美元协议等交易获取人才与技术。这些商业行为已经引起美国议员的反垄断审查，议员们怀疑这些举措旨在扼杀竞争。 作为 AI 芯片市场的主导企业，英伟达的锁定策略可能会抑制全球整个 AI 生态系统的创新与消费者选择，还会为监管机构如何处理快速发展的 AI 行业中的反竞争行为开创先例。这一事件可能会影响 AI 初创企业、竞争芯片厂商和下游 AI 服务客户。 英伟达同时身兼 AI 初创企业的供应商、投资者和债权人，这实际上将客户锁定在自身生态系统中，令客户难以转向 AMD 等竞争对手。美国民主党参议员已致函要求英伟达说明其交易结构，这些交易结构被怀疑旨在规避反垄断审查。

telegram · zaihuapd · Mar 24, 03:02

**背景**: 供应商锁定是一种令客户难以转向竞争供应商的商业行为，市场主导者的这类行为根据美国法律会引发反垄断担忧。CoreWeave 是美国人工智能云计算基础设施提供商，专门为 AI 开发者提供基于 GPU 的云服务，而 Groq 是一家 AI 芯片开发商，以其面向低延迟推理的语言处理单元著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vendor_lock-in">Vendor lock-in - Wikipedia</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#artificial intelligence`, `#antitrust regulation`, `#AI chip industry`

---

<a id="item-21"></a>
## [中国日均 AI 词元调用量两年涨超千倍](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

中国国家数据局公布的官方数据显示，2026 年 3 月我国日均人工智能词元调用量突破 140 万亿，较 2024 年初的 1000 亿实现两年增长超千倍，该数据由人民日报发布。 这一极高的增速标志着中国大语言模型的应用规模正在极速扩张，也印证了国内人工智能产业正在形成一套以词元为核心的新型商业价值体系。同时它也反映出我国支撑人工智能发展的数据要素市场化改革已经取得了明显进展。 到 2025 年底，我国日均词元调用量已经升至 100 万亿，意味着千倍增长中的大部分都来自近两年。词元本身具备可计量、可定价、可交易的特性，这为标准化人工智能商业体系的形成提供了基础。

telegram · zaihuapd · Mar 24, 07:22

**背景**: 词元是大语言模型处理文本信息的最小信息单元，每个词元大致对应 0.75 个英文单词。按词元计量和定价已经成为全球人工智能商业化的行业标准，词元被当作可计量的人工智能算力计价单位，以词元为核心的价值体系可以实现人工智能推理能力的标准化交易。第三方数据也显示，近期中国大模型的总调用量已经位居世界首位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/304222714184033">AI TRENDS | China's AI Model Call Volume Surpasses U.S. for Second Week - Binance</a></li>
<li><a href="https://arxiv.org/html/2603.21690v1">AI Token Futures Market: Commoditization of Compute and ...</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/03/19/how-token-economics-could-define-success-with-ai/">How Token Economics Could Define Success With AI</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#large language models`, `#industry trend`, `#token usage`

---

<a id="item-22"></a>
## [微软发布开源 Rust 培训教材](https://github.com/microsoft/RustTraining) ⭐️ 7.0/10

微软在 GitHub 发布了名为 RustTraining 的公开开源仓库，其中包含 7 本采用宽松许可证的 Rust 教材，覆盖从入门到专家的学习路径，面向从其他编程语言转用 Rust 的开发者。这些教材包含异步 Rust、类型驱动正确性等进阶 Rust 主题的内容。 这套全面的官方培训资源降低了开发者转型学习 Rust 的门槛，填补了同时覆盖入门基础和进阶行业主题的高质量结构化学习资源的缺口。它也将推动 Rust 在系统级和性能关键型开发领域的进一步行业应用。 每本教材包含 15 至 16 章内容，还配有 Mermaid 图表、可编辑的 Rust Playground 链接、练习和全文搜索功能。该项目采用 MIT 和 CC-BY-4.0 双重许可证发布，用户可以在 GitHub 直接阅读 Markdown 源文件，也可以通过 GitHub Pages 浏览渲染后的站点。

telegram · zaihuapd · Mar 24, 23:57

**背景**: Rust 是一门注重内存安全、性能和并发的系统编程语言，近年来包括微软在内的大型科技公司对 Rust 的采用率不断提升。Mermaid 是一个基于文本的开源工具，允许用户直接在 Markdown 中创建图表和可视化内容。类型驱动正确性是一种 Rust 开发方法，它利用 Rust 强大的类型系统在编译阶段消除错误、保证代码正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>
<li><a href="https://github.com/microsoft/RustTraining/blob/main/type-driven-correctness-book/src/ch01-the-philosophy-why-types-beat-tests.md">RustTraining/type-driven-correctness-book/src/ch01-the ...</a></li>
<li><a href="https://rust-lang.github.io/async-book/">Introduction - Asynchronous Programming in Rust</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Programming Education`, `#Training Materials`, `#Open Source`

---

<a id="item-23"></a>
## [Anthropic 为 Claude Code 推出自动模式](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) ⭐️ 7.0/10

Anthropic 从 2026 年 3 月 12 日开始为其 AI 编码工具 Claude Code 推送自动模式（Auto Mode）。该新功能允许 Claude 模型自主批准自身的权限操作，从而实现更高程度的任务自动化。 该功能减少了打断开发者工作流的频繁权限弹窗，让 AI 辅助编码的端到端流程更顺畅，推动行业向能力更强的自主 AI 编码代理发展。它直接解决了使用 AI 编码助手的开发者的一个常见痛点。 自动模式目前仅对 Claude Code 的 Team 订阅开放，企业客户和 API 用户将在未来几天内逐步灰度推送该功能。该功能在减少打扰的同时保留了内置 AI 安全机制，以维持使用安全性。

telegram · AI_News_CN · Mar 25, 00:48

**背景**: Claude Code 是 Anthropic 推出的智能 AI 编码工具，旨在帮助开发者处理整个代码库、编辑文件、运行终端命令，并更快交付软件。默认情况下，Claude Code 要求开发者手动批准大多数受权限限制的操作，比如编辑文件或运行命令，这会在自动化任务流程中造成频繁中断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.zdnet.com/article/claude-code-auto-mode/">How Claude Code's new auto mode prevents AI coding ... - ZDNET</a></li>
<li><a href="https://www.macobserver.com/news/anthropic-adds-auto-mode-to-claude-code-to-reduce-permission-prompts/">Anthropic Adds Auto Mode to Claude Code to Reduce Permission ...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI coding assistant`, `#feature announcement`, `#automation`

---

<a id="item-24"></a>
## [OpenAI 调整电商战略 放弃即时结账功能](https://www.aibase.com/zh/news/26520) ⭐️ 7.0/10

OpenAI 于周二宣布放弃 ChatGPT 的“即时结账”端到端交易功能，该功能因转化率低、灵活性不足已被降低开发优先级，公司将转用与 Stripe 合作开发的代理商务协议，重新聚焦电商领域的产品发现与消费者研究核心业务。 这一战略转变反映了当前生成式 AI 在电商领域遇到的实际瓶颈，明确了 OpenAI 在 AI 电商领域的未来路线图，将会影响其他科技和电商企业开发 AI 购物工具的方向。而构建开放的代理商务协议，也为未来 AI 代理自主购物打下了技术基础。 即时结账功能于 2024 年 9 月上线，初衷是让用户直接在 ChatGPT 对话界面内完成全流程购买。OpenAI 仍允许商家通过内置应用集成结账功能或引导用户跳转至商家官网付款，但 ChatGPT 不再将自身定位为直接交易入口。

telegram · AI_News_CN · Mar 25, 01:07

**背景**: ChatGPT 即时结账是 OpenAI 首次尝试将生成式 AI 聊天机器人打造为端到端电商交易平台的功能。代理商务协议（ACP）是 OpenAI 和 Stripe 联合开发的开放标准，可支持 AI 智能体与商家企业之间实现标准化的程序化电商交易交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.agenticcommerce.dev/">Agentic Commerce Protocol</a></li>
<li><a href="https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html">OpenAI revamps shopping experience in ChatGPT after Instant ...</a></li>
<li><a href="https://agenticcommerce.pro/zh-cn/docs/introduction/">ACP 协议介绍 – Agentic Commerce Protocol - International Communit...</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#E-commerce`, `#OpenAI`, `#ChatGPT`, `#AI Strategy`

---