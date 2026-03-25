---
layout: default
title: "Horizon Summary: 2026-03-25 (EN)"
date: 2026-03-25
lang: en
---

> From 51 items, 24 important content pieces were selected

---

1. [Litellm 1.82.7/1.82.8 PyPI packages compromised](#item-1) ⭐️ 9.0/10
2. [Compromised litellm steals credentials on PyPI](#item-2) ⭐️ 9.0/10
3. [Alibaba DAMO Unveils Record-breaking RISC-V CPU C950](#item-3) ⭐️ 9.0/10
4. [Original Founder Rewrites Video.js 88% Smaller](#item-4) ⭐️ 8.0/10
5. [Anthropic Launches Auto Mode for Claude Code](#item-5) ⭐️ 8.0/10
6. [Streaming experts runs trillion-parameter LLMs on consumer devices](#item-6) ⭐️ 8.0/10
7. [DarkSword iOS Safari zero-click exploit disclosed](#item-7) ⭐️ 8.0/10
8. [Google launches Gemini dark web security AI agent](#item-8) ⭐️ 8.0/10
9. [OpenAI to discontinue Sora AI video generator](#item-9) ⭐️ 8.0/10
10. [Anthropic launches Auto Mode for Claude Code](#item-10) ⭐️ 8.0/10
11. [OpenAI launches AI shopping protocol for ChatGPT](#item-11) ⭐️ 8.0/10
12. [OpenAI to shut down Sora AI video platform](#item-12) ⭐️ 8.0/10
13. [OpenAI terminates Sora text-to-video project](#item-13) ⭐️ 8.0/10
14. [Google releases Gemini 3.1 Flash-Lite lightweight LLM](#item-14) ⭐️ 8.0/10
15. [Judge questions US retaliation against Anthropic](#item-15) ⭐️ 8.0/10
16. [Popular AI library litellm hit by supply chain poisoning](#item-16) ⭐️ 8.0/10
17. [Litellm hit by supply chain poisoning, credentials leaked](#item-17) ⭐️ 8.0/10
18. [OpenAI shuts down consumer AI video app Sora](#item-18) ⭐️ 7.0/10
19. [Dependency cooldown support after LiteLLM attack](#item-19) ⭐️ 7.0/10
20. [Nvidia investment tactics draw antitrust scrutiny](#item-20) ⭐️ 7.0/10
21. [China's daily AI token calls hit 140T, up 1000x in 2 years](#item-21) ⭐️ 7.0/10
22. [Microsoft releases open source Rust training materials](#item-22) ⭐️ 7.0/10
23. [Anthropic Launches Auto Mode for Claude Code](#item-23) ⭐️ 7.0/10
24. [OpenAI pivots e-commerce strategy, abandons Instant Checkout](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Litellm 1.82.7/1.82.8 PyPI packages compromised](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

Recently published versions 1.82.7 and 1.82.8 of the popular Litellm PyPI package were confirmed to be compromised with malicious forkbomb code. The incident is linked to an ongoing CI/CD supply chain attack targeting the project's Trivy dependency. Litellm 是被数千开发者广泛使用的大语言模型统一调用工具，该事件会导致大量下游开发环境面临拒绝服务风险，同时也凸显了针对开源Python包的CI/CD供应链攻击的持续威胁。 The malicious code adds a base64-encoded blob to the Litellm source code that decodes and executes additional malware, and version 1.82.8 adds an executable _init.pth file that runs malicious code at Python interpreter startup. Only users who installed the compromised PyPI versions are affected; the project's pinned proxy Docker images are not impacted, and PyPI has already quarantined the malicious packages to block further downloads.

hackernews · dot_treo · Mar 24, 12:06

**Background**: LiteLLM is an open-source Python library that provides a standardized interface for calling more than 100 different large language model providers from a single codebase. A forkbomb is a simple denial-of-service attack that repeatedly replicates processes to exhaust system memory and processing power, causing the target system to slow down or crash. A CI/CD supply chain attack is a type of cyberattack where attackers compromise the automated build and release pipeline of a software project to insert malicious code into distributed packages, which is then delivered to all downstream users of the software.

<details><summary>References</summary>
<ul>
<li><a href="https://www.penligent.ai/hackinglabs/litellm-on-pypi-was-compromised-what-the-attack-changed-and-what-defenders-should-do-now/">LiteLLM on PyPI Was Compromised, What the Attack Changed and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fork_bomb">Fork bomb - Wikipedia</a></li>
<li><a href="https://www.darkreading.com/application-security/trivy-supply-chain-attack-targets-ci-cd-secrets">Trivy Supply Chain Attack Targets CI/CD Secrets</a></li>

</ul>
</details>

**Discussion**: LitellM maintainers confirmed the incident is still evolving and traced its origin to a compromised Trivy dependency in the project's CI/CD workflow. Community members expressed broader concerns about trust in software dependencies and development environments, with some sharing new security tools to help users detect malicious package activity, while others noted excessive spam in the incident's issue thread.

**Tags**: `#supply chain security`, `#malicious package`, `#software security`, `#pypi`

---

<a id="item-2"></a>
## [Compromised litellm steals credentials on PyPI](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

Versions 1.82.7 and 1.82.8 of the popular Python package litellm published to PyPI were compromised with credential-stealing malware. PyPI has since quarantined the litellm project after the compromise was discovered. This is a high-impact supply chain attack affecting a widely used LLM utility package, and can automatically steal credentials as soon as the package finishes installing. Any developer or organization that installed these two versions within the compromise window is at immediate risk of credential exposure. Version 1.82.8 hides the malware in a litellm_init.pth file, which runs automatically during Python startup when the package is installed, even if the user never imports litellm in their code. The attack originated from a prior compromise of the Trivy security scanner used in LiteLLM's CI pipeline, which allowed attackers to steal the project's PyPI publishing credentials.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is a popular open-source Python library that provides a unified interface for calling over 100 different large language models from different providers. A .pth file is a special file in Python packages that is automatically parsed and executed when Python starts up, normally used to modify the module search path. PyPI is the official public package repository for the Python programming language, and it quarantines compromised projects to stop further distribution of malicious versions.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://runebook.dev/en/docs/python/library/sys_path_init/pth-files">The Hidden Power and Problems of Python .pth Files</a></li>
<li><a href="https://www.penligent.ai/hackinglabs/litellm-on-pypi-was-compromised-what-the-attack-changed-and-what-defenders-should-do-now/">LiteLLM on PyPI Was Compromised, What the Attack Changed and What Defenders Should Do Now - Penligent</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#python`, `#malware`, `#pypi`, `#litellm`

---

<a id="item-3"></a>
## [Alibaba DAMO Unveils Record-breaking RISC-V CPU C950](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 9.0/10

On March 24, 2026, Alibaba DAMO Academy launched the new flagship RISC-V CPU Xuantie C950 at the 2026 Xuantie RISC-V Ecosystem Conference in Shanghai. The new chip scored over 70 points in the SPECint2006 single-core test, setting a new performance record for all publicly disclosed RISC-V processors. This breakthrough pushes the upper limit of open-source RISC-V processor performance into the high-end computing range, enabling RISC-V chips to enter demanding scenarios that were previously dominated by closed, proprietary CPU architectures. It accelerates the development of the open RISC-V ecosystem and expands application possibilities for cloud computing and generative AI infrastructure. Xuantie C950 is targeted at high-end computing scenarios including cloud computing, generative AI, high-end robotics and edge computing, and it integrates a self-developed AI acceleration engine from DAMO Academy that can natively run large models with hundreds of billions of parameters such as Qwen3 and DeepSeek V3.

telegram · zaihuapd · Mar 24, 06:01

**Background**: RISC-V is an open-source instruction set architecture for CPUs that allows developers to use and modify it freely without licensing fees, which has gained growing adoption globally in recent years. SPECint2006 is an industry-standard benchmark suite that measures a CPU's integer computing performance to enable fair comparison across different processor designs. DAMO Academy is a global cutting-edge technology research institute founded by Alibaba Group in 2017, covering research areas including semiconductors, artificial intelligence and fundamental sciences.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://pandaily.com/alibaba-damo-academy-launches-xuan-tie-c950-cpu-for-large-ai-models">Alibaba DAMO Academy Launches XuanTie C950 CPU for Large AI Models - Pandaily</a></li>
<li><a href="https://damo.alibaba.com/about?language=en">About Us - Damo - Alibaba</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#CPU`, `#Semiconductors`, `#AI Accelerator`, `#Cloud Computing`

---

<a id="item-4"></a>
## [Original Founder Rewrites Video.js 88% Smaller](https://videojs.org/blog/videojs-v10-beta-hello-world-again) ⭐️ 8.0/10

After regaining control of the 16-year-old open source Video.js project following acquisition and neglect by new owners, original founder Steve Heffernan released a v10 beta of a complete ground-up rewrite that is 88% smaller than the previous version. Video.js is used by billions of people monthly on major sites including Amazon, LinkedIn, and Dropbox, so this smaller, modern rewrite can improve web performance for a huge number of existing production deployments while reviving a critical widely used open source project. The rewrite was built with contributions from developers of four existing open source media projects: Plyr, Vidstack, and Media Chrome, and v10 adds first-class React and TypeScript support alongside a new composable modular architecture.

hackernews · Heff · Mar 24, 18:03

**Background**: Video.js is a long-standing open source HTML5 video player for the web that first launched 16 years ago. After the project was acquired by a private equity-backed company, new owners cut maintenance staffing, leaving the project understaffed and stuck with an outdated, bloated codebase. Media Chrome is an open source project that provides customizable media player controls built with web components, while Plyr is a popular lightweight customizable HTML5 media player.

<details><summary>References</summary>
<ul>
<li><a href="https://videojs.org/blog/videojs-v10-beta-hello-world-again">Video.js v10 Beta: Hello, World (again) | Blog | Video.js | Open Source Video Player</a></li>
<li><a href="https://github.com/muxinc/media-chrome">GitHub - muxinc/media-chrome: Custom elements (web components ... media-chrome - npm Get Started - Media Chrome Docs Media Chrome Examples Building the next generation of video players with Media Chrome Best of JS • media-chrome</a></li>
<li><a href="https://github.com/sampotts/plyr">sampotts/plyr: A simple HTML5, YouTube and Vimeo player plyr - npm Using Plyr Player for Lightweight, Accessible Video UI Plyr: CSS Styleable Video Player - CSS-Tricks Plyr download | SourceForge.net Plyr download | SourceForge.net Plyr : CSS Styleable Video Player - CSS-Tricks Using Plyr Player for Lightweight, Accessible Video UI Using Plyr Player for Lightweight, Accessible Video UI Plyr: The Ultimate HTML5, YouTube & Vimeo Player for Modern ...</a></li>

</ul>
</details>

**Discussion**: Community members congratulated the founder, expressed excitement to test the smaller version, and asked technical questions about architectural choices including why it was not distributed as a web component and how cross-feature state dependencies are handled. Some commenters also asked questions about the tradeoffs between streaming protocols HLS and DASH.

**Tags**: `#open source`, `#web development`, `#video player`, `#javascript`

---

<a id="item-5"></a>
## [Anthropic Launches Auto Mode for Claude Code](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 8.0/10

Anthropic has launched a new Auto mode for Claude Code, an autonomous permissions mode that lets Claude make its own action approval decisions while being guarded by a dedicated safety classifier model. This new feature replaces the existing all-or-nothing `--dangerously-skip-permissions` flag that completely disables permission checks. This feature addresses the common pain point of repeated permission prompts for developers using Claude Code, enabling fully autonomous AI-assisted coding while retaining built-in safety safeguards. It balances convenience and risk control better than the previous unregulated full-permission option, which is a meaningful advance for AI-assisted software engineering. The safety classifier runs on Claude Sonnet 4.6 regardless of the main model used in the session, and blocks out-of-scope actions, untrusted infrastructure targets, and hostile-content-driven actions. Auto mode ships with an extensive set of default allow and block filters that users can customize with their own additional rules.

rss · Simon Willison · Mar 24, 23:57

**Background**: Claude Code is Anthropic's agentic AI coding tool designed to help developers work with codebases, edit files, run terminal commands, and ship software faster. Before Auto mode, the only way to avoid repeated permission prompts was to use the `--dangerously-skip-permissions` flag, which disables all permission checks entirely and leaves users open to unintended or risky actions. Anthropic has long focused on AI safety, and uses specially trained classifier models to detect policy violations and risky actions in real time as part of its constitutional AI alignment approach.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://blog.promptlayer.com/claude-dangerously-skip-permissions/">claude --dangerously-skip-permissions</a></li>
<li><a href="https://www.anthropic.com/news/building-safeguards-for-claude">Building safeguards for Claude</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI assisted development`, `#autonomous coding`, `#Anthropic`

---

<a id="item-6"></a>
## [Streaming experts runs trillion-parameter LLMs on consumer devices](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Recent experiments with the streaming experts inference technique have enabled a 1 trillion parameter Kimi K2.5 LLM to run on a 96GB M2 Max MacBook Pro, and a 397B parameter Qwen3.5-397B-A17B model to run on an iPhone. This breakthrough unlocks on-device inference of very large mixture-of-experts language models on consumer hardware that lacks the RAM to fit the entire model, expanding access to powerful large AI models without relying on cloud servers. The Kimi K2.5 model only activates 32 billion parameters at any time during inference, and the iPhone-hosted Qwen model runs at 0.6 tokens per second, while a 128GB M4 Max runs Kimi K2.5 at around 1.7 tokens per second.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) is a large language model architecture that activates only a small subset of expert parameters for each input, allowing models to grow to very large total parameter sizes while keeping per-inference computation low. The streaming experts inference technique works around limited on-device RAM by loading only the currently needed expert weights from storage for each generated token, instead of loading the entire model into memory at once. Kimi K2.5 is an open-source multimodal large language model released by Moonshot AI.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/ Kimi - K 2 . 5 · Hugging Face</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Sparse Mixture-of-Experts Transformers for Efficient Scaling ... Applying Mixture of Experts in LLM Architectures | NVIDIA ... Mixture of Experts in Large Language Models: Intuition ... Mixture of experts approach for Large Language Models</a></li>

</ul>
</details>

**Discussion**: The topic has generated substantial excitement and follow-on experimentation in the global AI community, with independent developers continuing to iterate on optimizations to improve performance.

**Tags**: `#large language models`, `#mixture-of-experts`, `#on-device AI`, `#inference optimization`

---

<a id="item-7"></a>
## [DarkSword iOS Safari zero-click exploit disclosed](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

A zero-click iOS exploit chain called DarkSword that infects devices via malicious Safari web pages has been disclosed publicly. This exploit has been actively used by multiple attackers in Saudi Arabia, Turkey, Malaysia, and Ukraine since November 2025, and all associated vulnerabilities have now been patched in recent iOS updates. This exploit affects all iOS 18 versions from 18.4 to 18.7, covering millions of active Apple iPhone users globally. Since it requires no extra user interaction beyond opening a malicious webpage, it poses a severe security risk to unpatched devices, and the disclosure pushes affected users to install official security updates immediately. DarkSword chains together six separate vulnerabilities to deliver malware payloads including the crypto-stealing GhostBlade, which targets cryptocurrency wallet data on compromised iOS devices. While all vulnerabilities are fully patched in iOS 26.3, most were fixed incrementally by Apple in earlier updates, such as CVE-2025-43529 which was patched in iOS 18.7.3 and iOS 26.2.

telegram · zaihuapd · Mar 24, 11:45

**Background**: A zero-click exploit is a type of security vulnerability that allows attackers to install malware and compromise a device without requiring any interaction from the target user. DarkSword is a web-based exploit kit that can deliver different malware payloads to vulnerable iOS devices when a user visits a compromised or malicious website through the Safari browser. The GhostBlade payload deployed via DarkSword is a specialized crypto-stealing malware that scans infected devices for cryptocurrency exchange and wallet applications to steal user funds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.darkreading.com/threat-intelligence/darksword-iphone-exploit-spies-thieves">DarkSword: iPhone Exploit Kit Serves Spies & Thieves Alike - Dark Reading</a></li>
<li><a href="https://grokipedia.com/page/Zero-click_exploit">Zero-click exploit</a></li>
<li><a href="https://www.mexc.com/news/969892">DarkSword Malware Strikes iOS: Crypto Wallets Under... | MEXC News</a></li>

</ul>
</details>

**Tags**: `#iOS security`, `#zero-click exploit`, `#Safari vulnerability`, `#cyber security`

---

<a id="item-8"></a>
## [Google launches Gemini dark web security AI agent](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

Google has launched a Gemini-powered dark web intelligence AI agent for security operations, which is now available in public preview as part of Google Threat Intelligence. The tool scans 8 to 10 million daily dark web posts to find organization-specific security risks, and achieved 98% accuracy in internal testing. This launch brings large language model AI capabilities to dark web threat monitoring, a task that traditionally requires large amounts of manual labor from security teams. It can significantly improve threat detection efficiency for organizations, and represents a major new AI cybersecurity application from a top cloud provider. The AI agent first builds a custom organizational profile for each customer, then cross-references dark web content with the profile to identify risks including initial access broker activity, data leaks, and insider threats. The 98% accuracy figure is only from Google's internal testing, and independent third-party verification results are not yet public.

telegram · zaihuapd · Mar 24, 13:15

**Background**: Dark web intelligence refers to the practice of monitoring dark web forums and marketplaces to collect threat information relevant to an organization. Google Threat Intelligence is Google Cloud's threat intelligence platform that already hosts a large repository of threat data spanning over 50 billion files. AI agents for cybersecurity are autonomous AI tools that can independently identify and process security tasks to reduce manual workload for security teams.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era">Bringing dark web intelligence into the AI era - Google Cloud</a></li>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web</a></li>
<li><a href="https://cloud.google.com/transform/how-google-does-it-building-ai-agents-cybersecurity-defense/">How Google Does It: Building AI agents for cybersecurity and ...</a></li>

</ul>
</details>

**Tags**: `#Gemini AI`, `#cybersecurity`, `#dark web intelligence`, `#Google Cloud`, `#AI agent`

---

<a id="item-9"></a>
## [OpenAI to discontinue Sora AI video generator](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 8.0/10

Bloomberg reports that OpenAI plans to discontinue its Sora AI video generator just 6 months after its high-profile launch, shut down the Sora developer API, and wind down its related collaboration with Disney. The change is part of a product line simplification effort that will redirect resources to AI agents and a new model called Spud. This planned discontinuation of a high-profile generative AI project signals a major strategic shift at OpenAI ahead of its reported IPO, and will reshape the competitive landscape of the generative AI video industry as well as the related developer ecosystem. It also reflects OpenAI’s growing prioritization of enterprise-focused AI tools and general-purpose foundation models over consumer-facing generative video. OpenAI will also restructure part of its safety and assurance team to integrate related work more closely into its core development workflow, and initial development of the new Spud model has already been completed according to internal statements to staff. The move comes as OpenAI prepares for a potential initial public offering.

telegram · AI_News_CN · Mar 25, 00:32

**Background**: Sora was OpenAI’s high-profile text-to-video generative AI model that could generate one-minute long high-definition videos from text prompts. An AI agent is a goal-driven, self-operating AI system that can complete assigned tasks with minimal human input by planning steps and using required tools independently. Spud is the codename for OpenAI’s next major foundational AI model, which has finished initial development as of March 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomsguide.com/ai/openai-just-killed-sora-as-company-readies-ipo-and-new-spud-model">OpenAI just killed Sora as company readies IPO and new 'Spud ...</a></li>
<li><a href="https://www.tipranks.com/news/the-fly/openai-finished-initial-development-of-next-major-ai-model-the-information-says-thefly-news">OpenAI finished initial development of next major AI model ...</a></li>
<li><a href="https://medium.com/@kalumbalighton/is-everyone-sleeping-on-ai-agents-533d5ec93026">Is Everyone Sleeping on AI Agents ? | by Lighton N. Kalumba | Medium</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#OpenAI Sora`, `#AI Video Generation`, `#Industry Strategy`

---

<a id="item-10"></a>
## [Anthropic launches Auto Mode for Claude Code](https://claude.com/blog/auto-mode) ⭐️ 8.0/10

Anthropic has launched Auto Mode, an autonomous coding feature for its AI coding agent Claude Code. The new mode adds built-in pre-tool-call security classification to automatically approve safe operations and block high-risk actions, and is currently available as a research preview to Claude Team plan users. This release addresses the long-standing key tradeoff between autonomous workflow efficiency and operational safety for AI coding tools, allowing developers to reduce manual approval interruptions while avoiding the major security risks of fully disabling permission checks. It pushes the industry forward in building practical, usable autonomous AI coding agents. Auto Mode supports Claude Sonnet 4.6 and Opus 4.6 models, and will roll out to Enterprise and API users in the coming days; developers can enable it via the command `claude --enable-auto-mode` or through settings in Desktop app and VS Code. Anthropic notes that while the feature is safer than the existing `--dangerously-skip-permissions` option, it is not risk-free, and may slightly increase token consumption and latency.

telegram · AI_News_CN · Mar 25, 01:31

**Background**: Claude Code is Anthropic's agentic AI coding tool designed to help developers complete full coding workflows by understanding entire codebases, editing files, and running terminal commands. An AI coding agent is an AI system built to autonomously complete common coding tasks such as writing, editing, and refactoring code. The biggest challenge for fully autonomous AI coding has long been balancing workflow smoothness with preventing unintended harmful actions like accidental bulk file deletion or sensitive data exposure.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#AI coding agent`, `#Claude Code`, `#software development`, `#AI safety`, `#autonomous AI`

---

<a id="item-11"></a>
## [OpenAI launches AI shopping protocol for ChatGPT](https://www.aibase.com/zh/news/26519) ⭐️ 8.0/10

On March 24, OpenAI officially announced the launch of its Agentic Commerce Protocol, which enables full end-to-end product search, price comparison, and one-click checkout directly within the ChatGPT interface for all user tiers. This launch marks a key step for OpenAI to evolve from a question-and-answer engine into an execution agent, and it is expected to reshape online product distribution and search optimization, officially opening the era of AI agent commerce. The feature is available to all ChatGPT users ranging from free to Pro tiers, OpenAI has not signed exclusive agreements with any specific merchants and initial display positions are open to all participating e-commerce platforms, and checkout functionality is supported via a partnership with Stripe.

telegram · AI_News_CN · Mar 25, 00:58

**Background**: Agentic Commerce Protocol is an open standard that allows e-commerce platforms to connect their inventory data directly to OpenAI's interface, enabling AI agents to access real-time product information and complete purchases directly within chat. Traditional search engine optimization focuses on ranking web pages for human users browsing search results, while the rise of AI search and AI agent commerce is pushing marketers to develop new optimization strategies to get their products recommended by AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/future-shopping-what-chatgpts-agentic-ecommerce-protocol-means-rnwve">The Future of Shopping: What ChatGPT’s Agentic eCommerce...</a></li>
<li><a href="https://departmentofproduct.substack.com/p/what-is-acp-agentic-commerce-protocol">What is ACP? Agentic Commerce Protocol from Stripe and OpenAI...</a></li>
<li><a href="https://www.reddit.com/r/digital_marketing/comments/1s1k3bb/ai_search_is_quietly_changing_how_seo_works/">AI search is quietly changing how SEO works. : r/digital_marketing - Reddit</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#AI commerce`, `#agentic AI`, `#e-commerce`

---

<a id="item-12"></a>
## [OpenAI to shut down Sora AI video platform](https://ishare.ifeng.com/c/s/v006ltpxjezzcbv4UGiPup56TxU--voijLEBXhsV4nEsyHvtGuncunDkNIBKx04IOyBP2) ⭐️ 8.0/10

OpenAI announced this week that it plans to shut down its AI video generation platform and social app Sora, just six months after its launch. The company will reallocate the Sora team to enterprise business, programming tools and long-term robotics research to support a planned Q4 2024 IPO. This shutdown signals a major strategic shift for one of the world's most influential AI companies, refocusing resources on high-value enterprise and productivity-focused AI rather than consumer social products. It also reveals major unresolved challenges for fully open consumer-facing generative AI video platforms under current regulatory and technical conditions. The Sora consumer app, developer version, and video generation features inside ChatGPT will all be discontinued; the most advanced Sora 2 model will remain available behind ChatGPT's paywall as a productivity tool. The shutdown was driven by plummeting user downloads, widespread unmoderated copyright infringement and deepfake content, and the collapse of a potential $100 million IP licensing deal with Disney.

telegram · AI_News_CN · Mar 25, 01:02

**Background**: An agentic AI system is a class of generative AI systems that can operate semi-autonomously or fully autonomously to perceive, reason and complete tasks on their own, rather than only generating content in response to direct user prompts. The uncanny valley effect describes a psychological phenomenon where human observers feel strong discomfort and revulsion towards artificial figures that resemble humans to a high but not perfect degree.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/恐怖谷理论">恐怖谷理论 - 维基百科，自由的百科全书</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Generative AI`, `#Sora`, `#AI Industry`, `#Corporate Strategy`

---

<a id="item-13"></a>
## [OpenAI terminates Sora text-to-video project](https://www.aibase.com/zh/news/26521) ⭐️ 8.0/10

On March 24, 2026, OpenAI officially announced the termination of all subsequent development and service of its leading text-to-video model Sora as part of a business restructuring. This move ends a planned $10 billion partnership with Disney, and OpenAI will shift its focus to GPT-5 and AI Agent development to prepare for 2026 capital market activities. This sudden exit reshapes the competitive landscape of the generative AI video industry, creating new opportunities and uncertainties for competing text-to-video developers. It also signals a major strategic shift for OpenAI, and highlights growing tensions between OpenAI and its largest investor Microsoft. OpenAI has not released specific technical reasons for terminating Sora, but the move is widely interpreted as a business slimming effort to present a clearer, more profitable business profile to investors ahead of capital market activities. The Sora team confirmed they will gradually shut down related services and will publish a timeline for API shutdown and user content retention plans later.

telegram · AI_News_CN · Mar 25, 01:07

**Background**: Sora is OpenAI's text-to-video generative AI model first announced to the public in February 2024, capable of generating 60-second 1080p videos from text prompts. GPT-5 is OpenAI's fifth-generation generative pre-trained transformer foundation model, publicly launched in August 2025. AI agents are autonomous AI systems that can complete goal-oriented tasks for users through independent reasoning and planning, which has become a key development focus of the generative AI industry in 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to-video model)</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5">GPT-5 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#generative AI`, `#Sora`, `#text-to-video`, `#AI industry`

---

<a id="item-14"></a>
## [Google releases Gemini 3.1 Flash-Lite lightweight LLM](https://www.aibase.com/zh/news/26527) ⭐️ 8.0/10

Google DeepMind has publicly released Gemini 3.1 Flash-Lite, a lightweight large language model that delivers 2.5x faster first response speed and over 360 tokens per second throughput, and can perform near-real-time dynamic UI generation. The model outperformed larger competing models like Claude Opus 4.6 on third-party multi-modal task testing. This breakthrough in low-latency generative AI enables new real-time AI use cases such as rapid UI prototyping and dynamic interactive interface generation, expanding the practical application scenarios of lightweight large language models. It also sets a new benchmark for speed and performance in the lightweight LLM market, pushing the industry to explore faster AI applications. The output cost of Gemini 3.1 Flash-Lite rose from $0.40 per million tokens to $1.50 per million tokens, and its existing demonstration is still unstable when handling complex web logic, with content potentially becoming disordered over time. The model is currently publicly available for use on Google AI Studio and Vertex AI.

telegram · AI_News_CN · Mar 25, 01:41

**Background**: Gemini 3.1 Flash-Lite is part of Google's Gemini 3 series of large models, launched in March 2026 and optimized for high-volume, low-latency workloads. Google AI Studio is a free web-based development environment released in 2023 that lets developers and non-technical users quickly prototype generative AI applications with Gemini models. Vertex AI is Google Cloud's managed enterprise platform for building, training and deploying machine learning and generative AI applications at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/">Gemini 3.1 Flash Lite: Our most cost-effective AI model yet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Studio">Google AI Studio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vertex_AI">Vertex AI</a></li>

</ul>
</details>

**Tags**: `#Google Gemini`, `#Large Language Models`, `#Generative AI`, `#Low-latency AI`

---

<a id="item-15"></a>
## [Judge questions US retaliation against Anthropic](https://www.aibase.com/zh/news/26528) ⭐️ 8.0/10

US federal judge Rita Lin has publicly questioned whether the Biden administration's blacklisting of leading AI firm Anthropic as a supply chain risk is political retaliation, after Anthropic's CEO refused to grant the US Department of Defense unrestricted access to its Claude AI model over misuse concerns. This case sets a critical precedent for the autonomy of private AI companies when facing demands from the US government, and its outcome will shape future norms for AI governance and government access to private AI models. Major Silicon Valley companies including Microsoft are closely watching the case, as a ruling favoring the government could open the door to arbitrary targeting of any AI firm that refuses government requests. The blacklisting designation, originally created to target foreign hostile actors, is being used for the first time against a leading US domestic AI company, and the broad executive order even bars non-sensitive federal agencies like the National Endowment for the Arts from using Claude. Anthropic says the designation threatens hundreds of millions of dollars in potential near-term revenue as defense contractors avoid its product due to policy uncertainty.

telegram · AI_News_CN · Mar 25, 02:03

**Background**: Anthropic is a leading US artificial intelligence company that developed the Claude series of large language models, first released to the public in 2023. The US Department of Defense's supply chain risk blacklist is a regulatory tool designed to flag companies that pose potential threats to US national security, and inclusion on the list restricts federal government entities from doing business with the firm.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/anthropic-supply-chain-risk-shockwaves-silicon-valley/">Anthropic Hits Back After US Military Labels It a ‘Supply ...</a></li>
<li><a href="https://www.msn.com/en-us/money/companies/pentagon-blacklisting-anthropic-ai-as-supply-chain-risk-was-retaliatory-elizabeth-warren-suggests/ar-AA1ZdX4S">Pentagon blacklisting Anthropic AI as 'supply chain risk' was ...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#AI governance`, `#politics of AI`, `#AI industry`, `#government policy`

---

<a id="item-16"></a>
## [Popular AI library litellm hit by supply chain poisoning](https://www.aibase.com/zh/news/26529) ⭐️ 8.0/10

Attackers stole release credentials to push malware-infected versions 1.82.7 and 1.82.8 of the widely used Python AI library litellm to PyPI, and the attack was only discovered early due to an attacker coding bug that caused system crashes. Renowned AI researcher Andrej Karpathy publicly warned developers about the incident. litellm has nearly 100 million monthly downloads and is depended on by over 2000 common AI tools, so this attack puts sensitive credentials including LLM API keys, cloud access keys and SSH keys of a huge number of AI developers at risk of theft. This incident also highlights the widespread software supply chain security risks facing the open source AI ecosystem. The malware is implanted via a malicious .pth file that automatically runs every time the Python interpreter starts, meaning it executes even if users never explicitly import litellm in their code, and it steals all sensitive system information and sends it encrypted to the attacker's server. The attack originated from attackers stealing litellm release credentials after compromising the vulnerability scanning tool Trivy.

telegram · AI_News_CN · Mar 25, 02:20

**Background**: LiteLLM is a popular open-source Python library that provides a unified interface for calling more than 100 different large language model APIs, making it a core foundational tool for many AI development projects. PyPI is the official public package repository for the Python programming language, and software supply chain attacks that inject malware into legitimate popular PyPI packages have become an increasingly common security threat in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack: Malicious PyPI Packages ...</a></li>
<li><a href="https://www.litellm.ai/">LiteLLM</a></li>
<li><a href="https://www.xda-developers.com/popular-python-library-backdoor-machine/">A popular Python library just became a backdoor to your ...</a></li>

</ul>
</details>

**Tags**: `#software supply chain security`, `#AI infrastructure`, `#malware`, `#open source security`, `#Python packages`

---

<a id="item-17"></a>
## [Litellm hit by supply chain poisoning, credentials leaked](https://telegra.ph/Karpathy-%E7%B4%A7%E6%80%A5%E9%A2%84%E8%AD%A6AI-%E5%BC%80%E5%8F%91%E8%80%85%E7%A5%9E%E5%99%A8litellm-%E9%81%AD%E6%95%99%E7%A7%91%E4%B9%A6%E7%BA%A7%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E6%95%B0%E4%B8%87%E5%87%AD%E8%AF%81%E6%88%96%E5%B7%B2%E5%85%A8%E6%B3%84%E9%9C%B2-03-25) ⭐️ 8.0/10

An alleged textbook-style supply chain poisoning attack has hit the widely used AI developer tool Litellm, with tens of thousands of user credentials potentially fully leaked, and the warning was originally shared as an urgent alert attributed to Andrej Karpathy. This incident affects thousands of AI developers that rely on Litellm to connect to multiple large language model services, making it a critical cybersecurity issue that requires immediate user action to prevent unauthorized access to their LLM accounts. The warning labels this incident as a textbook example of supply chain poisoning, and it estimates that up to tens of thousands of user credentials may have been exposed in the attack.

telegram · AI_News_CN · Mar 25, 02:20

**Background**: LiteLLM is a popular open-source library that provides a unified interface for developers to call over 100 different large language models from providers like OpenAI, Anthropic, and Google. A software supply chain poisoning attack is a cyberattack that injects malicious code into a trusted widely used tool, allowing attackers to compromise all downstream users that install or use the compromised software.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/supply-chain-attack/">What Is a Supply Chain Attack? - CrowdStrike</a></li>
<li><a href="https://www.twingate.com/blog/glossary/supply-chain-poisoning-attack">What Is Supply Chain Poisoning ? How It Works & Examples | Twingate</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#AI development tools`, `#cybersecurity`, `#software supply chain`

---

<a id="item-18"></a>
## [OpenAI shuts down consumer AI video app Sora](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 7.0/10

OpenAI has announced that it will shut down its consumer short-form AI video app Sora just six months after its public launch. The company says it will reorient its focus toward other priorities including robotics for real-world physical tasks. This abrupt shutdown signals a major strategic shift for OpenAI, and raises questions about the commercial viability of standalone consumer generative AI entertainment apps. It also reflects the company's push to control costs amid a crowded competitive landscape in generative AI. OpenAI published a safety guidance document for Sora only one day before announcing the shutdown, which has drawn criticism for the sudden and poorly communicated decision. Sora had previously struck a content partnership with Disney to allow users to generate AI videos featuring Disney characters.

hackernews · mikeocool · Mar 24, 20:01

**Background**: Sora was a generative AI-powered consumer app that allowed users to create short custom videos from simple text prompts, and gained viral attention shortly after launching. Generative AI video technology uses trained machine learning models to produce original video content from text or image inputs, and has grown rapidly in popularity over the past two years.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/03/24/technology/openai-shutting-down-sora.html">OpenAI Is Shutting Down Sora, Its A.I. Video Generator Top Stories OpenAI shutting down Sora video-creation app - NBC News OpenAI is shutting down its Sora video app just months after ... OpenAI pulls the plug on Sora video generator | AP News OpenAI shutters video app Sora as company reels in costs - CNBC OpenAI is scrapping the Sora app to chase bigger AI goals OpenAI Discontinues AI Video Gen App Sora - Forbes</a></li>
<li><a href="https://edition.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down">OpenAI is shutting down its Sora video app just months after ...</a></li>

</ul>
</details>

**Discussion**: Community discussion is split, with some critics calling Sora a harmful example of addictive corporate-controlled AI entertainment that spreads low-quality 'AI slop', while others who enjoyed the app note its novelty wore off quickly after launch, with little long-term engagement to keep users returning. Many commenters also criticized the sudden timing of the shutdown coming right after a new safety guidance was published.

**Tags**: `#generative ai`, `#openai`, `#ai video`, `#product shutdown`

---

<a id="item-19"></a>
## [Dependency cooldown support after LiteLLM attack](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

Following the March 2026 malicious LiteLLM supply chain attack, Simon Willison published commentary highlighting Andrew Nesbitt's survey of dependency cooldown features across major modern package managers. The survey shows that most popular package managers have already added native dependency cooldown support in recent releases between September 2025 and February 2026. This commentary draws urgent attention to a simple, effective security measure that can block around 80% of open source supply chain attacks, helping engineering teams quickly adopt protections after the high-profile LiteLLM incident. It also documents the rapid progress native cooldown support has made across the entire package management ecosystem, raising awareness of a underutilized security feature. Packages managers that added native cooldown support include pnpm 10.16, Yarn 4.10.0, Bun 1.3, Deno 2.6, uv 0.9.17, and npm 11.10.0, all of which allow setting minimum release age rules and creating exemptions for trusted packages; pip 26.0 only supports absolute timestamps for cooldown filtering, with a documented cron-based workaround for relative duration use cases.

rss · Simon Willison · Mar 24, 21:11

**Background**: Dependency cooldown is a supply chain security practice that blocks installation of newly published package versions until they have been publicly available for a set waiting period, letting the open source community detect malicious code before most users install the update. A 7-day dependency cooldown is estimated to block 80% of typical open source supply chain attacks, including those from compromised maintainer accounts. The March 2026 LiteLLM supply chain attack was carried out by the threat group TeamPCP, which compromised a maintainer's PyPI account to push backdoored versions of the popular AI proxy package to end users.

<details><summary>References</summary>
<ul>
<li><a href="https://byteiota.com/dependency-cooldowns-supply-chain-security/">Dependency Cooldowns Block 80% of Supply Chain Attacks</a></li>
<li><a href="https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html">TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via ...</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns - blog.yossarian.net</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#package managers`, `#dependency management`, `#software security`

---

<a id="item-20"></a>
## [Nvidia investment tactics draw antitrust scrutiny](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 7.0/10

Since 2022, Nvidia has invested billions of dollars in AI startups including OpenAI, CoreWeave and Reflection, and acquired talent and technology through deals like a $20 billion agreement with chip startup Groq. These business practices have drawn antitrust scrutiny from U.S. lawmakers who suspect they are designed to stifle competition. As the dominant player in the AI chip market, Nvidia's lock-in tactics could restrict innovation and consumer choice across the entire global AI ecosystem, and set a precedent for how regulators handle anti-competitive behavior in the fast-growing AI industry. This could affect AI startups, competing chip developers, and downstream AI service customers. Nvidia acts simultaneously as a supplier, investor and creditor for AI startups, which locks customers into its ecosystem and makes it difficult for them to switch to competitors like AMD. U.S. Democratic senators have sent a letter requesting Nvidia to explain its deal structures that are suspected of being designed to avoid antitrust scrutiny.

telegram · zaihuapd · Mar 24, 03:02

**Background**: Vendor lock-in is a business practice that makes it difficult for customers to switch to competing suppliers, and such practices by dominant market players can raise antitrust concerns under U.S. law. CoreWeave is a U.S. AI cloud computing infrastructure provider that specializes in GPU-based cloud services for AI developers, while Groq is an AI chip developer known for its low-latency inference-focused Language Processing Unit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vendor_lock-in">Vendor lock-in - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#artificial intelligence`, `#antitrust regulation`, `#AI chip industry`

---

<a id="item-21"></a>
## [China's daily AI token calls hit 140T, up 1000x in 2 years](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

Official data from China's National Data Administration shows China's daily average AI token call volume exceeded 140 trillion in March 2026, rising from 100 billion in early 2024 to grow more than 1000-fold in two years. This data was published in the state-run newspaper People's Daily. This extreme growth rate signals extremely rapid expansion of large language model usage across China, and confirms that a new token-centered commercial value system is forming for the domestic AI industry. It also reflects the progress of China's market-oriented data要素 reform to support AI development. Daily average token call volume reached 100 trillion by the end of 2025, meaning most of the 1000-fold growth occurred within the past two years. Tokens have quantifiable, priceable, and tradable traits that enable the formation of a standardized AI commercial system.

telegram · zaihuapd · Mar 24, 07:22

**Background**: A token is the smallest unit of text information processed by large language models, with each token roughly corresponding to 0.75 words in English. Per-token metering and pricing has become the global industry standard for AI commercialization, treating tokens as a measurable currency for AI computing resources, and a token-centered value system enables standardized trading of AI inference capacity. External third-party data also shows China has recently led the world in total large model call volume.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/304222714184033">AI TRENDS | China's AI Model Call Volume Surpasses U.S. for Second Week - Binance</a></li>
<li><a href="https://arxiv.org/html/2603.21690v1">AI Token Futures Market: Commoditization of Compute and ...</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/03/19/how-token-economics-could-define-success-with-ai/">How Token Economics Could Define Success With AI</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#large language models`, `#industry trend`, `#token usage`

---

<a id="item-22"></a>
## [Microsoft releases open source Rust training materials](https://github.com/microsoft/RustTraining) ⭐️ 7.0/10

Microsoft has published a public open source GitHub repository called RustTraining that contains 7 permissively licensed Rust textbooks, covering learning paths from beginner to expert for developers switching from other programming languages. The materials include content on advanced Rust topics such as async Rust and type-driven correctness. This comprehensive, official training set lowers the learning barrier for developers transitioning to Rust, filling a gap for high-quality structured learning materials that cover both beginner basics and advanced industry-focused topics. It also supports the growing industry adoption of Rust for system-level and performance-critical development. Each textbook contains 15 to 16 chapters, and is supplemented with Mermaid diagrams, editable Rust Playground links, practice exercises, and full-text search functionality. The project is released under a dual MIT and CC-BY-4.0 license, and can be read as raw Markdown on GitHub or as a rendered site via GitHub Pages.

telegram · zaihuapd · Mar 24, 23:57

**Background**: Rust is a systems programming language focused on memory safety, performance, and concurrency, which has seen growing adoption from large technology companies including Microsoft in recent years. Mermaid is a text-based open source tool that lets users create diagrams and visualizations directly in Markdown. Type-driven correctness is a Rust development approach that uses the language's powerful type system to eliminate bugs and guarantee code correctness at compile time.

<details><summary>References</summary>
<ul>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>
<li><a href="https://github.com/microsoft/RustTraining/blob/main/type-driven-correctness-book/src/ch01-the-philosophy-why-types-beat-tests.md">RustTraining/type-driven-correctness-book/src/ch01-the ...</a></li>
<li><a href="https://rust-lang.github.io/async-book/">Introduction - Asynchronous Programming in Rust</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Programming Education`, `#Training Materials`, `#Open Source`

---

<a id="item-23"></a>
## [Anthropic Launches Auto Mode for Claude Code](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) ⭐️ 7.0/10

Anthropic is rolling out Auto Mode for its AI coding tool Claude Code starting March 12, 2026. The new feature allows the Claude model to autonomously approve its own permission actions to enable higher levels of task automation. This feature cuts down on frequent permission prompts that interrupt developer workflows, enabling smoother end-to-end AI-assisted coding and pushing the industry forward toward more capable autonomous AI coding agents. It directly addresses a common pain point for developers using AI coding assistants. Auto Mode is currently available exclusively to Claude Code Team subscriptions, with a gradual gradual rollout planned for enterprise customers and API users in the coming days. The feature retains built-in AI safeguards to maintain security while cutting down on interruptions.

telegram · AI_News_CN · Mar 25, 00:48

**Background**: Claude Code is Anthropic's agentic AI coding tool designed to help developers work with entire codebases, edit files, run terminal commands, and ship software faster. By default, Claude Code requires developers to manually approve most permission-restricted actions such as editing files or running commands, which creates frequent interruptions during automated task workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.zdnet.com/article/claude-code-auto-mode/">How Claude Code's new auto mode prevents AI coding ... - ZDNET</a></li>
<li><a href="https://www.macobserver.com/news/anthropic-adds-auto-mode-to-claude-code-to-reduce-permission-prompts/">Anthropic Adds Auto Mode to Claude Code to Reduce Permission ...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding assistant`, `#feature announcement`, `#automation`

---

<a id="item-24"></a>
## [OpenAI pivots e-commerce strategy, abandons Instant Checkout](https://www.aibase.com/zh/news/26520) ⭐️ 7.0/10

OpenAI announced on Tuesday it is abandoning the ChatGPT Instant Checkout end-to-end transaction feature due to low conversion rates and poor flexibility. It will refocus its e-commerce efforts on building ChatGPT as a product discovery and consumer research hub using the Agent Commerce Protocol developed with Stripe. This strategic shift reveals the current limitations of generative AI in e-commerce and clarifies OpenAI's future roadmap for AI commerce, which will influence how other tech and e-commerce players develop AI shopping tools. Building the open Agent Commerce Protocol also lays technical groundwork for future autonomous AI agent shopping. Instant Checkout launched in September 2024 to let users complete full transactions directly within ChatGPT's conversation interface. OpenAI will still allow merchants to integrate checkout functions via built-in apps or redirect users to merchant websites for payment, but ChatGPT will no longer position itself as a direct transaction entry point.

telegram · AI_News_CN · Mar 25, 01:07

**Background**: ChatGPT Instant Checkout was OpenAI's first attempt to turn the generative AI chatbot into an end-to-end e-commerce transaction platform. The Agent Commerce Protocol is an open standard co-developed by OpenAI and Stripe that enables standardized programmatic commerce interactions between AI agents and merchant businesses.

<details><summary>References</summary>
<ul>
<li><a href="https://www.agenticcommerce.dev/">Agentic Commerce Protocol</a></li>
<li><a href="https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html">OpenAI revamps shopping experience in ChatGPT after Instant ...</a></li>
<li><a href="https://agenticcommerce.pro/zh-cn/docs/introduction/">ACP 协议介绍 – Agentic Commerce Protocol - International Communit...</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#E-commerce`, `#OpenAI`, `#ChatGPT`, `#AI Strategy`

---