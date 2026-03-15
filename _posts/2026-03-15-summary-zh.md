---
layout: default
title: "Horizon Summary: 2026-03-15 (ZH)"
date: 2026-03-15
lang: zh
---

> From 29 items, 7 important content pieces were selected

---

1. [Ageless Linux 反对年龄验证法规](#item-1) ⭐️ 8.0/10
2. [Glassworm 攻击入侵超 151 个 GitHub 仓库](#item-2) ⭐️ 8.0/10
3. [AI 垃圾泛滥终结 Jazzband 开放模式](#item-3) ⭐️ 7.0/10
4. [Instagram 将取消私信端到端加密](#item-4) ⭐️ 7.0/10
5. [迪士尼指控字节跳动 Seedance 2.0 侵权](#item-5) ⭐️ 7.0/10
6. [欧洲国家支持禁止 AI 生成性化不雅图像](#item-6) ⭐️ 7.0/10
7. [微软 2026 年将 Gaming Copilot 引入 Xbox](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Ageless Linux 反对年龄验证法规](https://agelesslinux.org/) ⭐️ 8.0/10

开源项目 Ageless Linux 已正式推出，反对要求操作系统提供商收集并共享用户年龄信息的新型强制政府年龄验证法规，该议题是 Hacker News 上一场高赞讨论的主题。 这些新法规威胁用户隐私和公民自由，还向缺乏庞大法律预算的小型开源项目施加了难以承受的合规成本，对独立开源操作系统的未来构成威胁。 Ageless Linux 本身是一个抗议项目，而非完整的独立操作系统，本次讨论核心的加州法案是 AB 1043，该法案将于 2027 年 1 月 1 日正式生效。

hackernews · nateb2022 · Mar 14, 22:10

**背景**: 包括美国加州、英国和欧盟在内的多个地区近期已经通过或提出了强制年龄验证法规，要求所有操作系统提供商在用户账户设置阶段实施年龄检查。加州的 AB 1043 法案于 2025 年 10 月由州长 Gavin Newsom 签署，要求操作系统提供商收集用户年龄数据并共享给应用开发者。大多数小型开源项目的年度预算非常有限，对他们来说，哪怕是应对一桩无意义的不合规诉讼的成本都无力承担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agelesslinux.org/">Ageless Linux — Software for Humans of Indeterminate Age</a></li>
<li><a href="https://www.tomshardware.com/software/operating-systems/california-introduces-age-verification-law">California introduces age verification law for all operating systems, including Linux and SteamOS — user age verified during OS account setup | Tom's Hardware</a></li>
<li><a href="https://www.theregister.com/2026/03/06/os_age_verification/">US state laws push age checks into the operating system • The Register</a></li>

</ul>
</details>

**社区讨论**: 大多数 Hacker News 评论者都认为新法规存在逻辑缺陷，许多人指出保护未成年上网已经可以通过家庭教育和现有家长控制工具实现。评论者一致认为这些法规扩张了公共监控基础设施，却没有让对儿童造成伤害的成瘾性大型科技平台承担责任，同时称赞 Ageless Linux 是开源社区对抗有害法规的正确范例。

**标签**: `#open source`, `#age verification`, `#online privacy`, `#operating systems`, `#regulation`

---

<a id="item-2"></a>
## [Glassworm 攻击入侵超 151 个 GitHub 仓库](https://www.tomshardware.com/tech-industry/cyber-security/malicious-packages-using-invisible-unicode-found-in-151-github-repos-and-vs-code) ⭐️ 8.0/10

Aikido Security 的研究人员近日发现，黑客组织 Glassworm 针对 GitHub、npm 和 VS Code 市场发起大规模攻击，已经入侵了包括多个知名开源项目在内的超过 151 个仓库。该攻击利用不可见 Unicode 字符隐藏恶意负载，可窃取用户凭据，并使用 Solana 区块链作为隐蔽的指令控制通道。 这场新型高影响力的开源供应链攻击可以绕过人工代码审查，令数百万依赖受入侵仓库的开发者和下游项目面临凭据与密钥被盗的风险。它也凸显了攻击者结合混淆技术、大语言模型和区块链打造更隐蔽、更持久攻击的新趋势。 该攻击将恶意代码隐藏在 Unicode 私有使用区域特定范围内的零宽不可见字符中，人工代码审查时无法用肉眼识别，攻击者还利用大语言模型生成符合各项目编码风格的欺骗性代码，诱骗维护者合并恶意改动。使用 Solana 区块链进行指令控制，使得这场攻击比依赖中心化服务器的传统攻击更难被关停。

telegram · zaihuapd · Mar 15, 01:28

**背景**: 近年来针对开源仓库的供应链攻击愈发普遍，因为被入侵的开源代码可以快速将恶意软件传播给成千上万的下游用户。零宽 Unicode 字符是一类特殊字符，在大多数代码编辑器中会渲染为不可见的零宽空格，非常适合用来混淆恶意代码。攻击者开始测试将区块链作为替代指令控制通道，因为传统基于中心化服务器的通道很容易被安全研究人员关停。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/malicious-packages-using-invisible-unicode-found-in-151-github-repos-and-vs-code">Invisible malicious code attacks 151 GitHub repos and VS Code ...</a></li>
<li><a href="https://securityonline.info/glassworm-supply-chain-worm-uses-invisible-unicode-and-solana-blockchain-for-stealth-c2/">GlassWorm Supply Chain Worm Uses Invisible Unicode and Solana ...</a></li>
<li><a href="https://www.knostic.ai/blog/zero-width-unicode-characters-risks">Zero Width Unicode Characters: the Risks you Can't See</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#supply chain attack`, `#GitHub`, `#software security`

---

<a id="item-3"></a>
## [AI 垃圾泛滥终结 Jazzband 开放模式](https://simonwillison.net/2026/Mar/14/jannis-leidel/#atom-everything) ⭐️ 7.0/10

Jazzband 的 Jannis Leidel 宣布，GitHub 上被称为“slopocalypse”的 AI 生成垃圾拉取请求和议题泛滥，已经让 Jazzband 的开放会员制和共享推送权限协作模式无法维持。 这一广受关注的事件凸显了 AI 垃圾对开源协作的日益严重的威胁，迫使全球开源社区重新评估长期存在的开放贡献模式。 行业数据显示，每 10 个 AI 生成的拉取请求中仅有 1 个符合开源项目标准，知名项目 curl 已经因为垃圾提交确认率降至 5%以下，关闭了其公开漏洞赏金计划。

rss · Simon Willison · Mar 14, 18:41

**背景**: Jazzband 成立于十多年前，是一个专注于分担 Python 开源项目维护工作的实验性协作社区。它的核心模式是向所有新成员开放项目代码库的共享推送权限，旨在降低新贡献者的准入门槛，减少维护者的职业倦怠。slopocalypse 一词指的是近期托管在 GitHub 上的开源项目遭到大量低质量 AI 生成垃圾贡献涌入的现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jazzband.co/news/2026/03/14/sunsetting-jazzband">Jazzband - News - Sunsetting Jazzband</a></li>
<li><a href="https://github.com/jazzband">Jazzband · GitHub</a></li>
<li><a href="https://incusdata.com/blog/coding-matters-the-slopocalypse">Coding matters: The slopocalypse • 2025 • Incus Data Programming...</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI spam`, `#GitHub`, `#software maintenance`

---

<a id="item-4"></a>
## [Instagram 将取消私信端到端加密](https://www.theverge.com/tech/894752/instagram-end-to-end-encryption) ⭐️ 7.0/10

Meta 官方确认 Instagram 将在 2026 年 5 月 8 日后停止为私信提供端到端加密支持，做出该调整的原因是这一功能的实际用户使用率非常低。Meta 推荐有端到端加密通信需求的用户转用旗下另一平台 WhatsApp。 这一隐私相关变更影响全球最受欢迎的社交平台之一，因此得到了数字隐私倡导者和大型科技行业观察者的广泛关注。它也体现了 Meta 将加密通信业务整合到单一核心平台的战略方向。 这一停止服务的决定已经通过 Instagram 官方支持页面的更新得到确认，在 2026 年 5 月 8 日之后，Meta 不会在 Instagram 平台本身保留任何其他端到端加密服务选项。

telegram · zaihuapd · Mar 14, 04:47

**背景**: 端到端加密（E2EE）是一种安全通信方法，它能确保只有消息的发送方和接收方能访问通信的明文内容。即便是托管通信的服务提供商也无法读取未加密的内容，因此 E2EE 是保护个人通信隐私的核心功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hoganlovells.com/en/publications/endtoend-encryption-obstacle-or-pillar-of-national-security">End - to - end encryption : obstacle or pillar of national security?</a></li>
<li><a href="https://www.maketecheasier.com/end-to-end-encryption-principle-explained/">End - To - End Encryption (And Principle) Explained - Make Tech Easier</a></li>

</ul>
</details>

**标签**: `#end-to-end encryption`, `#digital privacy`, `#Instagram`, `#Meta`, `#social media`

---

<a id="item-5"></a>
## [迪士尼指控字节跳动 Seedance 2.0 侵权](https://t.me/zaihuapd/40265) ⭐️ 7.0/10

2026 年 2 月 13 日，华特迪士尼公司向字节跳动发出停止侵权函，该函件被 Axios 获取。迪士尼指控字节跳动未经补偿使用迪士尼版权作品训练商业 AI 视频生成模型 Seedance 2.0，且模型可生成迪士尼持有的热门 IP 角色内容，构成侵权。 这是全球生成式 AI 训练版权争议中备受关注的行业事件，可能会为 AI 企业使用娱乐公司版权内容开发商业产品奠定重要先例，也将影响全球生成式 AI 行业未来的合规框架。 函件称 Seedance 2.0 可生成包含《星球大战》、漫威旗下蜘蛛侠、达斯·维达等迪士尼 IP 角色的视频，部分用户生成的相关内容已经在社交媒体公开传播。发函前，美国电影协会主席兼 CEO Charles Rivkin 就已呼吁字节跳动停止涉嫌侵权活动。

telegram · zaihuapd · Mar 15, 00:43

**背景**: Seedance 2.0 是字节跳动开发的多模态文生图、图生视频 AI 模型，于 2026 年 2 月初开启 beta 测试。目前全球范围内对未经授权使用版权作品训练生成式 AI 是否合法仍存在争议，美国版权局也曾明确表示这类使用是否符合合理使用原则没有统一答案。近期已有多家内容创作者和影视公司针对 AI 企业未授权使用训练数据提起法律诉讼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://www.skadden.com/insights/publications/2025/05/copyright-office-report">Copyright Office Weighs In on AI Training and Fair Use | Skadden, Arps, Slate, Meagher & Flom LLP</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#copyright infringement`, `#AI video generation`, `#legal news`

---

<a id="item-6"></a>
## [欧洲国家支持禁止 AI 生成性化不雅图像](https://hk.news.yahoo.com/share/0a951dd0-216e-316c-9224-5ff4842422ae) ⭐️ 7.0/10

埃隆·马斯克的 Grok AI 生成非自愿性化不雅图像引发强烈反弹后，欧盟成员国支持将禁止 AI 生成非自愿性内容和儿童性虐待材料纳入欧盟全面 AI 规范的修订案，欧洲议会将于本月晚些时候对该项禁令进行表决。 这是全球 AI 治理中应对生成式 AI 有害滥用的重要里程碑，为保护个人尊严和弱势群体免受 AI 驱动的性剥削树立了明确的监管先例。 欧洲议会相关委员会将于 11 月 18 日对该项禁令进行表决，推动禁令的议员强调，该规则不止针对 Grok 的单个丑闻，更是要为 AI 贬抑人类尊严的权力划定明确边界。

telegram · AI_News_CN · Mar 14, 03:14

**背景**: Grok AI 是埃隆·马斯克旗下 xAI 公司开发的生成式聊天机器人，于 2023 年 11 月推出，此前曾生成包括非自愿性化图像在内的多个争议性输出内容。Deepfake（深度造假）是利用人工智能深度学习技术生成或编辑的一类合成媒体，可以制作出高度逼真的描绘真实人物的虚假内容。欧盟《人工智能法案》是欧盟针对人工智能的核心全面监管框架，采用基于风险的方法对不同类别的 AI 系统进行监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_AI">Grok AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_Intelligence_Act">Artificial Intelligence Act - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Regulation`, `#Generative AI`, `#Deepfake`, `#AI Governance`

---

<a id="item-7"></a>
## [微软 2026 年将 Gaming Copilot 引入 Xbox](https://www.cnbeta.com.tw/articles/game/1553460.htm) ⭐️ 7.0/10

微软确认旗下 AI 游戏助手 Gaming Copilot 将于 2026 年正式登陆 Xbox Series X|S 主机，该功能从 2025 年 10 月起已在 PC、移动端和华硕 ROG Xbox Ally 掌机开启 beta 测试。Xbox 游戏 AI 负责人 Sonali Yadav 在近期 GDC 大会上公布了该计划，并表示该服务后续会向更多玩家平台扩展。 本次发布是微软首次在主力主机产品线集成原生 AI 助手，体现了微软在下代 Xbox 发布前针对游戏硬件的整体 AI 布局战略。它很可能会改变玩家获取游戏推荐、攻略和游戏内帮助的方式，加速 AI 工具在消费游戏行业的普及。 Gaming Copilot 拥有三大核心功能：基于玩家游玩记录的个性化游戏推荐、无需退出游戏界面的即时攻略提示、帮助玩家改进操作的战术建议，它通过识别分析游戏截图和画面片段生成对应内容。当前测试版默认开启数据上传，将截取的屏幕内容用于 AI 模型训练，这引发了隐私合规担忧，目前尚不清楚主机上线后是否会保留这一默认开启设置。

telegram · AI_News_CN · Mar 14, 08:03

**背景**: Gaming Copilot 是微软专门为电子游戏玩家开发的 AI 驱动个人助手。Project Helix 是微软下一代 Xbox 主机的开发代号，计划在 2028 年前后推出，定位为同时支持 Xbox 和 PC 游戏的混合平台。GDPR 即《通用数据保护条例》，是欧盟出台的严格隐私法规，用于监管欧盟地区个人用户数据的收集和处理流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.xbox.com/en-US/gaming-copilot">Gaming Copilot (Beta): Your personal gaming sidekick | Xbox</a></li>
<li><a href="https://en.wikipedia.org/wiki/Project_Helix">Project Helix</a></li>
<li><a href="https://en.wikipedia.org/wiki/GDPR">GDPR</a></li>

</ul>
</details>

**标签**: `#Gaming AI`, `#Microsoft Copilot`, `#Xbox`, `#AI Privacy`

---