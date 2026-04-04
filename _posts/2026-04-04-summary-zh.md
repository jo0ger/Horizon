---
layout: default
title: "Horizon Summary: 2026-04-04 (ZH)"
date: 2026-04-04
lang: zh
---

> From 48 items, 16 important content pieces were selected

---

1. [AI 将自动化大多数零日漏洞研究](#item-1) ⭐️ 8.0/10
2. [Axios 供应链攻击使用定向社会工程学](#item-2) ⭐️ 8.0/10
3. [工信部通报 iOS 高危漏洞 建议尽快升级](#item-3) ⭐️ 8.0/10
4. [激光无线通信达 360Gbps 能耗仅 Wi-Fi 一半](#item-4) ⭐️ 8.0/10
5. [FCC 全面禁止外国产新型路由器](#item-5) ⭐️ 8.0/10
6. [美团开源统一多模态 LongCat-Next](#item-6) ⭐️ 8.0/10
7. [Anthropic 禁止订阅用户使用 OpenClaw](#item-7) ⭐️ 7.0/10
8. [AI 工具大幅增加 Linux 内核安全漏洞报告](#item-8) ⭐️ 7.0/10
9. [格雷格：AI 开源安全报告质量快速提升](#item-9) ⭐️ 7.0/10
10. [沙箱 iframe 中 CSP 元标签可阻止 JS 逃逸](#item-10) ⭐️ 7.0/10
11. [Google Vids 开放免费 Veo 3.1 AI 视频生成](#item-11) ⭐️ 7.0/10
12. [国家网信办就数字虚拟人监管征意见](#item-12) ⭐️ 7.0/10
13. [LinkedIn 被指扫描浏览器扩展并共享数据](#item-13) ⭐️ 7.0/10
14. [千问 App 上线万相 Wan2.7 视频模型](#item-14) ⭐️ 7.0/10
15. [OpenAI 多名高管职务发生变动](#item-15) ⭐️ 7.0/10
16. [Anthropic 实质上禁止 OpenClaw 接入 Claude](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 将自动化大多数零日漏洞研究](https://simonwillison.net/2026/Apr/3/vulnerability-research-is-cooked/#atom-everything) ⭐️ 8.0/10

安全研究员 Thomas Ptacek 提出，前沿大语言模型驱动的 AI 编码代理将在数月内彻底改变漏洞研究和漏洞利用开发，自动化完成大多数高影响力零日漏洞的发现工作。 这场即将到来的变革将彻底颠覆软件安全的整个经济逻辑，影响防御性安全团队和攻击性漏洞研究人员双方，需要行业立即关注，为新的格局做好准备。 Ptacek 指出，漏洞发现完全契合前沿大语言模型的优势，这些模型已经编码了大量关于源代码和常见漏洞类别的知识，且 AI 编码代理可以持续进行自动化测试而不会感到厌倦。Claude Code 已经证明了它在热门开源工具中发现新零日漏洞的实际能力。

rss · Simon Willison · Apr 3, 23:59

**背景**: 漏洞研究指在软件中寻找安全缺陷的过程，零日漏洞是尚未被公开披露、也没有补丁修复的未知漏洞，会带来极高的攻击风险。漏洞利用开发指编写可实际利用这些已发现漏洞的功能代码的工作。AI 编码代理是可以自主编写、测试和修改代码以完成指定软件任务的自主人工智能工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.csoonline.com/article/4153288/vim-and-gnu-emacs-claude-code-helpfully-found-zero-day-exploits-for-both.html">Vim and GNU Emacs: Claude Code helpfully found zero-day exploits for both | CSO Online</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/exploit-development">Exploit Development - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**标签**: `#vulnerability research`, `#AI agents`, `#cybersecurity`, `#large language models`

---

<a id="item-2"></a>
## [Axios 供应链攻击使用定向社会工程学](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/#atom-everything) ⭐️ 8.0/10

Axios 发布了针对其热门 JavaScript 库的 2026 年 3 月供应链攻击的完整事后分析，确认攻击者使用了复杂的定向社会工程学入侵了一名维护者的设备。攻击者诱骗该维护者安装了远程访问木马并窃取了他的凭证，借此发布了该库的恶意版本。 Axios 是一款被全球数百万项目依赖的极广泛使用的 JavaScript 库，因此成功的攻击会让大量下游系统面临风险。这种新型攻击载体表明开源维护者如今面临高度定制化、有组织的攻击，所有活跃维护者都需要更新自身的威胁认知。 此次攻击模仿了 Google 云安全团队记录过的 UNC1069 攻击活动：攻击者克隆了一家真实公司及其创始人的身份，诱骗维护者加入伪造的 Slack 工作区和微软 Teams 会议。维护者被说服安装了一个会议相关更新，而该更新实际上就是窃取发布凭证的 RAT 恶意软件。

rss · Simon Willison · Apr 3, 13:54

**背景**: Axios 是一款热门的基于 Promise 的 HTTP 客户端 JavaScript 库，可同时用于浏览器和 Node.js 应用。软件供应链攻击针对软件生态系统中受信任的依赖项，通过入侵上游组件向所有依赖它的下游用户投放恶意软件。UNC1069 是一个与朝鲜有关联的网络威胁组织，经常对软件开发人员和科技组织使用社会工程学策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>
<li><a href="https://grokipedia.com/page/UNC1069">UNC1069</a></li>
<li><a href="https://www.linkedin.com/pulse/axios-javascript-library-http-requests-rehan-a-xu3rc">AXIOS ( javaScript Library for HTTP requests)</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#social engineering`, `#open source security`, `#cybersecurity`

---

<a id="item-3"></a>
## [工信部通报 iOS 高危漏洞 建议尽快升级](https://www.nvdb.org.cn/publicAnnouncement/2040008892420247553) ⭐️ 8.0/10

中国工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）发布官方警告，确认存在一个正在被活跃利用的高危漏洞，该漏洞影响所有从 13.0 到 17.2.1 版本的苹果 iOS 系统，平台建议所有受影响用户立即升级系统修复该漏洞。 该漏洞影响了数亿 iPhone 和 iPad 用户，攻击者已经可以利用它窃取用户个人信息并完全控制设备，因此及时修复漏洞对防范针对苹果用户的大规模网络攻击至关重要。 攻击者通过短信、邮件或投毒网页发送恶意链接来传播漏洞利用代码，诱导用户访问恶意网站后，会植入远程控制木马并获取系统最高权限。

telegram · zaihuapd · Apr 3, 11:23

**背景**: NVDB 即工业和信息化部网络安全威胁和漏洞信息共享平台，是中国官方监测发布网络安全风险预警的平台。这种级别的高危远程代码执行漏洞允许攻击者在用户不知情的情况下，在目标设备上运行任意恶意代码，最终可导致设备被完全控制和数据被窃取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.henan100.com/news/2026/1240020.shtml">有攻击组织仿冒“龙虾”下载 网 站 和 安 装文件！ 工 信 部 NVDB ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/File_inclusion_vulnerability">File inclusion vulnerability - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/AMD_AutoUpdate_remote_code_execution_vulnerability">AMD AutoUpdate remote code execution vulnerability</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#iOS vulnerability`, `#security patch`, `#Apple security`

---

<a id="item-4"></a>
## [激光无线通信达 360Gbps 能耗仅 Wi-Fi 一半](https://www.sciencedaily.com/releases/2026/04/260402042734.htm) ⭐️ 8.0/10

研究人员展示了一套芯片级激光无线通信系统，在 2 米测试中实现了 362.7Gbps 的总传输速率，单位比特能耗仅为当前领先 Wi-Fi 技术的一半。该研究采用 5×5 的 VCSEL 激光阵列，相关成果已发表在同行评审期刊《Advanced Photonics Nexus》上。 这项突破比现有 Wi-Fi 拥有高得多的传输速率和更低的能耗，为未来满足日益增长数据需求的短距高速无线通信系统提供了极具潜力的新选择。它有望满足消费和企业应用场景对超高速无线连接不断增长的需求。 该系统测得的单位比特能耗为 1.4 纳焦耳，测试中 5×5 阵列共 25 个激光器启用了 21 个，单个激光器的传输速率介于 13Gbps 至 19Gbps 之间。

telegram · zaihuapd · Apr 4, 01:47

**背景**: VCSEL 全称垂直腔面发射激光器，是一类从芯片顶表面垂直方向发射激光的半导体光源。单个 VCSEL 的发射孔径很小，它可以方便地被组合成二维阵列来实现更高的输出功率与并行传输，非常适合应用在光无线通信场景中。《Advanced Photonics Nexus》是一本经同行评审的开放获取学术期刊，专注于发表光子学及相关工程领域具有高影响力的全新研究成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/垂直腔面射型雷射器">垂直腔面射型雷射器 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.highlightoptics.com/Product/1053.html">Inphenix垂直腔面发射激光器，VCSEL激光器，阵列芯片</a></li>
<li><a href="https://www.spiedigitallibrary.org/journals/advanced-photonics-nexus">Advanced Photonics Nexus</a></li>

</ul>
</details>

**标签**: `#laser wireless communication`, `#optical communication`, `#wireless technology`, `#research breakthrough`

---

<a id="item-5"></a>
## [FCC 全面禁止外国产新型路由器](https://t.me/zaihuapd/40689) ⭐️ 8.0/10

美国联邦通信委员会（FCC）出于对网络安全与供应链漏洞的担忧，宣布全面禁止将外国生产的新型消费级路由器进口到美国市场。已经获得批准的现有型号和已经投入使用的设备不受新规限制，厂商可向美国国家安全机构申请禁令豁免。 这一影响深远的监管变动将大幅重塑全球网络硬件市场，改变全球供应链格局，并影响消费级网络基础设施的国际贸易。它将迫使外国路由器厂商调整生产和销售策略，同时也会提升全行业对网络设备供应链安全的关注。 FCC 已将这些外国生产的消费级路由器列入其《安全网络法案》下的受管辖实体名单，未经认证的新型号将无法获得美国市场的销售授权。本次禁令遵循新老划断原则，已经获得批准和投入使用的现有设备的日常使用、进口与销售都完全不受影响。

telegram · zaihuapd · Apr 4, 02:35

**背景**: FCC 设有一份受管辖实体名单，被列入的通信设备供应商被认为会对美国国家安全构成威胁，该名单此前已将华为、中兴等中国大型网络设备企业纳入其中。厂商要在美国市场销售网络设备和电子产品，必须先通过合规测试与审批流程获得 FCC 的官方设备授权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fcc.gov/supplychain/coveredlist">List of Equipment and Services Covered By Section 2 of The Secure Networks Act | Federal Communications Commission</a></li>
<li><a href="https://legalclarity.org/fcc-covered-list-prohibited-equipment-and-services/">What Is the FCC Covered List? Rules and Penalties - LegalClarity</a></li>
<li><a href="https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization">Equipment Authorization - Federal Communications Commission</a></li>

</ul>
</details>

**标签**: `#network security`, `#regulatory policy`, `#supply chain security`, `#networking hardware`

---

<a id="item-6"></a>
## [美团开源统一多模态 LongCat-Next](https://www.aibase.com/zh/news/26849) ⭐️ 8.0/10

美团技术团队在 2025 年 4 月 3 日正式发布并开源原生多模态大模型 LongCat-Next，该模型通过全新 DiNA 架构将视觉、语音和文本处理统一到单个离散 Token 框架中，在多个行业基准测试上性能超越现有模型。 这一进展证明了来自视觉和语音的非语言物理信息可以像文本一样被离散化和建模，为构建能够原生感知并与现实世界交互的人工智能打下了基础，而完全开源也让整个研究和开发者社区受益。 LongCat-Next 采用 dNaViT 视觉分词器，支持任意分辨率输入，在保留关键任务细节的前提下实现了 28 倍像素空间压缩，在 MathVista 测试得分 83.1、C-Eval 得分 86.80，在 OmniDocBench 密集文本基准测试中性能超越 Qwen3-Omni 和专用视觉模型 Qwen3-VL。

telegram · AI_News_CN · Apr 3, 10:19

**背景**: 大多数现有多模态大语言模型遵循传统的「语言基座+插件」碎片化架构，将非文本模态视作以文本为核心的外部附加模块。而 LongCat-Next 采用离散原生自回归（DiNA）架构，将三种模态全部转换为同源离散 Token，在统一建模框架中平等处理所有模态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.27538">[2603.27538] LongCat-Next: Lexicalizing Modalities as Discrete Tokens</a></li>
<li><a href="https://a2a-mcp.org/blog/what-is-longcat-next">What Is LongCat-Next? Meituan's Open-Source Native Multimodal ...</a></li>
<li><a href="https://www.longcatai.org/news/longcat-next">LongCat-Next Released: Native Discrete Multimodal Model</a></li>

</ul>
</details>

**标签**: `#multi-modal large model`, `#large language model`, `#AI architecture`, `#open-source AI`

---

<a id="item-7"></a>
## [Anthropic 禁止订阅用户使用 OpenClaw](https://news.ycombinator.com/item?id=47633396) ⭐️ 7.0/10

从 2026 年 4 月 4 日太平洋时间中午 12 点起，Anthropic 将不再允许包括 OpenClaw 在内的第三方 AI 框架使用现有 Claude Code 订阅额度，这类使用场景需要单独的按量付费计费。该公司提供与用户月订阅价格等额的一次性额度来平滑过渡，还会为不接受新政策的用户办理退款。 这一政策变动会影响所有依赖 Claude 消费级订阅 API 的第三方自主 AI 代理工具，将重塑围绕 Anthropic 消费级 AI 服务构建的开发者生态，迫使开发者要么接受新定价模式，要么转投其他平台。它也凸显了 AI 服务商面临的矛盾：固定价格订阅制和自主代理使用场景高昂的算力成本之间的矛盾日益突出。 Anthropic 表示，OpenClaw 这类第三方框架给其基础设施带来了过大压力，因此需要做出这一调整，为官方核心产品用户优先保障算力容量。该政策将从 4 月 4 日起先对 OpenClaw 执行，后续会推广到所有其他第三方框架。

hackernews · firloop · Apr 3, 22:55

**背景**: OpenClaw 是一款免费开源自主 AI 代理，它可以通过 Claude Code 连接并调用 Claude 的大语言模型能力，自动化完成包括开发工作在内的端到端任务。Claude Code 是 Anthropic 推出的官方智能编码代理工具，允许开发者直接在终端中调用 Claude 来编辑代码、运行测试和交付软件。本文语境下的第三方 AI 框架指的是接入现有 Claude 订阅权限、来添加 Anthropic 官方工具不具备的全新自主功能或特色功能的外部工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 部分评论者认同 Anthropic 的决定，他们指出订阅制依赖大多数用户的低使用率来补贴高用量用户，而 OpenClaw 这类自主工具消耗的算力远超过普通用户。另一些用户对这一变动感到不满，表示他们会转用更便宜的替代 AI 模型，不愿意为单独的按量付费支付更高成本。还有开发者指出 OpenClaw 的集成方式和此前被封禁的工具不同，并担心 Conductor 这类其他合法第三方集成接下来也会被封禁。

**标签**: `#Anthropic Claude`, `#AI policy`, `#developer tools`, `#third-party integrations`, `#pricing changes`

---

<a id="item-8"></a>
## [AI 工具大幅增加 Linux 内核安全漏洞报告](https://simonwillison.net/2026/Apr/3/willy-tarreau/#atom-everything) ⭐️ 7.0/10

资深开源开发者 Willy Tarreau 指出，受 AI 漏洞检测工具推动，Linux 内核安全漏洞报告量从两年前的每周 2-3 份，暴涨至 2026 年初的每天 5-10 份。报告量激增（其中包含大量重复报告）迫使 Linux 内核安全团队新增更多维护人员来应对工作负载增长。 这一趋势展现了 AI 在安全研究中的普及如何改变核心开源基础设施的维护工作，它既带来了发现更多漏洞的新机遇，也给本就负担过重的维护团队带来了新的运营挑战。整个依赖 Linux 内核的软件生态都会受到影响，因此调整维护流程将产生广泛的安全影响。 Tarreau 指出，AI 生成的新漏洞报告中大部分技术结论仍然正确，但很大一部分是其他 AI 工具或研究人员已经发现过的重复漏洞。报告量在周五和周二达到最高。

rss · Simon Willison · Apr 3, 21:48

**背景**: AI 驱动的漏洞检测工具是利用人工智能自动扫描源代码，查找安全漏洞和缺陷的工具。Linux 内核是绝大多数现代服务器和消费级操作系统的核心基础软件，它依赖小规模志愿者维护团队对上报的安全漏洞进行分类、验证和修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalocean.com/resources/articles/ai-code-review-tools">10 AI Code Review Tools That Find Bugs & Flaws in 2025 | DigitalOcean</a></li>
<li><a href="https://www.browserstack.com/guide/bug-triage-process">Bug Triage : What, Why and How to perform? | BrowserStack</a></li>

</ul>
</details>

**标签**: `#open source security`, `#linux kernel`, `#AI in software`, `#software maintenance`

---

<a id="item-9"></a>
## [格雷格：AI 开源安全报告质量快速提升](https://simonwillison.net/2026/Apr/3/greg-kroah-hartman/#atom-everything) ⭐️ 7.0/10

知名 Linux 内核维护者格雷格·克罗阿-哈特曼观察到，AI 生成的开源安全报告在数月内迅速从明显错误的低质量「AI 垃圾」变成了合格、真实可用的报告，这一转变发生在 2026 年 3 月前后。 这位顶尖开源核心维护者的观察标志着人工智能对核心开源开发流程的影响发生了重大转变，说明 AI 正在成为开源安全工作中真正实用的工具，它将改变未来开源项目处理安全审计的方式。 克罗阿-哈特曼指出，就在几个月前这些 AI 生成报告质量极低，被直接归为「AI 垃圾」，但在他 2026 年 3 月接受采访的大约一个月前，质量发生了突变，所有开源项目得到的 AI 报告都已经可以使用。

rss · Simon Willison · Apr 3, 21:44

**背景**: 格雷格·克罗阿-哈特曼是 Linux 内核最知名、任职时间最长的维护者之一，而 Linux 内核是全球使用最广泛的开源操作系统的核心。Linux 内核维护者负责审核代码变更、管理子系统，保障内核项目的代码质量和安全。随着生成式 AI 在开源开发中的普及，AI 生成的安全扫描和报告已经越来越常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zdnet.com/article/maybe-open-source-needs-ai/">How AI has suddenly become much more useful to open-source ...</a></li>
<li><a href="https://www.linuxfoundation.org/blog/blog/role-of-a-linux-kernel-maintainer">Role of a Linux Kernel Maintainer</a></li>

</ul>
</details>

**标签**: `#open source`, `#linux kernel`, `#generative ai`, `#security`, `#software development`

---

<a id="item-10"></a>
## [沙箱 iframe 中 CSP 元标签可阻止 JS 逃逸](https://simonwillison.net/2026/Apr/3/test-csp-iframe-escape/#atom-everything) ⭐️ 7.0/10

开发者 Simon Willison 发现，注入到沙箱 iframe 内容顶部的内容安全策略元标签能够被正常执行，即便后续添加的不受信 JavaScript 试图修改它们也不受影响。 这一发现解决了开发者处理不受信嵌入内容时的常见实际问题，允许在不使用独立专用域名的情况下，在 iframe 中安全隔离不受信内容。 Willison 是在开发他自己的定制版 Claude Artifacts（一个承载隔离交互式内容的功能）时发现这个特性的。

rss · Simon Willison · Apr 3, 16:05

**背景**: 内容安全政策（CSP）是一种网络安全机制，它可以阻止未授权的脚本和资源，以防范跨站脚本等攻击。CSP 最常通过 HTTP 响应头传递，但也可以通过 HTML 中的元标签添加，不过此前人们知道这种方式的效果有限。沙箱 iframe 被用于隔离不受信的嵌入内容，但要对其应用 CSP 保护通常需要将 iframe 内容托管在独立域名上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Content_Security_Policy">Content Security Policy - Wikipedia</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html">Content Security Policy - OWASP Cheat Sheet Series How to Set Up a Content Security Policy (CSP) - Sucuri Blog Content Security Policy (CSP) Headers - Complete Reference Guide Content Security Policy ( CSP ) Headers - Complete Reference Guide Content Security Policy - Wikipedia Content Security Policy ( CSP ) Headers - Complete Reference Guide Content-Security-Policy ( CSP ) Header Quick Reference Free CSP Analyzer & Security Headers Scanner | HeaderTest Content Security Policy - Wikipedia</a></li>
<li><a href="https://web.dev/articles/sandboxed-iframes">Play safely in sandboxed IFrames | Articles | web.dev</a></li>

</ul>
</details>

**标签**: `#web security`, `#content security policy`, `#iframes`, `#javascript`, `#sandboxing`

---

<a id="item-11"></a>
## [Google Vids 开放免费 Veo 3.1 AI 视频生成](https://www.techradar.com/ai-platforms-assistants/google-is-pushing-ai-video-into-ordinary-life-just-as-openai-pulls-sora-back) ⭐️ 7.0/10

Google 更新了浏览器端 AI 视频制作工具 Google Vids，接入了 Veo 3.1 AI 视频生成模型，向所有 Google 账号持有者开放每月 10 次免费 AI 视频生成额度。本次更新还向付费订阅用户独家新增了 Lyria 3 和 Lyria 3 Pro AI 音乐生成功能以及可自定义的数字化身功能，同时将顶级订阅用户的生成额度提升至每月 1000 条。 本次更新扩大了普通用户对尖端生成式 AI 视频技术的获取渠道，是推动高级 AI 视频创作走进日常使用的重要一步。Google 面向普通消费者扩大 AI 视频使用权限的做法，也和 OpenAI 近日限制 SoraAI 生成器公开访问权限的决定形成了直接对比。 Veo 3.1 是 Google DeepMind 最新的顶级视频生成模型，支持最高 4K 分辨率输出并可原生生成音频，本次接入 Google Vids 的 Lyria 3 和 Lyria 3 Pro 音乐模型可以生成时长从 30 秒到 3 分钟不等的背景配乐。新 AI 音乐功能和数字化身功能仅对付费的 Google AI Pro、Google AI Ultra 和 Workspace AI Ultra 订阅用户开放，顶级订阅用户可获得大幅提升后的月度生成额度。

telegram · zaihuapd · Apr 3, 05:23

**背景**: Google Vids 是 Google Workspace 生产力套件中包含的一款 AI 驱动在线时间轴式视频编辑应用，旨在直接在浏览器中简化协作视频创作流程。Veo 3.1 是 Google DeepMind 对前代 Veo 3 生成式视频模型的增量优化更新，提升了输出质量，增强了音频生成效果并改进了图生视频能力。Lyria 3 和 Lyria 3 Pro 是 Google DeepMind 最新的 AI 音乐生成模型，其中 Pro 版本支持生成最长 3 分钟的更长曲目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Vids">Google Vids - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/video">Generate videos with Veo 3.1 in Gemini API | Google AI for ... Top Stories Introducing Veo 3.1 and new creative capabilities in the ... Google Veo 3.1: The AI Video Generator That Includes Audio Veo 3.1: Google's Latest AI Video Update — New Features and ... Veo 3.1 API – Free Access to Google’s Latest AI Video Model ... Generate videos with Veo 3 . 1 in Gemini API | Google AI for Developers Introducing Veo 3 . 1 and new creative capabilities in the Gemini API Veo 3 . 1 API – Free Access to Google’s Latest AI Video Model | Kie AI Introducing Veo 3 . 1 and new creative capabilities in the Gemini API</a></li>
<li><a href="https://workspaceupdates.googleblog.com/2026/03/create-longer-musical-tracks-in-gemini-app-with-Lyria-3-Pro.html">Create longer musical tracks in the Gemini app with Lyria 3 Pro</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#AI Video Generation`, `#Google Vids`, `#Veo 3.1`

---

<a id="item-12"></a>
## [国家网信办就数字虚拟人监管征意见](https://mp.weixin.qq.com/s/EHpjg2sfth0W7OE-v6hq9g) ⭐️ 7.0/10

2026 年 4 月 3 日，国家互联网信息办公室发布了《数字虚拟人信息服务管理办法（征求意见稿）》，公开向社会征求意见，反馈截止时间为 2026 年 5 月 6 日。征求意见稿提出了一系列监管要求，包括强制数字身份标识、限制敏感个人信息使用、禁止向未成年人提供虚拟伴侣和虚拟亲属服务、要求高影响力服务提供者完成算法备案，违规最高可处 20 万元罚款。 这是中国针对快速发展的数字虚拟人行业出台的首份专项监管征求意见稿，将规范行业发展，保护未成年人等弱势群体的合法权益。它会影响中国所有数字虚拟人服务提供者和开发者，为行业相关主体明确了合规要求。 征求意见稿明确要求，所有数字虚拟人的服务展示区域必须全程显著标注“数字人”字样。使用自然人敏感个人信息进行建模需要取得自然人的单独同意，处理未成年人信息需要获得监护人同意，用户撤回同意后提供者必须注销对应的数字虚拟人。

telegram · zaihuapd · Apr 3, 09:39

**背景**: 随着人工智能技术的进步，高保真数字虚拟人已经从科幻概念走进现实应用，在娱乐、电商、教育、陪伴等多个场景得到广泛使用。IDC 预测，2026 年中国 AI 数字虚拟人的市场规模将达到 102.4 亿元，但行业也出现了挪用名人肖像、擅自“复活”逝者、诱导未成年人沉迷不当服务等缺乏规范的问题。算法备案是要求具有舆论属性或社会动员能力的算法服务提供者向监管机构报送相关信息进行登记的行政监管流程，在 2026 年已经成为中国相关企业的法定合规要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-04/03/c_1776952388655846.htm">专家解读｜以人为本划定数字虚拟人服务边界，助力智能经济高质量发展_...</a></li>
<li><a href="https://news.bjd.com.cn/2026/04/03/11668741.shtml">专家解读｜以人为本，数字虚拟人管理规范引领技术向善_京报网</a></li>
<li><a href="https://baike.baidu.com/item/算法备案/67405404">算法备案_百度百科</a></li>

</ul>
</details>

**标签**: `#digital virtual human`, `#regulation`, `#policy`, `#internet governance`

---

<a id="item-13"></a>
## [LinkedIn 被指扫描浏览器扩展并共享数据](https://cybernews.com/privacy/linkedin-surveillance-browsergate/?utm_source=flipboard&amp;utm_content=CyberNews_com%2Fmagazine%2FLatest+cybersecurity+news) ⭐️ 7.0/10

代表 LinkedIn 商业用户的组织开展的 BrowserGate 调查指出，LinkedIn 秘密扫描用户已安装的浏览器扩展以收集敏感用户数据，且在未获得用户同意也未披露的情况下将该数据与包括 HUMAN Security 在内的第三方共享。这一指称的行为可能影响全球共计 4.05 亿 LinkedIn 用户。 这一指称影响了数亿用户，并且引发了 GDPR 等主要隐私法规下的严重合规问题。如果指控得到证实，它将成为大型社交平台违规收集敏感数据的先例，也会暴露浏览器活动用户隐私保护方面的漏洞。 被指的扫描行为覆盖超过 6000 款浏览器扩展，其中包括 200 多款竞品工具，扫描结果可以推导出用户的宗教信仰、政治倾向、健康状况以及求职状态等敏感信息。根据欧盟 GDPR 的要求，这类数据处理活动需要获得用户的明确同意，而根据指控 LinkedIn 并未取得这类同意。

telegram · zaihuapd · Apr 3, 12:09

**背景**: GDPR 是欧盟出台的综合性隐私法规，它要求企业在处理敏感个人数据前必须获得用户的明确同意，适用范围覆盖所有向欧盟境内用户提供服务的平台。BrowserGate 是发布针对 LinkedIn 指控的调查项目的名称，该项目已表示会继续调查，目前业内观察者都在等待 LinkedIn 和相关监管机构的官方回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/privacy/linkedin-surveillance-browsergate/">LinkedIn secretly injects code to spy on your browser | Cybernews</a></li>
<li><a href="https://gigazine.net/gsc_news/en/20260403-linkedin-browsergate/">BrowserGate is a research project that claims that every time ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GDPR">GDPR</a></li>

</ul>
</details>

**标签**: `#Privacy`, `#Data Security`, `#LinkedIn`, `#GDPR`, `#Browser Security`

---

<a id="item-14"></a>
## [千问 App 上线万相 Wan2.7 视频模型](https://www.aibase.com/zh/news/26850) ⭐️ 7.0/10

阿里巴巴的千问 App 在 4 月 3 日上线了全新 Wan2.7 视频生成模型，在已发布的 Wan2.7 图像模型之外，为所有用户新增了免费的文本驱动视频编辑、视频续写和动作模仿功能。 这次更新为普通用户免费带来了易用的专业 AI 视频创作与编辑工具，降低了短视频内容创作的技术门槛，拓展了生成式 AI 在日常创意工作中的可及应用场景。 该模型支持将 2 秒的输入视频续写延长至最长 15 秒，可以复刻参考视频中复杂的多人协同动作，还支持对角色动作、机位、视频风格进行精准调整，同时保持画面视觉一致性。

telegram · AI_News_CN · Apr 3, 14:33

**背景**: Wan2.7 是阿里巴巴推出的升级款生成式 AI 模型，原本专注于图像生成与编辑，本次拓展了视频能力。文本驱动视频编辑允许用户用自然语言提示词修改视频内容，无需进行复杂的手动剪辑操作，而视频续写则是为用户上传的现有视频生成连贯的新内容来延长时长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wan27.org/">Wan 2.7 (wan2.7) — AI Video Generation, Editing & Recreation ...</a></li>
<li><a href="https://www.eachlabs.ai/blog/wan-2-7-is-here-everything-the-new-model-can-do">Wan 2.7 Is Here: Everything the New Model Can Do | Eachlabs</a></li>
<li><a href="https://aivideomaker.ai/zh/extend-video">aivideomaker AI 延长视频工具｜基于原视频的智能续写与场景延展</a></li>

</ul>
</details>

**标签**: `#generative video AI`, `#AI model release`, `#video editing`, `#Wan2.7`, `#Qianwen`

---

<a id="item-15"></a>
## [OpenAI 多名高管职务发生变动](https://api3.cls.cn/share/article/2335203?sv=8.7.5) ⭐️ 7.0/10

在 OpenAI 可能于 2024 年启动 IPO 的前夕，公司出现了多项高层人事变动：任职已久的首席运营官 Brad Lightcap 将转任特别项目负责人，首席营销官 Kate Rouch 将卸任专注癌症康复治疗，AGI 业务负责人 Fidji Simo 将休数周病假治疗慢性神经免疫疾病。 由于 OpenAI 是全球领先的生成式人工智能企业，且正筹备备受关注的上市计划，这次高层重大变动可能影响公司的业务推进和 IPO 规划，也会对整个全球人工智能行业产生连锁影响。 Brad Lightcap 转岗后，新任命的首席营收官 Denise Dresser 将接管他原有的部分职责，Lightcap 转岗后将直接向首席执行官萨姆·奥尔特曼汇报，并牵头推进与私募股权公司的合资项目，拓展企业软件销售业务。

telegram · AI_News_CN · Apr 3, 22:58

**背景**: OpenAI 是全球最具影响力的人工智能研发企业之一，以开发 ChatGPT 和 GPT 系列大语言模型闻名。该公司一直传闻最早会在 2024 年启动首次公开募股，这也会是近年最受关注的科技企业 IPO 之一。AGI 即通用人工智能，指能够在各类任务上达到甚至超越人类能力水平的人工智能，是 OpenAI 的核心长期发展目标。

**标签**: `#OpenAI`, `#artificial intelligence`, `#management change`, `#AGI`

---

<a id="item-16"></a>
## [Anthropic 实质上禁止 OpenClaw 接入 Claude](https://www.cnbeta.com.tw/articles/tech/1556530.htm) ⭐️ 7.0/10

Anthropic 从 2025 年 4 月 4 日起实施新政策，禁止现有 Claude 订阅用户使用套餐内含额度访问第三方 AI 智能体 OpenClaw。想要继续使用 OpenClaw 的用户必须通过按需付费模式单独支付费用，实质上切断了免费第三方访问渠道。 这一变化凸显了 AI 平台所有者与在其模型之上开发工具的第三方开发者之间日益紧张的关系，标志着平台开始对生态使用施加更严格管控以管理基础设施成本。它还重塑了基于大语言模型平台的热门第三方 AI 工具的访问经济逻辑。 Anthropic 表示，此次政策调整是为了应对不断增长的基础设施负载，优先保障使用官方产品用户的体验，公司还将向所有订阅用户发放等同于月度套餐费用的一次性补贴。OpenClaw 的开发者目前已入职 OpenAI，在劝说 Anthropic 撤销决定失败后，仅争取到将政策推迟一周执行。

telegram · AI_News_CN · Apr 4, 01:13

**背景**: OpenClaw 是一款热门的开源自主 AI 个人助理，能够为用户完成邮件管理、日程安排、自动网页交互等多步实际任务，运行在 Anthropic 的 Claude 大语言模型之上。ClaudeCowork 是 Anthropic 官方自研的智能体 AI 工具，用于处理多步知识工作，定位与 OpenClaw 这类第三方智能体形成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/product/claude-cowork">Claude Cowork | Anthropic’s agentic AI for knowledge work</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI Industry`, `#Anthropic Claude`, `#Third-party AI Tools`, `#AI Policy`

---