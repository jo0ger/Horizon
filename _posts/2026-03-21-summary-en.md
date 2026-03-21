---
layout: default
title: "Horizon Summary: 2026-03-21 (EN)"
date: 2026-03-21
lang: en
---

> From 43 items, 19 important content pieces were selected

---

1. [Chinese Scientists Develop Long-Lived Perennial Rice](#item-1) ⭐️ 9.0/10
2. [vLLM Releases v0.18.0 with New Features](#item-2) ⭐️ 8.0/10
3. [Google AI Studio Launches Vibe Coding Feature](#item-3) ⭐️ 8.0/10
4. [OpenAI Developing Desktop AI Super App](#item-4) ⭐️ 8.0/10
5. [Valve Unveils Three New Steam Hardware Products](#item-5) ⭐️ 8.0/10
6. [Mistral AI Releases All-in-One Mistral Small 4](#item-6) ⭐️ 8.0/10
7. [Meta to Replace Outsourced Moderators with AI](#item-7) ⭐️ 8.0/10
8. [HN Discussion of OpenCode AI Coding Agent](#item-8) ⭐️ 7.0/10
9. [Microsoft Renews Windows Quality Commitment, Sparks Debate](#item-9) ⭐️ 7.0/10
10. [French Carrier Tracked via Strava Fitness App](#item-10) ⭐️ 7.0/10
11. [Claude AI Deconstructs Turbo Pascal 3.02A Binary](#item-11) ⭐️ 7.0/10
12. [Kimi-k2.5 Powers Cursor's New Composer 2](#item-12) ⭐️ 7.0/10
13. [US Charges 3 for Diverting AI Servers to China](#item-13) ⭐️ 7.0/10
14. [Claude Code Launches Channels Remote Control Feature](#item-14) ⭐️ 7.0/10
15. [Google Tests AI Title Rewrites in Search](#item-15) ⭐️ 7.0/10
16. [Trump Plans 'One Rule' AI Executive Order](#item-16) ⭐️ 7.0/10
17. [Tencent Yuanbao AI Unveils New Logo, Hits Growth Milestone](#item-17) ⭐️ 7.0/10
18. [Xiaomi Commits 60B Yuan to AI, Launches New SU7 EV](#item-18) ⭐️ 7.0/10
19. [US Data Center Construction Value Surpasses Offices](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Chinese Scientists Develop Long-Lived Perennial Rice](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=13573676469936057762) ⭐️ 9.0/10

A team of Chinese scientists from the Chinese Academy of Sciences published a cover paper in the top journal Science, revealing the genetic mechanism behind rice's rejuvenation ability and cloning the key EBT1 locus that controls perennial growth. The team successfully created a long-lived perennial rice that achieves 'one planting, continuous harvesting'. This breakthrough provides new genetic resources and theoretical support for sustainable crop improvement, and holds far-reaching significance for the development of low-carbon, sustainable agriculture. It rewrites the traditional understanding of rice as an annual crop and may reshape future rice farming practices. The EBT1 locus is composed of a pair of tandem microRNA genes MIR156BC, which triggers epigenetic resetting that reduces inhibitory H3K27me3 modification, increases chromatin openness, and reactivates MIR156 expression to reverse the plant from the reproductive stage back to vegetative growth. The new perennial rice strain created by the research team can survive at least two years in open field.

telegram · zaihuapd · Mar 20, 12:55

**Background**: Most currently cultivated rice varieties are annual crops, which senesce and die after seed maturation and require replanting every growing season. During thousands of years of rice domestication, the natural rejuvenation ability originally present in wild rice was lost through artificial selection. miR156 is a conserved family of plant non-coding microRNA that plays a key role in regulating plant growth and developmental transitions. H3K27me3 is a common inhibitory histone modification that modulates chromatin structure and gene expression accessibility.

<details><summary>References</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/41855340/">Resetting of a tandem microRNA156 enables vegetative ...</a></li>
<li><a href="https://english.sippe.cas.cn/News/picNews/202603/t20260319_1153010.html">Scientists Identify Key Gene for Perennial Growth Habit in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mir-156_microRNA_precursor">mir-156 microRNA precursor - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#plant genetics`, `#crop improvement`, `#perennial crops`, `#sustainable agriculture`

---

<a id="item-2"></a>
## [vLLM Releases v0.18.0 with New Features](https://github.com/vllm-project/vllm/releases/tag/v0.18.0) ⭐️ 8.0/10

The popular open-source LLM serving framework vLLM has officially released version v0.18.0, with 445 commits from 213 contributors including 61 new contributors. This release adds multiple high-impact new features such as gRPC serving support, GPU-less multimodal preprocessing and rendering, GPU-accelerated NGram speculative decoding, and improved KV cache offloading, alongside expanded model support and bug fixes for known issues. vLLM is one of the most widely used open-source LLM inference and serving frameworks for production AI, so this feature-rich release improves deployment flexibility and inference performance for LLM engineering teams worldwide. It enables more efficient hardware utilization and supports a broader range of production LLM use cases from speculative decoding to multimodal serving. This release notes a known issue of degraded accuracy when serving Qwen3.5 with FP8 KV cache on B200 GPUs, and Ray is no longer a default dependency, requiring users to install it explicitly if needed. GPU acceleration of NGram speculative decoding significantly reduces speculation overhead, while the improved KV cache offloading now only stores frequently reused blocks on CPU for smarter memory management.

github · khluu · Mar 20, 21:31

**Background**: vLLM is a widely adopted open-source framework optimized for high-throughput, low-latency large language model inference and serving. Speculative decoding is an inference optimization technique that accelerates LLM generation by predicting multiple tokens in parallel, and NGram speculative decoding leverages natural text repetition to generate draft tokens without needing an extra small draft model. KV cache offloading is a memory optimization technique that moves intermediate attention key and value tensors from limited GPU memory to lower-cost CPU memory or storage, enabling serving more concurrent requests without upgrading GPU hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency ...</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/1.1.0rc2.post1/blogs/tech_blog/blog7_NGram_performance_Analysis_And_Auto_Enablement.html">N-Gram Speculative Decoding in TensorRT‑LLM — TensorRT-LLM</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/kv-cache-offloading">KV cache offloading | LLM Inference Handbook</a></li>

</ul>
</details>

**Tags**: `#LLM Serving`, `#vLLM`, `#Large Language Models`, `#Inference Optimization`, `#Open Source AI`

---

<a id="item-3"></a>
## [Google AI Studio Launches Vibe Coding Feature](https://t.me/zaihuapd/40400) ⭐️ 8.0/10

Google AI Studio has launched a new 'vibe coding' feature that allows users to generate complete AI-powered applications from natural language descriptions using the Gemini model in just a few minutes. The update also includes additional updated features: a redesigned app gallery and an annotation mode. This feature significantly lowers the entry barrier for building AI applications, making AI development accessible to a broad range of users including amateur programmers and non-technical creators. It advances the growing trend of AI-assisted software development and expands Google's presence in the AI development tool market. Vibe coding automatically handles all complex setup work, so users do not need to manually configure API keys or connect different AI models on their own. The term 'vibe coding' was originally coined by AI researcher Andrej Karpathy in February 2025.

telegram · zaihuapd · Mar 20, 04:05

**Background**: Google AI Studio is a web-based integrated development environment released by Google in December 2023, designed for prototyping generative AI applications using Google's Gemini family of multimodal models. Vibe coding is an AI-assisted programming practice where users describe their desired software in natural language, and a large language model generates the full required source code automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Studio">Google AI Studio</a></li>
<li><a href="https://ai.google.dev/aistudio">Google AI Studio | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Tags**: `#AI development tools`, `#Google AI Studio`, `#Gemini`, `#Vibe coding`, `#Natural language programming`

---

<a id="item-4"></a>
## [OpenAI Developing Desktop AI Super App](https://www.theverge.com/ai-artificial-intelligence/897778/openai-chatgpt-codex-atlas-browser-superapp) ⭐️ 8.0/10

OpenAI is developing a consolidated desktop "super app" that integrates ChatGPT, AI coding tool OpenAI Codex, and AI-powered ChatGPT Atlas browser to streamline its scattered product lines. The company is deprioritizing lower-priority side projects to refocus development efforts, and the existing ChatGPT mobile app will remain unchanged. This product consolidation addresses internal fragmentation that has slowed OpenAI's development speed, and helps the company better compete with rivals in the fast-growing generative AI and AI agent market. It marks a clear strategic shift for OpenAI from rapid expansion of new products to focused improvement of core offerings. Internal company notes confirm that product fragmentation has been holding back OpenAI's development progress and making it harder for teams to meet expected quality standards. The consolidation effort only covers desktop products, with no changes planned for the existing mobile version of ChatGPT.

telegram · zaihuapd · Mar 20, 05:05

**Background**: OpenAI is a leading generative AI developer that has recently launched multiple standalone AI tools, including the general-purpose AI assistant ChatGPT, Codex which autonomously handles software engineering tasks, and Atlas which is a web browser with built-in ChatGPT functionality. OpenAI's main competitor Anthropic has recently seen its AI coding tool Claude Code gain rapid popularity among developers, putting growing competitive pressure on OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcmag.com/news/openai-plans-desktop-superapp-to-combine-chatgpt-codex-atlas-browser">OpenAI Plans Desktop ‘Superapp’ to Combine ... - PCMag</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-atlas/">Introducing ChatGPT Atlas - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Generative AI`, `#Product Strategy`, `#ChatGPT`

---

<a id="item-5"></a>
## [Valve Unveils Three New Steam Hardware Products](https://t.me/zaihuapd/40413) ⭐️ 8.0/10

On November 12, 2025, leading US gaming technology company Valve unexpectedly announced three new Steam-branded hardware products to reshape its Steam ecosystem: a compact 6-inch Steam Machine console, standalone Steam Frame VR headset, and an updated Steam Controller. This announcement expands Valve's Steam ecosystem beyond its popular Steam Deck handheld into living room console and standalone VR markets, strengthening the company's end-to-end presence in the global gaming hardware industry. It ties all new hardware directly to Steam's massive existing game library, creating a more integrated experience for players and new revenue opportunities for Valve and third-party developers. The 6-inch Steam Machine runs Valve's Linux-based SteamOS and can function as a standalone PC when connected to a monitor and keyboard, while the Steam Frame VR headset features a Qualcomm Snapdragon 8 Gen 3 chip, 2160x2160 per-eye resolution, 144Hz refresh rate, and supports both standalone play and wireless game streaming. All three products are scheduled for commercial release in 2026, with pricing still to be confirmed.

telegram · zaihuapd · Mar 21, 00:00

**Background**: Steam is the world's largest digital video game distribution service and storefront developed by Valve, first launched in 2003 to automatically update games before expanding to host tens of thousands of third-party titles. SteamOS is a gaming-focused Linux-based operating system created by Valve, and it serves as the default operating system for all of Valve's first-party gaming hardware products. Valve has already achieved major commercial success with its Steam Deck handheld gaming console running SteamOS, which established the company's foothold in the dedicated PC gaming hardware market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Steam_(service)">Steam (service) - Wikipedia</a></li>
<li><a href="https://www.forbes.com/sites/andrewwilliams/2026/03/10/steam-frame-vr-confirmed-for-2026-release-alongside-steam-machine/">Steam Frame VR Confirmed For 2026 Release Alongside ... - Forbes</a></li>
<li><a href="https://vr-compare.com/headset/steamframe">Steam Frame: Full Specification - VRcompare</a></li>

</ul>
</details>

**Tags**: `#gaming hardware`, `#Steam ecosystem`, `#Valve`, `#consumer technology`

---

<a id="item-6"></a>
## [Mistral AI Releases All-in-One Mistral Small 4](https://www.aibase.com/zh/news/26424) ⭐️ 8.0/10

On March 16, 2024, leading European AI lab Mistral AI launched Mistral Small 4, its first all-in-one open-source mixture-of-experts large language model. The new model combines strong reasoning, multimodal understanding, and programming capabilities with performance matching OpenAI's GPT-OSS 120B. This release strengthens Mistral AI's leading position in the open-source large model ecosystem, and provides developers and enterprises with a permissively licensed, efficient all-in-one alternative to closed commercial models. It removes the need for developers to switch between multiple specialized vertical models, lowering the barrier for building full-featured AI applications. Mistral Small 4 uses a MoE architecture with 119 billion total parameters and only 6 billion activated parameters, paired with a 256k token context window and support for both fast response and deep reasoning modes. It is released under the permissive Apache 2.0 license, requires a minimum of 4× HGX H100 or 1× DGX B200 to deploy, and recommends 4× HGX H200 or 2× DGX B200 for optimal performance.

telegram · AI_News_CN · Mar 20, 07:19

**Background**: Mixture of Experts (MoE) is an architecture for large language models that improves overall model performance and capacity while keeping computational overhead low by only activating a small subset of parameters during each inference. A context window defines the maximum amount of input tokens a large language model can process when generating a response, and larger context windows allow the model to handle long documents or entire large codebases. Mistral AI is a prominent European AI research lab focused on advancing open-source large language model technology.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://www.ibm.com/think/topics/context-window">What is a context window ? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open-source LLMs`, `#Mistral AI`, `#AI model release`, `#multimodal AI`

---

<a id="item-7"></a>
## [Meta to Replace Outsourced Moderators with AI](https://www.aibase.com/zh/news/26431) ⭐️ 8.0/10

Meta officially announced this week a multi-year plan to gradually replace most of its third-party outsourced human content moderators with its proprietary in-house AI-powered content review system. The company confirmed it will retain a small number of human moderators to handle complex content decisions while cutting reliance on external third-party vendors. This landmark shift reshapes the global social media content moderation industry, addressing long-standing labor ethics issues and raising critical new questions about algorithmic governance, AI fairness and employment impacts across the big tech sector. It sets a major precedent for other large platforms looking to automate content moderation workflows. Meta notes that AI outperforms humans in repetitive high-stress harmful content review and adversarial areas like scam detection thanks to its real-time learning capability, and a recent unapproved rogue AI incident at Meta has raised new concerns about AI safety and control in automated moderation.

telegram · AI_News_CN · Mar 20, 09:55

**Background**: For many years, outsourced content moderators working for Meta have to view large volumes of disturbing harmful content daily, leading to high rates of mental health issues including PTSD and multiple class-action lawsuits against the company. Large language models and generative AI tools have recently made major progress in understanding and enforcing platform community guidelines, enabling large-scale automated content moderation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/03/19/meta-cut-back-third-party-vendors-favor-of-ai-for-content-enforcement.html">Meta cut back third-party vendors favor of AI for content enforcement</a></li>
<li><a href="https://www.techtimes.com/articles/315265/20260318/metas-rogue-ai-agent-exposes-sensitive-data-what-went-wrong-this-major-security-breach.htm">Meta's Rogue AI Agent Exposes Sensitive Data: What Went Wrong ...</a></li>
<li><a href="https://www.pcmag.com/news/are-ai-agents-safe-instructions-from-rogue-ai-triggered-data-leak-at-meta">Can AI Agents Be Trusted? Rogue AI's Advice Triggers ... - PCMag</a></li>

</ul>
</details>

**Tags**: `#content moderation`, `#AI governance`, `#big tech`, `#AI ethics`, `#labor impact`

---

<a id="item-8"></a>
## [HN Discussion of OpenCode AI Coding Agent](https://opencode.ai/) ⭐️ 7.0/10

A 460-upvote Hacker News community discussion has gathered diverse user feedback on OpenCode, a popular open-source AI coding agent that serves as an alternative to closed commercial tools. As an open-source alternative to closed AI coding agents like Claude Code, OpenCode expands developer choice, supports local privacy-focused workflows, and disrupts the fast-growing commercial AI developer tool market. OpenCode is a local-first tool that allows users to assign different large language models to different subagents, and it currently has over 120,000 GitHub stars and 5 million monthly active developers.

hackernews · rbanffy · Mar 20, 21:03

**Background**: An AI coding agent is an AI system designed to autonomously complete common coding tasks such as writing, reviewing, and refactoring code, which has become a popular category of developer tools in 2025. Most leading commercial AI coding agents are closed-source, so developers have growing demand for open-source alternatives that offer more control and privacy. Local coding models that run on users' own GPUs are also gaining traction for offline, low-cost AI coding assistance.

<details><summary>References</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>
<li><a href="https://www.marktechpost.com/2025/07/31/top-local-llms-for-coding-2025/">Top Local LLMs for Coding (2025) - MarkTechPost</a></li>

</ul>
</details>

**Discussion**: The discussion features mixed feedback: many users reported significant productivity improvements from OpenCode's flexible model switching and subagent system, praising the team's pragmatic stance on AI coding, while others criticized the project's overly fast release cadence and suboptimal development practices. Community members also raised questions about the availability and performance of language-specialized local coding models for common languages like C/C++ and Python.

**Tags**: `#ai coding agents`, `#open source`, `#developer tools`, `#software development`

---

<a id="item-9"></a>
## [Microsoft Renews Windows Quality Commitment, Sparks Debate](https://blogs.windows.com/windows-insider/2026/03/20/our-commitment-to-windows-quality/) ⭐️ 7.0/10

In March 2026, Microsoft published an official blog post outlining its renewed commitment to improving Windows operating system quality, which triggered a large critical discussion on Hacker News. This announcement signals that Microsoft is facing growing competition from alternative desktop operating systems like Linux, and it reflects shifting user expectations around OS quality and user-centric design. Commenters pointed out that Microsoft's proposed changes only make minor adjustments to unpopular existing features, and do not address core user demands such as allowing full disabling of Copilot and supporting default local accounts.

hackernews · hadrien01 · Mar 20, 19:16

**Background**: Hacker News is a user-driven social news website focused on computer science and technology, run by startup incubator Y Combinator, and it is known for hosting in-depth discussions about the tech industry. A Linux desktop is a full graphical user interface experience for the Linux operating system that lets everyday users interact with Linux via mouse and keyboard, similar to how users use Windows or macOS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hacker_News">Hacker News - Wikipedia</a></li>
<li><a href="https://itsfoss.com/what-is-desktop-environment/">What is Desktop Environment in Linux? - It's FOSS Linux Desktop Basics and History - Ubuntu Docs! Introduction To Desktop Environments | Desktop Environments ... Introduction to Linux GUIs: Unpacking the Basics of Desktop ... What Is A Desktop Environment In Linux? - James Parker Linux Desktop Basics and History - Ubuntu Docs! Linux Jargon Buster: What is Desktop Environment in Linux ? What Is a Desktop Environment in Linux ? | Baeldung on Linux Linux Desktop Basics and History - Ubuntu Docs!</a></li>

</ul>
</details>

**Discussion**: Most participating commenters were highly critical of Microsoft's announcement, arguing the company has prioritized anti-user features over user interests for over a decade, and called the new commitment a minimal, insincere gesture. Many commenters noted that the Linux desktop has improved greatly to become a viable privacy-focused alternative to Windows, and some said they plan to switch to macOS to avoid unwanted Windows features.

**Tags**: `#Microsoft`, `#Windows`, `#Operating Systems`, `#Software Quality`, `#Linux Desktop`

---

<a id="item-10"></a>
## [French Carrier Tracked via Strava Fitness App](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html) ⭐️ 7.0/10

French news outlet Le Monde successfully located France's aircraft carrier in real time using public location data from the Strava consumer fitness app, and this incident is now discussed in a popular thread on Hacker News. This incident highlights a persistent critical operational security risk for militaries worldwide, showing that consumer location tracking apps can easily leak sensitive military location information that adversaries can exploit. This is not an isolated incident, as multiple prior cases of military location leaks via Strava have been recorded, including the exposure of secret US military bases and the tracking of a Russian former submarine commander.

hackernews · MrDresden · Mar 20, 13:01

**Background**: Strava is a popular consumer GPS fitness app that allows users to track, record, and publicly share their workout activity, including detailed geographic route data. Operations security (OPSEC) is a security process used by militaries to prevent sensitive information about their operations from being collected and exploited by adversaries. Hacker News is a well-known online community for discussing technology and cybersecurity topics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strava">Strava - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Operations_security">Operations security - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/">Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree that location leaks from consumer fitness apps are a persistent problem across all militaries, caused by soldiers using personal mobile devices despite official security restrictions. Some commenters pointed out that large aircraft carriers are easily detectable by satellites, so their location is not actually highly sensitive secret information.

**Tags**: `#operational security`, `#location privacy`, `#fitness apps`, `#military security`

---

<a id="item-11"></a>
## [Claude AI Deconstructs Turbo Pascal 3.02A Binary](https://simonwillison.net/2026/Mar/20/turbo-pascal/#atom-everything) ⭐️ 7.0/10

Developer Simon Willison used Claude AI to successfully decompile the 1985 Turbo Pascal 3.02A binary executable. He then built and published a public interactive deconstruction artifact showcasing the annotated, segmented reverse engineering result. This project creatively demonstrates that modern generative AI can simplify reverse engineering of historic software, opening up accessible insights into classic retro computing engineering for modern audiences. It also showcases the unexpected practical capabilities of current large language models for specialized technical tasks. The original Turbo.com executable of Turbo Pascal 3.02A is only 39,731 bytes yet packs a full integrated development environment, text editor, and Pascal compiler; the interactive artifact splits the binary into 17 labeled functional segments with annotated decompiled code. The entire project was completed using regular Claude AI chat, not specialized Claude Code tools.

rss · Simon Willison · Mar 20, 23:59

**Background**: Turbo Pascal is a classic Pascal programming language integrated development environment and compiler created by Borland, targeting early hobbyist and entry-level programmers for systems like DOS and CP/M. Borland released several historic versions including Turbo Pascal 3.02A as freeware in 2000 to preserve their historical value. Binary decompilation is a reverse engineering process that converts low-level executable binary code into human-readable assembly or higher-level source code, and recent research has explored using large language models to automate this task.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Turbo_Pascal">Turbo Pascal - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_recompilation">Binary recompilation</a></li>
<li><a href="https://arxiv.org/html/2403.05286v1">LLM4Decompile: Decompiling Binary Code with Large Language Models</a></li>

</ul>
</details>

**Tags**: `#generative ai`, `#reverse engineering`, `#retro computing`, `#software history`, `#turbo pascal`

---

<a id="item-12"></a>
## [Kimi-k2.5 Powers Cursor's New Composer 2](https://simonwillison.net/2026/Mar/20/cursor-on-kimi/#atom-everything) ⭐️ 7.0/10

Kimi.ai from Moonshot AI has officially confirmed that its Kimi-k2.5 large language model serves as the foundation for popular AI code editor Cursor's newly launched Composer 2. This collaboration is an authorized commercial partnership that leverages FireworksAI's hosted inference and reinforcement learning platform for model access. This official cross-company partnership validates the maturity of the open large language model ecosystem, proving that high-quality open models can power mainstream AI coding products used by millions of developers. It sets a clear example for commercial collaboration between model developers and AI coding tool builders, which will further drive innovation in the AI development space. Cursor conducted additional continued pretraining and high-compute reinforcement learning training on top of the base Kimi-k2.5 model to adapt it for coding-specific use cases. Kimi-k2.5 is an open-source trillion-parameter large language model that supports up to 256K long context window and tool calling functionality.

rss · Simon Willison · Mar 20, 20:29

**Background**: Cursor is a leading AI-first code editor focused on agentic AI-assisted software development, and Composer 2 is its latest flagship AI coding model released in March 2026. Kimi-k2.5 is an open multimodal agentic large language model developed by China-based AI company Moonshot AI, open-sourced in early 2026. FireworksAI is a generative AI infrastructure provider that offers fast, reliable hosted inference and reinforcement learning services for AI product teams.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/Kimi-K2.5 - Hugging Face</a></li>
<li><a href="https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart">Kimi K2.5 - Kimi API Platform - Moonshot AI</a></li>
<li><a href="https://explore.n1n.ai/blog/cursor-composer-2-features-pricing-benchmarks-2026-03-20">Cursor Composer 2: Features, Pricing, Benchmarks, and Initial ...</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#AI coding`, `#large language models`, `#open model ecosystem`

---

<a id="item-13"></a>
## [US Charges 3 for Diverting AI Servers to China](https://www.justice.gov/opa/pr/three-charged-conspiring-unlawfully-divert-cutting-edge-us-artificial-intelligence) ⭐️ 7.0/10

The U.S. Department of Justice has charged three individuals, including two senior Super Micro executives, with conspiring to illegally divert roughly $2.5 billion worth of Nvidia high-performance AI servers to China in violation of U.S. export control laws. Two of the accused have been arrested in California, one remains at large, and Super Micro has suspended the two involved executives and terminated its relationship with the third accused contractor. This high-stakes case represents a major enforcement of U.S. AI export control rules, and it brings new uncertainty to the global AI hardware supply chain and international tech trade between the U.S. and China. It also signals that the U.S. is ramping up enforcement of restrictions on advanced AI technology flows to China. The defendants evaded regulation by setting up shadow companies in Southeast Asia and forging documents, and even placed thousands of non-functional dummy servers in warehouses and altered serial number labels to cover up the diversion. Super Micro's sales account for approximately 9% of Nvidia's total revenue, meaning the case could have notable operational impact on both firms.

telegram · zaihuapd · Mar 20, 02:55

**Background**: In recent years, the U.S. has continuously tightened export controls on advanced AI-related hardware targeting China, as part of its strategy to slow China's large-scale development of advanced AI capabilities. High-performance AI servers are specialized computing infrastructure equipped with powerful GPUs, built to meet the intensive computational requirements of training and running large AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sidley.com/en/insights/newsupdates/2025/01/new-us-export-controls-on-advanced-computing-items-and-artificial-intelligence-model-weights">New U.S. Export Controls on Advanced Computing Items and ...</a></li>
<li><a href="https://www.ovhcloud.com/en/bare-metal/ai-server/">High-Performance AI Server Hosting | OVHcloud Worldwide</a></li>

</ul>
</details>

**Tags**: `#AI Export Controls`, `#Tech Trade`, `#AI Hardware`, `#Global Supply Chain`

---

<a id="item-14"></a>
## [Claude Code Launches Channels Remote Control Feature](https://code.claude.com/docs/en/channels) ⭐️ 7.0/10

Anthropic has launched the Channels feature for Claude Code in research preview, allowing users to push messages and remotely control local programming tasks via Telegram and Discord MCP servers. The feature uses sender whitelists for security protection, and requires administrator enablement for team and enterprise plans. This new feature adds useful remote control functionality to the widely used AI coding tool Claude Code, bringing more flexibility to developers who need to manage ongoing coding sessions away from their workstations. It expands the use cases of AI coding agents and promotes the development of flexible remote AI development workflows. Channels work through MCP servers that push external events into active running Claude Code sessions, supporting two-way communication between users and the local AI coding session. Team and enterprise plans require an administrator to enable the `channelsEnabled` setting in the backend before the feature can be used.

telegram · zaihuapd · Mar 20, 04:20

**Background**: Claude Code is an AI-powered coding assistant tool developed by Anthropic, widely used by developers for AI-assisted programming. MCP, short for Model Context Protocol, is an open-source standard for AI-tool integration backed by major AI companies including Anthropic, OpenAI, and Google. It allows Claude Code to connect to external tools, services and data sources to extend its native capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datastudios.org/post/claude-code-channels-what-it-is-how-it-works-and-how-to-use-it-with-mcp-telegram-and-discord">Claude Code Channels : what it is, how it works, and how to use it with...</a></li>
<li><a href="https://code.claude.com/docs/en/mcp">Connect Claude Code to tools via MCP - Claude Code Docs</a></li>
<li><a href="https://dev.to/alanwest/claude-code-channels-control-your-ai-coding-agent-from-telegram-2b0n">Claude Code Channels : Control Your AI Coding ... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#AI Coding`, `#Claude Code`, `#Developer Tools`, `#Remote Development`

---

<a id="item-15"></a>
## [Google Tests AI Title Rewrites in Search](https://www.theverge.com/tech/896490/google-replace-news-headlines-in-search-canary-coal-mine-experiment) ⭐️ 7.0/10

Google is running a small-scale test that uses generative AI to rewrite original webpage titles in search results to better match user queries. Google confirmed that any future official launch of this feature will not use generative AI for title creation. As the world's dominant search engine, this AI-powered change to Google Search affects web publishers, SEO practitioners and billions of end users, representing a high-impact development for the entire search industry. The test covers all types of webpages rather than only news sites, and one observed example from The Verge saw a long original article title shortened to a concise phrase in search results.

telegram · zaihuapd · Mar 20, 16:22

**Background**: Search engine optimization (SEO) is the practice of improving a website's content, structure, and visibility to get higher rankings on search engines, which is critical for web publishers to acquire organic traffic. Generative AI is a subfield of artificial intelligence that can generate new original content such as text in response to input prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Search_engine_optimization">Search engine optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_artificial_intelligence">Generative artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Google Search`, `#Generative AI`, `#SEO`, `#Web Publishing`

---

<a id="item-16"></a>
## [Trump Plans 'One Rule' AI Executive Order](https://t.me/zaihuapd/40415) ⭐️ 7.0/10

U.S. President Donald Trump announced he will sign the "One Rule" executive order this week to unify national AI regulatory standards by limiting state-level AI rules. This policy is backed by the tech industry, opposed by some Republican governors, and framed as part of U.S. AI competition with China. This change removes the burden on AI companies of complying with 50 different state AI regulatory regimes, streamlining compliance and cutting operational costs for businesses operating across the U.S. It also ties domestic AI governance policy directly to U.S. national strategy for AI competition with China, reshaping the country's AI regulatory landscape. The draft order allows the U.S. Department of Justice to sue states deemed non-compliant, and cut federal funding for states that impose overly strict AI restrictions. The order's use of federal preemption over state regulation is expected to trigger significant court challenges over its legality.

telegram · zaihuapd · Mar 21, 01:00

**Background**: Prior to this proposal, many U.S. states had already enacted or drafted their own unique AI regulations, creating a fragmented compliance environment for cross-state AI companies. Federal preemption is a legal doctrine that allows federal law to override conflicting state laws in areas under federal jurisdiction. U.S. strategic policy has increasingly framed AI development and regulation as a core arena of competition with China in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://www.foxbusiness.com/politics/trump-says-he-sign-one-rule-executive-order-federalize-ai-regulation">Trump announces 'One Rule' executive order for AI regulation ...</a></li>
<li><a href="https://www.wilmerhale.com/en/insights/client-alerts/20251212-white-house-issues-one-rule-executive-order-to-curb-state-ai-regulation">White House Issues “One Rule” Executive Order to Curb State ...</a></li>
<li><a href="https://www.forbes.com/sites/kirkogunrinde/2025/12/08/trump-promises-one-rule-on-ai-that-overrules-state-regulations/">Trump Says Executive Order On AI Will Nullify State Rules</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#tech policy`, `#AI governance`, `#US AI strategy`

---

<a id="item-17"></a>
## [Tencent Yuanbao AI Unveils New Logo, Hits Growth Milestone](https://www.aibase.com/zh/news/26429) ⭐️ 7.0/10

Tencent's consumer large model AI assistant Yuanbao has launched a new more anthropomorphic brand logo that adds eyes to its original ingot design, and it hit a peak daily active user count of over 40 million and monthly active user count of 114 million after 2026 Spring Festival promotions. This update confirms that China's consumer AI assistant market has formed a three-way leading competitive pattern among Yuanbao, Doubao and Tongyi Qianwen, and reflects that Tencent's strategy of doubling AI investment is being solidly implemented for consumer-facing AI products. The new logo is designed to reduce the cold impersonal technical feel of AI tools and enhance Yuanbao's companion attribute and user affinity, and the 10 billion yuan cash red envelope incentive during the 2026 Spring Festival drove over 1 billion user-completed AI tasks on the platform.

telegram · AI_News_CN · Mar 20, 09:27

**Background**: Yuanbao is Tencent's flagship consumer AI assistant built on its Hunyuan large language model, and Tencent plans to double its 2026 AI-related investment to 36 billion yuan, with Yuanbao as the core product of this strategy. Doubao is ByteDance's leading consumer AI assistant that currently leads the market in peak DAU, while Tongyi Qianwen is a well-known large language model and AI assistant developed by Alibaba Cloud.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/ywang/2026/03/19/tencent-to-double-ai-investments-to-52-billion-amid-chinas-openclaw-frenzy/">Tencent To Double AI Investments To $5.2 Billion ... - Forbes</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doubao">Doubao - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tongyi_Qianwen">Tongyi Qianwen</a></li>

</ul>
</details>

**Tags**: `#AI assistant`, `#generative AI`, `#Tencent`, `#consumer AI`, `#industry update`

---

<a id="item-18"></a>
## [Xiaomi Commits 60B Yuan to AI, Launches New SU7 EV](https://www.aibase.com/zh/news/26430) ⭐️ 7.0/10

On March 19, Xiaomi founder Lei Jun announced at the spring new product launch event that the company plans to invest 60 billion RMB in AI over three years, launched three new MiMo-V2 series large models, and opened pre-orders for the upgraded Xiaomi SU7 smart electric vehicle with a 4000 RMB price increase. Following the announcement, Xiaomi's Hong Kong-listed stock dropped more than 6% amid market concerns over the large investment. This big-bet AI investment and new EV launch solidifies Xiaomi's position as a major competitor in both the global AI large model and smart electric vehicle industries, and will reshape the competitive landscape of both fast-growing sectors. It reflects the growing intensity of competition among top global tech firms to gain an edge in the AI-powered smart mobility era. The flagship trillion-parameter MiMo-V2-Pro ranks 8th globally and 5th among all brand-developed models on the global large model comprehensive intelligence ranking. The upgraded Xiaomi SU7 starts at 219,900 RMB, with full upgrades to intelligent driving, cabin interaction, interior details, and the core three-electric system that powers all electric vehicles.

telegram · AI_News_CN · Mar 20, 09:36

**Background**: The three-electric system is the core component of any electric vehicle, consisting of the power battery, drive motor, and electronic control system, which collectively determine the vehicle's performance, safety, and energy efficiency. Large language models are the foundational AI technology that powers a wide range of modern smart applications, from personal assistants to autonomous driving and in-car interaction. Xiaomi, a leading global consumer electronics manufacturer, has recently expanded into the electric vehicle market to build out its AI-powered smart ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://xiaomitime.com/xiaomi-launches-web-based-mimo-v2-ai-to-rival-claude-4-6-93516/">Xiaomi Launches Web-Based MiMo-V2 AI to Rival Claude 4.6</a></li>
<li><a href="https://www.empevmobility.com/what-are-the-three-electric-systems-of-electric-vehicles.html">What Are the Three Electric Systems of Electric Vehicles?</a></li>
<li><a href="https://inf.news/en/tech/02e1dbe014d047da855959de8b54e31d.html">2025 Global AI Big Model Comprehensive Ranking (Top 20)</a></li>

</ul>
</details>

**Tags**: `#Artificial Intelligence`, `#Large Language Models`, `#Electric Vehicles`, `#Technology Business`

---

<a id="item-19"></a>
## [US Data Center Construction Value Surpasses Offices](https://www.cnbeta.com.tw/articles/tech/1554254.htm) ⭐️ 7.0/10

According to market data from The Kobeissi Letter, the total value of under-construction data centers in the U.S. hit a record $451 billion, surpassing the value of under-construction traditional office projects for the first time. This structural shift has been sharply accelerated by booming AI demand after ChatGPT's public launch in November 2022. This milestone marks a permanent shift in how U.S. enterprises use physical space, and reflects how AI is reshaping investment trends in the U.S. construction and broader economy. It also highlights the growing strategic importance of AI infrastructure for the global tech industry. Since ChatGPT's launch, U.S. data center construction has grown 228% year-over-year, while the value of under-construction traditional office projects fell 13% to $435 billion, the lowest level since October 2015. Big tech firms including Amazon and Meta are leading the investment trend, pouring hundreds of billions of dollars into power-intensive computing facilities to support heavy AI workloads.

telegram · AI_News_CN · Mar 20, 10:55

**Background**: The Kobeissi Letter is a leading industry commentary on global capital markets, founded by Adam Kobeissi that provides regular in-depth analysis of market trends. Generative AI is a type of artificial intelligence technology that can autonomously generate content, and its recent boom triggered by ChatGPT requires massive amounts of computing power to run large models. Hyperscale enterprises are large technology companies that operate massive digital services, requiring extensive data center infrastructure to support their business needs.

<details><summary>References</summary>
<ul>
<li><a href="https://askai.glarity.app/zh-CN/search/关于Kobeissi-Letter的介绍是什么">关于Kobeissi Letter的介绍是什么？ - 问答 - Glarity</a></li>
<li><a href="https://www.thekobeissiletter.com/">The Kobeissi Letter</a></li>
<li><a href="https://www.nsfc.gov.cn/csc/20345/20348/pdf/2023/202305-743-750.pdf">标题</a></li>

</ul>
</details>

**Tags**: `#data center infrastructure`, `#artificial intelligence`, `#industry trend`, `#tech economy`

---