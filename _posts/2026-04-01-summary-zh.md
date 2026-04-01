---
layout: default
title: "Horizon Summary: 2026-04-01 (ZH)"
date: 2026-04-01
lang: zh
---

> From 47 items, 15 important content pieces were selected

---

1. [OpenAI 完成融资估值达 8520 亿美元](#item-1) ⭐️ 9.0/10
2. [Axios npm 软件包遭遇供应链攻击](#item-2) ⭐️ 9.0/10
3. [axios 维护者账号被劫持 投毒 npm](#item-3) ⭐️ 9.0/10
4. [谷歌将比特币量子攻击门槛降低 20 倍](#item-4) ⭐️ 9.0/10
5. [OpenAI 完成 1220 亿美元巨额融资](#item-5) ⭐️ 9.0/10
6. [Anthropic Claude Code 源代码通过 NPM 泄露](#item-6) ⭐️ 8.0/10
7. [Claude Code 五十万行源码泄露](#item-7) ⭐️ 8.0/10
8. [谷歌推出低价 Veo 3.1 Lite 视频模型](#item-8) ⭐️ 8.0/10
9. [Salesforce 为 Slack 推出 30 项 AI 升级](#item-9) ⭐️ 8.0/10
10. [开源项目 LiteLLM 遭供应链攻击](#item-10) ⭐️ 8.0/10
11. [GitHub 出现非官方还原 Claude Code 源码](#item-11) ⭐️ 7.0/10
12. [Meta 发布新款 Ray-Ban 智能眼镜](#item-12) ⭐️ 7.0/10
13. [Claude Code 源码泄漏 微软转向原生应用](#item-13) ⭐️ 7.0/10
14. [Claude Code 泄露导致八千仓库下架](#item-14) ⭐️ 7.0/10
15. [Anthropic 源码泄露实为营销炒作](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 完成融资估值达 8520 亿美元](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html) ⭐️ 9.0/10

OpenAI 已于 2026 年 3 月 31 日完成 1220 亿美元融资轮，投后估值达到 8520 亿美元。 这一破纪录的估值巩固了 OpenAI 作为估值最高私有 AI 公司的地位，也重塑了市场对全球人工智能行业初创企业估值的预期。 这份融资公告将 1220 亿美元标注为承诺资本，这可能仅代表投资方承诺的投资，而非已经注入公司的资金，同时公布的估值可能是最高估值，并非所有投资者参与投资的价格。

hackernews · surprisetalk · Mar 31, 20:07

**背景**: 投后估值指的是企业在完成一轮投资、注入新资本后立即估算的总价值，计算公式为投资前企业估值加上本轮新增投资额。这个指标在风投领域被广泛使用，用于确定投资者出资后获得的企业所有权比例，计算逻辑和上市公司的市值计算类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-money_valuation">Post-money valuation</a></li>
<li><a href="https://www.investopedia.com/terms/p/postmoneyvaluation.asp">Understanding Post-Money Valuation: Key Concepts and Examples</a></li>

</ul>
</details>

**社区讨论**: 社区讨论涵盖多种观点：部分用户将 OpenAI 的收入增长和竞争对手 Anthropic 对比，指出两者的增长差距，该差距可能部分归因于双方不同的收入统计方式，另有用户对极高的估值表示质疑，指出该估值可能并非适用于所有投资者，还有许多批评者认为本轮融资标志着 OpenAI 彻底背离了最初的非盈利创始原则，即造福全人类而非优先追求利润。

**标签**: `#OpenAI`, `#artificial intelligence`, `#funding`, `#startup valuation`, `#AI industry`

---

<a id="item-2"></a>
## [Axios npm 软件包遭遇供应链攻击](https://simonwillison.net/2026/Mar/31/supply-chain-attack-on-axios/#atom-everything) ⭐️ 9.0/10

广受欢迎的 Axios npm 软件包的两个恶意版本（1.14.1 和 0.30.4）被发布，它们携带名为`plain-crypto-js`的恶意依赖，该依赖会窃取用户凭证并安装远程访问木马。本次攻击被认为源自泄露的长期有效 npm 访问令牌。 Axios 每周在 npm 上获得超过 1 亿次下载，因此这次攻击给整个 JavaScript 开发生态系统带来了广泛的安全风险。它还暴露了目前流行开源项目的 npm 软件包发布流程中存在严重安全漏洞。 这些恶意软件包在发布时没有对应的 GitHub 版本，这种模式也出现在近期针对 LiteLLM 项目的供应链攻击中。Axios 此前已经开启了一个公开 issue 讨论采纳 npm 可信发布功能，该功能可以阻止这类未经授权的发布行为。

rss · Simon Willison · Mar 31, 23:28

**背景**: npm 是 JavaScript 语言的默认包管理器，供开发者分发和复用开源代码库。长期有效 npm 访问令牌是一种持久化身份凭证，允许持有者发布软件包更新，这类令牌一旦泄露，被滥用的风险远高于短期凭证。可信发布是 npm 推出的新型安全功能，它使用 OpenID Connect 只允许授权的 CI/CD 工作流（例如 GitHub Actions）发布软件包更新，无需再使用长期有效访问令牌。远程访问木马（RAT）是一种恶意软件，它能让攻击者获得对受感染计算机的完全未授权远程控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/about-access-tokens/">About access tokens | npm Docs</a></li>
<li><a href="https://docs.npmjs.com/trusted-publishers/">Trusted publishing for npm packages</a></li>
<li><a href="https://www.bitdefender.com/en-us/business/infozone/what-is-a-remote-access-trojan-rat">What is Remote Access Trojan (RAT) - InfoZone</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#npm`, `#cybersecurity`, `#javascript`

---

<a id="item-3"></a>
## [axios 维护者账号被劫持 投毒 npm](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) ⭐️ 9.0/10

2026 年 3 月 31 日，安全机构 StepSecurity 发现广泛使用的 JavaScript HTTP 库 axios 的 npm 维护者账号遭劫持。攻击者手动发布了两个恶意版本 axios@1.14.1 和 axios@0.30.4，向 Windows、macOS 和 Linux 系统植入远程控制木马。 由于 axios 每周下载量超过 3 亿次，全球无数软件项目都依赖该库，这次重大 npm 供应链攻击对 JavaScript 开发者和终端用户构成了广泛威胁。受影响的项目需要立即修复，以防止发生未授权远程访问和数据泄露。 恶意版本通过名为 plain-crypto-js 的虚假依赖触发恶意代码，感染后会连接攻击者控制的命令与控制（C2）服务器，还会自动删除恶意脚本并伪造干净的配置文件以躲避检测。安全专家建议开发者降级到安全版本 1.14.0 或 0.30.3，并更换受影响设备上的所有凭据。

telegram · zaihuapd · Mar 31, 04:10

**背景**: npm 是 JavaScript 默认的包管理器，托管着数百万个开源软件包，开发者通常会将这些包作为依赖引入自己的项目。GitHub Actions 是热门的 CI/CD 平台，许多 npm 包维护者使用它来自动化包发布工作流。远程访问木马（RAT）是一种恶意软件，可让攻击者远程完全控制受感染设备，窃取数据或安装更多恶意程序。命令与控制（C2）服务器是网络犯罪分子用来向受感染设备发送指令、收集数据的中心化控制系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/actions/quickstart">Quickstart for GitHub Actions - GitHub Docs</a></li>
<li><a href="https://www.techtarget.com/searchsecurity/definition/RAT-remote-access-Trojan">What is a RAT ( Remote Access Trojan )? | Definition from TechTarget</a></li>
<li><a href="https://www.malwarepatrol.net/command-control-servers-c2-servers-fundamentals/">C2 Servers: Command and Control Fundamentals & Risks</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#npm`, `#axios`, `#software security`, `#javascript`

---

<a id="item-4"></a>
## [谷歌将比特币量子攻击门槛降低 20 倍](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) ⭐️ 9.0/10

谷歌量子 AI 团队发布了针对破解椭圆曲线加密的 Shor 算法的突破性优化，将破解所需的物理量子比特数量从此前估计的 1000 万个降低到不足 50 万个。这种优化后的攻击可以在 9 分钟内窃取未确认的比特币，导致约三分之一的比特币总供应量面临潜在风险。 这一突破让针对广泛使用的椭圆曲线加密和比特币的实用量子攻击离现实更近了一步，推动加密货币行业加快开发和采用后量子安全标准。它凸显了更新当前依赖 ECC 的密码系统的迫切需求，而目前几乎所有主流加密货币都使用 ECC。 攻击者可以提前完成大部分准备计算，在交易广播后约 9 分钟内推导出比特币私钥，因此有 41%的概率在下一个区块确认交易前劫持资金。2021 年比特币 Taproot 升级默认公开公钥，这可能会在已经暴露的 690 万枚比特币之外进一步扩大脆弱地址的范围。

telegram · zaihuapd · Mar 31, 08:03

**背景**: Shor 算法是 1994 年开发的量子算法，可以解决支撑椭圆曲线加密安全性的离散对数问题，让量子计算机能够从公开的公钥推导出私钥。椭圆曲线加密是一种公钥密码系统，它能用更小的密钥提供和 RSA 这类旧系统同等的安全性，因此成为比特币和大多数现代加密货币的默认选择。零知识证明是一种密码学协议，允许证明方在不披露任何额外基础信息的情况下证明某个陈述为真，谷歌团队在公开披露本次研究时用零知识证明隐藏了攻击方法的细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic-curve_cryptography">Elliptic-curve cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#bitcoin`, `#cryptocurrency security`

---

<a id="item-5"></a>
## [OpenAI 完成 1220 亿美元巨额融资](https://www.aibase.com/zh/news/26738) ⭐️ 9.0/10

当地时间 3 月 31 日，通用人工智能领军企业 OpenAI 宣布完成新一轮融资，募集资金总额达 1220 亿美元，投后估值升至 8520 亿美元，创下全球初创企业估值的新纪录。 这笔融资将加快 OpenAI 的通用人工智能研发进度，强化行业马太效应，加速全球 AI 产业向头部玩家集中，大幅抬高了新竞争者的进入门槛。 本次 1220 亿美元的融资被业内视为大模型竞赛进入重资本阶段的标志性事件，这笔天量资金将为 OpenAI 扩建算力基础设施、招募顶尖人才和开发下一代前沿模型提供充足支持。

telegram · AI_News_CN · Apr 1, 01:36

**背景**: 通用人工智能（AGI）指的是能够适应多样环境、处理各类复杂任务的人工智能，区别于只为特定单一任务构建的弱人工智能。投后估值指完成新融资后公司的整体估值，代表资本市场对融资后公司总价值的定价。行业中的马太效应指的是强者愈强、弱者愈弱的发展趋势，会推动产业向头部集中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://drjackeiwong.com/2023/04/08/人工智能比較：弱-ani-vs-強-agi-vs-超-asi/">人 工 智 能 比較：弱 (ANI) vs 強 ( AGI ) vs 超 (ASI) - Dr. Jackei...</a></li>
<li><a href="https://www.sec.gov/Archives/edgar/data/1879016/000106299324016874/exhibit10-1.htm">Ivanhoe Electric Inc.: Exhibit 10.1 - Filed by newsfilecorp.com - SEC.gov</a></li>
<li><a href="https://www.nccu.edu.tw/p/406-1000-17600,r41.php?Lang=zh-tw">ICI跨域講座「A Future with AGI - 通 用 人 工 智 慧（ AGI ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#artificial intelligence`, `#venture funding`, `#AGI`, `#industry landscape`

---

<a id="item-6"></a>
## [Anthropic Claude Code 源代码通过 NPM 泄露](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/) ⭐️ 8.0/10

Anthropic 的 Claude Code 源代码因发布到公共 NPM 注册表的源映射未被排除而意外泄露，此后 Anthropic 已对相关存储库发出 DMCA 下架通知，其中甚至包括部分未托管泄露代码的存储库。此次泄露披露了这款 AI 编码工具的专有实现细节，包括其“隐身模式”的相关内容。 此次泄漏凸显了现代 JavaScript 项目构建与发布管道配置错误的持续风险，暴露了全球最受欢迎的商业 AI 编码工具之一的专有内部逻辑，并引发了业内对代码已公开传播后仍采取激进 DMCA 下架做法的争论。 此次泄露源于 Bun JavaScript 运行时的默认源映射生成设置未被修改，仅因.npmignore 或 package.json 中缺少一行排除配置所导致。泄露的细节包括隐身模式的提示词，该提示词要求 Claude 避免在生成的代码提交和拉取请求中透露自己是 AI。

hackernews · alex000kim · Mar 31, 13:04

**背景**: Claude Code 是 Anthropic 开发的命令行 AI 编码工具，基于该公司自研的 Claude 大语言模型构建，可帮助开发者编写、编辑和管理代码。源映射是一种调试文件，可将压缩后的生产环境 JavaScript 映射回原始未编译源代码，如果公开到网上，任何人都可以通过它重建项目的完整原始源代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/">Anthropic accidentally leaked Claude Code source code via a map file ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区成员将作为常见构建配置错误的泄漏原因，和被暴露的专有内容分开讨论，并指出 Bun 已经存在关于默认源映射行为的开放 issue。许多社区成员批评 Anthropic 激进的 DMCA 下架行为，甚至删除了根本不含泄露代码的分支，观察者也对大量属于商业机密级别的内部注释被直接包含在发布的源代码中表示惊讶。

**标签**: `#source code leak`, `#Claude Code`, `#NPM`, `#software build pipelines`, `#AI coding tools`

---

<a id="item-7"></a>
## [Claude Code 五十万行源码泄露](https://www.aibase.com/zh/news/26735) ⭐️ 8.0/10

Anthropic 的低级 DevOps 配置错误导致 Claude Code 的 50 万行源代码通过 npm 包公开可访问，泄露的代码还披露了两个未发布功能：个性化像素赛博宠物伴侣 BUDDY，以及带有夜间做梦机制的自主后台学习功能 KAIROS。 这场泄露暴露了这家标榜专注于安全 AI 开发的头部 AI 公司存在重大运营安全漏洞，也给整个 AI 行业敲响了警钟，提醒人们在 AI 编码工具获得更高系统权限的当下，微小工程失误也会带来巨大风险。 本次泄露发生的原因是 Anthropic 没有从公开 npm 包中删除调试用的源代码映射（.map）文件，这种文件即使在压缩后的生产版本构建中也会完整暴露原始可读的 TypeScript 代码库，且泄露的代码已经在开发者社区中被永久存档和传播。

telegram · AI_News_CN · Apr 1, 01:04

**背景**: Claude Code 是 Anthropic 推出的官方智能 AI 编码工具，可帮助开发者理解代码库、编辑文件并更快交付项目。npm 是面向 JavaScript 和 TypeScript 代码的流行公共包 registry，源代码映射文件是一种调试资源，作用是将压缩打包后的代码映射回原始未编译的源代码，这类文件本不应该出现在私有软件的公开生产版本发布包中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/soufianebouaddis/claude-code">GitHub - soufianebouaddis/claude-code: Claude Code's leaked source ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo">Claude Code's Entire Source Code Was Just Leaked via npm Source ...</a></li>

</ul>
</details>

**标签**: `#Source Code Leak`, `#Anthropic Claude`, `#AI Security`, `#Software Development`

---

<a id="item-8"></a>
## [谷歌推出低价 Veo 3.1 Lite 视频模型](https://www.aibase.com/zh/news/26739) ⭐️ 8.0/10

谷歌正式发布了经过成本优化的轻量化 AI 视频生成模型 Veo 3.1 Lite，该模型生成 720P 分辨率视频的定价仅为每秒 0.05 美元。这款模型完善了谷歌的 Veo 3.1 产品矩阵，能以不到现有 Veo 3.1 Fast 模型一半的成本提供高质量输出。 推理成本的大幅下降消除了 AI 视频生成商业化落地的主要障碍，也标志着整个行业从单纯的参数竞赛转向效能优化的整体转变。它将为中小创作者和开发团队打开个性化定制视频、游戏实时过场生成等全新应用场景。 Veo 3.1 Lite 保留了 Google DeepMind 在时序一致性上的技术优势，避免了困扰许多早期轻量化视频模型的常见画面闪烁和畸变问题，同时能稳定输出 720P 质量，准确还原光影和运动细节。它的成本不到 Veo 3.1 Fast 的一半，生成速度却和后者保持一致。

telegram · AI_News_CN · Apr 1, 01:44

**背景**: 时序一致性是 AI 视频生成的核心性能指标，衡量模型在连续帧之间保持物体、光影、运动等视觉元素稳定、不出现闪烁畸变的能力。高昂的推理成本长期以来都是阻碍 AI 视频生成技术从实验室走向大规模商业化落地的主要瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/">How developers can use Veo 3.1 Lite for AI video generation</a></li>
<li><a href="https://getstream.io/glossary/temporal-consistency/">Temporal Consistency - What is it and how does it work?</a></li>
<li><a href="https://9to5google.com/2026/03/31/veo-3-1-lite/">Google commits to video generation, announces Veo 3.1 Lite</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#generative AI`, `#Google`, `#large language models`, `#AIGC`

---

<a id="item-9"></a>
## [Salesforce 为 Slack 推出 30 项 AI 升级](https://www.aibase.com/zh/news/26740) ⭐️ 8.0/10

Salesforce 宣布对 Slack 推出其发布以来规模最大的 AI 升级，新增了 30 项深度集成的生成式 AI 功能，这些功能连接 Salesforce Data Cloud，并且支持第三方大模型开放接入。 这次升级将 Slack 从单纯的沟通工具转变为 AI 驱动的企业生产力枢纽，符合企业协作工具 AI 化的行业趋势，将重塑企业内部团队的协作模式。 升级后的 Slack AI 可以生成跨频道的项目摘要，支持非技术用户通过自然语言构建自动化工作流，新增的上下文搜索可以直接回答问题并推荐相关专家，同时它既兼容 Salesforce 自家的 Einstein 模型，也支持 OpenAI、Anthropic 的第三方大模型。

telegram · AI_News_CN · Apr 1, 01:54

**背景**: Slack 是 Salesforce 旗下被广泛使用的企业协同办公平台，而 Salesforce 是全球客户关系管理（CRM）解决方案的领导者。Salesforce Einstein 是 Salesforce 平台的原生 AI 层，其在 2023 年推出的 Einstein GPT 是全球首个专门为 CRM 场景打造的生成式 AI 产品。Salesforce Data Cloud 是 Salesforce 自主开发的产品，能够统一企业所有客户数据，支持 AI 实时调取数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/668909967">Einstein GPT-生成式人工智能CRM全面解析：简介、架构、原理、产品、... Einstein AI 赋能 Salesforce：架构师视角下的预测智能深度解析 Artificial Intelligence (AI) at Salesforce AI销售10大标杆案例研究:Salesforce Einstein 如何用 AI 改造 B2B 销... Salesforce Einstein Copilot：企业生成式人工智能的最佳案例 - 53AI-... 他山之石系列报告 (一)：SALESFORCE的大模型TOB应用分析</a></li>
<li><a href="https://walk-ct.com/data-cloud/">Salesforce Data Cloud 的歷史與未來 - 沃克雲端</a></li>
<li><a href="https://slack.com/features/workflow-automation">Workflow Automation Tool, Software, & App | Slack</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Collaboration Tools`, `#Salesforce Slack`, `#Enterprise AI`, `#Productivity Software`

---

<a id="item-10"></a>
## [开源项目 LiteLLM 遭供应链攻击](https://www.aibase.com/zh/news/26745) ⭐️ 8.0/10

估值 100 亿美元的 AI 独角兽 Mercor 确认，其热门开源 AI 库 LiteLLM 遭到黑客组织 TeamPCP 发起的供应链攻击，被植入了恶意代码。勒索组织 Lapsus$也声称窃取了 Mercor 的内部数据，并泄露了包含内部通讯记录的样本数据。 作为日均百万级下载量、被广泛使用的大语言模型集成上游开源工具，本次攻击影响了数千家下游企业，暴露出快速扩张的开源 AI 基础设施生态存在严重安全漏洞。该事件推动整个 AI 行业重新审视开源组件的安全问题，促进行业建立更严格的安全监测机制。 被植入的恶意代码在攻击被发现后数小时内就得到识别和移除，Mercor 已经聘请第三方取证专家展开调查，并落实了紧急控制与补救措施。LiteLLM 也已紧急将合规认证机构更换为自动化合规服务提供商 Vanta。

telegram · AI_News_CN · Apr 1, 02:44

**背景**: LiteLLM 是一款热门开源 Python 开发工具与 AI 网关，可为开发者提供统一接口，用来调用 OpenAI、Anthropic 等厂商的 100 余种不同大语言模型 API。供应链攻击指黑客针对上游软件组件注入恶意代码，随后恶意代码会扩散到大量依赖该组件的下游用户与机构。Vanta 是一家提供自动化合规服务的科技公司，可帮助企业快速获取 ISO 27001、SOC 2 等常见安全认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM] · GitHub</a></li>
<li><a href="https://www.oldboyedu.com/blog/5152.html">供 应 链 攻 击 是什么? 应 该如何处理?</a></li>
<li><a href="https://36kr.com/p/2887512733080454">Vanta 获红杉、高盛参投的1.5亿美元C轮融资，用AI...</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#open source security`, `#AI infrastructure`, `#cybersecurity`

---

<a id="item-11"></a>
## [GitHub 出现非官方还原 Claude Code 源码](https://github.com/ChinaSiro/claude-code-sourcemap) ⭐️ 7.0/10

GitHub 上一个名为 claude-code-sourcemap 的非官方仓库，从官方公开的@anthropic-ai/claude-code npm 包附带的 source map 文件中，还原得到了 Claude Code 2.1.88 的共 4756 个源文件，其中包含 1884 个 TypeScript 和 TSX 文件。该仓库仅将还原得到的代码用于非商业研究发布，同时警告用户不要将该仓库链接到官方 Claude Code 安装，否则可能带来账户风险。 这次源码还原让外部研究人员可以对 Anthropic 的闭源 Claude Code CLI 进行独立安全审计和透明度分析，这在此前是无法实现的。该事件也暴露了商业 JavaScript/TypeScript 软件分发中的一个常见疏漏，可能导致专有源码意外完整泄露给公众。 还原的源码是直接从 Anthropic 官方分发的 cli.js.map source map 文件的`sourcesContent`字段提取得到，仓库也说明该结构不代表 Anthropic 官方内部开发仓库的原始结构。根据仓库声明，所有原始源码的版权仍归 Anthropic 所有。

telegram · zaihuapd · Mar 31, 09:33

**背景**: Claude Code 是 AI 公司 Anthropic 开发的闭源命令行工具，可供开发者在软件开发工作流中调用 Claude 大语言模型。Source map 是 JavaScript/TypeScript 编译打包过程中生成的标准文件，主要作用是将压缩后的生产代码映射回原始未编译的源码，方便开发人员调试。多数 source map 中包含的`sourcesContent`字段会存储原始源码的完整文本，因此当 source map 被公开分发时，就可以用来完整还原出原始源码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.theblockbeats.news/flash/338932">Claude Code 's latest npm package accidentally included a 60MB...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#source code reconstruction`, `#npm`, `#reverse engineering`, `#Anthropic`

---

<a id="item-12"></a>
## [Meta 发布新款 Ray-Ban 智能眼镜](https://www.aibase.com/zh/news/26741) ⭐️ 7.0/10

3 月 31 日，Meta 与依视路陆逊梯卡联合发布新款 Ray-Ban Meta 智能眼镜，该款新品支持包括渐进多焦、变色镜片在内的定制处方镜片，新增多项由 Meta AI 驱动的新功能，起售价定为 499 美元，将于 4 月 14 日在全球发售。 本次更新推动智能眼镜从极客小众产品转型为实用的 AI 移动计算终端，探索了后智能手机时代移动计算的全新范式，同时拓宽了多模态大模型的应用边界。 本次新品在保留轻量化设计的同时新增两款镜框款式，499 美元的起售价不包含后续定制处方镜片可能产生的数百美元额外费用。新增 AI 功能涵盖日语、普通话和阿拉伯语实时翻译、基于视觉识别的营养追踪，以及长对话摘要提取，解决了轻量化设备的信息过载交互问题。

telegram · AI_News_CN · Apr 1, 01:54

**背景**: 渐进多焦镜片是一种先进光学镜片，可实现近、中、远距离视野的无缝切换，适合老花眼等存在多种视力需求的人群。多模态大模型是能够处理文本、图像、音频、视频等多种数据类型的大型人工智能模型，可在不同设备上实现更丰富的交互体验。Meta AI 是 Meta Platforms 的人工智能研究部门，同时也是面向消费者的 AI 产品套件，基于 Meta 开源的 Llama 大语言模型搭建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.facebook.com/ElegantOptometry/photos/clear-vision-all-day-comfort-hoya-stellify-progressive-lensesenjoy-seamless-visi/1263015592505257/">有效阻隔有害光线与屏幕眩光，长时间使用电子产品也能减轻眼睛疲劳。 配备高端防反光与防刮涂层，镜片持久清晰，带来全方位锐利、舒适的视觉体验。无论是工作 - Facebook</a></li>
<li><a href="http://ilearn.hitsz.edu.cn/xsky/r/dmtdmx.htm">多模态大模型-智能媒体研究中心</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta_AI">Meta AI - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#smart wearables`, `#generative AI`, `#augmented reality`, `#mobile computing`

---

<a id="item-13"></a>
## [Claude Code 源码泄漏 微软转向原生应用](https://www.solidot.org/story?sid=83926) ⭐️ 7.0/10

Anthropic 意外通过 npm 的源映射文件泄漏了 AI 编程工具 Claude Code 的完整未混淆源代码，泄漏后的代码已经被上传到公开 GitHub 仓库。另一则消息中，微软计划为 Windows 11 开发更多原生应用以降低内存占用，不再使用资源消耗更高的基于网页的 PWA 架构。 Claude Code 泄漏事件揭示了一种简单低成本的 AI 内容审核优化方案，打破了所有轻量 AI 任务都需要大模型支持的固有认知，同时也引发了业内对生产构建最佳实践的广泛讨论。微软转向原生应用的策略标志着桌面端应用行业整体逆转了此前转向网页应用的趋势，因为内存价格上涨迫使开发者将效率放在比开发速度更优先的位置。 泄漏的代码显示 Claude Code 使用基于正则表达式的轻量方案检测用户提示词中的负面情绪，相比调用大模型完成相同任务，该方案速度快得多，也能大幅节省算力。微软现有的 Windows 11 应用如 Clipchamp 和 Copilot 都基于网页 PWA 架构构建，这种架构更便于开发，但会消耗多得多的系统内存。

telegram · AI_News_CN · Apr 1, 02:32

**背景**: 源映射是一种调试文件，作用是将打包压缩后的生产环境 JavaScript 代码映射回原始未修改的源代码，在公开 npm 包中意外包含源映射会暴露项目完整的未混淆源代码。Progressive Web App（PWA）是使用标准网页技术构建、拥有原生应用体验的网页应用，跨平台开发更简单，但资源占用通常比真正的原生应用更高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo">Claude Code's Entire Source Code Was Just Leaked via npm ...</a></li>
<li><a href="https://cybernews.com/security/anthropic-claude-code-source-leak/">Full source code for Anthropic’s Claude Code leaks | Cybernews</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps">Progressive web apps - MDN Progressive Web App Architecture: A Step-by-Step Guide Get started developing a PWA - Microsoft Edge Developer ... PWA Architecture (Progressive Web App) - Smart Digitants Progressive Web Apps (PWA): The Evolution of Web Apps and a ... PWA Architecture | All About Progressive Web Apps With Examples Get started developing a PWA - learn.microsoft.com Progressive Web App Architecture : A Step-by-Step Guide How to Build a Progressive Web App | MernStackDev</a></li>

</ul>
</details>

**社区讨论**: 本次泄漏事件已经在 Hacker News 上引发了大量公开讨论，许多开发者惊讶于顶级 AI 公司没有使用自家大模型，反而用简单的正则方案完成情绪检测，也有不少人指出在生产发布中误包含源映射的错误其实意外地普遍。

**标签**: `#Claude Code`, `#source code leak`, `#Windows 11`, `#AI programming tools`, `#native applications`

---

<a id="item-14"></a>
## [Claude Code 泄露导致八千仓库下架](http://cli.js.map/) ⭐️ 7.0/10

有人从 Anthropic 公开 npm 包的 source map 还原出 Claude Code 2.1.88 的源代码并上传至 GitHub 后，Anthropic 向 GitHub 提交了 DMCA 下架请求。GitHub 按照要求总共下架了 8100 个相关的父仓库与分叉仓库。 这次大规模下架事件引发了关于 AI 专有代码知识产权保护和开源社区可接受行为的关键问题，为处理通过公开开发工件传播的泄露源代码开创了值得关注的先例。 这个非授权仓库通过提取官方`@anthropic-ai/claude-code`npm 包附带的`cli.js.map`文件中`sourcesContent`字段的内容，还原出了包含 1884 个 TypeScript 和 TSX 文件在内的共 4756 个源文件。GitHub 的政策允许下架整个关联网络的全部 8100 个仓库，因为该网络规模超过 100 个，且 Anthropic 主张所有分叉都包含侵权内容。

telegram · AI_News_CN · Apr 1, 02:38

**背景**: Claude Code 是 AI 公司 Anthropic 开发的 AI 编程工具，Anthropic 也是 Claude 大语言模型的开发方。JavaScript source map 是一种构建产物，作用是将编译压缩后的 JavaScript 代码映射回原始未编译的源文件以方便调试，这类文件通常会和生产环境 JavaScript 包一起公开分发。DMCA 即美国数字千年版权法，它为 GitHub 这类在线服务提供商处理版权方的侵权下架请求提供了框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Claude Code overview - Claude Code Docs</a></li>
<li><a href="https://docs.github.com/articles/dmca-takedown-policy">DMCA Takedown Policy - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#DMCA`, `#Anthropic Claude`, `#source code leak`, `#GitHub`, `#intellectual property`

---

<a id="item-15"></a>
## [Anthropic 源码泄露实为营销炒作](https://www.aibase.com/zh/news/26746) ⭐️ 7.0/10

备受关注的 Anthropic Claude Code 源码泄露事件迎来戏剧性反转，此前声称是被开除 Anthropic 工程师、对泄露负责的男子被证实并非该公司员工，他只是为自己的初创公司 Ferryman 策划了这场钓鱼营销事件。而此次通过 npm 源映射文件泄露的超 50 万行内部代码，确实是 Anthropic 发生的真实意外工程事故。 这起事件暴露了头部 AI 公司 Anthropic 存在严重的 CI/CD 流程漏洞，揭示了即使是顶级 AI 企业在高速扩张阶段也会在基础设施安全上存在疏漏。它也说明了在炒作氛围浓厚的 AI 行业中，真实的安全事故很容易被利用来谋取 publicity，影响公众对头部 AI 开发商的信任。 泄露的代码曝光了 Claude Code 未公开的多项功能，其中包含全自动智能体命令执行逻辑、系统化的系统提示词矩阵，以及名为 Undercover Mode 和 Bypass Permissions Mode 的隐藏权限绕过测试模式。根据官方声明，此次泄露没有涉及任何敏感客户数据或凭证。

telegram · AI_News_CN · Apr 1, 03:10

**背景**: Anthropic 是开发 Claude 大语言模型系列的头部 AI 企业，Claude Code 是 Anthropic 推出的智能编码工具，用于帮助开发者处理代码库、编辑文件和运行终端命令。源映射文件是一种开发资产，可将压缩后的生产代码映射回原始可读源码，如果意外将此类文件发布到公开 npm 包中，就会使得任何人都可以重构出完整的内部源码。CI/CD 指持续集成与持续交付，是开发团队用来构建和发布软件的自动化工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know">Claude Code's source code appears to have leaked: here's what we know | VentureBeat</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#source code leak`, `#Anthropic Claude`, `#AI security`, `#software engineering`, `#marketing scandal`

---