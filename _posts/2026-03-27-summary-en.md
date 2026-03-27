---
layout: default
title: "Horizon Summary: 2026-03-27 (EN)"
date: 2026-03-27
lang: en
---

> From 44 items, 23 important content pieces were selected

---

1. [Google adds post-quantum crypto to Android 17](#item-1) ⭐️ 9.0/10
2. [CAS releases Xiangshan RISC-V processor and Ruyi OS](#item-2) ⭐️ 9.0/10
3. [Google Launches Gemini 3.1 Flash Live Globally](#item-3) ⭐️ 9.0/10
4. [Apple to open Siri to third-party AI in iOS 27](#item-4) ⭐️ 9.0/10
5. [Google globally launches Search Live with Gemini 3.1 Flash Live](#item-5) ⭐️ 9.0/10
6. [Judge blocks Pentagon's Anthropic risk label](#item-6) ⭐️ 8.0/10
7. [First-hand account of LiteLLM PyPI malware attack](#item-7) ⭐️ 8.0/10
8. [Interactive first-principles LLM quantization essay](#item-8) ⭐️ 8.0/10
9. [Apifox desktop hit by supply chain poisoning](#item-9) ⭐️ 8.0/10
10. [58th-generation recloned mice die, cloning limit found](#item-10) ⭐️ 8.0/10
11. [Wikipedia bans direct AI content generation](#item-11) ⭐️ 8.0/10
12. [Apple gets full Gemini access for on-device AI development](#item-12) ⭐️ 8.0/10
13. [Mistral Releases Open-Source Voxtral TTS Model](#item-13) ⭐️ 8.0/10
14. [China's first embodied intelligence standard released](#item-14) ⭐️ 8.0/10
15. [Microsoft defaults to Copilot data collection for AI training](#item-15) ⭐️ 8.0/10
16. [Meituan opens self-developed LongCat LLM to public](#item-16) ⭐️ 8.0/10
17. [Anthropic wins partial victory vs Trump AI ban](#item-17) ⭐️ 8.0/10
18. [AI ports JSONata to Go in a day, saves $500K/year](#item-18) ⭐️ 7.0/10
19. [Paternal age raises higher inheritable disease risk](#item-19) ⭐️ 7.0/10
20. [Bipartisan US bill to ban Chinese government robots](#item-20) ⭐️ 7.0/10
21. [Google Gemini Launches Cross-Platform Memory Import](#item-21) ⭐️ 7.0/10
22. [OpenAI cuts non-core work to focus on coding and enterprise](#item-22) ⭐️ 7.0/10
23. [Meituan 2025 Report Unveils LongCat AI Local Life Upgrade](#item-23) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google adds post-quantum crypto to Android 17](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) ⭐️ 9.0/10

Google announced that it will introduce post-quantum cryptography standards to Android 17, adding quantum-resistant digital signatures to the bootloader and upgrading the Android Keystore to a post-quantum cryptography compliant system. This update is designed to protect Android devices against future threats from quantum computing. This is a major industry-leading security update that will protect billions of existing and new Android devices against future quantum computing attacks, setting a benchmark for mobile post-quantum security migration that the wider industry can follow. Early preparation mitigates the long-term risk of harvest now, decrypt later attacks that could expose sensitive historical data. The update specifically targets two core Android security components: the bootloader, which runs during the device startup process, and the Keystore, which handles secure key storage and authentication for device-to-server communications. The changes focus on public-key cryptography, which is the category of algorithm most vulnerable to quantum computing attacks.

telegram · zaihuapd · Mar 26, 07:09

**Background**: Post-quantum cryptography, also called quantum-resistant cryptography, refers to new cryptographic algorithms designed to remain secure against attacks from powerful quantum computers. Most current widely-used public-key encryption algorithms can be broken by sufficiently powerful quantum computers running Shor's algorithm, so organizations are preparing new standards ahead of the arrival of capable quantum computers. Android Keystore is an Android platform service that securely generates, stores, and uses cryptographic keys on devices, while the Android bootloader is the low-level program that starts the Android operating system during device boot-up and verifies the integrity of system components.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://www.devsecopsnow.com/android-keystore/">What is Android Keystore ? Meaning, Examples... - DevSecOps Now!!!</a></li>
<li><a href="https://www.howtogeek.com/249439/how-to-enter-androids-bootloader-and-recovery-environments/">How to Enter Android’s Bootloader and Recovery Environments What Is Reboot to Bootloader and How to Use It [2025 New!] Bootloader in Android: what it is, risks, and how to unlock ... How to unlock the bootloader of an Android Phone - iFixit What Is Bootloader in Android: A Beginner's Guide ... How to Enter Android ’s Bootloader and Recovery Environments How to unlock Android bootloader safely and step by step What is a Bootloader & how do you unlock it on Android ? Find ... - PC … What Is Reboot to Bootloader and How to Use It [2025 New!] - iMobie What is a Bootloader & how do you unlock it on Android? Find ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Post-quantum cryptography`, `#Mobile Security`, `#Cybersecurity`

---

<a id="item-2"></a>
## [CAS releases Xiangshan RISC-V processor and Ruyi OS](https://h.xinhuaxmt.com/vh512/share/13024070?docid=13024070) ⭐️ 9.0/10

On March 26, 2024, the Chinese Academy of Sciences released the Xiangshan open-source high-performance RISC-V processor and the Ruyi native RISC-V operating system at a RISC-V ecosystem forum. Commercial chips based on the Xiangshan processor already have large-scale industrial adoption, and CAS has launched a joint next-generation open-source chip and system development project with dozens of enterprises and institutions. This announcement delivers a production-ready, internationally competitive open-source high-performance RISC-V processor and matching native operating system to the global open-source chip ecosystem, accelerating the widespread adoption of RISC-V architecture in industrial and commercial applications. It also brings broad industry participation to open-source RISC-V development, strengthening the global open hardware ecosystem. The Xiangshan processor release includes the world's first open-source on-chip network (NoC) interconnect IP, pushing it to the position of an internationally leading open-source high-performance RISC-V processor system. The Ruyi operating system is the first native OS to fully support international RISC-V standards, and the next-generation joint development will target the new Kunminghu architecture of Xiangshan.

telegram · zaihuapd · Mar 26, 10:08

**Background**: RISC-V is an open-source instruction set architecture for processor design that has gained broad industry traction in recent years as an alternative to closed, proprietary architectures. An open-source processor makes its full design files publicly available for anyone to use, modify, and build commercial products upon, lowering the barrier to chip development. A network-on-chip (NoC) interconnect is a critical IP component that manages communication between different functional blocks on a complex system-on-chip.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/OpenXiangShan/XiangShan">GitHub - OpenXiangShan/XiangShan: Open-source high-performance RISC-V processor · GitHub</a></li>
<li><a href="https://ruyisdk.org/en/docs/intro/">Hello Ruyi | RuyiSDK</a></li>
<li><a href="https://www.arteris.com/learn/network-on-chip-technology/">NoC Interconnect Fundamentals: Coherent & Non ... - Arteris</a></li>

</ul>
</details>

**Tags**: `#open-source hardware`, `#RISC-V processor`, `#operating system`, `#chip design`

---

<a id="item-3"></a>
## [Google Launches Gemini 3.1 Flash Live Globally](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/) ⭐️ 9.0/10

Google has released Gemini 3.1 Flash Live, a new high-quality real-time audio and voice large language model, and expanded its real-time multimodal Search Live feature to over 200 countries and regions worldwide. This new model brings faster responses and longer context retention to Google's existing Gemini Live conversational service. This release expands Google's real-time multimodal AI interaction capabilities to a massive global audience, marking a notable step forward in making natural real-time voice AI widely accessible to the public. It also provides developers and enterprises with new tools to build their own real-time conversational AI applications. Gemini 3.1 Flash Live doubles the context retention length of continuous conversations in Gemini Live, improves acoustic detail recognition and noisy environment voice processing, and supports real-time multimodal conversations in over 90 languages. It is available as a preview to developers via the Gemini Live API in Google AI Studio, and can also be used by enterprises for customer experience solutions.

telegram · zaihuapd · Mar 26, 17:01

**Background**: Gemini is Google's flagship line of generative AI large language models that support text, image, audio and video multimodal inputs and outputs. Gemini Live is Google's real-time conversational AI service that allows users to have back-and-forth voice conversations with the Gemini model, while Search Live is a feature that lets users conduct real-time conversational multimodal searches with Google via voice, audio or Google Lens camera input.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/">Gemini 3.1 Flash Live: Making audio AI more natural and reliable</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/search-live-global-expansion/">Google Search Live expands globally - The Keyword</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/live-api">Gemini Live API overview | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Tags**: `#generative ai`, `#large language model`, `#google gemini`, `#real-time ai`, `#multimodal ai`

---

<a id="item-4"></a>
## [Apple to open Siri to third-party AI in iOS 27](https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27?srnd=phx-technology) ⭐️ 9.0/10

Bloomberg reports that Apple plans to open up Siri integration to third-party AI assistants including Google Gemini, Anthropic Claude, and ChatGPT as part of the iOS 27 Siri overhaul. This new feature is expected to be announced at WWDC 2026, which will kick off on June 8, 2026. This change breaks Apple's prior exclusive arrangement for ChatGPT integration with Siri and will reshape the global mobile AI assistant ecosystem on the world's largest mobile platform. It will open up fairer competition for third-party AI services and strengthen Apple's positioning of the iPhone as a competitive AI platform. Users can enable or disable the third-party AI assistant integration in the Apple Intelligence and Siri settings menu, and AI companies need to adapt their services to support this new iOS 27 feature. The plan is still subject to adjustment or delay before the official release.

telegram · AI_News_CN · Mar 27, 01:54

**Background**: Apple Intelligence is Apple's on-device and cloud hybrid generative AI system launched at WWDC 2024, integrated across Apple's software platforms to power AI features including Siri. WWDC is Apple's annual developer conference where it showcases new software versions and upcoming AI technologies for its platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence - Wikipedia</a></li>
<li><a href="https://www.ithome.com/0/933/107.htm">古尔曼：苹果 iOS 27 将开放 Siri 第三方 AI 接口，谷歌 Gemini 与 Cl...</a></li>
<li><a href="https://developer.apple.com/wwdc26/">WWDC26 - Apple Developer</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#AI assistants`, `#iOS`, `#mobile AI`

---

<a id="item-5"></a>
## [Google globally launches Search Live with Gemini 3.1 Flash Live](https://www.aibase.com/zh/news/26607) ⭐️ 9.0/10

Google has officially launched Search Live, a new real-time multimodal AI search feature, globally across more than 200 countries and regions. The feature is powered by the new Gemini 3.1 Flash Live model and allows users to conduct real-time AI interaction with the physical world through phone cameras and voice commands on both Android and iOS. This launch represents a major paradigm shift for consumer search that moves the industry from traditional text and image retrieval toward real-time spatial multimodal interaction, and it is a key strategic move by Google to defend its market position in the growing AI search competition. It also accelerates the evolution of AI assistants from passive retrieval tools to active perception partners that connect the physical and digital worlds. Search Live is available within the Google app and Google Lens, and it can provide synchronized voice answers and relevant web links for use cases like furniture assembly guidance and plant and animal recognition. Gemini 3.1 Flash Live is a native multilingual audio and voice large language model that offers greatly improved response speed and natural conversational output while maintaining a lightweight footprint.

telegram · AI_News_CN · Mar 27, 01:45

**Background**: Google has long dominated the global consumer search market, but the rise of generative AI has brought new competitive pressure from companies including OpenAI and AI startup Luma AI. Gemini is Google's family of large language models focused on multimodal capabilities that can process and generate text, images, audio, and video content. Real-time spatial AI search combines computer vision, speech recognition, and large language models to allow users to get AI-powered information by interacting directly with their surrounding physical environment.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-1-flash-live/">Gemini 3.1 Flash Live - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/search-live-global-expansion/">Google Search Live expands globally</a></li>
<li><a href="https://medium.com/aimonks/google-unveils-search-live-an-ai-search-tool-powered-by-gemini-and-your-camera-b5f5ccc376a4">Google Unveils Search Live , an AI Search Tool Powered by... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI Search`, `#Gemini`, `#Multimodal AI`, `#Google`, `#Large Language Models`

---

<a id="item-6"></a>
## [Judge blocks Pentagon's Anthropic risk label](https://www.cnn.com/2026/03/26/business/anthropic-pentagon-injunction-supply-chain-risk) ⭐️ 8.0/10

A U.S. federal judge has blocked the Pentagon's attempt to label major AI developer Anthropic as a supply chain risk. Anthropic had previously sued the U.S. Defense Department over this designation after the Pentagon issued the label in early March 2026. This ruling establishes a judicial check on executive branch authority over AI supply chain designations, and sets an important precedent for government procurement rules and AI regulation affecting major private AI companies. It impacts how the U.S. government can restrict access to its contracts for leading AI developers moving forward. The supply chain risk label would have immediately barred all U.S. government contractors from using Anthropic's AI technology in their work for the Pentagon. The ruling came after Anthropic challenged the Pentagon's unilateral designation in federal court.

hackernews · prawn · Mar 26, 23:33

**Background**: Anthropic is a leading AI safety and research company best known for its Claude series of large language models, which are distributed via multiple channels including public APIs, Amazon Bedrock and consumer applications. A U.S. Pentagon supply chain risk designation blocks government contractors from working with the labeled company, effectively cutting the firm off from a large segment of U.S. federal government-related business.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/pentagon-informed-anthropic-it-is-supply-chain-risk-official-says-2026-03-05/">Pentagon designates Anthropic a supply chain risk | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Most Hacker News commenters agreed that the Pentagon's actions represented executive overreach, and viewed the judge's ruling as a welcome example of effective judicial checks and balances. One commenter noted that the thread appeared to have suspicious inorganic support for the government's position, while another questioned how many users had actually stopped using Anthropic's Claude because of the Pentagon's original edict.

**Tags**: `#AI policy`, `#government regulation`, `#Anthropic`, `#Pentagon`, `#judicial review`

---

<a id="item-7"></a>
## [First-hand account of LiteLLM PyPI malware attack](https://simonwillison.net/2026/Mar/26/response-to-the-litellm-malware-attack/#atom-everything) ⭐️ 8.0/10

Callum McMahon has published a minute-by-minute transcript of his response to the active malware attack on LiteLLM version 1.82.8 hosted on PyPI, including full evidence of the malicious code and his AI-assisted incident response process. He used Claude to help confirm the vulnerability and guide his reporting steps to PyPI security. This transparent first-hand account provides valuable reference for open source and AI security communities learning to handle supply chain attacks, and helps highlight ongoing risks to widely used Python LLM tools distributed via PyPI. It also demonstrates how AI can assist developers during fast-moving security incident responses. The malicious version 1.82.8 contains a `.pth` file that automatically executes malware whenever Python starts on an infected machine, even without the user importing the LiteLLM library, and the malware steals credentials such as SSH keys and cloud configuration. McMahon confirmed the malware in an isolated Docker container downloaded directly from PyPI.

rss · Simon Willison · Mar 26, 23:58

**Background**: LiteLLM is a widely used open-source Python LLM proxy that simplifies accessing over 100 different large language model APIs with a unified OpenAI-compatible interface, and it has accumulated over 95 million total downloads. PyPI, the Python Package Index, is the official default public repository for Python open source packages, used by millions of developers to install software and dependencies.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/LiteLLM">LiteLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PyPI">PyPI</a></li>
<li><a href="https://byteiota.com/litellm-pypi-attack-95m-downloads-hit-by-malware-today/">LiteLLM PyPI Attack: 95M Downloads Hit by Malware Today</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#malware`, `#PyPI`, `#LLM`, `#open source security`

---

<a id="item-8"></a>
## [Interactive first-principles LLM quantization essay](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose published a new interactive first-principles essay explaining LLM quantization, which includes an outstanding visual interactive explanation of binary floating point representation. This essay makes the critical LLM optimization technique of quantization accessible to more practitioners, helping more developers deploy capable LLMs on consumer hardware with minimal quality loss. The essay tests how different quantization levels affect Qwen 3.5 9B using the llama.cpp perplexity tool and GPQA benchmark, finding 8-bit quantization has almost no quality penalty, while 4-bit quantization retains roughly 90% of original model quality.

rss · Simon Willison · Mar 26, 16:21

**Background**: LLM quantization is a model compression technique that converts high-precision model weights into lower-precision representations to reduce memory usage, letting large models run on hardware with less VRAM. Binary floating point representation, defined by the IEEE 754 standard, is the standard way computers store fractional numeric values, split into sign, exponent, and significand bit fields.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@techresearchspace/what-is-quantization-in-llm-01ba61968a51">What is Quantization in LLM. Large Language Models comes in all… | by Nithin Devanand | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/IEEE_754">IEEE 754 - Wikipedia</a></li>
<li><a href="https://www.maartengrootendorst.com/blog/quantization/">A Visual Guide to Quantization - Maarten Grootendorst</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Quantization`, `#Technical explanation`, `#Floating point representation`

---

<a id="item-9"></a>
## [Apifox desktop hit by supply chain poisoning](https://t.me/zaihuapd/40514) ⭐️ 8.0/10

A disclosure confirms the Apifox desktop client suffered a supply chain attack starting March 4, where attackers tampered with a CDN-hosted script to steal SSH keys, Git credentials and other sensitive system data. Security researcher phith0n has independently reversed the malicious payload and published analysis code for the incident. This attack affects all Windows, macOS, and Linux users of the popular API development tool Apifox, and stolen credentials can enable further backdoor implantation and lateral movement across internal networks. It is also an urgent reminder of the growing risk of supply chain attacks targeting widely used developer tools. The attackers compromised a third-party event statistics script hosted on Apifox's CDN, and the malicious code is designed to collect SSH keys, Git credentials, shell command history and running process lists from affected devices. The attack impacts all three major desktop operating systems.

telegram · zaihuapd · Mar 26, 04:19

**Background**: Apifox is a popular all-in-one API development and management tool that combines functionalities of Postman, Swagger, Mock and JMeter for developers. A supply chain poisoning attack targets dependencies or third-party resources used by legitimate software to compromise end users indirectly. CDN script tampering is a common vector for this attack, which could have been prevented with the Subresource Integrity security feature that verifies resource integrity via cryptographic hashes.

<details><summary>References</summary>
<ul>
<li><a href="https://apifox.com/">Apifox - API 文档、调试、Mock...</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity">Subresource Integrity - Security | MDN - MDN Web Docs Usage example</a></li>
<li><a href="https://chanmeng666.medium.com/apifox-api-testing-tool-guide-from-beginner-to-practitioner-44d4deb6a9f4">Apifox API Testing Tool Guide: From Beginner to Practitioner | Medium</a></li>

</ul>
</details>

**Tags**: `#supply-chain attack`, `#cybersecurity`, `#software poisoning`, `#credential theft`

---

<a id="item-10"></a>
## [58th-generation recloned mice die, cloning limit found](https://www.nature.com/articles/s41467-026-69765-7) ⭐️ 8.0/10

After 20 years of iterative serial cloning experiments, a Japanese research team found that all 58th-generation recloned mice died within one day after birth, with cumulative genetic damage accumulating across cloning generations. The experiment produced 58 generations of recloned mice from a single original female mouse, totaling over 1200 cloned individuals. This study answers a long-standing open question about whether repeated iterative cloning can be sustained indefinitely in mammals, providing empirical evidence that mammals have an inherent hard limit to long-term propagation via repeated cloning. This result advances fundamental understanding in developmental biology and mammalian genetics, and will impact future cloning research and applications. The survival rate of 57th-generation recloned mice was already below 1%, and while 58th-generation mice appeared normal in external appearance, all died within a day of birth. The mutation rate in cloned mice was approximately three times higher than that of naturally bred offspring, and some cloned individuals even lost the entire X chromosome.

telegram · zaihuapd · Mar 26, 16:46

**Background**: Iterative serial cloning, also called recloning, refers to the process of repeatedly cloning a cloned individual to produce new cloned generations. Prior research on serial cloning in cattle and mice has already observed that cloning success rate tends to decrease as the number of generations increases. Cumulative genetic damage refers to the gradual buildup of unrepaired DNA mutations and abnormalities across multiple cell divisions or reproduction cycles, which is hypothesized to contribute to functional decline and limited lifespan.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/8550512_Serial_bull_cloning_by_somatic_cell_nuclear_transfer">(PDF) Serial bull cloning by somatic cell nuclear transfer</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNA_damage_(naturally_occurring)">DNA damage (naturally occurring) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNA_damage_theory_of_aging">DNA damage theory of aging - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mammalian cloning`, `#developmental biology`, `#genetic damage`, `#reproductive research`

---

<a id="item-11"></a>
## [Wikipedia bans direct AI content generation](https://www.aibase.com/zh/news/26601) ⭐️ 8.0/10

On March 26, Wikipedia passed a new large language model editing policy via community volunteer vote, which strictly prohibits users from directly using AI to generate or rewrite article content. The new policy only allows AI to be used as an auxiliary tool for editing suggestions, and all new content proposed by AI must be manually verified by editors. This policy marks a key step for the world's largest public knowledge resource to protect content accuracy and human editorial sovereignty in the age of generative AI. It also sets an important reference for AI governance for other public content platforms and community knowledge projects. The policy was passed by an overwhelming 40-to-2 vote among volunteer editors, and it upgraded Wikipedia's previous vague AI rules from a ban on generating full new articles from scratch to a full ban on all direct AI generation or rewriting of content. AI is not completely banned, but any unvetted new content introduced by AI is prohibited to prevent problems caused by model hallucination.

telegram · AI_News_CN · Mar 27, 01:11

**Background**: A large language model (LLM) is a type of deep learning model pre-trained on massive text data, capable of generating coherent human-like text and powering most current generative AI tools. AI hallucination is a common flaw of LLMs, where the model generates false or misleading information and presents it as factual content. Wikipedia is the world's largest open-access online encyclopedia, whose content is entirely curated and maintained by a global community of volunteer editors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Wikipedia`, `#AI policy`, `#generative AI`, `#knowledge governance`, `#content moderation`

---

<a id="item-12"></a>
## [Apple gets full Gemini access for on-device AI development](https://www.aibase.com/zh/news/26603) ⭐️ 8.0/10

Apple has obtained full access to Google's Gemini model, and uses model distillation with Gemini's outputs to train smaller capable on-device AI models alongside Apple's ongoing proprietary foundation model work. The new AI features are expected to be unveiled at Apple's WWDC event in June. This collaboration signals a broader industry shift from raw computing power competition to competition focused on more efficient AI training strategies. It strengthens Apple's on-device AI advantages and could lead to more powerful local AI capabilities in future consumer devices, accelerating the popularization of AI. Apple continues independent development of its own foundation models alongside this collaboration, and the partnership primarily fills Apple's gap in accessing high-quality synthetic training data. Gemini was originally designed for chatbots and enterprise applications, which differs from Apple's system-level planning for Siri.

telegram · AI_News_CN · Mar 27, 01:18

**Background**: Model distillation is a machine learning technique that transfers knowledge from a large 'teacher' model to a smaller 'student' model, allowing the smaller model to match most of the large model's performance while remaining lightweight enough to run on lower-power hardware. On-device AI refers to AI models that run directly on end-user devices like smartphones instead of relying on cloud processing, which offers better privacy and offline functionality. Google Gemini is Google's flagship generative large language model family, which supports multiple types of input and output and comes in variants ranging from lightweight on-device versions to high-capability large models for complex reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://semiconductor.samsung.com/technologies/processor/on-device-ai/">On-device AI | Technologies | Samsung Semiconductor Global</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini</a></li>

</ul>
</details>

**Tags**: `#model distillation`, `#on-device AI`, `#Gemini`, `#Apple AI`, `#industry collaboration`

---

<a id="item-13"></a>
## [Mistral Releases Open-Source Voxtral TTS Model](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/) ⭐️ 8.0/10

French AI company Mistral has launched Voxtral TTS, a new open-source text-to-speech model that supports 9 different languages. It can adapt to custom voices using less than 5 seconds of audio and captures fine-grained voice characteristics. This release expands high-quality open-source options for speech AI and brings Mistral into direct competition with major closed-source text-to-speech providers, creating more choices for both consumer and enterprise developers. It also advances the trend of making capable generative AI tools openly available to the broader developer community. Voxtral TTS currently supports nine languages: English, French, German, Spanish, Dutch, Portuguese, Italian, Hindi, and Arabic, and it is designed for use cases including voice AI assistants and enterprise customer support voice agents. The published 4B parameter version of the model is hosted on Hugging Face under open weights.

telegram · AI_News_CN · Mar 27, 02:05

**Background**: Mistral AI is a prominent French AI developer that focuses primarily on releasing high-performance open-source large language models. Text-to-speech (TTS) is a generative AI task that converts written text into natural-sounding human speech, and custom voice adaptation (also called voice cloning) allows the model to mimic a specific target voice using a small audio sample. Before this release, leading TTS tools from providers like ElevenLabs and OpenAI were mostly closed-source, limiting customization for developers.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/voxtral-tts">Speaking of Voxtral | Mistral AI</a></li>
<li><a href="https://huggingface.co/mistralai/Voxtral-4B-TTS-2603">mistralai/ Voxtral -4B- TTS -2603 · Hugging Face</a></li>
<li><a href="https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/">Mistral releases a new open source model for speech generation</a></li>

</ul>
</details>

**Tags**: `#open-source AI`, `#text-to-speech`, `#speech generation`, `#Mistral AI`, `#generative AI`

---

<a id="item-14"></a>
## [China's first embodied intelligence standard released](https://www.aibase.com/zh/news/26610) ⭐️ 8.0/10

China's first industry standard for embodied intelligence, jointly drafted by the China Academy of Information and Communications Technology and over 40 institutions, was announced on March 26, 2025 and will take effect on June 1, 2026. The standard establishes a unified multi-dimensional evaluation framework backed by a 10,000-task test library and full supporting testing tools. This standard ends the disordered, unregulated development of China's embodied intelligence industry and ushers in a standardized development phase. It provides clear guidance for corporate R&D and lays a solid evaluation foundation for the large-scale commercial deployment of embodied intelligence technologies. The standard supports in-depth testing across three core capability dimensions: basic capabilities, cognitive reasoning, and end-to-end closed-loop capabilities, and covers four testing modes including static simulation, dynamic simulation, real environment, and combined testing. The supporting 10,000-task test library includes 300 task types that cover mainstream application scenarios such as industrial production, household services, retail, and logistics.

telegram · AI_News_CN · Mar 27, 02:09

**Background**: Embodied intelligence, also called embodied AI, refers to artificial intelligence integrated into physical systems that can perceive information and interact dynamically with the physical environment. Common types of embodied intelligent systems include humanoid robots, industrial robots, autonomous vehicles, and intelligent warehouse facilities. Before the release of this standard, the fast-growing embodied intelligence field lacked unified industry norms and evaluation benchmarks, leading to disordered development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://www.aibase.com/news/26610">Embodied Intelligence Ends Uncontrolled Growth: First ...</a></li>
<li><a href="http://www.c114pro.com/ainews/155400.html">The First Industry Standard in the Field of Embodied AI is ...</a></li>

</ul>
</details>

**Tags**: `#embodied intelligence`, `#industry standard`, `#artificial intelligence`, `#technology regulation`

---

<a id="item-15"></a>
## [Microsoft defaults to Copilot data collection for AI training](https://www.solidot.org/story?sid=83887) ⭐️ 8.0/10

GitHub announced that starting April 24, 2025, Microsoft will by default collect user interaction data from GitHub Copilot to train AI models unless users manually opt out of the data collection. This new policy has been widely criticized for violating the default opt-out requirement specified by GDPR. This policy change affects millions of GitHub Copilot subscribers worldwide, and it raises widespread privacy and regulatory concerns for the AI development industry. It sets a precedent for how tech companies handle user data for AI training, which could influence future industry regulation and user trust in AI coding tools. Users can change their data collection preference at the dedicated GitHub settings page linked in the announcement. Critics note that GDPR requires data collection that processes personal data to be opted into by default, making GitHub's default enabled collection non-compliant with EU regulation.

telegram · AI_News_CN · Mar 27, 02:15

**Background**: GitHub Copilot is a subscription-based AI-powered coding assistant co-developed by GitHub and OpenAI that provides automatic code completions and programming assistance to developers working in common IDEs. GDPR is a comprehensive European Union privacy regulation that sets strict requirements for how companies collect and process personal data of users within the EU and European Economic Area, and it has become a global standard for data protection regulation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://en.wikipedia.org/wiki/GDPR">GDPR</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#AI privacy`, `#data collection`, `#GDPR`

---

<a id="item-16"></a>
## [Meituan opens self-developed LongCat LLM to public](https://www.aibase.com/zh/news/26611) ⭐️ 8.0/10

On March 26, Meituan CEO Wang Xing announced at an earnings call that the company's self-developed LongCat large language model now powers the fully launched AI assistant Xiaotuan as a new local life service entry, after three years of continuous investment. An embodied intelligence open source ecological plan was also released alongside the announcement. This announcement marks a major strategic shift for China's leading local life service platform, turning AI from an add-on feature into a core competitive engine for the next decade of industry competition. It also accelerates the commercial landing of large language models and embodied intelligence in the massive trillion-dollar local life service market. Meituan pursues a dual strategy of independent research and development plus third-party cooperation for its AI layout; the LongCat Flash-Thinking variant uses a Mixture-of-Experts architecture with 560 billion total parameters, and has been trained across tens of thousands of scenarios covering more than 20 domains. The Beijing Humanoid Robot Innovation Center, which jointly promoted the open source embodied intelligence plan, was built by enterprises covering complete humanoid robots, core components and large models.

telegram · AI_News_CN · Mar 27, 02:39

**Background**: Large language models are AI systems trained on massive text data that can understand and generate human-like text to perform a wide range of cognitive tasks. Embodied intelligence refers to the concept that intelligence is shaped by an agent's physical interaction with its environment, which enables AI systems in physical forms like robots to perform practical local life tasks such as delivery. Local life service refers to on-demand consumer services including food delivery, in-store dining, hotel booking and travel, which is a massive market in China.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-Flash-Thinking-2601">meituan-longcat/LongCat-Flash-Thinking-2601 · Hugging Face</a></li>
<li><a href="https://www.longcatai.org/models/flash-thinking">LongCat-Flash-Thinking - Reasoning Model | Meituan AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://english.beijing.gov.cn/latest/news/202311/t20231105_3295012.html">Beijing Establishes Humanoid Robot Innovation Center</a></li>

</ul>
</details>

**Tags**: `#Large Language Model`, `#AI Commercialization`, `#Local Life Service`, `#Meituan`

---

<a id="item-17"></a>
## [Anthropic wins partial victory vs Trump AI ban](https://ishare.ifeng.com/c/s/v006zV59yPqTbSz485eUscqvgFWuH8sAgBye-_HXxop65-_IzHQ05uAxefxN6iZDzCZEPN) ⭐️ 8.0/10

A US federal judge granted Anthropic a preliminary injunction that blocks the Trump administration's ban on federal agencies using Anthropic's Claude AI, ruling the ban violated Anthropic's First Amendment rights. This marks a partial victory for Anthropic's lawsuit against the White House. This ruling sets an important precedent for how AI regulation and government AI procurement interact with free speech protections in the United States, and it will impact all major AI companies that sell products to federal government agencies. The ruling was issued by Judge Jacqueline Lin in San Francisco, two days after a hearing between Anthropic and government legal teams. The final ruling on the case is still months away, and the injunction is only temporary pending the final outcome of the lawsuit.

telegram · AI_News_CN · Mar 27, 02:44

**Background**: A preliminary injunction is a temporary court order granted before or during a trial, designed to preserve the current situation and prevent irreparable harm to the applicant before a final judgment is issued. The First Amendment to the U.S. Constitution protects freedom of speech expression, and prohibits the government from retaliating against entities for protected speech.

<details><summary>References</summary>
<ul>
<li><a href="https://www.law.cornell.edu/wex/preliminary_injunction">preliminary injunction | Wex | US Law | LII / Legal ...</a></li>
<li><a href="https://www.law.cornell.edu/constitution/first_amendment">First Amendment | U.S. Constitution | LII / Legal Information Institute</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#Anthropic`, `#legal news`, `#Claude AI`, `#government AI`

---

<a id="item-18"></a>
## [AI ports JSONata to Go in a day, saves $500K/year](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

The Reco.ai team used generative AI to port the JSONata JSON query language from its existing implementation to Go in a single day, with only 7 hours of work and $400 in AI token costs. After a week of parallel shadow deployment to validate correctness, the project delivers an estimated annual cost savings of $500,000. This case study provides a replicable practical example of AI-assisted software development that delivers measurable, significant cost savings for engineering teams. It demonstrates that generative AI can speed up routine code migration projects drastically, opening up new efficiency gains for software organizations. The project relied on JSONata's existing comprehensive test suite to validate the correctness of the newly generated Go implementation during development. The team used a one-week shadow deployment running old and new versions in parallel to confirm the new implementation perfectly matched the original behavior before full rollout.

rss · Simon Willison · Mar 27, 00:35

**Background**: JSONata is a popular open-source declarative query and transformation language designed specifically for working with JSON data. Vibe porting is an AI-assisted software porting methodology that leverages generative AI to rewrite existing code in a new language, relying on an existing test suite to validate correctness. Shadow deployment is a software testing practice where new code is run in parallel with production code on live traffic without exposing it to end users, to verify its behavior matches expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata</a></li>
<li><a href="https://devops.com/what-is-a-shadow-deployment/">What is a Shadow Deployment? - DevOps.com</a></li>
<li><a href="https://dev.blues.io/blog/blues-university-anatomy-of-json-jsonata/">The Anatomy of JSON and JSONata - dev.blues.io</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#Go`, `#JSON processing`, `#software porting`

---

<a id="item-19"></a>
## [Paternal age raises higher inheritable disease risk](https://t.me/zaihuapd/40521) ⭐️ 7.0/10

British scientists performed high-precision sequencing on 81 human sperm samples, and found that the risk of inherited genetic disease in offspring caused by increasing paternal age is higher than previous estimates. The study also identified 31 previously unknown genes under positive selection in male germ cells that are linked to developmental disorders and cancer susceptibility. This finding revises the existing understanding of paternal age-related genetic risks, provides new genomic insights for human genetics and medical genetics research, and may help improve risk assessment for paternal-age-related inherited diseases. This research is particularly relevant for populations that choose to have children at older paternal ages. The study found that 3 to 5 percent of sperm from men over 50 years old carry disease-causing mutations, a proportion that is higher than previous estimates. A total of 40 genes with significant positive selection in the male germline were identified, 31 of which are newly discovered in this work.

telegram · zaihuapd · Mar 26, 12:47

**Background**: Positive selection is an evolutionary process where beneficial genetic variants become more common across generations, and detecting this process in the genome helps understand evolutionary adaptation. High-precision sequencing, a sequencing technology with advanced resolution, allows researchers to identify rare and subtle mutations in sperm that were hard to detect with older methods. Previous studies had already observed an association between older paternal age and increased inherited mutation risk, but the magnitude of the risk was underestimated before this work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-09448-3">Sperm sequencing reveals extensive positive selection in the ...</a></li>
<li><a href="https://depts.washington.edu/jtlab/positiveSelection.html">Detecting Positive Selection, Thomas lab</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12611766/">Sperm sequencing reveals extensive positive selection in the ...</a></li>

</ul>
</details>

**Tags**: `#genetics`, `#human reproduction`, `#medical research`, `#genetic sequencing`

---

<a id="item-20"></a>
## [Bipartisan US bill to ban Chinese government robots](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQemI2WXhEQVhWUE5zTnlnRHNVUG5kdUdldVJOQWxYQ1M1WnhBZXVxZFFmVEFyeFl0ZjBaMWNDWHZIRlV0Y002cjhiZ2VRZlI0RWx1Z1ZZTFA3T2VBbFlRZDhnVnBsaVNJUFdQb200dlM3d1ZYZG1iMFpDVUJRZkhFaFdOSXBKNU1jejQ4UlVGbGVoSDlvN2ZkU3lpZVRqOVE2XzVtMTFDVTcydw?oc=5) ⭐️ 7.0/10

US senators Tom Cotton and Chuck Schumer plan to introduce the American Security Robot Act on March 26, which will ban US federal government procurement and use of unmanned ground vehicles made by Chinese companies, and block related federal funding. A companion House version of the bill will also be introduced by Representative Elise Stefanik. This bill will block Chinese robotics companies from accessing the US federal public market, impact global cross-border robotics trade and the global industrial robot industry, and escalate tech regulatory restrictions between the US and China in the robotics sector. The bill grants limited exemptions for research use by the US military and law enforcement agencies, which requires that the robots do not send or receive any data with China. The proposed ban targets unmanned ground vehicle systems, covering products from humanoid robots to remote surveillance vehicles.

telegram · zaihuapd · Mar 26, 14:16

**Background**: An unmanned ground vehicle is a land-based robotic platform that operates without an on-board human operator, and can be controlled autonomously or remotely. It is widely used in both military and civilian scenarios including surveillance, public safety and industrial work, and has become an important strategic sector for technology development and government procurement globally.

<details><summary>References</summary>
<ul>
<li><a href="https://thehill.com/policy/technology/5801982-schumer-cotton-chinese-robotics/">Senators push to ban Chinese robots in U.S. - The Hill</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unmanned_ground_vehicle">Unmanned ground vehicle</a></li>
<li><a href="https://theaiinsider.tech/2026/03/26/report-us-lawmakers-to-introduce-american-security-robotics-act-to-ban-federal-agencies-from-buying-chinese-humanoid-robots/">Report: US Lawmakers to Introduce American Security Robotics ...</a></li>

</ul>
</details>

**Tags**: `#industrial robotics`, `#US policy`, `#international trade`, `#tech regulation`

---

<a id="item-21"></a>
## [Google Gemini Launches Cross-Platform Memory Import](https://www.aibase.com/zh/news/26598) ⭐️ 7.0/10

On March 27, Google launched a memory import feature for its AI assistant Gemini that allows users to migrate personal preferences and conversation history from other AI assistants. The feature supports both lightweight preference summary transfer and bulk full conversation import with a maximum 5GB file size. This feature solves the core pain point of having to retrain a new AI assistant when switching platforms, greatly lowering the switching cost for frequent AI users. It also shifts the direction of AI assistant competition from pure feature comparison to user experience continuity, marking an important development for consumer AI. Gemini offers two migration paths: a lightweight option where users paste a summary of personal preferences generated by their original AI, and a bulk import option that accepts up to 5GB zip files of full conversation history. Google states imported data will be stored in user activity records for service optimization and model training, and users can view, manage, or delete their data at any time.

telegram · AI_News_CN · Mar 27, 00:55

**Background**: Personalized AI assistants learn user preferences, communication styles and custom needs from repeated interactions over time, so switching to a new assistant requires users to re-provide this context to get the same experience, a process that is inefficient and called 'retraining' the assistant. Google Gemini is Google's flagship generative AI assistant that competes with other popular consumer AI products like ChatGPT.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/">How to switch to Gemini: Import your chats and data from ...</a></li>
<li><a href="https://www.androidauthority.com/gemini-memory-chat-import-rollout-3652475/">Gemini launches memory import feature for easier switching ...</a></li>
<li><a href="https://support.google.com/gemini/answer/16868299?hl=en&co=GENIE.Platform=Desktop">Import from other AI platforms to Gemini Apps - Google Help</a></li>

</ul>
</details>

**Tags**: `#Google Gemini`, `#AI assistants`, `#feature release`, `#user experience`, `#data migration`

---

<a id="item-22"></a>
## [OpenAI cuts non-core work to focus on coding and enterprise](https://www.aibase.com/zh/news/26604) ⭐️ 7.0/10

OpenAI is conducting a major strategic contraction, shutting down non-core experimental projects to reallocate computing and R&D resources to high-value coding assistants and enterprise services. This strategic shift is a response to competitive pressure from rival Anthropic, which is planning an upcoming IPO. This strategic shift will alter OpenAI's product development roadmap, and may reshape the competitive landscape of the generative AI industry as leading players increasingly prioritize profitable commercialization over broad experimental expansion. It also signals a broader industry trend of AI companies moving away from the era of indiscriminate spending to focus on sustainable profitability. OpenAI previously spread resources across many projects including the text-to-video model Sora and various consumer-facing plugins, which consumed large amounts of computing power. The main goals of this contraction are to improve cash flow with high-value enterprise orders, demonstrate consistent profitability to investors ahead of potential capital operations, and retake market leadership in professional productivity AI tools.

telegram · AI_News_CN · Mar 27, 01:18

**Background**: OpenAI is one of the world's leading generative AI developers, best known for products like ChatGPT and GPT large language models. Sora is OpenAI's text-to-video generative AI model that can create high-quality short videos from text prompts. GitHub Copilot is an existing AI coding assistant co-developed by GitHub and OpenAI that is already a dominant product in the AI coding assistant market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to-video model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#generative AI`, `#corporate strategy`, `#AI business`

---

<a id="item-23"></a>
## [Meituan 2025 Report Unveils LongCat AI Local Life Upgrade](https://www.aibase.com/zh/news/26606) ⭐️ 7.0/10

Meituan released its 2025 annual financial report on March 26, 2026, announcing continued development of its self-developed large language model LongCat and launching consumer AI products Xiaotuan assistant and independent app Xiaomei to transform its local life platform into an AI-driven entrance. The 2025 full-year revenue reached 364.9 billion yuan, an 8% year-over-year increase, with a net loss of 23.4 billion yuan amid intensified即时零售 competition. This announcement marks a formal strategic shift of a major Chinese local life service player to AI-driven development, pushing the entire industry's competition from traditional subsidy battles to competition over AI-powered operational efficiency and user service experience. It also positions AI agent development as a core driving factor for the digital transformation of the local service industry. Meituan's AI strategy focuses on integrating digital and physical worlds, and the Xiaotuan AI assistant can already handle complex natural language demand scenarios such as finding restaurants that meet specific parking and taste requirements in a designated area, powered by the company's massive merchant POI and real-time operational data. Current AI investments have dragged down Meituan's short-term financial performance, but the company plans to continue increasing AI R&D investment.

telegram · AI_News_CN · Mar 27, 01:28

**Background**: LongCat is Meituan's self-developed native multimodal large language model, and the team has already open-sourced lightweight and next-generation versions of the model to the public. POI data refers to information about physical locations of interest, including geographic coordinates, merchant categories and business details, which is core basic data for location-based local life services. In the generative AI era, AI agents are autonomous intelligent systems that can make independent decisions and complete tasks in complex environments without continuous manual oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-Next">meituan-longcat/LongCat-Next · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://www.placer.ai/guides/poi-data">Point of Interest Data (POI data) - All You Need To Know - Placer</a></li>

</ul>
</details>

**Tags**: `#large language model`, `#AI industry strategy`, `#local life service`, `#AI assistant`, `#corporate financial report`

---