---
layout: default
title: "Horizon Summary: 2026-03-26 (EN)"
date: 2026-03-26
lang: en
---

> From 54 items, 24 important content pieces were selected

---

1. [Swift 6.3 Officially Released With Official Android Support](#item-1) ⭐️ 9.0/10
2. [Apifox desktop hit by supply chain poisoning](#item-2) ⭐️ 9.0/10
3. [CCF boycotts NeurIPS over US sanction-based submission ban](#item-3) ⭐️ 9.0/10
4. [Apple Google partner: Gemini powers Siri AI](#item-4) ⭐️ 9.0/10
5. [AI2 Releases Open-Source Vision-Driven MolmoWeb](#item-5) ⭐️ 9.0/10
6. [GitHub to Use Copilot User Data for AI Training](#item-6) ⭐️ 9.0/10
7. [DeepMind launches Lyria 3 Pro AI music model](#item-7) ⭐️ 9.0/10
8. [Hacker News debates new ARC-AGI-3 benchmark](#item-8) ⭐️ 8.0/10
9. [SC rules for Cox in music copyright piracy case](#item-9) ⭐️ 8.0/10
10. [47,000 downloads of compromised LiteLLM on PyPI](#item-10) ⭐️ 8.0/10
11. [Google TurboQuant compresses LLM KV cache to 3 bits](#item-11) ⭐️ 8.0/10
12. [Intel, AMD extend server CPU delivery to Chinese clients](#item-12) ⭐️ 8.0/10
13. [Trump forms AI policy council with tech leaders](#item-13) ⭐️ 8.0/10
14. [Apple distills Google Gemini for on-device iPhone AI](#item-14) ⭐️ 8.0/10
15. [Hacker runs Model 3 computer on desktop from crashed car parts](#item-15) ⭐️ 7.0/10
16. [Hacker News debate on EU Chat Control push](#item-16) ⭐️ 7.0/10
17. [Critique of rushed AI agent code generation](#item-17) ⭐️ 7.0/10
18. [NASA adjusts Artemis plan, pauses Gateway for lunar base](#item-18) ⭐️ 7.0/10
19. [AI short dramas displace Hengdian extras](#item-19) ⭐️ 7.0/10
20. [Kuaishou Ke Ling grows after OpenAI Sora shutdown](#item-20) ⭐️ 7.0/10
21. [Amap adds OpenClaw-compatible AI agent skills](#item-21) ⭐️ 7.0/10
22. [Tongyi Qianwen enters Hongqi mass production cars](#item-22) ⭐️ 7.0/10
23. [OpenAI invests in AI agent startup Isara](#item-23) ⭐️ 7.0/10
24. [Apifox SaaS JS tampering security alert](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Swift 6.3 Officially Released With Official Android Support](https://swift.org/blog/swift-6.3-released/) ⭐️ 9.0/10

Swift 6.3 was officially released on March 25, 2026, bringing the first official Swift SDK for Android. This release allows developers to write native Android applications in Swift, or integrate Swift code into existing Kotlin/Java Android projects via the Swift Java plugin. This release marks a major milestone for Swift in cross-platform development, enabling developers to share a single codebase across Apple platforms and Android instead of maintaining separate native codebases. It expands Swift's use cases beyond the Apple ecosystem and creates new options for cross-platform native application development. The official Swift SDK for Android includes all required libraries, headers and resources to generate and run Swift code targeting Android devices, and the Swift Java plugin enables Swift code to call existing Java/Kotlin APIs by wrapping Java classes into corresponding Swift types. As of the 2025 pre-release testing, Android community developers noted that available Swift-covered Android APIs were still limited.

telegram · zaihuapd · Mar 25, 03:45

**Background**: Swift is a general-purpose programming language originally developed by Apple for iOS, macOS and other Apple platform development, and it has become open-source since its launch. Before this official release, experimental nightly builds of the Swift SDK for Android had been available to developers since October 2025 for testing and porting work. Cross-platform development allows developers to build applications that run on multiple operating systems with shared code, reducing overall development and maintenance workload.

<details><summary>References</summary>
<ul>
<li><a href="https://www.swift.org/documentation/articles/swift-sdk-for-android-getting-started.html">Getting Started with the Swift SDK for Android | Swift.org</a></li>
<li><a href="https://www.swift.org/blog/nightly-swift-sdk-for-android/">Announcing the Swift SDK for Android | Swift.org</a></li>
<li><a href="https://github.com/swiftlang/swift-java">GitHub - swiftlang/swift-java: Java interopability support for Swift · GitHub</a></li>

</ul>
</details>

**Discussion**: In Reddit's Android developer community discussion of the pre-release SDK, some developers expressed concern that the Android API support provided by Swift is still very limited, and that Swift will likely lag behind the fast iteration of official Android APIs such as Jetpack Compose. Third-party tools like skip.tools have already built additional functionality on top of this SDK to help developers bring SwiftUI apps to Android by bridging to Jetpack Compose.

**Tags**: `#Swift`, `#cross-platform development`, `#Android development`, `#programming language release`

---

<a id="item-2"></a>
## [Apifox desktop hit by supply chain poisoning](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 9.0/10

Attackers tampered with a CDN-hosted statistics script in the Apifox desktop client to steal sensitive developer data including SSH keys and Git credentials, with the attack active since March 4 affecting users on Windows, macOS, and Linux. Security researcher phith0n has independently recovered the malicious payload and shared public analysis code, and Apifox has since removed the malicious script from the latest version. This attack is a high-impact supply chain incident targeting a widely used API development tool, putting the sensitive core credentials of thousands of software developers at severe risk of compromise. It also highlights the ongoing security threat of compromised third-party CDN resources for desktop applications. Users can check for compromise by searching for suspicious domains like apifox.it.com in their local Apifox Network Persistent State file or LevelDB database, and mitigation steps include blocking the suspicious domains via firewall or DNS and reinstalling the latest version of Apifox. Apifox has not released an official public statement about the incident as of the disclosure.

telegram · zaihuapd · Mar 25, 11:10

**Background**: Apifox is a popular integrated API development collaboration platform that combines features of tools like Postman, Swagger, Mock, and JMeter, used by a large number of software developers. A supply chain poisoning attack is a sophisticated cyberattack where malicious actors compromise a trusted third-party component in a software's distribution chain to inject malicious code, and CDN (Content Delivery Network) is a common service used to host and deliver static scripts and resources for software.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/apifox">Apifox · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://www.idmanagement.gov/experiments/cdns/paper2/">CDN Attack Vectors and Mitigation - IDManagement</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#cybersecurity`, `#software security`, `#credential theft`

---

<a id="item-3"></a>
## [CCF boycotts NeurIPS over US sanction-based submission ban](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 9.0/10

The China Computer Federation (CCF) issued an official statement on March 25, 2026 opposing NeurIPS 2026's new policy that bans submissions from institutions on US sanction lists. CCF called on Chinese scholars to boycott the conference and threatened to remove NeurIPS from its recommended academic conference directory if the policy is not reversed. This marks one of the strongest institutional responses to the growing politicalization of top global AI academic conferences, and it could significantly shift participation patterns in one of the field's most influential events, with lasting impacts on international scholarly exchange in computer science and AI. CCF's statement specifically calls on Chinese computer scientists and researchers to refuse all academic services for NeurIPS as well as refuse to submit papers to the conference, and the removal from the recommended directory will only take effect if NeurIPS does not reverse its policy.

telegram · zaihuapd · Mar 25, 14:07

**Background**: NeurIPS, full name Conference on Neural Information Processing Systems, is one of the three most influential top annual conferences in machine learning and artificial intelligence research, alongside ICML and ICLR. The CCF-recommended directory of international academic conferences and journals is a widely referenced ranking in Chinese academia that affects academic evaluation, promotion and graduate graduation requirements for many Chinese computer science researchers. The core value of open and inclusive academic exchange free from political interference is a widely accepted norm in the global academic community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeurIPS">NeurIPS</a></li>
<li><a href="https://ccf.atom.im/">中国计算机学会推荐国际学术会议和期刊目录（2026）</a></li>

</ul>
</details>

**Tags**: `#AI research`, `#academic conferences`, `# NeurIPS`, `#academic policy`, `#scholarly exchange`

---

<a id="item-4"></a>
## [Apple Google partner: Gemini powers Siri AI](https://t.me/zaihuapd/40506) ⭐️ 9.0/10

Apple and Google have announced a multi-year partnership where Google's Gemini model and cloud technology will power Apple's new AI features launching this year, including a more personalized Siri. Apple will maintain its existing privacy standards, with all AI processing running on-device or on private cloud. This partnership reshapes the global AI assistant market and upends the long-standing competitive dynamic between two of the world's largest technology companies. It will directly improve the AI capability of Siri, which has long lagged behind competitors in generative features, giving iPhone users a smarter assistant experience. Apple's next-generation Apple Foundation Models will be built on top of Google's Gemini technology to power the new Siri features. Apple retains control over its privacy framework, so user data will not be compromised by the partnership with Google.

telegram · zaihuapd · Mar 25, 16:32

**Background**: Gemini is Google's latest family of large generative AI models, with Gemini 3 being its most capable version to date that supports advanced reasoning tasks. Apple Foundation Models is Apple's on-device large language model framework that powers Apple Intelligence, its brand of on-device AI features for Apple devices. On-device AI refers to AI processing that runs directly on the user's local hardware rather than external cloud servers, which helps improve response speed and protect user privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/">Gemini 3 — Google DeepMind</a></li>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>
<li><a href="https://www.articsledge.com/post/on-device-ai">What Is On-Device AI? How It Works in 2026 - articsledge.com</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#apple`, `#google`, `# Gemini`, `#siri`

---

<a id="item-5"></a>
## [AI2 Releases Open-Source Vision-Driven MolmoWeb](https://www.aibase.com/zh/news/26564) ⭐️ 9.0/10

The Allen Institute for Artificial Intelligence (AI2) has launched MolmoWeb, a fully open-source vision-driven web agent that only uses browser screenshots to make navigation decisions. It also released MolmoWebMix, the largest open dataset of human and synthetic web navigation data to date. This release shifts the web agent paradigm away from reliance on webpage DOM structure, enabling more robust web automation that works across most websites regardless of underlying code changes. Its strong performance with smaller model sizes and fully open licensing also democratizes web agent research, challenging closed monopolies held by large tech companies. The 8B-parameter version of MolmoWeb scores 78.2% on the WebVoyager benchmark, near OpenAI's closed o3 model score of 79.3%, and outperforms Anthropic's Claude 3.7 on UI element positioning tasks; rerunning tasks to select the best result pushes its success rate to 94.7%. The model and dataset are released under the permissive Apache 2.0 license on GitHub and Hugging Face, though it still faces challenges with complex instructions, login authentication, and legal compliance.

telegram · AI_News_CN · Mar 26, 01:28

**Background**: Traditional web agents rely on accessing the Document Object Model (DOM), the underlying code structure of a webpage, to identify elements and make decisions. DOM structures often change when websites are updated, breaking traditional agents, and DOM access is not always available for all web platforms. A vision-driven design lets agents operate like humans, by viewing the page visually rather than parsing raw code, making it more broadly compatible. WebVoyager is a standard benchmark that measures how well web agents complete real-world navigation tasks across common websites.

<details><summary>References</summary>
<ul>
<li><a href="https://allenai.org/blog/molmoweb">MolmoWeb: An open agent for automating web tasks | Ai2</a></li>
<li><a href="https://www.researchgate.net/publication/384207409_WebVoyager_Building_an_End-to-End_Web_Agent_with_Large_Multimodal_Models">WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | Request PDF</a></li>
<li><a href="https://arxiv.org/html/2401.13919v3">WebVoyager : Building an End-to-End Web Agent with Large...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open-source AI`, `#web automation`, `#computer vision`, `#machine learning`

---

<a id="item-6"></a>
## [GitHub to Use Copilot User Data for AI Training](https://www.aibase.com/zh/news/26566) ⭐️ 9.0/10

GitHub announced that starting April 24, 2026, it will by default use interaction data from Copilot Free, Pro, and Pro+ users to train its AI models, with an opt-out mechanism that lets users manually disable data usage in privacy settings. Copilot Business, Enterprise, and education users are not affected by this policy change. This policy shift affects millions of developers, raises critical questions about data privacy, intellectual property ownership, and the definition of private code, and signals a broader industry trend where major AI firms are turning to private user interaction data to improve model performance as public high-quality code data becomes scarce. This change also marks a key strategic shift for GitHub from an open source code hosting platform to a closed-loop AI training ecosystem. The collected data includes model input and output, code snippets, context information, repository structure, chat interaction records, cursor context, comments, documentation, file names, and user feedback on code suggestions, and this data may be shared with affiliated companies including Microsoft but will not be provided to third-party AI providers. The policy uses an opt-out default mechanism rather than requiring users to actively opt in to data usage, which is the core point of community controversy.

telegram · AI_News_CN · Mar 26, 01:45

**Background**: GitHub Copilot is an AI-powered code assistant co-developed by GitHub and OpenAI, which provides automatic code suggestions to developers based on existing code context, and the model has relied on training data from public code repositories to improve its performance so far. Generative AI model quality is heavily dependent on the scale and quality of training data, and data compliance for AI training has become a core regulatory and industry issue globally in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oschina.net/news/290253/github-copilot-workspace">GitHub 发布 AI 原生开发工具 GitHub Copilot Workspace - OSCHINA - 中文开源技术交流社区</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1888887013358404123">AI大模型训练数据合规法律风险及应对 - 知乎</a></li>
<li><a href="https://blog.csdn.net/w605283073/article/details/141014372">浅析 GitHub Copilot 工作原理帮你更高效使用-CSDN博客</a></li>

</ul>
</details>

**Discussion**: The policy change has sparked broad discussion in the global developer community, with most debates centered on whether it is reasonable for GitHub to use user's private code snippets and repository data for AI training by default, and how the policy redefines the traditional concept of private repositories.

**Tags**: `#GitHub Copilot`, `#AI policy`, `#data privacy`, `#software development`

---

<a id="item-7"></a>
## [DeepMind launches Lyria 3 Pro AI music model](https://www.aibase.com/zh/news/26569) ⭐️ 9.0/10

Google DeepMind has released Lyria 3 Pro, an advanced AI music generation model that can create complete, structured full-length high-fidelity songs from text prompts, advancing AI music generation beyond short 30-second fragments. This model can independently generate entire songs with standard song structures including intros, verses, choruses, and bridges. This marks a major leap in generative AI for audio, shifting AI music tools from auxiliary creative aids toward autonomous full composition, and it has the potential to reshape the entire digital music production industry. It enables faster, lower-cost music creation for content creators while forcing human musicians to shift their focus to deeper emotional and artistic work. Lyria 3 Pro supports 24-bit high-fidelity audio output that meets the basic requirements of professional audio production, and leverages Google's multimodal technology to let users generate songs directly from natural text descriptions of style, mood and rhythm. The model is also available for use within Google's Gemini app for creating custom tracks for content projects.

telegram · AI_News_CN · Mar 26, 02:02

**Background**: Before Lyria 3 Pro, most existing AI music generation models could only create short 30-second melody fragments rather than complete structured full songs. Google DeepMind launched the original version of Lyria 3 in February 2025, and has accelerated its development iteration in the AI music track to release this upgraded Pro version just months later.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/ai/lyria-3-pro/">Lyria 3 Pro: Create longer tracks in more Google products</a></li>
<li><a href="https://workspaceupdates.googleblog.com/2026/03/create-longer-musical-tracks-in-gemini-app-with-Lyria-3-Pro.html">Create longer musical tracks in the Gemini app with Lyria 3 Pro</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#AI music`, `#DeepMind`, `#large language model`, `#audio generation`

---

<a id="item-8"></a>
## [Hacker News debates new ARC-AGI-3 benchmark](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

The ARC Prize team has publicly released the ARC-AGI-3 benchmark and its accompanying technical report, which sparked a high-engagement critical discussion on Hacker News. The conversation focuses on flaws in the benchmark's human baseline methodology and whether ARC challenges actually measure true general intelligence. As one of the most prominent public benchmarks for measuring progress toward artificial general intelligence, debates over ARC-AGI-3's design will shape how researchers evaluate next-generation AI systems and measure AGI progress. The discussion also highlights ongoing disagreements within the AI community over how to define and test for general intelligence. Critics point out that ARC-AGI-3 defines its human baseline as the second-best first-run human performance among self-selected puzzle-solving volunteers, rather than using an average human score across a representative sample. The benchmark also uses per-level action efficiency as its core scoring metric, and critics note it does not clearly report how many full challenge levels models complete.

hackernews · lairv · Mar 25, 18:16

**Background**: The ARC-AGI benchmark is a prominent test designed to measure a machine's ability to reason, abstract, and generalize to new unseen problems, which are considered core capabilities of artificial general intelligence. The ARC Prize is a million-dollar nonprofit public competition that challenges participants to develop open-source solutions that can beat the ARC-AGI benchmark. Previous versions including ARC-AGI-2 were released before 2025 as an upgrade over earlier iterations to avoid common benchmark issues like memorization and overfitting.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>
<li><a href="https://spectrum.ieee.org/arc-prize-agi-test">ARC Prize Challenge: AI's Struggle With Simple Puzzles - IEEE ...</a></li>
<li><a href="https://www.adaline.ai/blog/what-is-the-arc-agi-benchmark-and-its-significance-in-evaluating-llm-capabilities-in-2025">What is the ARC AGI Benchmark and its significance in... | Adaline</a></li>

</ul>
</details>

**Discussion**: Most commenters expressed criticism of the benchmark, with some arguing it does not actually measure general intelligence because performance depends heavily on prior puzzle-solving experience that not all humans share. There is also disagreement over whether ARC-AGI's approach to measuring intelligence is valid, with some comparing it to the argument that airplanes count as flying even if they do not use bird-like wing flapping, while supporters argue testing both humans and AI on the same problems is a fair approach to evaluating intelligence.

**Tags**: `#AGI`, `#AI Benchmarking`, `#ARC Challenge`, `#AI Evaluation`

---

<a id="item-9"></a>
## [SC rules for Cox in music copyright piracy case](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html) ⭐️ 8.0/10

In March 2026, the U.S. Supreme Court ruled in favor of internet service provider Cox Communications in a copyright liability lawsuit filed by major music labels over Cox's subscribers sharing pirated music. The original jury verdict that found Cox liable was overturned by the high court's decision. This landmark decision reshapes rules of third-party copyright liability for internet service providers across the U.S., and sets a major precedent that reduces pressure on ISPs to conduct widespread monitoring of their subscribers' online activity. It will affect the balance of power between copyright holders, internet intermediaries, and the online privacy of everyday internet users. The Supreme Court's majority opinion cited the 1984 Sony Betamax case, which established that the Copyright Act does not automatically hold third-party providers liable for infringement committed by their users. The music labels had argued Cox financially benefited from piracy by its subscribers and failed to take sufficient action to stop it.

hackernews · oj2828 · Mar 25, 15:02

**Background**: Under U.S. copyright law, internet service providers have long been protected from secondary liability for user infringement under the safe harbor provisions of the Digital Millennium Copyright Act, so long as they meet certain requirements to address infringing activity. This case centered on whether ISPs can still be held directly liable for failing to curb widespread piracy by their subscribers when safe harbor protections do not apply.

**Discussion**: Most Hacker News commenters reacted positively to the ruling, celebrating it as a small win that reduces incentives for ISPs to monitor user activity online. Some commenters used analogies to clarify the ruling's logic, while others criticized the existing modern copyright system as overly restrictive and harmful. One commenter also noted that the ruling appropriately cited the older Betamax copyright precedent.

**Tags**: `#copyright law`, `#internet policy`, `#supreme court`, `#internet service provider`

---

<a id="item-10"></a>
## [47,000 downloads of compromised LiteLLM on PyPI](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 8.0/10

Daniel Hnyk analyzed that compromised versions 1.82.7 and 1.82.8 of LiteLLM were downloaded 46,996 times during 46 minutes they were live on PyPI, and 88% of dependent packages were unpinned and vulnerable. This incident highlights widespread dependency version pinning risks in the Python AI supply chain, affecting thousands of developers and organizations that use LiteLLM to connect to multiple large language models. The analysis was done using the public BigQuery PyPI dataset that records official PyPI download statistics, and the two malicious versions were only available on PyPI for less than an hour before being removed.

rss · Simon Willison · Mar 25, 17:21

**Background**: LiteLLM is a popular open-source Python library that provides a unified interface for accessing over 100 different large language models from various providers. PyPI is the official public package repository for the Python programming language. Version pinning is the practice of specifying exact versions for dependencies, which prevents automatic installation of untested or malicious new versions.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.litellm.ai/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://stackoverflow.com/questions/28509481/should-i-pin-my-python-dependencies-versions">Should I pin my Python dependencies versions? - Stack Overflow</a></li>
<li><a href="https://docs.pypi.org/api/bigquery/">BigQuery Datasets - PyPI Docs</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#pypi`, `#software packaging`, `#llm`

---

<a id="item-11"></a>
## [Google TurboQuant compresses LLM KV cache to 3 bits](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) ⭐️ 8.0/10

Google Research has introduced TurboQuant, an online vector quantization algorithm that can compress large language model KV cache down to 3 bits without requiring any model retraining or fine-tuning. The method delivers up to 6x memory reduction and up to 8x faster attention computation on H100 GPUs while maintaining original model performance. This advance addresses the critical memory bottleneck caused by growing KV cache size during long-context large language model inference, enabling efficient deployment of longer context windows on consumer and data center hardware. It outperforms existing quantization methods, pushing the boundaries of achievable compression levels without sacrificing accuracy. TurboQuant will be presented at ICLR 2026, alongside two related compression methods QJL and PolarQuant that will be presented at AISTATS 2026. In high-dimensional vector search tasks, TurboQuant also delivers better recall than existing methods PQ and RabbiQ.

telegram · zaihuapd · Mar 25, 05:15

**Background**: KV cache is a technique that stores intermediate key and value computation results during large language model inference to speed up text generation, but its size grows linearly with context length and batch size, creating major memory bottlenecks for long-context inference. Vector quantization is a classical lossy compression technique that groups similar high-dimensional vectors and represents each group with a single prototype vector, reducing the total memory required to store the dataset.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant : Redefining AI efficiency with extreme compression</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vector_quantization">Vector quantization</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#model quantization`, `#KV cache compression`, `#AI efficiency`

---

<a id="item-12"></a>
## [Intel, AMD extend server CPU delivery to Chinese clients](https://t.me/zaihuapd/40507) ⭐️ 8.0/10

Reuters reports that Intel and AMD have notified Chinese clients of extended server CPU delivery times due to tight supply. Intel has implemented limited allocations of its 4th and 5th Gen Xeon processors in China and raised overall server product prices by over 10%, while some AMD products now have delivery times extended to 8 to 10 weeks. This development affects global semiconductor supply chains and the deployment of cloud and AI infrastructure in China, and will directly influence local hardware procurement costs and availability. The AI-driven server CPU shortage also reflects the broader global boom in AI infrastructure investment that is reshaping semiconductor market dynamics. Intel attributes the supply tightness to demand growth driven by rapid AI adoption, and predicts that its inventory will hit a bottom in the first quarter of 2026 and begin to improve in the second quarter of that year. Some Intel server CPU models now have delivery lead times as long as 6 months for Chinese clients.

telegram · zaihuapd · Mar 26, 00:03

**Background**: Server CPUs are specialized processors designed to power server hardware, which provide computing resources and services for cloud platforms, data centers, and AI model training and inference. The 4th and 5th Gen Intel Xeon are Intel's latest generations of server-focused CPUs, widely used in enterprise data centers and AI infrastructure around the world.

<details><summary>References</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon/5th-gen-xeon-scalable-processors.html">5th Gen Intel® Xeon® Processors – Intel</a></li>
<li><a href="https://en.wikipedia.org/wiki/Server_(computing)">Server (computing)</a></li>
<li><a href="https://www.serversimply.com/blog/intels-5th-generation-vs-4th-generation-xeon-cpus-advancements-and-integrations">Intel Xeon 4th Gen Vs 5th Gen Scalable Processors | Server Simply</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#supply chain`, `#server CPU`, `#hardware industry`

---

<a id="item-13"></a>
## [Trump forms AI policy council with tech leaders](https://www.aibase.com/zh/news/26565) ⭐️ 8.0/10

Former U.S. President Donald Trump plans to form an AI policy advisory council called PCAST, with an initial batch of 13 members including top tech leaders Jensen Huang, Mark Zuckerberg, and Sergey Brin. The council will advise the White House on U.S. AI strategy focused on deregulation, maintaining global AI leadership, economic impact, and national security. This council brings together the most influential figures in the global AI industry to directly shape U.S. national AI policy, so its policy recommendations will likely have far-reaching impacts on global AI development, regulatory trends, and international AI competitiveness. This move signals a shift toward more industry-aligned U.S. AI policy that prioritizes reducing regulatory barriers to innovation. The 13 initial members cover AI hardware infrastructure, internet applications, and enterprise technology, and the council is co-chaired by White House AI and crypto affairs official David Sacks. Its core priorities also include addressing the impact of AI on the U.S. labor market.

telegram · AI_News_CN · Mar 26, 01:45

**Background**: PCAST stands for the President's Council of Advisors on Science and Technology, a long-standing advisory body that dates back to 1933. It is tasked with gathering leading science and technology experts to provide policy recommendations directly to the U.S. President on pressing national technology-related issues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/President's_Council_of_Advisors_on_Science_and_Technology">President's Council of Advisors on Science and Technology - Wikipedia</a></li>
<li><a href="https://kyma.com/decision-2024/national-politics/2026/03/25/president-trump-appoints-first-members-of-pcast/">President Trump appoints first members of PCAST - KYMA</a></li>
<li><a href="https://obamawhitehouse.archives.gov/administration/eop/ostp/pcast/about">About PCAST | The White House</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#artificial intelligence`, `#regulation`, `#technology policy`, `#U.S. politics`

---

<a id="item-14"></a>
## [Apple distills Google Gemini for on-device iPhone AI](https://www.aibase.com/zh/news/26568) ⭐️ 8.0/10

Per a March 25, 2026 disclosure, Apple has gained full access to Google's full-size Gemini model via a deep cooperation agreement, and uses knowledge distillation to transfer Gemini's capabilities into a small lightweight model that can run locally on iPhones. This distilled model will be used to improve native iOS AI applications like Siri in future iOS updates. This move shifts mobile AI competition from cloud parameter size races to on-device execution efficiency, and balances cutting-edge AI capability with improved user privacy and faster response speeds for mobile consumers. It also sets a new precedent for leveraging third-party large models to accelerate on-device AI deployment. Apple is pursuing a dual strategy of short-term reliance on distilled Gemini to quickly improve on-device AI, while continuing independent research and development of its own Apple Foundation Models for long-term AI autonomy. The distilled small model can maintain performance close to the full-size Gemini while requiring far less computing power to run locally.

telegram · AI_News_CN · Mar 26, 02:02

**Background**: Knowledge distillation is an AI model compression technique that follows a teacher-student framework, where a large, powerful 'teacher' model transfers its learned knowledge to a smaller 'student' model, allowing the small model to retain most of the original model's capability at a much smaller size. On-device AI refers to AI processing that runs directly on end-user hardware like mobile phones instead of sending data to cloud servers for computation, which offers faster responses and better user privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.csdn.net/weixin_43694096/article/details/127505946">一文搞懂【知识蒸馏】【Knowledge Distillation】算法原理_知识蒸馏算... 让小模型也能深度思考：推理知识蒸馏（Knowledge Distillation for Re... 知识蒸馏_百度百科 知识蒸馏原理分类方法及Hinton经典算法解读-开发者社区-阿里云 知识蒸馏研究综述 - ict.ac.cn 【AI系统】知识蒸馏原理 - ZOMI酱酱 - 博客园</a></li>
<li><a href="https://ssshooter.com/kitten-large-language-model-6/">小猫都能懂的 大 模 型 原 理 6 - 模 型 优化 • Usubeni Fantasy</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1935796159261148086">知识蒸馏（Knowledge Distillation）：一篇从核心原理到前沿应用的完...</a></li>

</ul>
</details>

**Tags**: `#On-device AI`, `#Knowledge Distillation`, `#Large Language Model`, `#Apple`, `#Gemini`

---

<a id="item-15"></a>
## [Hacker runs Model 3 computer on desktop from crashed car parts](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 7.0/10

A technical blog post published March 23, 2026 details how a researcher reverse engineered and successfully booted a Tesla Model 3 infotainment computer on a desktop using salvaged parts from crashed Tesla vehicles. The project sparked over 120 community comments on Hacker News covering automotive electronics and related topics. This project expands public knowledge of Tesla automotive hardware and software, and advances open reverse engineering work that can help improve automotive cybersecurity research and after-market modification accessibility. It also shines a light on Tesla's bug bounty program structure for root access research. Tesla offers a permanent SSH root certificate for researchers' personal vehicles as part of its bug bounty program, awarded to researchers who submit at least one valid rooting vulnerability, similar to Apple's Security Research Device Program. Other community members have already gotten Tesla's Qt-based QtCar UI software running in the QEMU emulator when the correct firmware is available.

hackernews · driesdep · Mar 25, 21:11

**Background**: Reverse engineering of automotive electronics involves pulling apart and understanding how a vehicle's internal computer systems work, a practice that is core to automotive security research and after-market vehicle modifications. Tesla runs a public bug bounty program hosted on Bugcrowd that pays security researchers for reporting valid security vulnerabilities in its systems.

<details><summary>References</summary>
<ul>
<li><a href="https://bugcrowd.com/tesla">Bug Bounty: Tesla | Bugcrowd</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Model_3">Tesla Model 3 - Wikipedia</a></li>
<li><a href="https://undercodetesting.com/unlock-hardware-hacking-secrets-free-uart-course-essential-tool-guide-video/">Unlock Hardware Hacking Secrets: Free UART... - Undercode Testing</a></li>

</ul>
</details>

**Discussion**: Community commenters found Tesla's root access qualification program interesting, noting it strikes a good balance between enabling research and controlling access similar to Apple's program. Multiple commenters shared their own related experiences, from testing disconnected ECUs to modifying Tesla vehicles and noting shared common hardware interfaces like LVDS.

**Tags**: `#reverse engineering`, `#automotive electronics`, `#Tesla`, `#hardware hacking`

---

<a id="item-16"></a>
## [Hacker News debate on EU Chat Control push](https://fightchatcontrol.eu/?foo=bar) ⭐️ 7.0/10

The EU is continuing to push for new legislation that would allow scanning of private user messages and photos, sparking a high-engagement discussion on Hacker News featuring input from the creator of the Fight Chat Control advocacy campaign. This legislation would fundamentally reshape digital privacy protections for all EU residents, as it would require messaging providers to bypass end-to-end encryption for content scanning, setting a major precedent for government-mandated mass digital surveillance. The current push comes after trilogue negotiations between EU institutions failed when the Council refused to compromise on replacing blanket mass surveillance with targeted, judicially-approved monitoring of suspects, putting the original temporary regulation at risk of lapsing.

hackernews · MrBruh · Mar 25, 20:27

**Background**: The EU regulation officially called the Regulation to Prevent and Combat Child Sexual Abuse (CSAR), is commonly nicknamed Chat Control by its critics. It was first proposed by the European Commission in 2022, with critics referring to updated versions as Chat Control 2.0, and Fight Chat Control is a grassroots advocacy campaign organized to oppose the legislation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.politico.eu/article/one-man-spam-campaign-ravages-eu-chat-control-bill-fight-chat-control/">One-man spam campaign ravages EU 'Chat Control' bill</a></li>
<li><a href="https://edri.org/our-work/chat-control-what-is-actually-going-on/">Chat Control: What is actually going on? - European Digital ...</a></li>

</ul>
</details>

**Discussion**: Community discussion is largely opposed to the proposed surveillance regulation, with one participant questioning why there is no proactive legislation to enshrine the right to private communications, while others shared heuristics to evaluate the proposal and voiced broader criticism of rising surveillance in the EU.

**Tags**: `#digital privacy`, `#EU regulation`, `#mass surveillance`, `#chat control`

---

<a id="item-17"></a>
## [Critique of rushed AI agent code generation](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Experienced software engineer and Pi agent framework creator Mario Zechner published a critique of the modern agentic AI code generation trend, which was amplified by developer Simon Willison in a March 25, 2026 blog post. Zechner argues that removing the human coding bottleneck lets AI agent mistakes accumulate at unsustainable rates, and calls for slowing development to enforce discipline. This commentary highlights an underdiscussed risk of the current industry rush to adopt autonomous AI coding agents, pointing to long-term problems with unmaintainable, mistake-ridden codebases that affect all software teams working with generative AI. It pushes the industry to re-evaluate the tradeoff between development speed and code quality as AI-powered coding becomes mainstream. Zechner recommends limiting daily AI-generated code output to match human review capacity and writing all core architectural and API code by hand, while Simon Willison disagrees with the hand-writing requirement but agrees that new discipline is needed to balance speed and thoroughness.

rss · Simon Willison · Mar 25, 21:47

**Background**: Agentic AI refers to autonomous AI systems that can plan, complete tasks, and write code with minimal continuous human oversight. Agentic engineering is the emerging discipline of building software using these autonomous AI coding agents, which has grown rapidly in popularity alongside improvements in large language model capabilities. Cognitive debt describes the future maintenance and comprehension cost created by rushing development and cutting corners on clear, intentional code design.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>
<li><a href="https://db0.ai/docs/pi">Persistent memory extension for the Pi coding agent . | db0.ai</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software development`, `#AI code generation`, `#industry commentary`

---

<a id="item-18"></a>
## [NASA adjusts Artemis plan, pauses Gateway for lunar base](https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/) ⭐️ 7.0/10

NASA has announced a major strategic adjustment to its Artemis lunar exploration program, suspending the original Gateway lunar orbital station program to refocus on building a permanent lunar surface base by 2029. It also plans a 2028 nuclear-powered propulsion demonstration mission to Mars and will accelerate commercial lunar landing missions. This major shift changes the core focus of NASA's Artemis program, accelerating human return to the lunar surface and influencing the development direction of global lunar exploration. It also pushes forward the development of nuclear propulsion technology that is critical for future deep space exploration to Mars and beyond. Under the new plan, NASA will conduct at least one lunar landing per year, and after Artemis V it aims to achieve one crewed lunar landing mission every six months by increasing commercial procurement and adopting reusable hardware. NASA also plans to launch 30 robotic lunar landing missions starting from 2027 under its accelerated commercial lunar payload service program.

telegram · zaihuapd · Mar 25, 04:30

**Background**: The Artemis program is NASA's ongoing human lunar exploration initiative, and Artemis V is the fourth crewed mission of the program, originally scheduled to deliver components to the Gateway lunar orbital station. Gateway was planned as a multinational cooperative small space station in lunar orbit that would serve as a hub for Artemis surface missions and deep space exploration. Nuclear electric propulsion is a deep space propulsion technology that uses a nuclear reactor to generate electricity to drive electric thrusters, which offers far higher energy efficiency than traditional chemical propulsion for long-distance missions.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/月球门户">月球门户 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/wiki/核电火箭">核电火箭 - 维基百科，自由的百科全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artemis_V">Artemis V</a></li>

</ul>
</details>

**Tags**: `#space exploration`, `#NASA`, `#lunar program`, `#aerospace engineering`

---

<a id="item-19"></a>
## [AI short dramas displace Hengdian extras](https://www.aibase.com/zh/news/26559) ⭐️ 7.0/10

Rising adoption of low-cost AI-generated short dramas is displacing large numbers of extras and supporting actors at major Chinese production hubs including Hengdian, and has cut the pay of top short drama actors by half. As of January 2026, AI-generated short dramas already account for 38% of China's top 100 ranked manga-style short dramas, up from just 7% one year prior. This disruption represents one of the first large-scale impacts of generative AI on blue-collar creative labor, and is rapidly reshaping the economics and production model of the global short-form content industry. The explosive growth of low-cost AI content is also opening up the short drama market to far more producers while drastically lowering entry barriers. A full high-quality AI short drama can be produced for under 200,000 yuan, compared to 1.5 to 3 million yuan for an equivalent traditional live-action short drama, and per-episode costs can drop as low as 500 yuan. One major platform projects it will reach a monthly production capacity of 150 AI short dramas by March 2026, a rate impossible for traditional live-action production teams.

telegram · AI_News_CN · Mar 26, 01:21

**Background**: Hengdian World Studios is China's largest film and television production hub, and has long relied on a large workforce of background extras and supporting actors to supply the country's massive entertainment production industry. Short dramas are a popular, fast-growing vertical short-form content format that typically run 1 to 3 minutes per episode, designed for mobile binge-watching. AI-generated short dramas use generative AI tools to automatically create character visuals, lip-sync, and scene footage, replacing large portions of on-location filming and human acting work.

<details><summary>References</summary>
<ul>
<li><a href="https://variety.com/2026/digital/news/short-form-video-ai-generated-dramas-filmart-1236692132/">How Short-Form Video, AI-Generated Dramas Power Global Content</a></li>
<li><a href="https://ktla.com/business/press-releases/globenewswire/9361091/skyreels-open-sources-the-worlds-first-human-centric-video-foundation-model-for-ai-short-drama-creation-skyreels-v1-reshaping-the-ai-short-drama-landscape">SkyReels Open Sources the World's First Human-Centric Video ...</a></li>
<li><a href="https://news.futunn.com/en/post/69843567/the-ai-short-drama-huo-qubing-has-gained-popularity-discussions">The AI short drama 'Huo Qubing' has gained popularity! Discussions arise over production costs and viewership. How far along is the industrialization of AI manga dramas?</a></li>

</ul>
</details>

**Tags**: `#AI for content creation`, `#industry disruption`, `#AI impact on labor`, `#digital media`, `#generative AI`

---

<a id="item-20"></a>
## [Kuaishou Ke Ling grows after OpenAI Sora shutdown](https://www.aibase.com/zh/news/26560) ⭐️ 7.0/10

On the same day OpenAI wound down its Sora text-to-video model on March 25 2026, Kuaishou announced that its domestic Ke Ling AI video generation model has earned strong early commercial results, and set a 100% year-over-year revenue growth target for 2026. Kuaishou also plans to increase its 2026 total capital expenditure to 26 billion yuan, mostly for Ke Ling's AI infrastructure. This news proves that profitable commercialization of large generative AI video models is achievable outside of OpenAI's high-cost development path, and shifts the global generative AI video race from technical demonstration to sustainable profitability. It also marks a major milestone for Chinese large model commercialization. In Q4 2025, Ke Ling AI generated 340 million yuan in revenue, with December 2025 revenue exceeding 20 million USD, and its annualized revenue run rate topped 300 million USD as of January 2026. Unlike Sora, which struggled with unsustainable high development and running costs, Ke Ling pursues a lower-barrier, rapid multi-scenario penetration strategy to grow revenue faster than costs.

telegram · AI_News_CN · Mar 26, 01:21

**Background**: Sora was OpenAI's high-profile text-to-video generation model that was shut down in March 2026 less than two years after its launch, mainly due to unsustainable high development and operating costs and internal product streamlining. Ke Ling (also called Kling AI) is Kuaishou's domestic Chinese text-to-video generation model, which can generate 1080p 30fps videos with improved motion smoothness. Annualized revenue run rate (ARR) is a financial metric that extrapolates current short-term revenue to estimate full-year annual revenue.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c3w3e467ewqo">Sora: OpenAI closes AI video app and cancels $1bn Disney deal</a></li>
<li><a href="https://skywork.ai/blog/keling-ai-2-5-turbo-hands-on-test-40-improvement-in-smoothness-realistic-light-and-shadow-even-ordinary-users-can-create-cinematic-grade-ai-videos/">Keling AI 2.5 Turbo Hands-On Test: 40% Improvement in... - Skywork ai</a></li>
<li><a href="https://www.linkedin.com/posts/mikelingle_whats-the-difference-between-run-rate-and-activity-7170760249753210880-J4La">What's the difference between Run Rate and ARR ? Both Run Rate ...</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#text-to-video model`, `#AI commercialization`, `#large language model`, `#Chinese AI`

---

<a id="item-21"></a>
## [Amap adds OpenClaw-compatible AI agent skills](https://www.aibase.com/zh/news/26567) ⭐️ 7.0/10

On March 25, 2026, Amap Open Platform announced it has packaged its map capabilities into standardized OpenClaw-compatible Skills and published them on ClawHub for all developers and end users. This integration marks a shift from traditional API-based geospatial services to natural language-driven AI agent interactions, lowering development barriers and accelerating the geospatial industry's integration into the AI agent ecosystem. The released Skills cover daily life and office geospatial assistants as well as a map website generation tool, cutting POI application development time from days to minutes and letting AI generate customized travel itineraries in seconds from natural language prompts.

telegram · AI_News_CN · Mar 26, 01:45

**Background**: OpenClaw is a free open-source AI agent framework that allows developers to build AI-powered automations on their own infrastructure. ClawHub is an open skill registry and marketplace for OpenClaw that supports version management and vector search for agent skills. AI agent Skills are pre-packaged reusable capabilities that let AI agents add new functionality without requiring retraining of the underlying large language model.

<details><summary>References</summary>
<ul>
<li><a href="https://openclaw-ai.dev/">OpenClaw AI — Skills, Templates & Agent Showcase</a></li>
<li><a href="https://grokipedia.com/page/ClawHub">ClawHub</a></li>
<li><a href="https://github.com/heilcheng/awesome-agent-skills">GitHub - heilcheng/awesome-agent-skills: A curated list of ...</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Geographic Information Service`, `#Location-Based Services`, `#Large Language Models`

---

<a id="item-22"></a>
## [Tongyi Qianwen enters Hongqi mass production cars](https://www.aibase.com/zh/news/26570) ⭐️ 7.0/10

Alibaba's Tongyi Qianwen general-purpose AI assistant has been integrated into Hongqi Motors' smart cockpit as of March 26, 2025, and will first launch on the Hongqi HS6 PHEV. This integration marks the first time a full general-purpose AI assistant has entered mass production automotive scenarios in China. This deployment advances in-vehicle AI from single-function responses to end-to-end proactive travel services, opening up new practical application scenarios for general large language models. It also pushes Alibaba forward in its strategy of building a cross-device, full-scene general AI assistant that spans multiple hardware terminals. The system can identify multiple ambiguous user intentions from a single natural voice query, break down and arrange tasks via cloud-based multi-Agent collaborative decision-making, then link with on-car applications to execute the plan. In the future, more Alibaba ecosystem services including instant retail and ticket booking will be added to expand in-vehicle service capabilities.

telegram · AI_News_CN · Mar 26, 02:13

**Background**: Tongyi Qianwen (also called Qwen) is a family of open large language models developed by Alibaba Cloud, trained on up to 3 trillion tokens of multilingual data covering multiple domains. Multi-agent collaborative decision-making is an AI framework that lets multiple independent AI agents work together to complete complex tasks that are difficult for a single model to handle, and it has been widely explored for use in automotive and travel scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2503.13415">[2503.13415] A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives</a></li>
<li><a href="https://github.com/QwenLM/Qwen">GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#In-vehicle AI`, `#Smart Cockpit`, `#AI Assistant`, `#Large Language Model`

---

<a id="item-23"></a>
## [OpenAI invests in AI agent startup Isara](https://www.aibase.com/zh/news/26572) ⭐️ 7.0/10

OpenAI has secretly invested in Isara, a San Francisco-based startup founded in June 2024 by two 23-year-old AI researchers, Eddie Zhang and Henry Gasztowtt. Isara is developing software architecture to coordinate thousands of collaborating AI agents to solve large complex industrial problems. This investment signals industry endorsement of the multi-agent collaboration approach, which is widely viewed as a key step toward advancing artificial general intelligence and unlocking new AI applications in heavy industry sectors. It could open a new direction for AI development that focuses on coordinated agent work rather than just scaling single model size. According to public reporting, Isara has raised a total of $94 million at a $650 million valuation, and it has already hired more than ten top researchers from Google, Meta and OpenAI since its founding less than a year ago.

telegram · AI_News_CN · Mar 26, 02:26

**Background**: An AI agent is an autonomous entity that perceives its environment and takes actions to achieve set goals, and a multi-agent system is a framework that coordinates multiple AI agents to collaborate on shared tasks. Distributed artificial intelligence, the research field behind large-scale multi-agent systems, studies how decentralized groups of agents can work together to solve problems that are too complex for a single large model.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techmeme.com/260325/p44">Isara, which aims to build software that can coordinate the ...</a></li>
<li><a href="https://www.ibm.com/think/topics/multiagent-system">What is a Multi-Agent System? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_agent">Intelligent agent - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#OpenAI`, `#startup funding`, `#artificial general intelligence`

---

<a id="item-24"></a>
## [Apifox SaaS JS tampering security alert](https://mp.weixin.qq.com/s/GpACQdnhVNsMn51cm4hZig?scene=0&subscene=90) ⭐️ 7.0/10

Apifox has issued an official risk warning and upgrade announcement, confirming that an external JavaScript file dynamically loaded by its public network SaaS version desktop client was maliciously tampered with in a supply chain attack. The attack affected users who used the affected service between March 4, 2026 and March 22, 2026, and the company urges all affected users to upgrade to fix the issue. Apifox is a widely used collaborative API development platform, so this incident exposes a critical supply chain attack vector that threatens sensitive developer and enterprise data. This alert requires immediate attention from all users of Apifox's public cloud SaaS version to avoid information leakage or further malicious activity. Only the public network SaaS version of Apifox is affected by this incident, and other deployment versions such as independent private deployment are not impacted. Users who accessed the service between March 4 and March 22, 2026 face potential sensitive information leakage risks.

telegram · AI_News_CN · Mar 26, 02:43

**Background**: Apifox is an all-in-one collaborative API development platform that combines API documentation, debugging, mocking, and automated testing capabilities, widely used by developers around the world. SaaS is a cloud-based software delivery model where the provider hosts the service on public cloud infrastructure, and users access it over the internet without managing underlying infrastructure. A JavaScript file tampering supply chain attack targets third-party external resources loaded by legitimate software, allowing attackers to inject malicious code to steal data or perform other harmful actions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.v2ex.com/t/1201146">Apifox 遭受供应链攻击 - V2EX</a></li>
<li><a href="https://github.com/apifox/apifox">GitHub - apifox/apifox: Apifox = Postman + Swagger + Mock + JMeter。Apifox 官网：https://www.apifox.cn/</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/328295460">了解一下，什么是SaaS部署?什么又是独立部署呢? - 知乎</a></li>

</ul>
</details>

**Tags**: `#Security Alert`, `#JavaScript Tampering`, `#Supply Chain Security`, `#Apifox`, `#SaaS`

---