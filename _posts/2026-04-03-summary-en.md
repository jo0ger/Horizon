---
layout: default
title: "Horizon Summary: 2026-04-03 (EN)"
date: 2026-04-03
lang: en
---

> From 47 items, 24 important content pieces were selected

---

1. [Google DeepMind releases open Gemma 4 models](#item-1) ⭐️ 9.0/10
2. [Google DeepMind launches open Gemma 4 LLMs](#item-2) ⭐️ 9.0/10
3. [Microsoft Releases Three Self-Developed AI Models](#item-3) ⭐️ 9.0/10
4. [Google launches open Gemma 4 model family](#item-4) ⭐️ 9.0/10
5. [Google Officially Releases Open-Source Gemma 4 LLM](#item-5) ⭐️ 9.0/10
6. [Google launches Gemma4 under Apache 2.0 license](#item-6) ⭐️ 9.0/10
7. [vLLM v0.19.0 officially released](#item-7) ⭐️ 8.0/10
8. [AMD launches open source Lemonade local LLM server](#item-8) ⭐️ 8.0/10
9. [Alibaba releases new Qwen3.6-Plus LLM](#item-9) ⭐️ 8.0/10
10. [Backdoor found in Nekogram 12.5.2 on Google Play](#item-10) ⭐️ 8.0/10
11. [Arm to sell AGI server CPU in China](#item-11) ⭐️ 8.0/10
12. [Microsoft Accelerates Self-Developed AI Models to 2027](#item-12) ⭐️ 8.0/10
13. [China launches first native physical AI platform ORCA Lab 1.0](#item-13) ⭐️ 8.0/10
14. [Apple LGTM enables 4K 3D rendering on Vision Pro](#item-14) ⭐️ 8.0/10
15. [Microsoft launches world's most accurate speech-to-text model](#item-15) ⭐️ 8.0/10
16. [Ex-Azure engineer criticizes trust-eroding decisions](#item-16) ⭐️ 7.0/10
17. [Hacker News discusses new Cursor 3 AI code editor](#item-17) ⭐️ 7.0/10
18. [Alibaba Launches Closed Qwen3.6-Plus for AI Agents](#item-18) ⭐️ 7.0/10
19. [Nvidia's China AI chip share falls to 55% in 2025](#item-19) ⭐️ 7.0/10
20. [ElevenLabs launches ElevenMusic AI music iOS app](#item-20) ⭐️ 7.0/10
21. [Hackers plant GitHub phishing traps after Claude Code leak](#item-21) ⭐️ 7.0/10
22. [OpenAI buys TBPN after shutting down Sora](#item-22) ⭐️ 7.0/10
23. [Google Vids adds Veo3.1 for prompt-controlled AI avatars](#item-23) ⭐️ 7.0/10
24. [Google plans 933MW gas plant for AI data centers](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google DeepMind releases open Gemma 4 models](https://deepmind.google/models/gemma/gemma-4/) ⭐️ 9.0/10

Google DeepMind has released the new open Gemma 4 large language model family, which adds native support for reasoning, multimodality, and tool use compared to prior versions. A high-engagement Hacker News thread hosts community testing results, benchmark comparisons, and shared quantized model versions plus run guides. As a major update to one of the most popular open large language model families, Gemma 4 brings strong benchmark performance and expanded capabilities that make capable open AI more accessible to developers and hobbyist users. This release continues the industry trend of more powerful open models that can run locally on consumer hardware. The Gemma 4 family includes multiple parameter sizes from 2B up to 31B, with mixture-of-experts variants like the 26B-a4b that deliver strong performance suitable for laptop local running. Some users report that the 31B checkpoint has a bug that causes it to output repeated separators regardless of prompts, though the hosted API version works correctly.

hackernews · jeffmcjunkin · Apr 2, 16:10

**Background**: Gemma is Google DeepMind's open large language model line designed for accessible development and deployment, built using the same research that powers Google's closed Gemini models. Open large language models are publicly released with permissive licenses that allow developers to run, modify, and deploy them locally instead of relying on third-party API services.

**Discussion**: Most community testers praise Gemma 4's performance, with one user noting the 26B-a4b variant produces the best local image generation result they have seen on a laptop, and community members have already shared pre-quantized versions to make local running easier. Some users shared benchmark comparisons with competing models like Qwen 3.5, noting that the entry-level Gemma 4 E4B is competitive with 8B to 9B models from other lineups, while the 31B model has a reported broken checkpoint for local use.

**Tags**: `#large language models`, `#open AI`, `#Google DeepMind`, `#Gemma 4`, `#machine learning releases`

---

<a id="item-2"></a>
## [Google DeepMind launches open Gemma 4 LLMs](https://simonwillison.net/2026/Apr/2/gemma-4/#atom-everything) ⭐️ 9.0/10

Google DeepMind has released Gemma 4, a family of four new permissively Apache 2.0 licensed open multimodal large language models optimized for on-device use with groundbreaking parameter efficiency. The model line includes 2B, 4B, 31B dense variants and a 26B-A4B Mixture-of-Experts variant, with native support for vision, video, and for the smaller sizes, native audio input. This release advances the fast-growing field of small capable on-device AI models, delivering high intelligence per parameter with a fully permissive open license that enables broad commercial and non-commercial use. It makes powerful multimodal reasoning AI accessible to developers for deployment on consumer devices without relying on cloud connectivity. The smaller 2B and 4B models use Per-Layer Embeddings (PLE) to reduce the effective parameter count loaded into memory during inference, while the 31B dense model currently has a broken GGUF build that fails to generate valid outputs. Common local LLM runners like LM Studio and Ollama do not yet support the native audio input feature of the smaller models.

rss · Simon Willison · Apr 2, 18:28

**Background**: Parameter efficiency refers to techniques that improve model performance without increasing the amount of computation required per inference. Mixture-of-Experts is a neural network architecture that routes each input token to a small subset of specialized sub-networks called experts, keeping total computation per token low while maintaining a large total parameter count for better knowledge capacity. Per-Layer Embeddings is an optimization technique that adds small per-layer token embeddings to boost model performance without increasing the number of active parameters that need to be loaded into memory during on-device inference.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Mixture of Experts (MoE) | Sebastian Raschka, PhD What Is Mixture of Experts (MoE)? How It Works (2026) How Mixture-of-Experts LLMs Work. An innovative approach to ... What Is Mixture of Experts (MoE)? How Modern LLMs Get ...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/gemma-3n">Gemma 3n model overview | Google AI for Developers</a></li>
<li><a href="https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/">Introducing Gemma 3n: The developer guide - Google Developers Blog</a></li>

</ul>
</details>

**Tags**: `#large-language-models`, `#open-ai`, `#google-deepmind`, `#on-device-ai`, `#parameter-efficient-models`

---

<a id="item-3"></a>
## [Microsoft Releases Three Self-Developed AI Models](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) ⭐️ 9.0/10

On April 2, Microsoft released three fully self-developed foundational AI models named MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2, covering speech transcription, speech generation, and image generation respectively. All three models are now available to developers and users via Microsoft Foundry and the new MAI Playground. This announcement marks Microsoft's major push into building its own competitive foundational AI lineup, reducing its reliance on external model partners and intensifying competition in the generative AI market. These models target high-value enterprise use cases and can improve the AI capabilities of Microsoft's own consumer and business products. MAI-Transcribe-1 outperforms OpenAI's Whisper-large-v3 across 25 major languages on the FLEURS benchmark, achieving an average word error rate of 3.8%. MAI-Voice-1 can generate 60 seconds of speech in 1 second and supports voice cloning with a few seconds of sample audio, while MAI-Image-2 has at least doubled generation speed compared to its predecessor and is already rolling out to Bing and PowerPoint.

telegram · zaihuapd · Apr 2, 11:31

**Background**: Microsoft Foundry, formerly known as Azure AI Studio, is a unified AI development platform on Microsoft Azure that allows developers to build, deploy, and scale AI applications with built-in enterprise security and governance tools. MAI Playground is a public testing space that lets developers and users try out Microsoft's new MAI models directly, and it is currently only available to users in the United States. FLEURS is a standard multilingual benchmark used to evaluate the performance of automatic speech recognition models across different languages.

<details><summary>References</summary>
<ul>
<li><a href="https://azure.microsoft.com/en-us/products/ai-foundry/">Microsoft Foundry | Microsoft Azure</a></li>
<li><a href="https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/">Today we're announcing 3 new world class MAI models, available in Foundry | Microsoft AI</a></li>
<li><a href="https://blog.csdn.net/gitblog_00009/article/details/150778442">Voxtral-Mini-3B-2507性能 基 准 测 试 -CSDN博客</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#foundation models`, `#microsoft`, `#speech ai`, `#image generation`

---

<a id="item-4"></a>
## [Google launches open Gemma 4 model family](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) ⭐️ 9.0/10

Google has officially released its open large language model family Gemma 4, which comes in four different sizes covering devices from mobile phones to high-end workstations and is released under the permissive Apache 2.0 license. The new model family supports multi-modal inputs and advanced AI agent workflows, with smaller variants optimized for on-device offline operation. This release expands access to high-performance open AI by bringing Google-grade model capabilities to edge devices, and strengthens Google's position in the fast-growing open AI ecosystem by offering permissive licensing that allows commercial and custom modification. It meets growing developer and enterprise demand for flexible, deployable open model options that work across different hardware. The four model variants are 2B E2B, 4B E4B, 26B MoE, and 31B Dense, with 2B and 4B variants natively supporting audio input in addition to image and video processing. The 31B dense model currently ranks third among open models on the Arena AI text benchmark, while the 26B MoE model ranks sixth, and the first-generation Gemma family has already surpassed 400 million total downloads and 100,000 derivative versions.

telegram · zaihuapd · Apr 2, 16:12

**Background**: Gemma is Google's family of open large language models built on the same underlying technology as Google's closed Gemini models, designed to give developers open and customizable alternatives to proprietary models. MoE, short for Mixture of Experts, is a neural network architecture that splits model computation across smaller specialized sub-networks called experts, to achieve higher overall performance without proportional increases in inference cost. On-device AI refers to AI models that run directly on local end-user hardware such as mobile phones or laptops instead of relying on cloud servers, enabling offline use and better data privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Gemma 4 : Our most capable open models to date</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/On-device_artificial_intelligence">On-device artificial intelligence</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#open AI`, `#Gemma 4`, `#on-device AI`, `#Google`

---

<a id="item-5"></a>
## [Google Officially Releases Open-Source Gemma 4 LLM](https://www.aibase.com/zh/news/26812) ⭐️ 9.0/10

Google officially launched its new generation open-source large model Gemma 4 on April 3, 2025 Beijing time, which includes four different model sizes and supports multi-modal input and end-side deployment. The 31B dense version of Gemma 4 ranks third among all open-source models on the Arena AI text ranking, with leading performance in logic reasoning and function calling. As a major new open-source large model from Google released under the permissive Apache 2.0 license, Gemma 4 lowers the barrier for developers to build cutting-edge local, privacy-preserving AI applications, and will bring far-reaching impact to the global open-source AI ecosystem. It also sets a new standard for open-source models to power autonomous agent workflows, advancing the development of on-device AI. Gemma 4 is built on the Gemini 3 technology stack, with four variants: 2.3B E2B, 4.5B E4B, 26B MoE, and 31B dense; the 31B non-quantized model can run on a single 80GB H100 GPU, while the quantized version works on consumer graphics cards. The small E2B and E4B variants natively support voice input, can run on Raspberry Pi and smartphones with low latency via PLE embedding technology, and support 128K long context windows.

telegram · AI_News_CN · Apr 3, 01:02

**Background**: Apache 2.0 is a permissive free software license that allows users to use, modify, distribute, and redistribute modified versions of the code for any purpose, making it friendly for both commercial and non-commercial open-source projects. Mixture of Experts (MoE) is a large language model architecture that improves model performance while keeping computational cost low by activating only a small subset of model parameters (called experts) for each input. Embeddings are vector representations of text and other data that power core AI features like retrieval-augmented generation and AI agent memory.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>

</ul>
</details>

**Tags**: `#large language model`, `#open-source AI`, `#Gemma 4`, `#Google AI`, `#end-side AI`

---

<a id="item-6"></a>
## [Google launches Gemma4 under Apache 2.0 license](https://www.aibase.com/zh/news/26816) ⭐️ 9.0/10

Google has officially released its new generation open large language model Gemma4 under the permissive Apache 2.0 license, shifting from the previous restrictive custom license the company used for earlier Gemma versions. The new model delivers improved performance on standard benchmarks and better compatibility with existing developer ecosystems. This license change removes major legal barriers to commercial and open-source development based on Gemma, opening up high-quality Google-developed AI technology to more developers and small and medium-sized enterprises. It also reflects a major strategic shift by Google in open AI development, which will affect the competitive landscape of the global open large language model ecosystem. Gemma4 supports offline local deployment across multiple devices including servers, smartphones and Raspberry Pi, and it can seamlessly integrate with existing ecosystems that use the Apache 2.0 license such as Android, lowering the deployment threshold for developers.

telegram · AI_News_CN · Apr 3, 01:10

**Background**: Gemma is a family of open large language models developed by Google DeepMind and other Google teams, named after the Latin word for precious stone. The Apache 2.0 license is a widely accepted permissive free software license that allows users to freely use, modify, and distribute the licensed software for any purpose, including commercial applications.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/">Google announces Gemma 4 open AI models, switches to Apache 2 ...</a></li>
<li><a href="https://www.zdnet.com/article/google-gemma-4-fully-open-source-powerful-local-ai/">Google's Gemma 4 model goes fully open-source and ... - ZDNET</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open-source AI`, `#large language model`, `#Google Gemma`, `#Apache 2.0 license`

---

<a id="item-7"></a>
## [vLLM v0.19.0 officially released](https://github.com/vllm-project/vllm/releases/tag/v0.19.0) ⭐️ 8.0/10

The vllm-project has released version 0.19.0 of the open-source vLLM large language model inference engine on GitHub. This is a feature-rich minor release that brings important incremental improvements to the tool. vLLM is one of the most widely used, high-impact open-source tools for LLM inference and serving in the global AI/ML community. Improvements to this critical tool benefit thousands of developers and organizations that run LLM deployments for research or production. As a minor feature release, v0.19.0 focuses on incremental improvements to the existing vLLM codebase rather than large-scale architectural changes, building on the project's already industry-leading throughput and memory efficiency.

github · khluu · Apr 3, 02:19

**Background**: vLLM is an open-source high-throughput, memory-efficient inference and serving engine for large language models originally developed by the Sky Computing Lab at UC Berkeley. Its core innovation is the PagedAttention memory management algorithm, which lets it deliver up to 24x higher inference throughput than standard HuggingFace pipelines. It is now a community-driven project used for both research and large-scale production deployments, and has gained over 74,900 GitHub stars as of 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory ...</a></li>
<li><a href="https://vllm.ai/">vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/">vLLM</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#machine learning inference`, `#open source software`, `#release announcement`

---

<a id="item-8"></a>
## [AMD launches open source Lemonade local LLM server](https://lemonade-server.ai/) ⭐️ 8.0/10

AMD has officially announced Lemonade, an open source local multimodal LLM inference server that supports running inference across AMD CPU, GPU, and NPU hardware. The project unifies inference support for text, image, and audio AI models across AMD's consumer and enterprise hardware lines. This release addresses longstanding pain points with the ROCm local inference experience for AMD hardware, providing an official, turnkey solution that simplifies dependency and driver setup for local AI. It also leverages AMD's integrated NPUs to enable lower-power, faster local AI inference on modern Ryzen systems, pushing forward the ecosystem for on-device local AI. Lemonade supports multiple backends including ROCm, Vulkan, CPU, GPU, and NPU, and covers capabilities including TTS, STT, text generation, image generation, and image editing. The NPU-specific kernels and models used by Lemonade remain proprietary and are not released as open source software.

hackernews · AbuAssar · Apr 2, 11:04

**Background**: An NPU, or neural processing unit, is a specialized hardware accelerator designed to speed up neural network inference operations with lower power consumption than general-purpose CPUs or GPUs. A multimodal LLM server can handle and run inference across multiple types of AI data, including text, images, and audio, enabling integrated local AI workflows. ROCm is AMD's open source software platform for GPU-accelerated high-performance computing and machine learning inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/lemonade-for-local-ai.html">Lemonade by AMD: A Unified API for Local AI Developers</a></li>
<li><a href="https://medium.com/@waranmadesh826/what-is-an-npu-and-why-it-matters-in-the-ai-era-36b83590323b">What Is an NPU and Why It Matters in the AI Era | Medium</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-llm">What is a multimodal LLM (MLLM)? - IBM</a></li>

</ul>
</details>

**Discussion**: Long-time users praise Lemonade's steady development pace and broad feature set for AMD hardware, noting it already supports most common local AI workloads on modern AMD systems. Many commenters welcome the official tooling to fix poor ROCm user experience, but questions remain about real-world NPU inference performance compared to dedicated AMD dGPUs. Some community members have noted the proprietary NPU components and expressed a desire for fully open source NPU support.

**Tags**: `#local LLMs`, `#AMD`, `#open source`, `#inference server`, `#AI runtime`

---

<a id="item-9"></a>
## [Alibaba releases new Qwen3.6-Plus LLM](https://t.me/zaihuapd/40658) ⭐️ 8.0/10

Alibaba has released a new generation of its Qwen large language model, Qwen3.6-Plus, which delivers large performance gains over previous versions. Its programming performance approaches the top-tier Claude family of models, and it enables usable 'atmosphere programming' where short natural language prompts drive autonomous end-to-end AI coding. This release marks meaningful progress for open-capable large language models in the area of practical AI-powered software engineering, bringing end-to-end autonomous AI coding closer to real-world usability. It narrows the performance gap between domestic Chinese large models and top-tier global coding-focused models, offering developers a more capable local option for AI-assisted development. Qwen3.6-Plus has native multimodal understanding and reasoning capabilities, and its programming performance ranks close to Claude on two authoritative benchmarks, the agentic coding SWE-bench and the real-world agent task benchmark Claw-Eval. In real testing scenarios like front-end web development and repository-level complex tasks, the model can independently break down tasks, plan workflows, test and revise code until the task is fully completed.

telegram · zaihuapd · Apr 2, 05:02

**Background**: SWE-bench is a standard benchmark that tests large language models' ability to fix real-world coding issues collected from GitHub, measuring what percentage of problems a model can resolve with generated patches. Claw-Eval is an end-to-end benchmark for evaluating AI agents on real-world tasks, with all tasks human-verified to accurately test an agent's full task completion capability. Unlike the established Atmosphere Framework for Java real-time applications, 'atmosphere programming' in this context refers to a workflow where simple natural language prompts drive AI to complete full coding projects autonomously.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/swe-bench-verified">SWE-Bench Verified Leaderboard</a></li>
<li><a href="https://dev.to/sky_05/new-benchmark-for-open-source-agents-what-is-claw-eval-how-step-35-flash-secured-the-2-spot-592d">New Benchmark for Open-Source Agents: What is Claw-Eval? How ...</a></li>
<li><a href="https://github.com/Atmosphere/atmosphere">GitHub - Atmosphere/atmosphere: Real-time transport layer for ...</a></li>

</ul>
</details>

**Tags**: `#large language model`, `#Qwen`, `#AI coding`, `#multimodal AI`, `#model release`

---

<a id="item-10"></a>
## [Backdoor found in Nekogram 12.5.2 on Google Play](https://thebadinteger.github.io/nekogram-phone-exfiltration/) ⭐️ 8.0/10

Security researchers have discovered an obfuscated backdoor in the Google Play version of third-party Telegram client Nekogram 12.5.2 that silently steals logged-in users' phone numbers and sends them to a developer-controlled Telegram bot. The malicious code is not included in the project's public GitHub source code, and the developer's explanation of the bot's purpose contradicts the actual behavior of the code. This is a confirmed supply chain attack targeting users of a widely distributed open-source mobile app, meaning users who trust the project's open-source model cannot assume distributed releases match the published code. This incident puts the app's large user base at risk of identity and account exposure, and highlights risks of trusting pre-compiled app releases even for open-source projects. The backdoor is located in the obfuscated Extra.java file, which extracts phone numbers from up to 8 logged-in accounts and exfiltrates the data via encrypted Telegram inline queries to the bot @nekonotificationbot. Only the pre-built APK distributed on Google Play contains the backdoor; versions self-compiled from the public GitHub source code do not include the malicious code.

telegram · zaihuapd · Apr 2, 12:58

**Background**: Nekogram is an open-source third-party client for the Telegram messaging platform that offers additional customization features not available in the official client. Third-party Telegram clients are popular among users who want more control over their app experience, and many users trust them due to their open-source licensing. Obfuscation is a technique commonly used by malware to hide malicious code and avoid detection by security tools. Telegram inline queries are a feature that allows bots to receive requests directly from user input fields in any chat.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Nekogram/Nekogram?search=1">Nekogram / at main · Nekogram / Nekogram · GitHub</a></li>
<li><a href="https://core.telegram.org/bots/inline">Inline Bots</a></li>
<li><a href="https://attack.mitre.org/techniques/T1027/">Obfuscated Files or Information, Technique T1027 - MITRE ATT&CK®</a></li>

</ul>
</details>

**Tags**: `#security vulnerability`, `#malware`, `#telegram client`, `#supply chain attack`

---

<a id="item-11"></a>
## [Arm to sell AGI server CPU in China](https://www.tomshardware.com/pc-components/cpus/arm-to-sell-its-new-agi-cpu-in-china-we-would-expect-the-demand-for-this-product-to-be-just-as-strong-in-china-as-it-is-in-the-rest-of-the-world) ⭐️ 8.0/10

Arm announced it will sell its newly launched 136-core Neoverse V3-based AGI server CPU to the Chinese market, and confirmed the finished processor complies with current US export control rules, while the Neoverse V3 IP core cannot be licensed to Chinese developers. This decision creates a workaround for existing semiconductor export restrictions, which helps sustain Arm's market share in China while meeting China's growing demand for AI infrastructure hardware, and impacts the global AI hardware supply chain and export regulation landscape. This 136-core AGI server CPU is Arm's first proprietary data center chip in 35 years, designed for infrastructure and supercomputing artificial general intelligence workloads, and finished chips are subject to different export control rules than IP core licenses.

telegram · zaihuapd · Apr 3, 02:30

**Background**: Neoverse is a line of 64-bit Arm CPU cores designed for data centers, edge computing and high performance computing, and Neoverse V3 is the latest generation targeted at advanced AI and high-performance systems. A semiconductor IP core is a pre-designed reusable logic unit that developers can license to build their own chips, while a finished server CPU is a complete processor ready for use in servers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_Neoverse">ARM Neoverse - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_intellectual_property_core">Semiconductor intellectual property core - Wikipedia</a></li>
<li><a href="https://awesomeagents.ai/news/arm-agi-cpu-first-chip-35-years/">Arm Launches AGI CPU , Its First Chip in 35 Years | Awesome Agents</a></li>

</ul>
</details>

**Tags**: `#Semiconductors`, `#AI Hardware`, `#Export Control`, `#Server CPU`

---

<a id="item-12"></a>
## [Microsoft Accelerates Self-Developed AI Models to 2027](https://www.aibase.com/zh/news/26817) ⭐️ 8.0/10

Microsoft is accelerating its self-developed large AI model strategy, and aims to achieve world-leading text, image and audio processing capabilities as well as full AI technology autonomy by 2027 after its partnership agreement with OpenAI was relaxed. Microsoft has already obtained early results, with a new competitive speech transcription model released on April 2 that outperforms existing products in 11 out of 25 tested major languages. 这一战略转变标志着微软从AI技术集成商转型为拥有核心自主能力的顶尖AI研发商，将重塑全球生成式AI行业的竞争格局。同时它也会降低微软对OpenAI等外部合作伙伴的长期依赖，为自身的AI产品开发带来更大的自由度。 Microsoft is supporting this R&D effort by massively deploying NVIDIA's latest GB200 computing clusters, and plans to boost its underlying computing power to a world-leading scale within the next 12 to 18 months. The plan's core goal is to build a cutting-edge AI system that can compete with OpenAI and Anthropic's models.

telegram · AI_News_CN · Apr 3, 01:22

**Background**: Microsoft has been a key partner and major investor of OpenAI for many years, and its existing generative AI products such as Copilot have long relied on OpenAI's model technologies. The partnership agreement between the two companies originally imposed restrictions on Microsoft's independent research and development of large-scale general AI models, and the agreement adjustment last year removed these restrictions.

**Tags**: `#Large Language Models`, `#Microsoft`, `#AI Strategy`, `#Self-developed AI`, `#Generative AI`

---

<a id="item-13"></a>
## [China launches first native physical AI platform ORCA Lab 1.0](https://www.aibase.com/zh/news/26820) ⭐️ 8.0/10

Shanghai Songying Technology has officially released ORCA Lab 1.0, China's first native physical AI developer platform built specifically for individual developers and small lightweight teams. The platform lowers the barrier to embodied intelligence research through core features including zero-code workflow, low cost, and single-machine operation. This release democratizes access to physical AI and embodied intelligence research, which was previously limited to large tech companies and top research institutions due to its high cost and high hardware requirements. It opens up the field to more individual creators, accelerating the development and commercialization of China's embodied intelligence industry. ORCA Lab 1.0 breaks the past dependence of robot model training on high-performance computing clusters, allowing developers to run the entire workflow smoothly on an ordinary laptop. It supports full lifecycle development covering robot design, simulation training and real robot deployment, and provides open APIs to encourage the construction of an open developer ecosystem.

telegram · AI_News_CN · Apr 3, 01:35

**Background**: Physical AI, also closely linked to embodied intelligence, refers to AI systems that interact with the physical world, which traditionally requires complex dynamic simulation and massive computing power, resulting in very high research and development costs. A digital twin robot is a virtual mirror copy of a physical robot, which allows developers to test and train models in a simulated environment to reduce reliance and wear on expensive physical hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/delltechnologies/2025/12/17/the-ai-native-factory-remaking-manufacturing-with-physical-ai/">Dell Technologies BrandVoice: The AI-Native Factory: Remaking Manufacturing With Physical AI</a></li>
<li><a href="https://eureka.patsnap.com/article/what-is-a-digital-twin-in-robotics">What is a digital twin in robotics? - eureka.patsnap.com</a></li>

</ul>
</details>

**Tags**: `#Physical AI`, `#Embodied Intelligence`, `#Developer Platform`, `#AI Tools`

---

<a id="item-14"></a>
## [Apple LGTM enables 4K 3D rendering on Vision Pro](https://www.aibase.com/zh/news/26822) ⭐️ 8.0/10

Apple researchers in collaboration with the University of Hong Kong have launched the LGTM (Less Gaussians, Texture More) framework that fixes 3D Gaussian Splatting's high-resolution computational bottleneck, enabling 4K real-time 3D rendering on Apple Vision Pro with reduced computational load. This breakthrough removes a major barrier to high-fidelity real-time 3D content for spatial computing devices like Apple Vision Pro, which can deliver more immersive and realistic experiences for end users and advance the practical development of the spatial computing industry. LGTM works via a two-step process: it first learns basic scene geometry from low-resolution images, then uses a dedicated appearance network to extract fine details from high-resolution source images as textures that are overlaid on the simple geometry. It can also upgrade existing 3D Gaussian Splatting models such as NoPoSplat and DepthSplat.

telegram · AI_News_CN · Apr 3, 02:18

**Background**: 3D Gaussian Splatting is a popular 3D reconstruction and rendering technique introduced in 2023 that converts multiple 2D images into a 3D scene representation for fast real-time rendering, outperforming older methods like NeRF in speed and quality. Traditional feed-forward 3D Gaussian Splatting requires quadratic growth in computation as rendering resolution increases, making 4K real-time rendering on high-resolution headsets infeasible for resource-constrained mobile devices.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.25745v1">LGTM enables feed-forward 4K textured Gaussian splatting.</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>
<li><a href="https://alanhou.org/blog/arxiv-less-gaussians-texture-more-4k-feed/">LGTM: Breaking the 4K Barrier in Feed-Forward 3D Gaussian Splatting / LGTM：突破前馈式3D高斯泼溅的4K分辨率瓶颈 | Alan Hou</a></li>

</ul>
</details>

**Tags**: `#3D Gaussian Splatting`, `#3D Rendering`, `#Spatial Computing`, `#Apple Vision Pro`, `#Computer Graphics`

---

<a id="item-15"></a>
## [Microsoft launches world's most accurate speech-to-text model](https://www.aibase.com/zh/news/26823) ⭐️ 8.0/10

Microsoft has launched MAI-Transcribe-1, a new speech-to-text model that achieves a 3.9% average word error rate across 25 languages, outperforming OpenAI Whisper-large-v3 and Google Gemini 3.1 Flash. The model is now available via the Microsoft Foundry platform for batch transcription at a price of $0.36 per hour of audio. This new model sets a new accuracy benchmark for multilingual automatic speech recognition, pushing the state of the art for transcription technology that powers many commercial AI applications. It gives developers and enterprises a higher-performance, competitively priced alternative to existing leading models from OpenAI and Google. MAI-Transcribe-1 scored first in transcription accuracy for 11 out of its 25 supported languages on the FLEURS standard benchmark, and its batch transcription speed is 2.5 times faster than the existing Microsoft Azure Fast product, but the current release does not yet support real-time transcription or speaker separation features which Microsoft plans to add in future updates.

telegram · AI_News_CN · Apr 3, 02:30

**Background**: MAI-Transcribe-1 is the third model in Microsoft's self-developed MAI series, following the MAI-Voice-1 speech synthesis model and the MAI-Image-2 image generation model. FLEURS is a widely accepted industry standard benchmark for evaluating multilingual automatic speech recognition model performance. Microsoft Foundry is Microsoft's unified platform that lets developers build, manage, and deploy AI applications.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/">State of the Art Speech Recognition with MAI-Transcribe-1 | Microsoft AI</a></li>
<li><a href="https://arxiv.org/abs/2205.12446">[2205.12446] FLEURS : Few-shot Learning Evaluation of Universal...</a></li>
<li><a href="https://www.logicintelligence.com/microsoft-foundry/">Microsoft Foundry - Logic Intelligence</a></li>

</ul>
</details>

**Tags**: `#speech recognition`, `#large language model`, `#automatic speech transcription`, `#Microsoft`, `#multimodal AI`

---

<a id="item-16"></a>
## [Ex-Azure engineer criticizes trust-eroding decisions](https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion) ⭐️ 7.0/10

A former Azure Core engineer has published a public critique of internal Microsoft decisions that they claim eroded customer and developer trust in Azure, and the post has sparked widespread corroborating discussion on Hacker News. This insider exposé provides rare unfiltered insight into organizational issues at one of the world's top three public cloud platforms, affecting millions of cloud developers and enterprise customers that rely on Azure globally. The author stated they first sent their concerns to Microsoft's CEO in January 2025 and escalated to the company's board after receiving no response before publishing the public critique.

hackernews · axelriet · Apr 2, 16:00

**Background**: Azure Core is the foundational component of Microsoft Azure, which can refer both to the core underlying infrastructure of the Azure cloud platform and the shared core library that powers all official Azure client SDKs. Microsoft Azure is one of the largest global public cloud service providers, alongside Amazon Web Services and Google Cloud.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/overview/azure/core-readme?view=azure-dotnet">Azure Core shared client library for .NET - Azure for .NET Developers | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/">Describe the core architectural components of Azure - Training | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: Many current and former Azure users and developers agreed with the critique, sharing their own negative experiences ranging from poor UI and outdated documentation to cross-user data leaks in Azure OpenAI. Some commentators questioned whether the author was a genuine whistleblower or a disgruntled ex-employee, while another former Azure engineer argued the author's dramatic writing undermines their core points.

**Tags**: `#Azure`, `#Cloud Computing`, `#Microsoft`, `#Software Engineering`, `#Industry Insider`

---

<a id="item-17"></a>
## [Hacker News discusses new Cursor 3 AI code editor](https://cursor.com/blog/cursor-3) ⭐️ 7.0/10

Anysphere has released the major new version Cursor 3 of its AI-powered code editor, sparking a wide-ranging Hacker News discussion where users share their real-world experiences comparing Cursor to competitor Claude Code. As a popular AI-assisted development tool, Cursor 3's new agent-first design direction shapes the evolving landscape of AI developer tools, and community feedback reflects what developers actually want from AI coding workflows. Cursor 3 is a fork of Visual Studio Code with proprietary AI features, and this major update adds a new Agents Window and design mode focused on agent-driven development workflows, with support for local machines and remote SSH environments.

hackernews · adamfeldman · Apr 2, 18:13

**Background**: Cursor is a proprietary AI-powered code editor developed by San Francisco startup Anysphere, founded in 2022. Claude Code is Anthropic's standalone agentic coding tool that can understand entire codebases, edit files and run terminal commands to help developers ship code faster.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor) - Wikipedia</a></li>
<li><a href="https://cursor.com/blog/cursor-3">Meet the new Cursor · Cursor</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: Opinions are split: some long-term users find Cursor more efficient than Claude Code even with its new default Composer 2 model, while others combine free Cursor autocomplete with Claude Code and question Cursor's paid subscription value. Multiple users expressed concern that Cursor 3 is shifting toward an agent-first, chat-centric design that pushes less focus on the code itself, which many developers dislike.

**Tags**: `#AI code editor`, `#developer tools`, `#Cursor`, `#AI-assisted development`

---

<a id="item-18"></a>
## [Alibaba Launches Closed Qwen3.6-Plus for AI Agents](https://qwen.ai/blog?id=qwen3.6) ⭐️ 7.0/10

Alibaba has launched Qwen3.6-Plus, a new closed-hosted large language model optimized for real-world AI agents. This release marks Qwen's strategic shift away from the open-weight model releases it was previously known for. This shift from a popular open-weight LLM provider to closed hosted services signals a broader industry trend of AI vendors moving to monetize their model development after building brand recognition through open releases. It impacts AI developers and researchers who relied on Qwen's open access for experimentation and customization. Qwen3.6-Plus does not publicly disclose its parameter count, and its official benchmark comparisons used older versions of competing models (Anthropic Claude Opus 4.5 instead of 4.6, Google Gemini Pro 3.0 instead of 3.1). A free preview of the model is currently available via OpenRouter's API.

hackernews · pretext · Apr 2, 14:28

**Background**: An open-weight large language model publishes its trained model parameters to the public, allowing developers to run, modify, and deploy the model locally. A closed-hosted LLM keeps model weights and core code proprietary, and only provides access via a cloud API managed by the developer company.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3.6-plus-preview:free">Qwen3.6 Plus Preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://www.metriccoders.com/post/closed-source-large-language-models">Closed Source Large Language Models - metriccoders.com</a></li>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>

</ul>
</details>

**Discussion**: Many community members expressed anger at Qwen's strategic shift, noting the brand was built on goodwill from open smaller model releases. Some users argued that criticism of Qwen's benchmark comparison methodology is overblown, given how frequently new model versions are released in the AI industry. Other users tested the model, noting that the free inference option on OpenRouter produces usable outputs that are hard to beat at a $0 price point.

**Tags**: `#large language models`, `#Qwen`, `#AI agents`, `#open AI`, `#machine learning`

---

<a id="item-19"></a>
## [Nvidia's China AI chip share falls to 55% in 2025](https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips) ⭐️ 7.0/10

In 2025, Nvidia's AI chip market share in China dropped to 55% from 95% before U.S. export sanctions, while domestic Chinese vendors captured 41% of the market, with Huawei holding nearly 20% as the top domestic supplier. Huawei also recently launched the Atlas 350 AI accelerator, which claims performance close to three times that of Nvidia's H20 chip. This major market shift shows that U.S. export sanctions and China's domestic semiconductor localization policy are rapidly reshaping the global AI chip supply chain, and it will impact the development strategies of both global chipmakers and Chinese AI industry players. In 2025, Nvidia shipped around 2.2 million AI chips to China, while domestic vendors shipped a combined 1.65 million units; after Huawei, the next largest domestic players are Tencent's Pingtouge, Baidu's Kunlunxin, and Cambricon, in that order. The H20 is currently the most advanced AI chip Nvidia is legally allowed to export to China under U.S. restrictions.

telegram · zaihuapd · Apr 2, 06:08

**Background**: Starting in October 2022, the United States implemented successive export sanctions to restrict the sale of advanced AI chips and related semiconductor technology to China, which cut off Nvidia's access to China's high-end AI chip market. The Chinese government has since pushed domestic data centers to prioritize using locally made chips to support the development of China's domestic semiconductor industry. The H20 is an Nvidia AI chip specifically designed to comply with current U.S. export restrictions for the Chinese market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/opinion/articles/2025-04-14/could-nvidia-ceo-s-mar-a-lago-meal-cost-the-west-its-ai-lead">Nvidia 's Mar-a-Lago Dinner Could Be a Raw Deal for US AI - Bloomberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China">United States New Export Controls on Advanced Computing ... - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#semiconductor market`, `#Nvidia`, `#domestic chips`, `#trade policy`

---

<a id="item-20"></a>
## [ElevenLabs launches ElevenMusic AI music iOS app](https://www.aibase.com/zh/news/26811) ⭐️ 7.0/10

Leading generative voice AI firm ElevenLabs launched the iOS app ElevenMusic on April 1, 2025, officially entering the AI music creation market to compete with platforms like Suno and Udio. This launch marks the company's strategic transition from a single voice AI provider to a full-stack creative platform. 这次入场加剧了快速增长的AI音乐生成市场的竞争，将重塑生成音频领域的创作者经济，同时帮助ElevenLabs拓展业务范围，降低音频模型商品化的风险。它也为寻求易用AI创作工具的普通创作者和消费者带来了更多选择。 ElevenMusic supports natural language prompt-based custom music generation with adjustable track length, lyrics, and artistic style, and integrates social streaming features like real-time radio and mood-based playlists. It uses a freemium model: free users can generate 7 tracks per day, while the $9.99 monthly pro plan offers 500 tracks per month and 500GB of storage.

telegram · AI_News_CN · Apr 3, 01:02

**Background**: ElevenLabs was originally a leading pioneer in generative AI voice technology focused on creating natural, expressive AI speech solutions for content production. Suno and Udio are two existing leading platforms in the AI music generation space that allow users to create custom high-quality music from simple text prompts. ElevenLabs completed a Series C funding round in February 2025 with a valuation of $11 billion, giving it capital to expand into new generative audio verticals.

<details><summary>References</summary>
<ul>
<li><a href="https://elevenlabscn.com/about.html">ElevenLabs - 关于我们</a></li>
<li><a href="https://suno.com/">Suno | AI Music Generator</a></li>
<li><a href="https://www.udio.com/">Udio | AI Music Generator - Official Website</a></li>

</ul>
</details>

**Tags**: `#AI music generation`, `#generative AI`, `#product launch`, `#ElevenLabs`

---

<a id="item-21"></a>
## [Hackers plant GitHub phishing traps after Claude Code leak](https://www.aibase.com/zh/news/26813) ⭐️ 7.0/10

After Anthropic accidentally leaked Claude Code source code via human error, hackers have created SEO-optimized fake GitHub repositories offering fake unlocked enterprise versions of the leaked code to distribute the Vidar information-stealing malware targeting developers. This attack targets developers who are actively seeking the leaked Claude Code source code, and it demonstrates how attackers can quickly exploit recent public security incidents to launch secondary phishing campaigns that threaten sensitive developer data. The malware installed on infected devices includes the mature Vidar infostealer that steals browser credentials, cryptocurrency wallet data and other sensitive information, plus the GhostSocks proxy tool that establishes a secret channel for remote control and data exfiltration. At least two similar fake repositories have been found, and the malicious archives are updated very frequently to bypass basic security detection.

telegram · AI_News_CN · Apr 3, 01:02

**Background**: Claude Code is an agentic AI coding tool developed by Anthropic for software developers. Vidar is an established information-stealing malware that has been distributed as a malware-as-a-service since 2018, and GhostSocks is a proxy tool commonly used by attackers to maintain stealthy access to compromised networks.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/what-is-vidar-malware/">What is Vidar Malware? - Check Point Software</a></li>
<li><a href="https://www.darktrace.com/blog/phantom-footprints-tracking-ghostsocks-malware">Tracking & Detecting GhostSocks Malware - Darktrace</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#phishing`, `#cybersecurity`, `#Claude Code`, `#malware`

---

<a id="item-22"></a>
## [OpenAI buys TBPN after shutting down Sora](https://www.aibase.com/zh/news/26815) ⭐️ 7.0/10

One month after shutting down its Sora AI video application, OpenAI announced the completion of its acquisition of major technology business podcast TBPN. This acquisition marks OpenAI's strategic shift from developing AI tools to controlling the public narrative around AI development. This move represents a new trend of AI companies expanding into media to shape public opinion and regulatory narratives around AGI development, raising new challenges for regulators and the general public. If the trend continues, it may reshape how the public understands and regulates artificial general intelligence. OpenAI has promised to maintain TBPN's editorial independence, allowing the podcast to continue making independent editing decisions and selecting guests independently. According to industry analysis, Sora was shut down primarily because it cost $1 million per day to operate and saw its user base cut in half, making it unable to turn a profit.

telegram · AI_News_CN · Apr 3, 01:10

**Background**: TBPN is a popular daily technology podcast with a large cult following in Silicon Valley, featuring high-profile interviews with top tech industry leaders including Mark Zuckerberg and Mark Cuban. In the context of this news, AGI stands for artificial general intelligence, which refers to the hypothetical AI that has the ability to understand or learn any intellectual task that a human being can.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inc.com/ben-sherry/openai-acquires-tbpn-the-irreverent-tech-podcast-with-a-cult-following/91326232">OpenAI Acquires TBPN, the Irreverent Tech Podcast With a Cult ...</a></li>
<li><a href="https://podcast.app/tbpn-p6101625">TBPN podcast - Free on The Podcast App OpenAI acquires popular tech podcast TBPN - CNBC TBPN - Podcast - Apple Podcasts TBPN podcast - Free on The Podcast App TBPN podcast - Free on The Podcast App TBPN podcast - Free on The Podcast App OpenAI acquires TBPN, the buzzy founder-led business talk ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI industry`, `#corporate strategy`, `#media acquisition`, `#AGI`

---

<a id="item-23"></a>
## [Google Vids adds Veo3.1 for prompt-controlled AI avatars](https://www.aibase.com/zh/news/26818) ⭐️ 7.0/10

Google announced a major upgrade for its enterprise video creation app Vids on April 2, integrating the Veo3.1 AI video generation model to enable text-prompt controlled interactive AI avatars, and added new workflow features including direct YouTube export and a new Chrome screen recording extension. Microsoft also released three competing MAI multi-modal foundation models on the same day. This update marks progress in controllable AI video generation, pushing AI video tools from basic content creation toward professional automated direction, and reshaping the cost structure and creative boundaries of enterprise content production. The concurrent release of competing models also highlights the accelerating competition in the generative AI industry. The new feature allows users to command AI avatars to complete specific interactions with props and products via text prompts while maintaining consistent character visuals, and the integration supports generating 8-second video clips. Free users get 10 generation quotas per month, while enterprise advanced accounts get up to 1000 quotas per month.

telegram · AI_News_CN · Apr 3, 01:22

**Background**: Google Vids is an enterprise AI video creation tool launched by Google in 2024, which has added 3D cartoon avatars and multi-language support through rapid iteration. Veo3.1 is Google DeepMind's latest AI video generation model, capable of generating high-quality cinematic videos from text or image prompts with strong character consistency. Lyria3 is Google DeepMind's most advanced music generation model that produces high-quality stereo audio from prompts, and it was already integrated into Vids before this update.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yolly.ai/veo-3.1">Google Veo 3 . 1 — AI Video Generator | Yolly AI</a></li>
<li><a href="https://deepmind.google/models/lyria/">Lyria 3 — Google DeepMind</a></li>
<li><a href="https://www.forbes.com/sites/janakirammsv/2026/04/02/microsoft-builds-its-own-ai-model-stack-to-reduce-openai-dependence/">Microsoft Builds Its Own AI Model Stack To Reduce OpenAI ...</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#Google Vids`, `#generative AI`, `#AI avatars`

---

<a id="item-24"></a>
## [Google plans 933MW gas plant for AI data centers](https://www.aibase.com/zh/news/26821) ⭐️ 7.0/10

Google and Crusoe Energy have started constructing a 933-megawatt natural gas power plant in Armstrong County, Texas to power Google's Goodnight AI data center park, after submitting permits in January 2026. This plant is projected to emit 4.5 million tons of carbon dioxide annually, and has driven Google's total greenhouse gas emissions up 48% since 2019 amid AI expansion. This development exposes the growing tension between the AI industry's exploding demand for energy and big tech companies' public net-zero carbon pledges, highlighting a systemic industry challenge that has not been fully resolved. It sets a visible example of how major tech firms are prioritizing AI expansion over climate goals when renewable energy cannot meet immediate power needs. Google notes it is still pursuing wind energy cooperation and has not signed a formal power purchase agreement for the plant, but states that stable baseload power is an unavoidable current necessity for running large AI data centers. This choice is not unique to Google, as multiple major tech companies have turned to fossil gas to fill energy gaps from slow renewable energy expansion.

telegram · AI_News_CN · Apr 3, 01:45

**Background**: Baseload power refers to the minimum consistent level of electricity demand that a power grid must meet at all times, and power plants that provide this constant power are called baseload power plants, which are traditionally often fueled by natural gas, coal, or nuclear power due to their operational stability. Installed capacity is a standard metric that describes the total maximum power output a power plant can produce under ideal conditions, measured in watts. Crusoe Energy is a private company that specializes in providing energy-focused AI infrastructure and cloud computing services.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/基荷电厂/5158241">基荷电厂_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/装机容量/10782194">装机容量_百度百科</a></li>
<li><a href="https://www.crusoe.ai/">Crusoe | The AI factory company | Renewable-powered AI ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#carbon emissions`, `#energy`, `#big tech`

---