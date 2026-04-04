---
layout: default
title: "Horizon Summary: 2026-04-04 (EN)"
date: 2026-04-04
lang: en
---

> From 48 items, 16 important content pieces were selected

---

1. [AI will automate most zero-day vulnerability research](#item-1) ⭐️ 8.0/10
2. [Axios supply chain attack used targeted social engineering](#item-2) ⭐️ 8.0/10
3. [MIIT warns of critical iOS exploit, urges update](#item-3) ⭐️ 8.0/10
4. [360 Gbps laser comms uses half Wi-Fi's energy](#item-4) ⭐️ 8.0/10
5. [FCC bans new foreign-made consumer routers](#item-5) ⭐️ 8.0/10
6. [Meituan open-sources unified multimodal LongCat-Next](#item-6) ⭐️ 8.0/10
7. [Anthropic blocks OpenClaw from Claude Code subscriptions](#item-7) ⭐️ 7.0/10
8. [AI tools boost Linux kernel security bug reports](#item-8) ⭐️ 7.0/10
9. [Greg KH: AI open source security reports improved fast](#item-9) ⭐️ 7.0/10
10. [CSP meta tags block JS escape in sandboxed iframes](#item-10) ⭐️ 7.0/10
11. [Google Vids adds free Veo 3.1 AI video generation](#item-11) ⭐️ 7.0/10
12. [China proposes digital virtual person regulation rules](#item-12) ⭐️ 7.0/10
13. [LinkedIn accused of scanning extensions for data sharing](#item-13) ⭐️ 7.0/10
14. [Qianwen App launches Wan2.7 video generative model](#item-14) ⭐️ 7.0/10
15. [OpenAI sees multiple senior management changes](#item-15) ⭐️ 7.0/10
16. [Anthropic blocks free OpenClaw access to Claude](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI will automate most zero-day vulnerability research](https://simonwillison.net/2026/Apr/3/vulnerability-research-is-cooked/#atom-everything) ⭐️ 8.0/10

Security researcher Thomas Ptacek argues that frontier large language model-powered AI coding agents will drastically reshape vulnerability research and exploit development within months, automating most high-impact zero-day discovery. This impending shift upends the entire economics of software security, affecting both defensive security teams and offensive vulnerability researchers, and requires immediate industry attention to prepare for the new landscape. Ptacek notes that vulnerability discovery matches the strengths of frontier LLMs perfectly, as these models already encode extensive knowledge of source code and common bug classes, and AI coding agents can run continuous automated testing without getting bored. Claude Code has already demonstrated real capability to discover new zero-day vulnerabilities in popular open source tools.

rss · Simon Willison · Apr 3, 23:59

**Background**: Vulnerability research is the process of finding security flaws in software, while zero-day vulnerabilities are previously unknown, unpatched flaws that carry high risk for attack. Exploit development is the practice of creating working code to take advantage of these found vulnerabilities. AI coding agents are autonomous AI tools that can write, test, and modify code on their own to complete targeted software tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.csoonline.com/article/4153288/vim-and-gnu-emacs-claude-code-helpfully-found-zero-day-exploits-for-both.html">Vim and GNU Emacs: Claude Code helpfully found zero-day exploits for both | CSO Online</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/exploit-development">Exploit Development - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**Tags**: `#vulnerability research`, `#AI agents`, `#cybersecurity`, `#large language models`

---

<a id="item-2"></a>
## [Axios supply chain attack used targeted social engineering](https://simonwillison.net/2026/Apr/3/supply-chain-social-engineering/#atom-everything) ⭐️ 8.0/10

Axios published a full postmortem of the March 2026 supply chain attack against its popular JavaScript library, which confirmed attackers used sophisticated individually targeted social engineering to compromise a maintainer's device. Attackers stole the maintainer's credentials by tricking them into installing a Remote Access Trojan, which allowed them to publish a malicious release of the library. Axios is an extremely widely used JavaScript library that is depended on by millions of projects globally, so a successful compromise can put huge numbers of downstream systems at risk. This novel attack vector demonstrates that open source maintainers now face highly personalized, coordinated targeting, requiring all active maintainers to update their threat awareness. The attack mimicked a UNC1069 campaign that the Google Cloud security team documented: attackers cloned a real company and cloned the company founder's identity, then tricked the maintainer into joining a fake Slack workspace and an MS Teams meeting. The maintainer was convinced to install a meeting-related update that was actually the RAT malware that stole their publish credentials.

rss · Simon Willison · Apr 3, 13:54

**Background**: Axios is a popular promise-based HTTP client JavaScript library used for both browser and Node.js applications. A software supply chain attack targets trusted dependencies in a software ecosystem, compromising the upstream component to deliver malware to all downstream users that rely on it. UNC1069 is a North Korean-linked cyber threat group that regularly uses social engineering tactics against software developers and technology organizations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>
<li><a href="https://grokipedia.com/page/UNC1069">UNC1069</a></li>
<li><a href="https://www.linkedin.com/pulse/axios-javascript-library-http-requests-rehan-a-xu3rc">AXIOS ( javaScript Library for HTTP requests)</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#social engineering`, `#open source security`, `#cybersecurity`

---

<a id="item-3"></a>
## [MIIT warns of critical iOS exploit, urges update](https://www.nvdb.org.cn/publicAnnouncement/2040008892420247553) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology's National Vulnerability Database (NVDB) has issued an official warning about a critical actively exploited vulnerability affecting all Apple iOS versions from 13.0 to 17.2.1, and it advises all affected users to upgrade their system immediately to patch the flaw. This vulnerability affects hundreds of millions of iPhone and iPad users globally, as attackers can already exploit it to steal personal data and fully compromise devices, so timely patching is critical to preventing widespread cyberattacks against Apple users. Attackers deliver the exploit via malicious links sent through SMS, email, or poisoned web pages, which trick users into visiting malicious sites to implant remote control trojans and gain root-level system privileges.

telegram · zaihuapd · Apr 3, 11:23

**Background**: NVDB, the Ministry of Industry and Information Technology's cybersecurity threat and vulnerability information sharing platform, is China's official platform for monitoring and publishing network security risk alerts. A remote code execution vulnerability of this severity allows attackers to run arbitrary malicious code on a target device without the user's knowledge, which can lead to full device control and data theft.

<details><summary>References</summary>
<ul>
<li><a href="https://www.henan100.com/news/2026/1240020.shtml">有攻击组织仿冒“龙虾”下载 网 站 和 安 装文件！ 工 信 部 NVDB ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/File_inclusion_vulnerability">File inclusion vulnerability - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/AMD_AutoUpdate_remote_code_execution_vulnerability">AMD AutoUpdate remote code execution vulnerability</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#iOS vulnerability`, `#security patch`, `#Apple security`

---

<a id="item-4"></a>
## [360 Gbps laser comms uses half Wi-Fi's energy](https://www.sciencedaily.com/releases/2026/04/260402042734.htm) ⭐️ 8.0/10

Researchers demonstrated a chip-scale laser wireless communication system that achieved a total transmission rate of 362.7 Gbps in 2-meter testing, with energy consumption per bit half that of leading current Wi-Fi technology. The work uses a 5×5 VCSEL laser array and has been published in the peer-reviewed journal *Advanced Photonics Nexus*. This breakthrough delivers vastly higher throughput and lower energy consumption than existing Wi-Fi, offering a promising new option for future short-range high-speed wireless communication systems that need to handle increasing data demands. It could help meet growing requirements for ultra-high-speed wireless connectivity in consumer and enterprise applications. The system has a measured energy consumption of 1.4 nanojoules per bit, and 21 of the 25 lasers in the 5×5 array were activated during testing, with each individual laser achieving a transmission rate between 13 and 19 Gbps.

telegram · zaihuapd · Apr 4, 01:47

**Background**: VCSEL, short for vertical-cavity surface-emitting laser, is a type of semiconductor laser that emits light perpendicular to its top surface. Individual VCSELs have small emission apertures, and they can be easily grouped into two-dimensional arrays to achieve higher output power and parallel transmission, making them well-suited for optical wireless communication applications. Advanced Photonics Nexus is a peer-reviewed open access academic journal that focuses on publishing high-impact new research in photonics and related engineering fields.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/垂直腔面射型雷射器">垂直腔面射型雷射器 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.highlightoptics.com/Product/1053.html">Inphenix垂直腔面发射激光器，VCSEL激光器，阵列芯片</a></li>
<li><a href="https://www.spiedigitallibrary.org/journals/advanced-photonics-nexus">Advanced Photonics Nexus</a></li>

</ul>
</details>

**Tags**: `#laser wireless communication`, `#optical communication`, `#wireless technology`, `#research breakthrough`

---

<a id="item-5"></a>
## [FCC bans new foreign-made consumer routers](https://t.me/zaihuapd/40689) ⭐️ 8.0/10

The U.S. Federal Communications Commission (FCC) has announced a full ban on importing new foreign-manufactured consumer routers into the U.S. market over cybersecurity and supply chain vulnerability concerns. Existing approved models and already deployed devices are exempt from the new ban, and vendors can apply for exemptions from the ban through U.S. national security agencies. This high-impact regulatory change will significantly reshape the global networking hardware market, alter global supply chains, and impact international trade of consumer network infrastructure. It will force foreign router manufacturers to adjust production and sales strategies, while raising industry-wide focus on supply chain security for networking devices. The FCC added these foreign-produced consumer routers to its Covered Entity List under the Secure Networks Act, and new uncertified models will not receive sales authorization for the U.S. market. The ban follows a cut-off rule that leaves ongoing use, import, and sales of existing approved and deployed devices completely unaffected.

telegram · zaihuapd · Apr 4, 02:35

**Background**: The FCC maintains a Covered List of communications equipment providers that are deemed to pose a threat to U.S. national security, which already includes major Chinese networking firms such as Huawei and ZTE. To sell networking and electronic devices in the U.S. market, vendors must first obtain official FCC equipment authorization through a compliance testing and approval process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fcc.gov/supplychain/coveredlist">List of Equipment and Services Covered By Section 2 of The Secure Networks Act | Federal Communications Commission</a></li>
<li><a href="https://legalclarity.org/fcc-covered-list-prohibited-equipment-and-services/">What Is the FCC Covered List? Rules and Penalties - LegalClarity</a></li>
<li><a href="https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization">Equipment Authorization - Federal Communications Commission</a></li>

</ul>
</details>

**Tags**: `#network security`, `#regulatory policy`, `#supply chain security`, `#networking hardware`

---

<a id="item-6"></a>
## [Meituan open-sources unified multimodal LongCat-Next](https://www.aibase.com/zh/news/26849) ⭐️ 8.0/10

On April 3, 2025, Meituan's technical team officially released and open-sourced the native multimodal large model LongCat-Next, which unifies visual, speech, and text processing into a single discrete token framework via its novel DiNA architecture and outperforms existing models on multiple industry benchmarks. This advancement proves that non-linguistic physical information from vision and speech can be discretized and modeled the same way as text, laying foundational work for building AI that can natively perceive and interact with the real world, and the full open-sourcing benefits the entire research and developer community. LongCat-Next uses the dNaViT visual tokenizer that supports arbitrary resolution inputs, achieves 28x pixel space compression while retaining key task details, scores 83.1 on MathVista and 86.80 on C-Eval, and beats both Qwen3-Omni and the dedicated Qwen3-VL model on the OmniDocBench dense text benchmark.

telegram · AI_News_CN · Apr 3, 10:19

**Background**: Most existing multimodal large language models follow a traditional 'language base + plugin' fragmented architecture that treats non-text modalities as external add-ons to a text-centric core. LongCat-Next instead uses a discrete native autoregressive (DiNA) architecture that converts all three modalities into homogeneous discrete tokens, treating them equally in a single modeling framework.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.27538">[2603.27538] LongCat-Next: Lexicalizing Modalities as Discrete Tokens</a></li>
<li><a href="https://a2a-mcp.org/blog/what-is-longcat-next">What Is LongCat-Next? Meituan's Open-Source Native Multimodal ...</a></li>
<li><a href="https://www.longcatai.org/news/longcat-next">LongCat-Next Released: Native Discrete Multimodal Model</a></li>

</ul>
</details>

**Tags**: `#multi-modal large model`, `#large language model`, `#AI architecture`, `#open-source AI`

---

<a id="item-7"></a>
## [Anthropic blocks OpenClaw from Claude Code subscriptions](https://news.ycombinator.com/item?id=47633396) ⭐️ 7.0/10

Starting April 4 2026 at 12pm PT, Anthropic will no longer allow third-party AI harnesses including OpenClaw to use existing Claude Code subscription limits, requiring separate pay-as-you-go billing for this type of usage. The company is offering a one-time credit equal to a user's monthly subscription price to smooth the transition, and will issue refunds for users who do not want to accept the new policy. This policy change affects all third-party autonomous AI agent tools that rely on Claude's consumer subscription APIs, reshaping the developer ecosystem built around Anthropic's consumer AI services and forcing developers to either adopt the new pricing model or switch to alternative platforms. It also highlights the growing tension between flat-rate subscription pricing and the high compute costs of autonomous agent usage for AI providers. Anthropic stated that third-party harnesses like OpenClaw put outsized strain on its infrastructure, so the change is needed to prioritize capacity for users of its official core products. The policy will be enforced first for OpenClaw starting April 4, and will later be rolled out to all other third-party harnesses.

hackernews · firloop · Apr 3, 22:55

**Background**: OpenClaw is a free open-source autonomous AI agent that can automate end-to-end tasks, including development work, by connecting to and using Claude's LLM capabilities through Claude Code. Claude Code is Anthropic's official agentic coding tool that allows developers to work with Claude directly from their terminal to edit code, run tests, and ship software. Third-party AI harnesses in this context are external tools that tap into existing Claude subscription access to add new autonomous or specialized features that are not available in Anthropic's official tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: Some commenters sympathized with Anthropic's decision, noting that subscription services rely on underuse by most users to subsidize heavy usage, and autonomous tools like OpenClaw consume far more capacity than regular users. Other users expressed frustration with the change and stated they will switch to cheaper alternative AI models rather than pay the higher cost of separate pay-as-you-go billing. Some developers also pointed out the difference between OpenClaw's integration method and previous banned tools, and worried that other legitimate third-party integrations like Conductor will be blocked next.

**Tags**: `#Anthropic Claude`, `#AI policy`, `#developer tools`, `#third-party integrations`, `#pricing changes`

---

<a id="item-8"></a>
## [AI tools boost Linux kernel security bug reports](https://simonwillison.net/2026/Apr/3/willy-tarreau/#atom-everything) ⭐️ 7.0/10

Senior open source developer Willy Tarreau notes that daily Linux kernel security bug reports have jumped from 2-3 per week two years ago to 5-10 per day in early 2026, driven by AI-powered bug finding tools. This surge in reports, which includes many duplicate findings, has forced the Linux kernel security team to add more maintainers to handle the increased workload. This trend reveals how the growing adoption of AI in security research is reshaping core open source infrastructure maintenance, creating both new opportunities to find more vulnerabilities and new operational challenges for overstretched maintainer teams. It affects the entire software ecosystem that relies on the Linux kernel, so adapting maintenance workflows will have broad security impacts. Most of the new AI-generated bug reports are still technically correct, but a large share are duplicates of bugs already found by other AI tools or researchers. Report volume is highest on Fridays and Tuesdays, according to Tarreau's observation.

rss · Simon Willison · Apr 3, 21:48

**Background**: AI-powered bug finding tools are automated tools that use artificial intelligence to scan source code for security vulnerabilities and bugs. The Linux kernel is the core foundational software of most modern server and consumer operating systems, and it relies on a small team of volunteer maintainers to triage, verify, and fix reported security bugs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalocean.com/resources/articles/ai-code-review-tools">10 AI Code Review Tools That Find Bugs & Flaws in 2025 | DigitalOcean</a></li>
<li><a href="https://www.browserstack.com/guide/bug-triage-process">Bug Triage : What, Why and How to perform? | BrowserStack</a></li>

</ul>
</details>

**Tags**: `#open source security`, `#linux kernel`, `#AI in software`, `#software maintenance`

---

<a id="item-9"></a>
## [Greg KH: AI open source security reports improved fast](https://simonwillison.net/2026/Apr/3/greg-kroah-hartman/#atom-everything) ⭐️ 7.0/10

Prominent Linux kernel maintainer Greg Kroah-Hartman observed that AI-generated open source security reports have rapidly evolved from obviously incorrect low-quality 'AI slop' to good, real, usable reports within months, with the shift occurring around March 2026. This observation from a leading open source core maintainer marks a major shift in AI's impact on core open source development practices, and signals that AI is becoming a genuinely useful tool for open source security work. It will change how open source projects handle security auditing going forward. Kroah-Hartman noted that just months ago these AI-generated reports were low-quality enough to be dismissed as 'AI slop', but a sudden qualitative shift happened around a month before his March 2026 interview that produced usable output across open source projects.

rss · Simon Willison · Apr 3, 21:44

**Background**: Greg Kroah-Hartman is one of the most prominent and long-serving maintainers of the Linux kernel, the core of one of the world's most widely used open source operating systems. A Linux kernel maintainer is responsible for reviewing code changes, managing subsystems, and upholding code quality and security for the kernel project. AI-generated security scans and reports have become increasingly common as generative AI adoption has grown in open source development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zdnet.com/article/maybe-open-source-needs-ai/">How AI has suddenly become much more useful to open-source ...</a></li>
<li><a href="https://www.linuxfoundation.org/blog/blog/role-of-a-linux-kernel-maintainer">Role of a Linux Kernel Maintainer</a></li>

</ul>
</details>

**Tags**: `#open source`, `#linux kernel`, `#generative ai`, `#security`, `#software development`

---

<a id="item-10"></a>
## [CSP meta tags block JS escape in sandboxed iframes](https://simonwillison.net/2026/Apr/3/test-csp-iframe-escape/#atom-everything) ⭐️ 7.0/10

Developer Simon Willison discovered that Content Security Policy meta tags injected at the top of sandboxed iframe content are properly enforced even when untrusted JavaScript added later tries to modify them. This discovery solves a common practical problem for developers working with untrusted embedded content, allowing safe isolation of untrusted content in iframes without requiring a separate dedicated domain. Willison made this discovery while working to build his own custom version of Claude Artifacts, a feature for hosting isolated interactive content.

rss · Simon Willison · Apr 3, 16:05

**Background**: Content Security Policy (CSP) is a web security mechanism that blocks unauthorized scripts and resources to prevent cross-site scripting and other attacks. CSP is most commonly delivered via HTTP response headers, but it can also be added to HTML via a meta tag, though this method was previously known to have limited effectiveness. Sandboxed iframes are used to isolate untrusted embedded content, but applying CSP protection to them normally requires hosting the iframe content on a separate domain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Content_Security_Policy">Content Security Policy - Wikipedia</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html">Content Security Policy - OWASP Cheat Sheet Series How to Set Up a Content Security Policy (CSP) - Sucuri Blog Content Security Policy (CSP) Headers - Complete Reference Guide Content Security Policy ( CSP ) Headers - Complete Reference Guide Content Security Policy - Wikipedia Content Security Policy ( CSP ) Headers - Complete Reference Guide Content-Security-Policy ( CSP ) Header Quick Reference Free CSP Analyzer & Security Headers Scanner | HeaderTest Content Security Policy - Wikipedia</a></li>
<li><a href="https://web.dev/articles/sandboxed-iframes">Play safely in sandboxed IFrames | Articles | web.dev</a></li>

</ul>
</details>

**Tags**: `#web security`, `#content security policy`, `#iframes`, `#javascript`, `#sandboxing`

---

<a id="item-11"></a>
## [Google Vids adds free Veo 3.1 AI video generation](https://www.techradar.com/ai-platforms-assistants/google-is-pushing-ai-video-into-ordinary-life-just-as-openai-pulls-sora-back) ⭐️ 7.0/10

Google has updated its browser-based Google Vids tool to integrate the Veo 3.1 AI video generation model, offering all Google account holders 10 free monthly AI video generations. The update also adds Lyria 3 and Lyria 3 Pro AI music generation and a customizable digital avatar feature exclusively for paid subscribers, while increasing the generation quota for top-tier subscribers to 1000 videos per month. This update expands consumer access to cutting-edge generative AI video technology, marking a major step toward bringing advanced AI video creation into everyday use for ordinary users. Google's public expansion of consumer AI video access also stands in direct contrast to OpenAI's recent decision to restrict public access to its Sora AI video generator. Veo 3.1 is Google DeepMind's latest state-of-the-art video generation model that supports up to 4K resolution output with native audio generation, while the Lyria 3 and Lyria 3 Pro music models integrated into Google Vids can generate background tracks ranging from 30 seconds to 3 minutes in length. Only paid Google AI Pro, Google AI Ultra and Workspace AI Ultra subscribers can access the new AI music and expanded avatar features, with top-tier subscribers receiving a greatly increased monthly generation quota.

telegram · zaihuapd · Apr 3, 05:23

**Background**: Google Vids is an AI-powered online timeline-based video editing application that is part of the Google Workspace productivity suite, designed to simplify collaborative video creation directly in the browser. Veo 3.1 is an incremental refined update to Google DeepMind's earlier Veo 3 generative video model, offering improved output quality, enhanced audio generation and better image-to-video conversion capabilities. Lyria 3 and Lyria 3 Pro are Google DeepMind's latest AI music generation models, with the Pro variant supporting longer track generation up to 3 minutes in length.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Vids">Google Vids - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/video">Generate videos with Veo 3.1 in Gemini API | Google AI for ... Top Stories Introducing Veo 3.1 and new creative capabilities in the ... Google Veo 3.1: The AI Video Generator That Includes Audio Veo 3.1: Google's Latest AI Video Update — New Features and ... Veo 3.1 API – Free Access to Google’s Latest AI Video Model ... Generate videos with Veo 3 . 1 in Gemini API | Google AI for Developers Introducing Veo 3 . 1 and new creative capabilities in the Gemini API Veo 3 . 1 API – Free Access to Google’s Latest AI Video Model | Kie AI Introducing Veo 3 . 1 and new creative capabilities in the Gemini API</a></li>
<li><a href="https://workspaceupdates.googleblog.com/2026/03/create-longer-musical-tracks-in-gemini-app-with-Lyria-3-Pro.html">Create longer musical tracks in the Gemini app with Lyria 3 Pro</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#AI Video Generation`, `#Google Vids`, `#Veo 3.1`

---

<a id="item-12"></a>
## [China proposes digital virtual person regulation rules](https://mp.weixin.qq.com/s/EHpjg2sfth0W7OE-v6hq9g) ⭐️ 7.0/10

On April 3, 2026, China's Cyberspace Administration released the draft Administrative Measures for Digital Virtual Human Information Services to solicit public comments, with the feedback deadline set for May 6, 2026. The draft proposes a series of regulatory requirements including mandatory digital identity labeling, restrictions on sensitive personal information usage, a ban on virtual partner and virtual kin services for minors, and mandatory algorithm filing for high-impact service providers, with maximum fines of 200,000 yuan for violations. This is the first targeted regulatory draft for China's fast-growing digital virtual human industry, which will standardize industry development and protect the rights and interests of vulnerable groups including minors. It affects all digital virtual human service providers and developers in China, and brings clear compliance requirements for stakeholders in the industry. The draft explicitly requires that all digital virtual human service display areas must prominently label the text 'digital human' throughout the entire service period. Modeling using a natural person's sensitive personal information requires separate consent from the person, and processing minor's information requires guardian consent, and providers must delete the digital virtual person after a user withdraws consent.

telegram · zaihuapd · Apr 3, 09:39

**Background**: Driven by advances in artificial intelligence technology, high-fidelity digital virtual humans have moved from science fiction to real-world applications, and are widely used in entertainment, e-commerce, education, companionship and other scenarios. IDC predicts that the market size of China's AI digital virtual human industry will reach 10.24 billion yuan in 2026, but the industry has also faced unregulated issues such as misappropriation of celebrity likenesses, unauthorized resurrection of deceased persons, and inducing minors to indulge in inappropriate services. Algorithm filing is an administrative regulatory process that requires algorithm service providers with public opinion attributes or social mobilization capabilities to submit relevant information to regulators for official record-keeping, which has become a statutory compliance requirement for relevant enterprises in China in 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-04/03/c_1776952388655846.htm">专家解读｜以人为本划定数字虚拟人服务边界，助力智能经济高质量发展_...</a></li>
<li><a href="https://news.bjd.com.cn/2026/04/03/11668741.shtml">专家解读｜以人为本，数字虚拟人管理规范引领技术向善_京报网</a></li>
<li><a href="https://baike.baidu.com/item/算法备案/67405404">算法备案_百度百科</a></li>

</ul>
</details>

**Tags**: `#digital virtual human`, `#regulation`, `#policy`, `#internet governance`

---

<a id="item-13"></a>
## [LinkedIn accused of scanning extensions for data sharing](https://cybernews.com/privacy/linkedin-surveillance-browsergate/?utm_source=flipboard&amp;utm_content=CyberNews_com%2Fmagazine%2FLatest+cybersecurity+news) ⭐️ 7.0/10

The BrowserGate investigation by a LinkedIn business user organization alleges that LinkedIn secretly scans installed browser extensions to collect sensitive user data, and shares this data with third parties including HUMAN Security without user consent or disclosure. This alleged practice potentially affects up to 405 million global LinkedIn users. This allegation impacts hundreds of millions of users and raises serious compliance concerns under major privacy regulations like GDPR. If confirmed, it would set a precedent for unregulated sensitive data collection by large social platforms and highlight gaps in user privacy protections for browser activity. The alleged scanning covers over 6,000 browser extensions including more than 200 competitor tools, and can reveal sensitive user information such as religious beliefs, political leanings, health status, and job search activity. The practice requires explicit user consent under the EU GDPR, which LinkedIn has not obtained according to the allegation.

telegram · zaihuapd · Apr 3, 12:09

**Background**: GDPR is the European Union's comprehensive privacy regulation that requires companies to obtain clear user consent before processing sensitive personal data, and applies to any service that serves users within the EU. BrowserGate is the name of the research investigation that published the allegations against LinkedIn, and the project has stated it will continue its investigation while industry observers wait for official responses from LinkedIn and relevant regulators.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/privacy/linkedin-surveillance-browsergate/">LinkedIn secretly injects code to spy on your browser | Cybernews</a></li>
<li><a href="https://gigazine.net/gsc_news/en/20260403-linkedin-browsergate/">BrowserGate is a research project that claims that every time ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GDPR">GDPR</a></li>

</ul>
</details>

**Tags**: `#Privacy`, `#Data Security`, `#LinkedIn`, `#GDPR`, `#Browser Security`

---

<a id="item-14"></a>
## [Qianwen App launches Wan2.7 video generative model](https://www.aibase.com/zh/news/26850) ⭐️ 7.0/10

Alibaba's Qianwen App launched the new Wan2.7 video generative model on April 3, 2025, adding free text-driven video editing, video extension, and action imitation capabilities alongside the already released Wan2.7 image model for all users. This update brings easy-to-use professional AI video creation and editing tools to ordinary users for free, lowering the technical barrier for short-form content creation and expanding the accessible use cases for generative AI in daily creative work. The model supports 2-second input videos to be extended up to 15 seconds, can replicate complex and multi-person coordinated actions from reference videos, and allows precise adjustments including character actions, camera angles and video styles while maintaining visual consistency.

telegram · AI_News_CN · Apr 3, 14:33

**Background**: Wan2.7 is an upgraded generative AI model from Alibaba that originally focused on image generation and editing before expanding to video capabilities. Text-driven video editing allows users to modify video content using natural language prompts instead of complex manual editing operations, while video extension (also called video continuation) generates new coherent content to extend the length of an existing uploaded video.

<details><summary>References</summary>
<ul>
<li><a href="https://wan27.org/">Wan 2.7 (wan2.7) — AI Video Generation, Editing & Recreation ...</a></li>
<li><a href="https://www.eachlabs.ai/blog/wan-2-7-is-here-everything-the-new-model-can-do">Wan 2.7 Is Here: Everything the New Model Can Do | Eachlabs</a></li>
<li><a href="https://aivideomaker.ai/zh/extend-video">aivideomaker AI 延长视频工具｜基于原视频的智能续写与场景延展</a></li>

</ul>
</details>

**Tags**: `#generative video AI`, `#AI model release`, `#video editing`, `#Wan2.7`, `#Qianwen`

---

<a id="item-15"></a>
## [OpenAI sees multiple senior management changes](https://api3.cls.cn/share/article/2335203?sv=8.7.5) ⭐️ 7.0/10

Ahead of OpenAI's potential 2024 IPO, multiple senior leadership changes have occurred: long-time COO Brad Lightcap will move to a role as head of special projects, CMO Kate Rouch will step down to focus on cancer rehabilitation, and head of AGI business Fidji Simo will take a several-week medical leave to treat a chronic neuroimmune condition. As OpenAI is the world's leading generative artificial intelligence company approaching a high-profile public listing, these major senior management changes may affect the company's business progress and IPO planning, and will bring ripple effects to the entire global AI industry. After Brad Lightcap's transfer, newly appointed chief revenue officer Denise Dresser will take over part of his original duties, and Lightcap will now report directly to CEO Sam Altman while leading a joint venture with a private equity firm to expand enterprise software sales.

telegram · AI_News_CN · Apr 3, 22:58

**Background**: OpenAI is one of the most influential artificial intelligence research and deployment companies in the world, best known for developing ChatGPT and the GPT series of large language models. The company has been rumored to be preparing for an initial public offering as early as 2024, which would be one of the most highly anticipated tech IPOs in recent years. AGI, or artificial general intelligence, refers to a hypothetical artificial intelligence that possesses the ability to understand, learn and apply knowledge across a wide range of tasks at a level equal to or beyond human capability, and is the core long-term development goal of OpenAI.

**Tags**: `#OpenAI`, `#artificial intelligence`, `#management change`, `#AGI`

---

<a id="item-16"></a>
## [Anthropic blocks free OpenClaw access to Claude](https://www.cnbeta.com.tw/articles/tech/1556530.htm) ⭐️ 7.0/10

Anthropic implemented a new policy starting April 4, 2025 that bars existing Claude subscription users from using their included quota to access the third-party AI agent OpenClaw. Users who wish to continue using OpenClaw must pay for usage separately through a pay-as-you-go model, effectively cutting off free third-party access. This change highlights growing tensions between AI platform owners and third-party developers building tools on top of their models, and signals that platforms are starting to enforce tighter control over ecosystem usage to manage infrastructure costs. It also reshapes the access economics for popular third-party AI tools built on LLM platforms. Anthropic stated the policy change is intended to manage growing infrastructure load and prioritize the experience of users accessing its official products, and it will give all subscription users a one-time credit equal to their monthly plan cost. OpenClaw's developer, who now works at OpenAI, negotiated to delay the policy's implementation by one week after unsuccessfully convincing Anthropic to reverse the decision.

telegram · AI_News_CN · Apr 4, 01:13

**Background**: OpenClaw is a popular free and open-source autonomous AI personal assistant that can complete multi-step practical tasks for users, such as managing emails, scheduling, and automatic web interactions, running on top of Anthropic's Claude LLM. Claude Cowork is Anthropic's official in-house agentic AI tool built for multi-step knowledge work, designed to compete with third-party agents like OpenClaw.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/product/claude-cowork">Claude Cowork | Anthropic’s agentic AI for knowledge work</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#AI Industry`, `#Anthropic Claude`, `#Third-party AI Tools`, `#AI Policy`

---