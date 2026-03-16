---
layout: default
title: "Horizon Summary: 2026-03-16 (EN)"
date: 2026-03-16
lang: en
---

> From 39 items, 22 important content pieces were selected

---

1. [Claude Launches 1 Million Token Context Window](#item-1) ⭐️ 9.0/10
2. [Google Launches Chrome DevTools MCP Integration](#item-2) ⭐️ 8.0/10
3. [Sebastian Raschka's LLM Architecture Gallery](#item-3) ⭐️ 8.0/10
4. [Adult Mouse Brain Vitrification and Function Recovery](#item-4) ⭐️ 8.0/10
5. [Google Maps' Largest 10-Year Gemini AI Upgrade](#item-5) ⭐️ 8.0/10
6. [Zhipu AI Launches GLM-5-Turbo AI Agent Model](#item-6) ⭐️ 8.0/10
7. [Tesla to Launch Terafab AI Chip Factory Next Week](#item-7) ⭐️ 8.0/10
8. [Canada's 2026 Bill C-22 Expands Mass Surveillance](#item-8) ⭐️ 7.0/10
9. [Hacker News Discussion of 49MB Bloated News Page](#item-9) ⭐️ 7.0/10
10. [River Splits Wayland Compositor and Window Manager](#item-10) ⭐️ 7.0/10
11. [Simon Willison Defines Agentic Engineering](#item-11) ⭐️ 7.0/10
12. [Apple Unveils New M5 Series Laptop Chips](#item-12) ⭐️ 7.0/10
13. [ImageGlass 10 Beta 1 Released With Cross-Platform Support](#item-13) ⭐️ 7.0/10
14. [OpenAI Begins Testing Ads in ChatGPT](#item-14) ⭐️ 7.0/10
15. [GreenLink and MiniMax Turn NAS into Private AI](#item-15) ⭐️ 7.0/10
16. [Yuewen Launches Claw AI Agent for Web Novels](#item-16) ⭐️ 7.0/10
17. [Enterprise WeChat OpenClaw Upgraded](#item-17) ⭐️ 7.0/10
18. [Global Surge in AI Deepfake Voice Fraud](#item-18) ⭐️ 7.0/10
19. [Wondershare Launches First Full-Link AI Manga Drama Platform](#item-19) ⭐️ 7.0/10
20. [Musk's xAI Restructures After Talent Exodus, Unveils Digital Optimus](#item-20) ⭐️ 7.0/10
21. [Elon Musk vs OpenAI $134B lawsuit set for 2026 trial](#item-21) ⭐️ 7.0/10
22. [AI Treatment Shrinks Dog's Tumor By 75%](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Claude Launches 1 Million Token Context Window](https://www.aibase.com/zh/news/26226) ⭐️ 9.0/10

Anthropic has officially launched a 1 million token context window for its Claude large language model, with the capability available on both Claude Opus 4.6 and Claude Sonnet 4.6 at a flat price for the full window. This new capacity allows Claude to process entire codebases, very large documents, and multiple full-length books in a single prompt. This breakthrough marks a major leap in long-context large language model technology, reshapes AI-assisted development workflows, and could disrupt multiple industries that work with large volumes of text or code. The flat non-premium pricing also makes long-context AI accessible to a much wider range of developers than competing premium offerings. A 1 million token context can hold roughly 7.5 million English words, which equals seven full copies of the entire Harry Potter book series. Claude Opus 4.6 scored 78.3% on the needle-in-a-haystack long context retrieval test, the highest score among all comparable existing models.

telegram · AI_News_CN · Mar 16, 01:27

**Background**: Tokens are the basic text units that large language models use to process input and generate output, and a context window defines the maximum number of tokens a model can process and reference in one single interaction. The needle-in-a-haystack test is a standard evaluation that measures how well a long context LLM can retrieve small specific pieces of information hidden in a large volume of input text. Prior to this launch, most leading LLMs had much smaller context window limits, forcing developers to manually split large inputs like entire codebases into smaller chunks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/">Tokens and Context Windows in LLMs - GeeksforGeeks</a></li>
<li><a href="https://arize.com/blog-course/the-needle-in-a-haystack-test-evaluating-the-performance-of-llm-rag-systems/">The Needle In a Haystack Test : Evaluating the Performance... - Arize AI</a></li>

</ul>
</details>

**Discussion**: OpenAI President Greg Brockman praised the new capability, noting that the freedom from manually writing large amounts of code eases a heavy mental burden for developers. No broader community discussion is included in the original news report.

**Tags**: `#Large Language Models`, `#Claude`, `#Long Context AI`, `#AI Programming`, `#Anthropic`

---

<a id="item-2"></a>
## [Google Launches Chrome DevTools MCP Integration](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) ⭐️ 8.0/10

Google has officially announced Chrome DevTools MCP, which enables AI agents to interact with and debug live Chrome browser sessions. A standalone unannounced CLI for the project has already shipped in the latest v0.20.0 release. This integration brings standardized MCP-based AI tool access to one of the world's most widely used developer tools, accelerating the development of AI-powered web debugging and automation workflows. It creates new opportunities for AI agents to automate complex web-based tasks that require browser inspection and interaction. Chrome DevTools MCP runs as an MCP server that grants AI coding assistants full access to Chrome DevTools' native functionality. MCP can incur high token usage for large payloads like full DOM snapshots, while the new standalone CLI offers a lower-cost alternative for direct access.

hackernews · xnx · Mar 15, 19:12

**Background**: Model Context Protocol (MCP) is an open-source standard launched by Anthropic in November 2024, created to standardize how large language models and AI agents connect to external tools, systems, and data sources. Chrome DevTools is Google's official built-in suite of developer tools for building, testing, and debugging web applications directly in the Chrome browser.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">ChromeDevTools/chrome-devtools-mcp - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/tutorial/chrome-devtools-mcp">Chrome DevTools MCP: AI-Powered Browser Automation and Debugging | DataCamp</a></li>

</ul>
</details>

**Discussion**: Community participants debated the tradeoffs between MCP and direct CLI access, with most agreeing both serve different use cases: MCP offers uniform cross-tool integration while direct CLI is faster and lower cost. A former (and current) Chrome DevTools team member confirmed the unannounced standalone CLI launch in v0.20.0, addressing MCP's token cost concerns. Multiple users shared practical automation use cases and third-party tools built on top of Chrome DevTools MCP that they already use daily.

**Tags**: `#Chrome DevTools`, `#Model Context Protocol`, `#AI Agents`, `#Debugging`, `#Web Development`

---

<a id="item-3"></a>
## [Sebastian Raschka's LLM Architecture Gallery](https://sebastianraschka.com/llm-architecture-gallery/) ⭐️ 8.0/10

Researcher Sebastian Raschka has launched a new curated LLM Architecture Gallery, a visual overview of modern large language model architectures that sparked insightful discussion on Hacker News. This curated reference is highly valuable for machine learning practitioners and researchers, and the discussion around it highlights a key industry trend of architectural convergence in modern open-weight LLMs. The gallery compiles architecture diagrams from previous LLM comparison work into one accessible reference, and observers note that leading competitive open-weight LLMs have converged on a narrow design space centered on dense decoder-only transformers with standard components like RMSNorm, rotary position embeddings, and SwiGLU activations.

hackernews · tzury · Mar 15, 16:01

**Background**: Large language models (LLMs) are AI models trained on massive text corpora to handle natural language tasks, and their architecture has evolved continuously since the release of GPT-2 seven years ago. Researchers have experimented with many different architectural approaches, including Mixture-of-Experts, state-space models, and linear attention, to improve LLM performance and efficiency. Open-weight LLMs are publicly available for use and modification, unlike closed proprietary models developed by private companies.

<details><summary>References</summary>
<ul>
<li><a href="https://sebastianraschka.com/blog/2026/llm-architecture-gallery.html">New LLM Architecture Gallery | Sebastian Raschka, PhD</a></li>
<li><a href="https://github.com/rasbt/llm-architecture-gallery">rasbt/llm-architecture-gallery - GitHub</a></li>
<li><a href="https://maxpool.dev/llm-design/">LLM Architecture Design Guide | MaxPool</a></li>

</ul>
</details>

**Discussion**: Most community members praised the gallery as a high-quality useful resource, and many agreed that there has been no fundamental LLM architectural innovation since GPT-2, with the field converging on a shared core design. Some commenters compared the gallery to the classic Neural Network Zoo visualization project, and others suggested adding evolutionary sorting and size scaling to improve the resource further.

**Tags**: `#Large Language Models`, `#LLM Architecture`, `#Machine Learning`, `#Curated Resources`

---

<a id="item-4"></a>
## [Adult Mouse Brain Vitrification and Function Recovery](https://www.pnas.org/doi/10.1073/pnas.2516848123) ⭐️ 8.0/10

Researchers published their findings in PNAS, reporting that they developed the V3 vitrification protectant which successfully enabled glassy cryopreservation of adult mouse brain slices and intact in-situ whole brains, with neural function recovered after rewarming. This work is an important milestone in functional cryopreservation of intact adult mammalian brains, advancing both neuroscience research and the broader field of organ preservation. It provides a new feasible path for long-term functional preservation of complex whole neural organs. The V3 protectant avoids ice crystal damage during cooling via an optimized cooling process, and experiments confirmed that rewarmed brain slices recovered cell metabolism while retaining electrophysiological activity and synaptic plasticity. For whole brain preservation, researchers used vascular perfusion to balance dehydration and protectant penetration, achieving initial in-situ whole brain functional preservation.

telegram · zaihuapd · Mar 15, 08:30

**Background**: Vitrification, or glassy cryopreservation, is a cryopreservation technique that converts a sample into a non-crystalline amorphous glass solid instead of crystalline ice, which avoids the damage ice crystals cause to living cells and tissues. Cryoprotective agents (CPAs) are required to achieve vitrification, as they reduce cell dehydration damage and help the entire sample form a stable glassy state during cooling. Prior to this study, successful functional cryopreservation of intact adult mammalian whole brains had not been reported.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vitrification">Vitrification - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8162897/">Mathematical modeling of protectant transport in tissues - PMC</a></li>
<li><a href="https://www.21cm.com/vm3.html">VM3 Cryoprotectant for Successful Tissue Preservation</a></li>

</ul>
</details>

**Tags**: `#cryopreservation`, `#neuroscience`, `#biotechnology research`, `#vitrification`

---

<a id="item-5"></a>
## [Google Maps' Largest 10-Year Gemini AI Upgrade](https://www.aibase.com/zh/news/26233) ⭐️ 8.0/10

Google CEO Sundar Pichai announced Google Maps' largest upgrade in over a decade, which integrates the Gemini AI model to launch two new AI-powered features: conversational location recommendation tool Ask Maps and 3D real-time rendered Immersive Navigation, rolling out to iOS and Android users in select regions. As one of the world's most widely used consumer navigation apps, this major generative AI integration marks a transformative shift for the mapping industry and accelerates AI adoption in daily consumer applications. Ask Maps is already available in the United States and India, and it can analyze massive user data to answer complex natural language queries, even helping users book reservations. Immersive Navigation uses Gemini to real-time render hundreds of millions of Street View and aerial photos, displaying fine road details to reduce wrong turns at complex interchanges.

telegram · AI_News_CN · Mar 16, 02:19

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, first announced in December 2023 as Google's flagship generative AI succeeding earlier models like PaLM 2. Google Maps is one of the world's most popular consumer mapping and navigation applications, used by billions of people globally for travel and location services.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/">Ask Maps and Immersive Navigation: New AI features in Google Maps</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**Tags**: `#Google Maps`, `#Gemini`, `#Generative AI`, `#AI Integration`, `#Navigation Technology`

---

<a id="item-6"></a>
## [Zhipu AI Launches GLM-5-Turbo AI Agent Model](https://autoglm.zhipuai.cn/autoclaw) ⭐️ 8.0/10

Zhipu AI has released GLM-5-Turbo, the first OpenClaw (lobster) scenario-native foundation model optimized for complex AI Agent tasks, which ranks first among Chinese large models on Zhipu's in-house ZClawBench benchmark. The company also launched new subscription plans and enterprise security management tools for its OpenClaw AI Agent ecosystem alongside the model release. This release shifts the focus of large language model competition from pure semantic understanding to end-to-end execution efficiency, accelerating the large-scale commercialization of AI Agents and pushing the transition of large models from productivity tools to enterprise digital workforce. It sets a standard paradigm for AI Agent commercial落地 in the Chinese AI industry. GLM-5-Turbo is optimized from the training stage for core AI Agent capabilities including tool calling, complex instruction decomposition, timed triggering and high-throughput continuous execution, and received 90% win approval rate in developer blind tests. The model is already integrated into the world's first native AI Agent terminal Lobster Box, and developers can call its API via Zhipu's open platform BigModel.cn starting March 16, 2026.

telegram · AI_News_CN · Mar 16, 02:45

**Background**: AI Agents are autonomous AI systems that can independently complete long-chain, multi-step complex tasks, and have become a core development focus of the large language model industry in recent years. General-purpose large language models often suffer from stalling or failure during long-chain task execution, which cannot meet the requirements of complex AI Agent scenarios. OpenClaw is an open-source autonomous AI agent framework that supports large models to execute tasks and expand capabilities through modular skills.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibase.com/news/26235">Zhipu Launches GLM-5-Turbo: The First Lobster-Specific Scene ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://open-claw.org/">OpenClaw | The Open -Source Personal AI Assistant & Autonomous...</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#AI Agent`, `#Model Release`, `#GLM-5-Turbo`, `#Zhipu AI`

---

<a id="item-7"></a>
## [Tesla to Launch Terafab AI Chip Factory Next Week](https://www.aibase.com/zh/news/26236) ⭐️ 8.0/10

On March 14, 2026, Elon Musk announced that Tesla's in-house giant AI chip manufacturing project Terafab will launch next week, seven days after the announcement. The move is driven by unmet AI chip demand for Tesla's Full Self-Driving program and production delays from external foundries. This development marks Tesla's push toward full vertical integration of AI chip production, which could reshape the global automotive AI chip market and reduce Tesla's exposure to semiconductor supply chain risks for autonomous driving. If successful, it sets a new precedent for automakers taking full control of their core AI hardware supply. Tesla's fifth-generation AI chip AI5 is expected to be among the first products manufactured at Terafab, with small-batch production planned for 2026 and volume production projected for 2027. Tesla's next-generation AI6 chip has already been delayed to late 2027 due to Samsung's 2nm process tapeout delays, which accelerated Tesla's timeline for building its own fab.

telegram · AI_News_CN · Mar 16, 02:53

**Background**: Tesla has long relied on external foundries including TSMC and Samsung to produce AI chips for its autonomous driving systems. Musk has stated multiple times that even with suppliers running at full capacity, they cannot meet Tesla's growing demand for AI chips to power FSD. Tape-out is the final stage of integrated circuit design before chips are sent for manufacturing, so a tape-out delay directly pushes back mass production timelines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/autos-transportation/musk-says-teslas-gigantic-chip-fab-project-launch-seven-days-2026-03-14/">Musk says Tesla's mega AI chip fab project to launch in seven days | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tape-out">Tape - out - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Chips`, `#Tesla`, `#Autonomous Driving`, `#Semiconductor Manufacturing`, `#Supply Chain`

---

<a id="item-8"></a>
## [Canada's 2026 Bill C-22 Expands Mass Surveillance](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/) ⭐️ 7.0/10

In March 2026, Canada tabled new Bill C-22, which expands surveillance powers for police and security agencies, requiring electronic service providers to retain user metadata and comply with government data access requests. This bill threatens the digital privacy rights of all Canadian residents, not just criminal suspects, and sets a concerning precedent for broad government surveillance that impacts both domestic and foreign technology companies serving the Canadian market. The bill establishes a mandatory mass metadata retention regime requiring companies to store location data, device information, and other sensitive metadata for all Canadians, and allows judges to waive the rule that requires notifying a person that their data has been accessed via warrant.

hackernews · opengrass · Mar 15, 21:22

**Background**: Metadata is data that describes other digital information, acting like the envelope of a digital communication that reveals sender, receiver, location, and timing details even when the content of the communication is encrypted. Mass metadata surveillance refers to the practice of collecting and storing metadata for an entire population rather than only individual suspects, for use by law enforcement and intelligence agencies. Previous Canadian attempts to pass similar broad surveillance legislation have been defeated by privacy advocacy groups.

<details><summary>References</summary>
<ul>
<li><a href="https://ssd.eff.org/module/why-metadata-matters">Why Communication Metadata Matters | Surveillance Self-Defense</a></li>
<li><a href="https://reclaimthenet.org/canada-bill-c22-lawful-access-act-metadata-retention-surveillance">Canada's Bill C-22 Mandates Mass Metadata Surveillance of Canadians</a></li>
<li><a href="https://www.canada.ca/en/public-safety-canada/news/2026/03/backgrounder--securing-access-to-information-in-bill-c-22.html">Backgrounder – Securing Access to Information (Bill C-22 – Part 2) - Canada.ca</a></li>

</ul>
</details>

**Discussion**: Hacker News community participants highlighted that while the bill requires warrants for data access, it includes provisions that allow notifying targets of the access to be waived, and criticized the bill as a non-transparent expansion of Five Eyes surveillance cooperation. Community members also shared practical action steps for opposing the bill, including contacting elected representatives and supporting established privacy advocacy groups.

**Tags**: `#digital privacy`, `#surveillance`, `#public policy`, `#technology regulation`

---

<a id="item-9"></a>
## [Hacker News Discussion of 49MB Bloated News Page](https://thatshubham.com/blog/news-audit) ⭐️ 7.0/10

An audit found a single news web page weighs 49MB, sparking a high-engagement Hacker News discussion that collects user complaints and anecdotes about extreme resource bloat on modern commercial and news websites. This issue harms end user experience, wastes limited bandwidth and device resources, and pushes users away from traditional news outlets, highlighting a systemic problem in the modern web ecosystem. The discussion includes 177 substantive comments from both developers and end users, with shared anecdotes of pages reaching 750MB in resource usage and major news sites driving off power users with excessive JavaScript and tracking.

hackernews · kermatt · Mar 15, 19:25

**Background**: Software bloat is a phenomenon where software or web pages require far more system resources and bandwidth than needed for their core functionality, often with little corresponding improvement to user experience. Website resource bloat forces visitors to consume more data than necessary, slows down page loads, and drains device processing power and battery life.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software_bloat">Software bloat - Wikipedia</a></li>
<li><a href="https://www.curotec.com/insights/how-to-improve-website-performance/">Getting the Fast Website Load Times - A Web Performance... - Curotec</a></li>

</ul>
</details>

**Discussion**: Commenters universally expressed frustration with web bloat, sharing multiple personal experiences of excessive resource usage, poor performance, and unauthorized privacy tracking by major news sites. Many commenters noted that bloat has pushed them to stop visiting popular news outlets entirely.

**Tags**: `#web performance`, `#web development`, `#software bloat`, `#community discussion`

---

<a id="item-10"></a>
## [River Splits Wayland Compositor and Window Manager](https://isaacfreund.com/blog/river-window-management/) ⭐️ 7.0/10

The River Wayland compositor has implemented a new architectural separation between the Wayland compositor core and the window manager, as outlined in a developer's recent blog post. This development sparked a high-engagement discussion thread on Hacker News. This change addresses a long-criticized default design choice in Wayland, enabling more modular, flexible window management and cleaner code for the Linux desktop Wayland ecosystem. It also prompts important conversation about reducing protocol fragmentation that has plagued Wayland's development for years. The new design avoids per-frame roundtrips while still delivering frame-perfect window rearrangement, and introduces a new protocol called river-window-management-v1 for the separated window manager. Unlike most existing Wayland compositors that combine both functions, River is now explicitly structured as a non-monolithic project.

hackernews · dpassens · Mar 15, 15:09

**Background**: Wayland is a modern display protocol for Linux desktops designed to replace the aging X11 protocol, with a focus on smoother, more secure hardware-accelerated graphics. Traditionally, Wayland compositors have combined the two distinct roles of compositor (which handles screen compositing and graphics output) and window manager (which handles window arrangement and user input) into one program. River is a wlroots-based open-source dynamic tiling Wayland compositor, inspired by popular tiling window managers like Xmonad.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayland_(protocol)">Wayland (protocol) - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/River">river - ArchWiki</a></li>
<li><a href="https://github.com/riverwm/river">GitHub - riverwm/ river : [mirror] A non-monolithic Wayland compositor</a></li>

</ul>
</details>

**Discussion**: Most commenters reacted positively to the change, with many stating it fixes a long-standing Wayland flaw and makes Wayland feel significantly more usable. The top shared concern is whether the new river-window-management-v1 protocol will become a cross-compositor standard, or if it will add to Wayland's existing fragmentation caused by compositor-specific custom extensions. Some commenters joked that Wayland is slowly re-inventing X11 one feature at a time, while existing River users expressed excitement for the update and recommended it to former Xmonad users.

**Tags**: `#Wayland`, `#window management`, `#software architecture`, `#Linux desktop`

---

<a id="item-11"></a>
## [Simon Willison Defines Agentic Engineering](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/#atom-everything) ⭐️ 7.0/10

Respected industry commentator Simon Willison published a formal definition of the emerging term 'agentic engineering' as part of his ongoing Agentic Engineering Patterns guide, alongside clear definitions for related concepts like LLM agents and coding agents. This clear definition helps establish a common vocabulary for the fast-evolving field of AI-assisted software development, helping practitioners align on practices for working with AI coding tools. It also clarifies the complementary roles of human engineers and AI coding agents, reducing confusion around AI-augmented software development. Willison defines LLM agents in this context as systems that run tools in a loop to achieve a stated user goal, and notes that direct code execution is the defining capability that makes agentic engineering possible. His guide is an ongoing work in progress, and he plans to update it as new patterns and techniques for agentic engineering emerge.

rss · Simon Willison · Mar 15, 22:41

**Background**: Agentic engineering is an emerging discipline focused on AI-augmented software development that has grown in popularity alongside the increasing capabilities of large language models for code generation. Before Willison's formal definition, the term was used inconsistently across the tech industry, with varying interpretations from different technology leaders. LLM-based coding agents are AI tools designed to assist with software development by interacting directly with codebases and development environments.

<details><summary>References</summary>
<ul>
<li><a href="https://addyosmani.com/blog/agentic-engineering/">AddyOsmani.com - Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Claude Code overview - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#agentic engineering`, `#AI-assisted development`, `#LLM agents`, `#software engineering`

---

<a id="item-12"></a>
## [Apple Unveils New M5 Series Laptop Chips](https://t.me/zaihuapd/40272) ⭐️ 7.0/10

In March 2026, Apple announced the release of M5 Pro and M5 Max chips for new MacBook Pro models, as well as a base M5 chip for the updated MacBook Air. The new pro-grade M5 chips feature Apple's all-new Fusion Architecture and an 18-core CPU with 6 super cores and 12 performance cores. This is a major generational update to Apple's widely used M-series laptop chips, introducing a new architecture that pushes the boundary of pro laptop performance. The update will affect professional content creators, general consumers, and the global personal computing and semiconductor industries. Unlike the base M5 and previous generation Apple Silicon chips that use a single-die design, Fusion Architecture bonds two dies into a single system-on-chip using advanced packaging. The new "super cores" are Apple's highest-performing CPU core design to date, prioritizing performance for demanding professional workloads.

telegram · zaihuapd · Mar 15, 07:20

**Background**: Apple Silicon is Apple's line of custom ARM-based system-on-chips for its own devices, which replaced Intel processors in Mac computers starting from 2020. The M-series is Apple's current family of Apple Silicon chips designed for Mac laptops and desktops, with each generation delivering incremental gains in performance and energy efficiency. Before the M5 generation, all high-end M-series Pro and Max chips used a traditional single-die design to integrate all processing components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/">Apple debuts M5 Pro and M5 Max to supercharge the most ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://dev.to/tyson_cung/apple-m5-fusion-architecture-explained-two-dies-one-chip-infinite-possibilities-o9e">Apple M 5 Fusion Architecture Explained - Two Dies, One Chip ...</a></li>

</ul>
</details>

**Tags**: `#Apple Silicon`, `#Semiconductors`, `#Laptop Hardware`, `#Apple M5`

---

<a id="item-13"></a>
## [ImageGlass 10 Beta 1 Released With Cross-Platform Support](https://imageglass.org/news/imageglass-10-beta-1-is-here-99) ⭐️ 7.0/10

Popular free open source image viewer ImageGlass has launched ImageGlass 10 Beta 1, which has been fully rewritten with .NET and Avalonia to add native macOS and Linux support alongside existing Windows support. The previous version ImageGlass 9 has been moved to maintenance mode, with all future development focus shifted to ImageGlass 10. This update fulfills the long-awaited cross-platform demand from the ImageGlass user community, turning a popular Windows-only image viewer into a viable option for all major desktop systems. It gives macOS and Linux users a new free open source alternative for lightweight image viewing. This beta release includes multiple performance improvements such as faster startup, quicker image switching, and smooth zooming for large image files, but the beta binary files are not yet digitally signed.

telegram · zaihuapd · Mar 15, 11:40

**Background**: ImageGlass is a free open source image tool that supports common and many professional image formats, with free usage allowed for both personal and commercial scenarios. Avalonia is an open source cross-platform UI framework built for the .NET ecosystem that allows developers to build multi-platform apps from a single shared codebase. When a software enters maintenance mode, the team stops adding new major features and only fixes critical bugs to keep the existing version running properly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Avalonia_(software_framework)">Avalonia (software framework) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Maintenance_mode">Maintenance mode - Wikipedia</a></li>
<li><a href="https://avaloniaui.net/">Avalonia UI – Open-Source .NET XAML Framework | WPF & MAUI ...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#software release`, `#cross-platform`, `#image viewer`, `#.NET`

---

<a id="item-14"></a>
## [OpenAI Begins Testing Ads in ChatGPT](https://t.me/zaihuapd/40282) ⭐️ 7.0/10

Starting February 9, OpenAI has begun testing clearly marked advertisements in ChatGPT, and expects long-term ad revenue to contribute nearly half of its total revenue. The company also confirmed ChatGPT's monthly growth has returned to over 10%, and plans to launch an updated chat model this week. This announcement reveals OpenAI's core commercial monetization strategy for its flagship product, and sets an important example for the broader generative AI industry's monetization efforts. This move will impact how AI companies balance revenue goals and user privacy protection going forward. The tested ads are placed in a separate area below the chat dialog, accessible to both free users and ChatGPT Go subscribers, and will not access private user conversations, while advertisers cannot alter ChatGPT's generated responses. OpenAI CEO Sam Altman confirmed long-term ad revenue will account for less than 50% of the company's total revenue.

telegram · zaihuapd · Mar 16, 01:23

**Background**: ChatGPT Go is OpenAI's new low-cost subscription tier for ChatGPT, which launched globally after initial testing, priced at $8 per month in the United States. Generative AI companies have been exploring diverse monetization methods after the initial industry boom, with advertising seen as a major potential revenue source alongside existing subscription models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-go/">Introducing ChatGPT Go , now available worldwide | OpenAI</a></li>
<li><a href="https://www.marketingdive.com/news/chatgpt-to-begin-testing-ads-as-generative-ai-competition-heats-up/809964/">ChatGPT to begin testing ads as generative AI competition heats up | Marketing Dive</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#Generative AI`, `#AI Monetization`, `#Digital Advertising`

---

<a id="item-15"></a>
## [GreenLink and MiniMax Turn NAS into Private AI](https://www.aibase.com/zh/news/26221) ⭐️ 7.0/10

Leading NAS brand GreenLink and AI firm MiniMax announced a deep strategic partnership to launch the one-click OpenClaw (Lobster) application that natively integrates MiniMax's large language model into GreenLink NAS, turning consumer private cloud into a local private AI brain. All GreenLink NAS users can access a 30-day full free trial of the service through April 12, 2026. This collaboration greatly simplifies the previously complex process of adding large AI model capabilities to consumer private cloud, expanding access to private on-premise AI for mainstream consumers and small businesses. It also sets a new direction for the intelligent upgrade of consumer private cloud products in 2026. Unlike previous DIY setups that required manual Docker environment debugging and complex API configuration, OpenClaw can be installed with one click directly from the GreenLink UGOS Pro application center. The AI feature will first roll out to GreenLink's DXP series and upcoming iDX series NAS devices.

telegram · AI_News_CN · Mar 16, 01:16

**Background**: NAS (Network-Attached Storage) is a local private cloud storage device that keeps user data on-premise for better privacy control compared to public cloud services. UGOS Pro is GreenLink's proprietary Linux-based operating system built specifically for its line of NAS devices. MiniMax is a leading general artificial intelligence company that develops high-performance large language models suited for reasoning, coding and long context tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://needtoknowit.com.au/blog/ugreen-ugos-pro-review-nas-software-and-ecosystem-explained/">UGREEN UGOS Pro Review — NAS Software and Ecosystem Explained — Need to Know IT</a></li>
<li><a href="https://github.com/openclaw/lobster">GitHub - openclaw/lobster: Lobster is a Openclaw-native workflow shell: a typed, local-first “macro engine” that turns skills/tools into composable pipelines and safe automations—and lets Openclaw call those workflows in one step.</a></li>
<li><a href="https://github.com/MiniMax-AI/MiniMax-M1">GitHub - MiniMax-AI/MiniMax-M1: MiniMax-M1, the world's first open-weight, large-scale hybrid-attention reasoning model. · GitHub</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Private AI`, `#NAS`, `#AI Deployment`

---

<a id="item-16"></a>
## [Yuewen Launches Claw AI Agent for Web Novels](https://www.aibase.com/zh/news/26223) ⭐️ 7.0/10

On March 15, Yuewen Group launched internal testing for Writer Assistant Claw, the first dedicated AI agent for Chinese web novel creation built on its domain-specific Yuewen Miaobi large model. The AI agent provides multi-role full-workflow assistance for creators and adopts privacy-focused local data storage. This launch marks a key milestone for AI adoption in the vertical web novel industry, moving beyond basic general content generation to end-to-end workflow governance. It will lower creation barriers, enable more efficient industrialized collaboration, and boost IP operation efficiency for the entire Chinese web literature ecosystem. Claw is built on Yuewen Miaobi, the first domestic web novel-specific large language model released by Yuewen in 2023, and currently supports interaction via QQ robot, with all user data stored locally to protect creator privacy. The product plans to evolve into an all-in-one creation assistant covering multiple roles including editor, manager and agent through continuous grayscale testing and data training.

telegram · AI_News_CN · Mar 16, 01:16

**Background**: Yuewen Group (officially China Literature) is the largest online literature platform in China, which released the first ever web novel-specific large language model Yuewen Miaobi for the domestic industry in July 2023. Vertical domain-specific large language models are AI models trained on targeted industry data, delivering more accurate and scenario-fitting performance for specific use cases than general-purpose large models. An AI agent for content creation is an AI system that can provide end-to-end support across an entire workflow, rather than only offering one-off content generation.

<details><summary>References</summary>
<ul>
<li><a href="http://m.nbdpress.com/a/49062">China Literature releases first large-scale model for webnovel</a></li>
<li><a href="https://kr-asia.com/tencents-china-literature-unveils-industrys-first-large-language-model-for-writers">Tencent’s China Literature unveils industry's first large ...</a></li>
<li><a href="https://hellotars.com/ai-agents/novel-writer-ai-agent">Novel Writer AI Agent For Creative Fiction Writing by Tars</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#Vertical Large Model`, `#AI Writing`, `#Content Creation`, `#Product Launch`

---

<a id="item-17"></a>
## [Enterprise WeChat OpenClaw Upgraded](https://www.aibase.com/zh/news/26224) ⭐️ 7.0/10

Enterprise WeChat has launched a major upgrade for its OpenClaw AI integration, adding one-click scan code deployment and automated document operation capabilities for enterprise AI agents. Multiple mainstream cloud service and model ecosystem providers have already completed adaptation for this new release. This upgrade significantly lowers the application barrier for enterprise AI agents, pushing practical AI integration deeper into enterprise office workflows. It also reflects the broader industry trend that large model development is shifting from parameter competition to real-world engineering deployment. AI agents can now automatically create documents and write content based on simple text commands, with strict permission isolation that only grants AI agents editing rights to documents they created, allowing employees to refine AI-generated content later. Administrators can complete deployment via one-click scan authorization from the Tencent Cloud backend without complex underlying development.

telegram · AI_News_CN · Mar 16, 01:27

**Background**: OpenClaw is a free and open-source autonomous AI agent that executes tasks via large language models, using messaging platforms as its main user interface. KimiClaw is an AI workspace that enables low-barrier workflow automation for professionals, while Zhipu AI's AutoClaw is a one-click installable local version of OpenClaw designed for Chinese users. Enterprise WeChat is Tencent's widely used enterprise-grade office collaboration platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw</a></li>
<li><a href="https://autoglm.zhipuai.cn/autoclaw/">AutoClaw（澳龙）- OpenClaw一键安装 | 飞书集成 | AI助手下载</a></li>
<li><a href="https://www.linkedin.com/pulse/kimiclaw-ai-workspace-structured-environment-where-scales-goldie-qkcyc">KimiClaw AI Workspace: Structured Environment Where Automation...</a></li>

</ul>
</details>

**Tags**: `#Enterprise AI`, `#AI Agents`, `#Digital Transformation`, `#Workflow Automation`

---

<a id="item-18"></a>
## [Global Surge in AI Deepfake Voice Fraud](https://www.aibase.com/zh/news/26225) ⭐️ 7.0/10

A new large-scale Techradar survey spanning six countries shows that AI deepfake voice fraud, which impersonates trusted contacts to scam victims, is surging globally, with 24% of consumers unable to distinguish fake voices from real ones. The survey finds that adults over 55 suffer three times the average economic loss of younger victims, and the fraud grows at a 16% annual compound rate. This is a rapidly growing emerging public and cybersecurity threat that disproportionately harms vulnerable groups like seniors, and it highlights the urgent need for coordinated action from industry and governments to address the growing AI-enabled fraud risk. The survey included over 12,000 consumers across six North American and European countries, and security experts call for telecom operators to deploy AI-based detection systems called "AI shields" to filter out fake synthetic voices, rather than relying on individual users to spot scams.

telegram · AI_News_CN · Mar 16, 01:27

**Background**: AI deepfake voice cloning, also known as audio deepfake, is an application of generative artificial intelligence that creates speech convincingly mimicking a specific individual, even lines the person never actually spoke. The spread of low-cost generative AI tools has made this technology easily accessible to malicious actors, and current detection technology still often struggles to reliably tell deepfake voices apart from authentic human voices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Audio_deepfake">Audio deepfake - Wikipedia</a></li>
<li><a href="https://www.nbcnews.com/tech/security/ai-voice-cloning-software-flimsy-guardrails-report-finds-rcna195131">AI can steal your voice, and there's not much you can do about it Beyond Cybersecurity: Deepfake Audio Is An Evidence Crisis AI Voice Cloning: What It Is & the Technology Behind It Top 7 AI Voice Cloning Tools for Realistic Speech 2026 (PDF) A Systematic Literature Review on AI Voice Cloning ...</a></li>

</ul>
</details>

**Tags**: `#AI Deepfake`, `#Voice Fraud`, `#Cybersecurity`, `#Generative AI`

---

<a id="item-19"></a>
## [Wondershare Launches First Full-Link AI Manga Drama Platform](http://reelmate.cn/) ⭐️ 7.0/10

On March 13, 2026, Wondershare partnered with Shengshu Technology's Vidu to launch China's first full-link premium AI manga drama creation platform, Wondershare Reelmate. One manga drama produced via this platform hit 200 million views just 29 hours after its public release. This launch marks the transition of AI manga drama production from small-scale workshop-style creation to industrial mass production, kicking off the large-scale commercialization phase of AIGC in the short content industry. It is expected to reshape the production logic and cost structure of the entire online short drama industry. The platform deeply integrates Shengshu Technology's leading ViduQ3 manga drama large model, solves the long-standing core pain point of cross-episode character inconsistency in AI-generated video, and reaches 80% first-draw availability for storyboards. It also achieves a 6x efficiency improvement for Agent-based storyboard creation for live-action dramas, and a 3-person team can deliver 75 full episodes of finished manga drama in just 5 days using the platform.

telegram · AI_News_CN · Mar 16, 01:27

**Background**: AI manga drama is a fast-growing high-potential segment in AIGC-powered content creation, and the industry projects the global AI manga drama market will exceed 100 billion yuan in size within the next three years. Before this launch, existing AI generation tools could not resolve core issues like inconsistent character appearance across episodes, which made large-scale industrial mass production of AI manga drama impossible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.3dmgame.com/news/202602/3937037.html">国产AI视频 模 型 ViduQ 3 火出圈 复刻高燃动 漫 战斗_3DM单机</a></li>
<li><a href="https://www.ithome.com/0/927/864.htm">绘梦工坊全链路 AI 漫剧创作平台：单项目制作周期压缩至 3 天，入局千...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2000469156861089713">AI漫剧制作工具大集合：11款漫剧制作软件，免费付费都有 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AIGC`, `#Generative AI`, `#AI Video Generation`, `#Content Creation`

---

<a id="item-20"></a>
## [Musk's xAI Restructures After Talent Exodus, Unveils Digital Optimus](https://www.aibase.com/zh/news/26228) ⭐️ 7.0/10

Elon Musk has acknowledged that most of xAI's founding team has departed his AI startup, apologized for early mismanagement, and is restructuring the team by re-engaging past qualified candidates and hiring new executives from AI coding tool startup Cursor. He also announced that the joint xAI-Tesla Digital Optimus AI project will open for user testing in 6 months. As one of the world's most high-profile valuable AI startups, xAI's massive talent turnover and restructuring highlights the intense competition for top AI talent across the global AI industry. The upcoming Digital Optimus joint project expands AI agent use cases into consumer automotive and productivity spaces, and will impact the development direction of consumer-facing AI products. Only two of xAI's original founding members remain with the company today, and xAI's valuation has reached 250 billion USD after its merger with SpaceX. Digital Optimus is a real-time intelligent AI system built to assist car owners with office tasks, and will eventually be deployed across Tesla's global supercharger network to provide massive distributed computing power.

telegram · AI_News_CN · Mar 16, 01:46

**Background**: xAI is an artificial intelligence startup founded by Elon Musk, which was recently merged into SpaceX after being acquired by the rocket company. Cursor is a popular AI-assisted code editor developed by San Francisco-based startup Anysphere, which has grown a large user base among developers competing with products like GitHub Copilot. Digital Optimus is a joint AI project between xAI and Tesla, also humorously nicknamed Macrohard as a jab at Microsoft, designed to automate office work for users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/03/13/elon-musk-xai-co-founders-spacex-ipo.html">Musk says xAI must be 'rebuilt' amid co-founder exodus ...</a></li>
<li><a href="https://www.teslarati.com/tesla-xai-digital-optimus-explained/">What is Digital Optimus? The new Tesla and xAI project explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Artificial Intelligence`, `#xAI`, `#Industry News`, `#Digital Optimus`, `#Team Restructuring`

---

<a id="item-21"></a>
## [Elon Musk vs OpenAI $134B lawsuit set for 2026 trial](https://www.aibase.com/zh/news/26232) ⭐️ 7.0/10

Elon Musk's $1340 billion lawsuit against OpenAI and Microsoft has been scheduled for an April 28, 2026 trial following a recent procedural court hearing. The judge rejected OpenAI's motion to dismiss key expert testimony from Musk's legal team, while publicly questioning the logic behind Musk's damage calculation. This high-stakes dispute involving top AI industry players is one of the most high-profile legal cases in the AI sector, and its outcome will likely set important precedents for future conflicts over founding missions and commercialization of major AI ventures. It will also directly shape the competitive landscape of the global generative AI industry, given that Musk's competing AI startup xAI is a core party behind the lawsuit. Musk claims OpenAI abandoned its original non-profit founding mission and accuses OpenAI CEO Sam Altman of fraud, while OpenAI has countered that the lawsuit is business-motivated harassment meant to give Musk's xAI a competitive advantage. The judge called Musk's $1340 billion damage calculation logic nearly "fabricated out of thin air", but ruled that the jury rather than the court should decide the ultimate validity of the expert testimony.

telegram · AI_News_CN · Mar 16, 02:03

**Background**: Elon Musk was an early founding contributor to OpenAI, providing $38 million in early funding to the organization before launching his own competing AI venture. xAI is Elon Musk's artificial intelligence startup, launched in July 2023, which is a wholly owned subsidiary of SpaceX and competes directly with OpenAI in the generative AI market. A motion to dismiss is a standard legal procedure in U.S. courts, where the defendant formally requests the judge to throw out part or all of a lawsuit due to claimed legal flaws in the plaintiff's case.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">xAI (company) - Wikipedia</a></li>
<li><a href="https://www.reuters.com/technology/elon-musks-ai-firm-xai-launches-website-2023-07-12/">Elon Musk launches AI firm xAI as he looks to take on OpenAI | Reuters</a></li>
<li><a href="https://legalterms.net/what-is-a-motion-to-dismiss/">What Is a Motion to Dismiss? - Legal Terms</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#OpenAI`, `#legal dispute`, `#Elon Musk`, `#Microsoft`

---

<a id="item-22"></a>
## [AI Treatment Shrinks Dog's Tumor By 75%](https://www.aibase.com/zh/news/26234) ⭐️ 7.0/10

Australian AI expert Paul Conyngham used multiple AI models including ChatGPT, AlphaFold and Grok to develop an experimental personalized cancer treatment for his dog with terminal mast cell cancer, leading to a reported 75% shrinkage of the tumor. Independent experts caution that the actual contribution of the AI-designed treatment remains unconfirmed, as the dog also received concurrent traditional therapy. This case serves as a notable early real-world demonstration of combining multiple AI tools for personalized cancer treatment, showing that AI can enable even non-medical experts to process complex biological information for personalized care. It also pushes AI-driven personalized medicine from the lab closer to real-world application, indicating potential fundamental improvements to future medical research and development efficiency. The project started in November 2024, with ChatGPT recommending tumor genome sequencing, AI identifying target proteins and screening FDA-approved drugs, and Grok completing the key vaccine design step. This type of personalized AI-designed treatment is estimated to cost between 20,000 and 50,000 USD, and proving its long-term safety and efficacy still faces huge unmet challenges.

telegram · AI_News_CN · Mar 16, 02:45

**Background**: AlphaFold is an AI system developed by Google DeepMind that predicts the 3D structure of proteins from their amino acid sequences with high accuracy, a breakthrough that earned its lead developers half of the 2024 Nobel Prize in Chemistry. Grok is a generative AI chatbot developed by xAI, which was launched in November 2023 and features real-time access to web information for various tasks. Personalized cancer treatment tailors interventions to an individual's specific tumor characteristics, which is widely expected to deliver better outcomes than generic one-size-fits-all treatments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI in healthcare`, `#personalized medicine`, `#generative AI`, `#AlphaFold`, `#cancer research`

---