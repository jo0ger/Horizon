---
layout: default
title: "Horizon Summary: 2026-04-01 (EN)"
date: 2026-04-01
lang: en
---

> From 47 items, 15 important content pieces were selected

---

1. [OpenAI raises $122B at $852B post-money valuation](#item-1) ⭐️ 9.0/10
2. [Supply chain attack hits Axios npm package](#item-2) ⭐️ 9.0/10
3. [axios npm maintainer account compromised with malware](#item-3) ⭐️ 9.0/10
4. [Google cuts Bitcoin quantum attack threshold 20x](#item-4) ⭐️ 9.0/10
5. [OpenAI completes $122B funding at $852B valuation](#item-5) ⭐️ 9.0/10
6. [Anthropic Claude Code source code leaked via NPM](#item-6) ⭐️ 8.0/10
7. [500k lines of Claude Code source leaked publicly](#item-7) ⭐️ 8.0/10
8. [Google launches low-cost Veo 3.1 Lite video model](#item-8) ⭐️ 8.0/10
9. [Salesforce rolls out 30 AI upgrades for Slack](#item-9) ⭐️ 8.0/10
10. [Malicious code injected in popular open source LiteLLM](#item-10) ⭐️ 8.0/10
11. [Unofficial Claude Code source reconstruction on GitHub](#item-11) ⭐️ 7.0/10
12. [Meta launches new Ray-Ban Meta smart glasses](#item-12) ⭐️ 7.0/10
13. [Claude Code leak and Microsoft's Windows 11 shift](#item-13) ⭐️ 7.0/10
14. [8,100 Repos Taken Down Over Claude Code Leak](#item-14) ⭐️ 7.0/10
15. [Anthropic Claude source leak was a publicity stunt](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI raises $122B at $852B post-money valuation](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html) ⭐️ 9.0/10

OpenAI has closed a $122 billion funding round with an $852 billion post-money valuation as of March 31, 2026. This record-breaking valuation solidifies OpenAI's position as the highest-valued private AI company and reshapes market expectations for startup valuations in the global artificial intelligence industry. The funding announcement labels the $122 billion as committed capital, which may only represent a promised investment rather than capital already transferred to the company, and the stated valuation may be a maximum figure rather than the price all investors paid.

hackernews · surprisetalk · Mar 31, 20:07

**Background**: Post-money valuation refers to the estimated total value of a company immediately after new capital from an investment round is added, and it is calculated as the sum of the company's pre-investment valuation and the amount of new capital invested in the round. This metric is commonly used in venture capital to determine how much ownership investors receive in exchange for their investment, and it is similar to the market capitalization calculation for public companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-money_valuation">Post-money valuation</a></li>
<li><a href="https://www.investopedia.com/terms/p/postmoneyvaluation.asp">Understanding Post-Money Valuation: Key Concepts and Examples</a></li>

</ul>
</details>

**Discussion**: Community discussion covers multiple viewpoints: some users compare OpenAI's revenue growth to rival Anthropic, noting the growth gap between the two firms that may be partially explained by differing revenue reporting methods, others express skepticism about the extremely high valuation and point out that the valuation may not be consistent across all investors, while many critics argue that this funding round represents a complete betrayal of OpenAI's original non-profit founding principles focused on benefiting humanity rather than prioritizing profit.

**Tags**: `#OpenAI`, `#artificial intelligence`, `#funding`, `#startup valuation`, `#AI industry`

---

<a id="item-2"></a>
## [Supply chain attack hits Axios npm package](https://simonwillison.net/2026/Mar/31/supply-chain-attack-on-axios/#atom-everything) ⭐️ 9.0/10

Two compromised versions of the popular Axios npm package, versions 1.14.1 and 0.30.4, have been published with a malicious dependency `plain-crypto-js` that steals user credentials and installs a remote access trojan. The attack is believed to have originated from a leaked long-lived npm access token. Axios receives over 100 million weekly npm downloads, so this attack poses a widespread security risk to the entire JavaScript development ecosystem. It also highlights critical security gaps in current npm package publishing practices for widely used open-source projects. The malicious packages were published without a corresponding GitHub release, a pattern that was also observed in a recent supply chain attack against the LiteLLM project. Axios already had an open issue to adopt npm's trusted publishing, which would block this type of unauthorized publication.

rss · Simon Willison · Mar 31, 23:28

**Background**: npm is the default package manager for the JavaScript programming language, used by developers to distribute and reuse open-source code libraries. A long-lived npm access token is a persistent authentication credential that allows holders to publish updates to a package, and these tokens are at higher risk of being leaked and misused if compromised. Trusted publishing is a newer npm security feature that uses OpenID Connect to only allow authorized CI/CD workflows (such as GitHub Actions) to publish package updates, eliminating the need for long-lived access tokens. A remote access trojan (RAT) is a type of malware that grants attackers full unauthorized remote control over an infected computer.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/about-access-tokens/">About access tokens | npm Docs</a></li>
<li><a href="https://docs.npmjs.com/trusted-publishers/">Trusted publishing for npm packages</a></li>
<li><a href="https://www.bitdefender.com/en-us/business/infozone/what-is-a-remote-access-trojan-rat">What is Remote Access Trojan (RAT) - InfoZone</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#npm`, `#cybersecurity`, `#javascript`

---

<a id="item-3"></a>
## [axios npm maintainer account compromised with malware](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) ⭐️ 9.0/10

On March 31, 2026, security firm StepSecurity discovered that the npm maintainer account of the widely used JavaScript HTTP library axios had been compromised. Attackers manually published two malicious versions, axios@1.14.1 and axios@0.30.4, that inject a remote access trojan targeting Windows, macOS and Linux systems. As axios receives over 300 million downloads per week and is relied on by countless software projects globally, this major npm supply chain compromise poses a widespread risk to JavaScript developers and end users. Affected projects need to be patched immediately to prevent unauthorized remote access and data theft. The malicious versions use a fake dependency called plain-crypto-js to trigger malicious code, which connects to an attacker-controlled command and control (C2) server after infection, and automatically deletes the malicious script and fakes clean configuration files to avoid detection. Security experts recommend developers downgrade to the safe versions 1.14.0 or 0.30.3 and rotate all credentials on affected machines.

telegram · zaihuapd · Mar 31, 04:10

**Background**: npm is the default package manager for JavaScript, hosting millions of open-source packages that developers commonly include as dependencies in their own projects. GitHub Actions is a popular CI/CD platform that many npm package maintainers use to automate package publishing workflows. A remote access trojan (RAT) is a type of malware that lets attackers fully control an infected device remotely to steal data or install more malicious software. A command and control (C2) server is a central system that cybercriminals use to send commands to and collect data from compromised devices.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/actions/quickstart">Quickstart for GitHub Actions - GitHub Docs</a></li>
<li><a href="https://www.techtarget.com/searchsecurity/definition/RAT-remote-access-Trojan">What is a RAT ( Remote Access Trojan )? | Definition from TechTarget</a></li>
<li><a href="https://www.malwarepatrol.net/command-control-servers-c2-servers-fundamentals/">C2 Servers: Command and Control Fundamentals & Risks</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#npm`, `#axios`, `#software security`, `#javascript`

---

<a id="item-4"></a>
## [Google cuts Bitcoin quantum attack threshold 20x](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) ⭐️ 9.0/10

Google Quantum AI has published a breakthrough optimization of Shor's algorithm for cracking elliptic curve cryptography, reducing the required number of physical qubits from the prior estimate of 10 million to under 500,000. This optimized attack could steal unconfirmed Bitcoin within 9 minutes, putting around one-third of the total Bitcoin supply at potential risk. This breakthrough brings practical quantum attacks on widely used elliptic curve cryptography and Bitcoin much closer to reality, pushing the cryptocurrency industry to accelerate development and adoption of post-quantum security standards. It highlights the urgent need to update cryptography systems that currently rely on ECC, which is used by nearly all major cryptocurrencies today. An attacker can complete most precomputation ahead of time, then derive a Bitcoin private key in about 9 minutes after a transaction is broadcast, giving a 41% chance of hijacking funds before the transaction is confirmed in the next block. The 2021 Bitcoin Taproot upgrade defaults to exposing public keys, which may expand the range of vulnerable Bitcoin addresses beyond the already exposed 6.9 million coins.

telegram · zaihuapd · Mar 31, 08:03

**Background**: Shor's algorithm is a quantum algorithm developed in 1994 that can solve the discrete logarithm problem that underpins elliptic curve cryptography's security, allowing quantum computers to derive private keys from exposed public keys. Elliptic curve cryptography is a public-key cryptography system that uses smaller keys to deliver the same security as older systems like RSA, making it the default choice for Bitcoin and most modern cryptocurrencies. Zero-knowledge proof is a cryptographic protocol that allows a prover to confirm a statement is true without revealing any additional underlying information, which the Google team used to hide the details of their attack method in their public disclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic-curve_cryptography">Elliptic-curve cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#cryptography`, `#bitcoin`, `#cryptocurrency security`

---

<a id="item-5"></a>
## [OpenAI completes $122B funding at $852B valuation](https://www.aibase.com/zh/news/26738) ⭐️ 9.0/10

On March 31 local time, leading artificial general intelligence developer OpenAI announced it had completed a new funding round raising $122 billion, pushing its post-money valuation to $852 billion, the highest valuation ever for a global startup. This funding will accelerate OpenAI's AGI development, strengthen the industry's matthew effect and accelerate the concentration of the global AI industry towards top players, greatly raising the barriers to entry for new competitors. This $122 billion funding round is seen as a landmark event showing that the large foundation model competition has entered a capital-intensive stage, and the massive capital will support OpenAI's expansion of computing infrastructure, talent recruitment and next-generation model development.

telegram · AI_News_CN · Apr 1, 01:36

**Background**: Artificial General Intelligence, or AGI, refers to artificial intelligence that can adapt to diverse environments and handle a wide range of complex tasks, unlike narrow AI which is built for specific single tasks. Post-money valuation is the valuation of a company after new investment is added to its value, and it represents the market's pricing of the company's total worth after the funding round. The Matthew effect in industry describes the trend where stronger players get even stronger while weaker players fall further behind, increasing industry concentration.

<details><summary>References</summary>
<ul>
<li><a href="https://drjackeiwong.com/2023/04/08/人工智能比較：弱-ani-vs-強-agi-vs-超-asi/">人 工 智 能 比較：弱 (ANI) vs 強 ( AGI ) vs 超 (ASI) - Dr. Jackei...</a></li>
<li><a href="https://www.sec.gov/Archives/edgar/data/1879016/000106299324016874/exhibit10-1.htm">Ivanhoe Electric Inc.: Exhibit 10.1 - Filed by newsfilecorp.com - SEC.gov</a></li>
<li><a href="https://www.nccu.edu.tw/p/406-1000-17600,r41.php?Lang=zh-tw">ICI跨域講座「A Future with AGI - 通 用 人 工 智 慧（ AGI ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#artificial intelligence`, `#venture funding`, `#AGI`, `#industry landscape`

---

<a id="item-6"></a>
## [Anthropic Claude Code source code leaked via NPM](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/) ⭐️ 8.0/10

Anthropic's Claude Code source code was accidentally leaked via an unexcluded source map published to the public NPM registry, and Anthropic has since issued DMCA takedown requests for related repositories including some that did not host the leaked code. The leak reveals proprietary implementation details such as an 'undercover mode' for the AI coding tool. This leak highlights ongoing risks of misconfigured build and publishing pipelines for modern JavaScript projects, exposes proprietary internal logic of one of the most popular commercial AI coding tools, and has sparked industry debate over aggressive DMCA takedown practices after code has already spread publicly. The leak was caused by a default source map generation setting in the Bun JavaScript runtime that was not overridden, with one missing exclusion line in either .npmignore or package.json. Leaked details include undercover mode prompts that instruct Claude to avoid mentioning it is an AI in generated code commits and pull requests.

hackernews · alex000kim · Mar 31, 13:04

**Background**: Claude Code is a command-line AI coding tool developed by Anthropic, built on the company's proprietary Claude large language models, that assists developers with writing, editing and managing code. Source maps are debugging files that map minified production JavaScript back to the original uncompiled source code, and if published publicly, they can allow anyone to reconstruct the full original source code of a project.

<details><summary>References</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/">Anthropic accidentally leaked Claude Code source code via a map file ...</a></li>

</ul>
</details>

**Discussion**: Hacker News community members separated the leak mechanism, a common build configuration error, from the exposed proprietary content, and noted that an open issue already exists for Bun's default source map behavior. Many community members criticized Anthropic's aggressive DMCA takedowns that removed forks that did not even contain the leaked code, and observers expressed surprise at how many internal trade secret-level comments were included directly in the shipped source code.

**Tags**: `#source code leak`, `#Claude Code`, `#NPM`, `#software build pipelines`, `#AI coding tools`

---

<a id="item-7"></a>
## [500k lines of Claude Code source leaked publicly](https://www.aibase.com/zh/news/26735) ⭐️ 8.0/10

A low-level DevOps configuration mistake by Anthropic left 500,000 lines of Claude Code source code publicly accessible via an npm package, and the leaked code reveals two unannounced features: personalized pixel cyber pet companion BUDDY and the autonomous background learning feature KAIROS with a nightly dreaming mechanism. This leak exposes major operational security vulnerabilities at a leading AI company that brands itself as focused on safe AI development, and serves as a critical warning to the entire AI industry about the risks of small engineering oversights as AI coding tools gain higher system permissions. The leak occurred because Anthropic failed to remove debug source map (.map) files from its public npm package, which effectively exposes the full original readable TypeScript codebase even for minified production builds, and the leaked code has already been permanently archived and shared across developer communities.

telegram · AI_News_CN · Apr 1, 01:04

**Background**: Claude Code is Anthropic's official agentic AI coding tool that helps developers understand codebases, edit files and ship projects faster. npm is a popular public package registry for JavaScript and TypeScript code, and source map files are debugging assets that map compressed bundled code back to the original uncompiled source files, which are not intended to be included in public production releases of proprietary software.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/soufianebouaddis/claude-code">GitHub - soufianebouaddis/claude-code: Claude Code's leaked source ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo">Claude Code's Entire Source Code Was Just Leaked via npm Source ...</a></li>

</ul>
</details>

**Tags**: `#Source Code Leak`, `#Anthropic Claude`, `#AI Security`, `#Software Development`

---

<a id="item-8"></a>
## [Google launches low-cost Veo 3.1 Lite video model](https://www.aibase.com/zh/news/26739) ⭐️ 8.0/10

Google has officially released Veo 3.1 Lite, a cost-optimized lightweight AI video generation model priced at only $0.05 per second for 720P resolution output. This model completes Google's Veo 3.1 product family and offers high output quality at less than half the cost of the existing Veo 3.1 Fast model. This drastic reduction in inference cost removes a major barrier to commercial adoption of AI video generation, and signals a broader industry shift from pure parameter scaling to efficiency optimization. It will open up new use cases like personalized custom video and real-time game cutscene generation for small creators and development teams. Veo 3.1 Lite retains Google DeepMind's advantage in temporal consistency, avoiding common flickering and distortion issues that plague many early lightweight video models while maintaining stable 720P output quality with accurate light, shadow and motion details. It costs less than 50% of Veo 3.1 Fast while matching its generation speed.

telegram · AI_News_CN · Apr 1, 01:44

**Background**: Temporal consistency is a core performance metric for AI video generation, measuring a model's ability to keep visual elements such as objects, lighting and motion stable across consecutive frames without flickering or distortion. High inference cost has long been a major bottleneck that prevented AI video generation technology from moving out of research labs and into large-scale commercial applications.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/">How developers can use Veo 3.1 Lite for AI video generation</a></li>
<li><a href="https://getstream.io/glossary/temporal-consistency/">Temporal Consistency - What is it and how does it work?</a></li>
<li><a href="https://9to5google.com/2026/03/31/veo-3-1-lite/">Google commits to video generation, announces Veo 3.1 Lite</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#generative AI`, `#Google`, `#large language models`, `#AIGC`

---

<a id="item-9"></a>
## [Salesforce rolls out 30 AI upgrades for Slack](https://www.aibase.com/zh/news/26740) ⭐️ 8.0/10

Salesforce has announced the largest AI upgrade in Slack's history, adding 30 deeply integrated generative AI features connected to Salesforce Data Cloud that support open access for third-party large models. This upgrade transforms Slack from a simple communication tool into an AI-powered enterprise productivity hub, aligning with the industry trend of AI integration for enterprise collaboration tools and reshaping how internal enterprise teams collaborate. The upgraded Slack AI can generate cross-channel project summaries, allow non-technical users to build automated workflows with natural language, and contextual search that can answer questions and recommend relevant experts, and it is compatible with Salesforce's own Einstein model as well as third-party models from OpenAI and Anthropic.

telegram · AI_News_CN · Apr 1, 01:54

**Background**: Slack is a widely used enterprise collaboration platform owned by Salesforce, which is the global leader in customer relationship management (CRM) solutions. Salesforce Einstein is the native AI layer for the Salesforce platform, and Einstein GPT launched in 2023 is the first generative AI product built specifically for CRM scenarios. Salesforce Data Cloud is a Salesforce-built product that unifies all enterprise customer data to support real-time AI data calls.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/668909967">Einstein GPT-生成式人工智能CRM全面解析：简介、架构、原理、产品、... Einstein AI 赋能 Salesforce：架构师视角下的预测智能深度解析 Artificial Intelligence (AI) at Salesforce AI销售10大标杆案例研究:Salesforce Einstein 如何用 AI 改造 B2B 销... Salesforce Einstein Copilot：企业生成式人工智能的最佳案例 - 53AI-... 他山之石系列报告 (一)：SALESFORCE的大模型TOB应用分析</a></li>
<li><a href="https://walk-ct.com/data-cloud/">Salesforce Data Cloud 的歷史與未來 - 沃克雲端</a></li>
<li><a href="https://slack.com/features/workflow-automation">Workflow Automation Tool, Software, & App | Slack</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#Collaboration Tools`, `#Salesforce Slack`, `#Enterprise AI`, `#Productivity Software`

---

<a id="item-10"></a>
## [Malicious code injected in popular open source LiteLLM](https://www.aibase.com/zh/news/26745) ⭐️ 8.0/10

$100 billion valued AI unicorn Mercor confirmed that its popular open source AI library LiteLLM was injected with malicious code in a supply chain attack by hacking group TeamPCP. Ransomware group Lapsus$ also claimed to have stolen Mercor's internal data and leaked sample data including internal communication records. As a widely used upstream open source tool for LLM integration with millions of daily downloads, this attack affects thousands of downstream enterprises and exposes critical security vulnerabilities in the fast-growing open source AI infrastructure ecosystem. This event pushes the entire AI industry to re-examine the security of open source components and promote stricter security monitoring mechanisms. The injected malicious code was identified and removed within a few hours after the attack was discovered, and Mercor has hired third-party forensics experts to conduct an investigation and implemented emergency containment and remediation measures. LiteLLM has also urgently changed its compliance certification body to Vanta, an automated compliance service provider.

telegram · AI_News_CN · Apr 1, 02:44

**Background**: LiteLLM is a popular open source Python SDK and AI gateway that provides developers with a unified interface to call more than 100 different large language model APIs from providers including OpenAI and Anthropic. A supply chain attack targets upstream software components to inject malicious code, which can then spread malware to a large number of downstream users and organizations that rely on the compromised component. Vanta is a technology company that provides automated compliance services to help enterprises quickly obtain common security certifications such as ISO 27001 and SOC 2.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM] · GitHub</a></li>
<li><a href="https://www.oldboyedu.com/blog/5152.html">供 应 链 攻 击 是什么? 应 该如何处理?</a></li>
<li><a href="https://36kr.com/p/2887512733080454">Vanta 获红杉、高盛参投的1.5亿美元C轮融资，用AI...</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#open source security`, `#AI infrastructure`, `#cybersecurity`

---

<a id="item-11"></a>
## [Unofficial Claude Code source reconstruction on GitHub](https://github.com/ChinaSiro/claude-code-sourcemap) ⭐️ 7.0/10

An unofficial GitHub repository called claude-code-sourcemap has reconstructed 4756 source files (including 1884 TypeScript and TSX files) for Claude Code 2.1.88 from the source map included in the official public @anthropic-ai/claude-code npm package. The repository released the reconstructed code for non-commercial research use only, and warns users that linking the repository to an official Claude Code installation may lead to account risks. This reconstruction allows independent security auditing and transparency analysis of Anthropic's closed-source Claude Code CLI, which was not previously possible for outside researchers. The incident also highlights a common oversight in commercial JavaScript/TypeScript software distribution that can accidentally leak full proprietary source code to the public. The reconstruction pulls full source code content directly from the `sourcesContent` field of the `cli.js.map` source map file distributed by Anthropic itself, and it does not claim to match the exact internal repository structure of Anthropic's official development version. All original source code copyright is still held by Anthropic, per the repository's disclaimer.

telegram · zaihuapd · Mar 31, 09:33

**Background**: Claude Code is a closed-source command-line interface tool developed by AI company Anthropic that lets developers use Claude large language models for software development workflows. Source maps are standard files generated during JavaScript/TypeScript build processes, primarily used to help developers debug minified production code by mapping it back to the original uncompiled source files. The `sourcesContent` field included in many source maps stores the full text of the original source files, which enables full source reconstruction when the source map is distributed publicly.

<details><summary>References</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.theblockbeats.news/flash/338932">Claude Code 's latest npm package accidentally included a 60MB...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#source code reconstruction`, `#npm`, `#reverse engineering`, `#Anthropic`

---

<a id="item-12"></a>
## [Meta launches new Ray-Ban Meta smart glasses](https://www.aibase.com/zh/news/26741) ⭐️ 7.0/10

On March 31, Meta and EssilorLuxottica launched the new Ray-Ban Meta smart glasses, which support custom prescription lenses including progressive and photochromic options, add multiple new Meta AI-powered features, and are set to ship globally on April 14 with a starting price of $499. This update moves smart glasses beyond niche geek products to a practical AI-enabled mobile computing terminal, exploring a new paradigm for post-smartphone mobile computing and expanding the application boundaries of multimodal large models. The new release adds two new frame styles while retaining a lightweight design; the $499 starting price does not include potential hundreds of dollars in additional costs for custom prescription lenses. New AI features cover real-time translation for Japanese, Mandarin and Arabic, vision-based nutrition tracking, and long conversation summarization to resolve information overload issues on lightweight devices.

telegram · AI_News_CN · Apr 1, 01:54

**Background**: Progressive lenses are advanced optical lenses that allow seamless switching of vision between near, medium and far distances, making them suitable for people with multiple vision needs such as presbyopia. Multimodal large models are large AI models that can process and understand multiple types of data including text, images, audio and video, enabling richer interactive experiences across devices. Meta AI is Meta Platforms' AI research division and consumer-facing AI product suite built on Meta's open-source Llama large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.facebook.com/ElegantOptometry/photos/clear-vision-all-day-comfort-hoya-stellify-progressive-lensesenjoy-seamless-visi/1263015592505257/">有效阻隔有害光线与屏幕眩光，长时间使用电子产品也能减轻眼睛疲劳。 配备高端防反光与防刮涂层，镜片持久清晰，带来全方位锐利、舒适的视觉体验。无论是工作 - Facebook</a></li>
<li><a href="http://ilearn.hitsz.edu.cn/xsky/r/dmtdmx.htm">多模态大模型-智能媒体研究中心</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta_AI">Meta AI - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#smart wearables`, `#generative AI`, `#augmented reality`, `#mobile computing`

---

<a id="item-13"></a>
## [Claude Code leak and Microsoft's Windows 11 shift](https://www.solidot.org/story?sid=83926) ⭐️ 7.0/10

Anthropic accidentally leaked the full unobfuscated source code of its AI programming tool Claude Code via an npm source map file, and copies of the leaked code have been uploaded to public GitHub repositories. In a separate announcement, Microsoft plans to build more native Windows 11 applications to cut memory usage, moving away from resource-heavy web-based PWA architectures. The Claude Code leak reveals a simple, low-cost optimization for AI content moderation that challenges assumptions that large language models are required for all lightweight AI tasks, and it has sparked broad discussion about production build best practices. Microsoft's shift to native applications signals a broader industry reversal of the move to web-based apps for desktop, as rising memory costs push developers to prioritize efficiency over development speed. The leaked code shows Claude Code uses a lightweight regex-based approach to detect negative sentiment in user prompts, which is much faster and uses far less computing power than calling a large language model for the same task. Microsoft's existing Windows 11 apps like Clipchamp and Copilot are built on web-based PWA architecture, which is easier for developers to build but consumes significantly more system memory.

telegram · AI_News_CN · Apr 1, 02:32

**Background**: Source maps are debugging files that map bundled, minified production JavaScript code back to the original unmodified source code, and accidentally including a source map in a public npm package can expose the full unobfuscated source code of a project. A Progressive Web App is a web application built with standard web technologies that behaves like a native app, offering easier cross-platform development but typically higher resource usage than true native applications.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo">Claude Code's Entire Source Code Was Just Leaked via npm ...</a></li>
<li><a href="https://cybernews.com/security/anthropic-claude-code-source-leak/">Full source code for Anthropic’s Claude Code leaks | Cybernews</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps">Progressive web apps - MDN Progressive Web App Architecture: A Step-by-Step Guide Get started developing a PWA - Microsoft Edge Developer ... PWA Architecture (Progressive Web App) - Smart Digitants Progressive Web Apps (PWA): The Evolution of Web Apps and a ... PWA Architecture | All About Progressive Web Apps With Examples Get started developing a PWA - learn.microsoft.com Progressive Web App Architecture : A Step-by-Step Guide How to Build a Progressive Web App | MernStackDev</a></li>

</ul>
</details>

**Discussion**: The leak has generated substantial public discussion on Hacker News, with many developers surprised that a major AI company uses a simple regex solution for sentiment detection instead of relying on its own large language models, and many noting that the mistake of including source maps in production releases is surprisingly common.

**Tags**: `#Claude Code`, `#source code leak`, `#Windows 11`, `#AI programming tools`, `#native applications`

---

<a id="item-14"></a>
## [8,100 Repos Taken Down Over Claude Code Leak](http://cli.js.map/) ⭐️ 7.0/10

Anthropic filed a DMCA takedown request to GitHub after Claude Code 2.1.88 source code was reconstructed from the source map of Anthropic's public npm package and uploaded to GitHub. GitHub took down a total of 8,100 connected forked and related repositories per the request. This large-scale takedown raises key questions about intellectual property protection for AI proprietary code and acceptable practices in the open source community, and it sets a notable precedent for handling leaked source code distributed through public development artifacts. The unauthorized repository reconstructed 4756 source files including 1884 TypeScript and TSX files by extracting content from the `sourcesContent` field of `cli.js.map` included with the official `@anthropic-ai/claude-code` npm package. GitHub's policy allows disabling all 8100 repositories in the connected network because the network exceeds 100 repositories and Anthropic claimed all forks contained infringing content.

telegram · AI_News_CN · Apr 1, 02:38

**Background**: Claude Code is an AI-powered coding tool developed by Anthropic, the company behind the Claude large language model. JavaScript source maps are build artifacts that map compiled minified JavaScript code back to the original uncompiled source files for debugging purposes, and they are often distributed publicly alongside production JavaScript packages. DMCA is a United States copyright law that provides a framework for online service providers like GitHub to process copyright infringement takedown requests from rights holders.

<details><summary>References</summary>
<ul>
<li><a href="https://web.dev/articles/source-maps">What are source maps? | Articles | web.dev</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Claude Code overview - Claude Code Docs</a></li>
<li><a href="https://docs.github.com/articles/dmca-takedown-policy">DMCA Takedown Policy - GitHub Docs</a></li>

</ul>
</details>

**Tags**: `#DMCA`, `#Anthropic Claude`, `#source code leak`, `#GitHub`, `#intellectual property`

---

<a id="item-15"></a>
## [Anthropic Claude source leak was a publicity stunt](https://www.aibase.com/zh/news/26746) ⭐️ 7.0/10

The high-profile Anthropic Claude Code source leak incident has seen a dramatic reversal, as the man claiming to be a fired Anthropic engineer responsible for the leak was revealed to be a non-employee running a bait-and-switch marketing stunt for his startup Ferryman. The underlying source code exposure, which published over 500,000 lines of internal code via an npm source map file, was a real accidental engineering error from Anthropic. This incident exposes serious CI/CD process vulnerabilities at leading AI company Anthropic, revealing that even top-tier AI firms cutting corners on infrastructure security during rapid expansion. It also highlights how easily real security accidents can be exploited for publicity in the hype-driven AI industry, affecting public trust in major AI developers. The leaked code reveals unpublicized Claude Code features including fully autonomous agent command logic, a systematic system prompt matrix, and hidden permission bypass testing modes called Undercover Mode and Bypass Permissions Mode. No sensitive customer data or credentials were exposed in the leak, according to official statements.

telegram · AI_News_CN · Apr 1, 03:10

**Background**: Anthropic is a leading AI developer that created the Claude large language model series, and Claude Code is Anthropic's official agentic coding tool designed to help developers work with codebases, edit files and run terminal commands. Source map files are developer assets that map minified production code back to original human-readable source code, and accidental publication of these files in public npm packages can allow attackers to reconstruct full internal source code. CI/CD refers to continuous integration and continuous delivery, the automated workflow teams use to build and publish software.

<details><summary>References</summary>
<ul>
<li><a href="https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know">Claude Code's source code appears to have leaked: here's what we know | VentureBeat</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#source code leak`, `#Anthropic Claude`, `#AI security`, `#software engineering`, `#marketing scandal`

---