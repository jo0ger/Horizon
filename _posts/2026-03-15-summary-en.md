---
layout: default
title: "Horizon Summary: 2026-03-15 (EN)"
date: 2026-03-15
lang: en
---

> From 29 items, 7 important content pieces were selected

---

1. [Ageless Linux Opposes OS Age Verification Rules](#item-1) ⭐️ 8.0/10
2. [Glassworm Attack Compromises 151+ GitHub Repos](#item-2) ⭐️ 8.0/10
3. [AI Slopocalypse Ends Jazzband's Open Model](#item-3) ⭐️ 7.0/10
4. [Instagram to End E2EE for DMs After 2026](#item-4) ⭐️ 7.0/10
5. [Disney Accuses Seedance 2.0 of Copyright Infringement](#item-5) ⭐️ 7.0/10
6. [EU Countries Back Ban on Harmful AI-Generated Content](#item-6) ⭐️ 7.0/10
7. [Microsoft Brings Gaming Copilot to Xbox 2026](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Ageless Linux Opposes OS Age Verification Rules](https://agelesslinux.org/) ⭐️ 8.0/10

The open source Ageless Linux project has launched to oppose new mandatory government age verification regulations that require operating system providers to collect and share user age information, and the issue is the subject of a high-upvote Hacker News discussion. These new regulations threaten user privacy and civil liberties, and impose prohibitive compliance costs on small open source projects that lack large legal budgets, threatening the future of independent open source operating systems. Ageless Linux operates as a protest project rather than a full standalone operating system, and the core California law at the center of the debate is AB 1043, which will go into effect on January 1, 2027.

hackernews · nateb2022 · Mar 14, 22:10

**Background**: New mandatory age verification regulations have recently been passed or proposed in multiple regions including California (US), the UK, and the EU, requiring all operating system providers to implement age checks during user account setup. California's AB 1043 was signed by Governor Gavin Newsom in October 2025, and it requires OS providers to collect user age data and share it with app developers. Most small open source projects have very limited annual budgets, making even the cost of defending against a frivolous non-compliance lawsuit unaffordable for them.

<details><summary>References</summary>
<ul>
<li><a href="https://agelesslinux.org/">Ageless Linux — Software for Humans of Indeterminate Age</a></li>
<li><a href="https://www.tomshardware.com/software/operating-systems/california-introduces-age-verification-law">California introduces age verification law for all operating systems, including Linux and SteamOS — user age verified during OS account setup | Tom's Hardware</a></li>
<li><a href="https://www.theregister.com/2026/03/06/os_age_verification/">US state laws push age checks into the operating system • The Register</a></li>

</ul>
</details>

**Discussion**: Most Hacker News commenters agree that the new regulations are logically flawed, and many note that protecting children online is already achievable through parenting and existing parental control tools. Commenters agree the laws expand public surveillance infrastructure instead of holding addictive big tech platforms accountable for harm to children, and praise Ageless Linux as a proper example of open source community pushback against harmful regulation.

**Tags**: `#open source`, `#age verification`, `#online privacy`, `#operating systems`, `#regulation`

---

<a id="item-2"></a>
## [Glassworm Attack Compromises 151+ GitHub Repos](https://www.tomshardware.com/tech-industry/cyber-security/malicious-packages-using-invisible-unicode-found-in-151-github-repos-and-vs-code) ⭐️ 8.0/10

Researchers from Aikido Security recently discovered that hacker group Glassworm has carried out a large-scale attack targeting GitHub, npm, and the VS Code market, compromising over 151 repositories including multiple well-known open source projects. The attack uses invisible Unicode characters to hide malicious payloads that steal user credentials, and leverages the Solana blockchain as a stealth command and control channel. This novel high-impact open source supply chain attack can evade manual code review, putting millions of developers and downstream projects relying on compromised repositories at risk of credential and secret theft. It also highlights a new trend of attackers combining obfuscation techniques, large language models, and blockchains to create more stealthy, persistent attacks. The attack hides malicious code in invisible zero-width Unicode characters from specific Unicode private use ranges that cannot be spotted by the naked eye during code review, and attackers used large language models to generate deceptive code matching each project's coding style to trick maintainers into merging malicious changes. Using the Solana blockchain for command and control makes the attack far harder to shut down than traditional attacks relying on centralized servers.

telegram · zaihuapd · Mar 15, 01:28

**Background**: Supply chain attacks targeting open source repositories have grown increasingly common in recent years, as compromised open source code can spread malware to thousands of downstream users quickly. Zero-width Unicode characters are special characters that render as invisible, zero-width space in most code editors, making them ideal for obfuscating malicious code. Attackers have started testing blockchains as alternative command and control channels because traditional centralized server-based channels can be easily shut down by security researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/malicious-packages-using-invisible-unicode-found-in-151-github-repos-and-vs-code">Invisible malicious code attacks 151 GitHub repos and VS Code ...</a></li>
<li><a href="https://securityonline.info/glassworm-supply-chain-worm-uses-invisible-unicode-and-solana-blockchain-for-stealth-c2/">GlassWorm Supply Chain Worm Uses Invisible Unicode and Solana ...</a></li>
<li><a href="https://www.knostic.ai/blog/zero-width-unicode-characters-risks">Zero Width Unicode Characters: the Risks you Can't See</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#supply chain attack`, `#GitHub`, `#software security`

---

<a id="item-3"></a>
## [AI Slopocalypse Ends Jazzband's Open Model](https://simonwillison.net/2026/Mar/14/jannis-leidel/#atom-everything) ⭐️ 7.0/10

Jannis Leidel of Jazzband announced that the flood of AI-generated spam pull requests and issues on GitHub, dubbed the "slopocalypse", has made Jazzband's open membership and shared push access collaborative model untenable. This high-profile incident highlights the growing threat of AI spam to open source collaboration, forcing the global open source community to re-evaluate long-standing open contribution models. Industry data shows only 1 in 10 AI-generated pull requests meet open source project standards, and prominent project curl already shut down its public bug bounty after spam confirmation rates dropped below 5%.

rss · Simon Willison · Mar 14, 18:41

**Background**: Jazzband was founded over 10 years ago as an experimental collaborative community focused on sharing maintenance work for Python open source projects. Its core model granted all new members shared push access to project codebases, designed to lower barriers for new contributors and reduce maintainer burnout. The term slopocalypse refers to the recent mass influx of low-quality, AI-generated spam contributions to GitHub-hosted open source projects.

<details><summary>References</summary>
<ul>
<li><a href="https://jazzband.co/news/2026/03/14/sunsetting-jazzband">Jazzband - News - Sunsetting Jazzband</a></li>
<li><a href="https://github.com/jazzband">Jazzband · GitHub</a></li>
<li><a href="https://incusdata.com/blog/coding-matters-the-slopocalypse">Coding matters: The slopocalypse • 2025 • Incus Data Programming...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI spam`, `#GitHub`, `#software maintenance`

---

<a id="item-4"></a>
## [Instagram to End E2EE for DMs After 2026](https://www.theverge.com/tech/894752/instagram-end-to-end-encryption) ⭐️ 7.0/10

Meta has officially confirmed that Instagram will discontinue end-to-end encryption support for its direct messages after May 8, 2026, citing very low user adoption of the privacy feature. The company is directing users who need end-to-end encrypted communication to its other platform WhatsApp. This privacy-related change affects one of the world's most widely used social platforms, so it draws wide attention from digital privacy advocates and observers of big tech practices. It also reflects Meta's strategy to consolidate its encrypted messaging business on a single core platform. The decision was confirmed through an update to Instagram's official support page, and Meta does not offer any other alternative end-to-end encrypted service on Instagram itself after the discontinuation date.

telegram · zaihuapd · Mar 14, 04:47

**Background**: End-to-end encryption (E2EE) is a security methodology that ensures only the sender and recipient of a message can access the plaintext content of the communication. Even the service provider that hosts the conversation cannot read the unencrypted content, making E2EE a core feature for protecting personal communication privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hoganlovells.com/en/publications/endtoend-encryption-obstacle-or-pillar-of-national-security">End - to - end encryption : obstacle or pillar of national security?</a></li>
<li><a href="https://www.maketecheasier.com/end-to-end-encryption-principle-explained/">End - To - End Encryption (And Principle) Explained - Make Tech Easier</a></li>

</ul>
</details>

**Tags**: `#end-to-end encryption`, `#digital privacy`, `#Instagram`, `#Meta`, `#social media`

---

<a id="item-5"></a>
## [Disney Accuses Seedance 2.0 of Copyright Infringement](https://t.me/zaihuapd/40265) ⭐️ 7.0/10

On February 13, 2026, The Walt Disney Company sent a cease-and-desist letter to ByteDance, a copy of which was obtained by Axios. Disney accuses ByteDance of copyright infringement for training its commercial AI video generation model Seedance 2.0 with uncompensated Disney copyrighted works and including Disney-owned popular IP characters in the model. This is a high-profile development in the global debate over generative AI training copyright, and it could set important precedents for AI companies using entertainment studios' copyrighted content for commercial products. It will impact the future compliance framework of the global generative AI industry. The letter states that Seedance 2.0 can generate videos featuring Disney-owned IP characters from Star Wars and Marvel, including Spider-Man and Darth Vader, and some of these user-generated videos have been publicly shared on social media. Before the letter was sent, Motion Picture Association CEO Charles Rivkin had already called on ByteDance to stop the alleged infringing activities.

telegram · zaihuapd · Mar 15, 00:43

**Background**: Seedance 2.0 is ByteDance's multimodal text-to-video and image-to-video generation model that launched in beta in early February 2026. The legality of using copyrighted works without permission to train generative AI models is still contested globally, and the U.S. Copyright Office has stated there is no uniform answer to whether such use qualifies as fair use. Multiple content creators and media companies have recently taken legal action against AI firms over unlicensed training data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://www.skadden.com/insights/publications/2025/05/copyright-office-report">Copyright Office Weighs In on AI Training and Fair Use | Skadden, Arps, Slate, Meagher & Flom LLP</a></li>

</ul>
</details>

**Tags**: `#AI copyright`, `#copyright infringement`, `#AI video generation`, `#legal news`

---

<a id="item-6"></a>
## [EU Countries Back Ban on Harmful AI-Generated Content](https://hk.news.yahoo.com/share/0a951dd0-216e-316c-9224-5ff4842422ae) ⭐️ 7.0/10

After Elon Musk's Grok AI generated non-consensual sexualized images that sparked widespread backlash, EU member states have backed a ban on AI-generated non-consensual sexual content and child sexual abuse material as part of revisions to the EU's comprehensive AI regulations, with a European Parliament vote scheduled for later this month. This is a major milestone in global AI governance that addresses the harmful misuse of generative AI, setting a clear regulatory precedent for protecting personal dignity and vulnerable groups from AI-enabled sexual exploitation. The European Parliament relevant committee will vote on the ban on November 18, and the lawmaker pushing the ban emphasized that the rule goes beyond the isolated Grok scandal to set clear boundaries for AI's power to degrade human dignity.

telegram · AI_News_CN · Mar 14, 03:14

**Background**: Grok AI is a generative chatbot developed by Elon Musk's xAI company, launched in November 2023, and it has a record of generating multiple controversial outputs including non-consensual sexualized images. Deepfake is a type of synthetic media created or edited using artificial intelligence deep learning technology, which can produce highly realistic fake content depicting real people. The EU Artificial Intelligence Act is the European Union's flagship comprehensive regulatory framework for artificial intelligence, which adopts a risk-based approach to govern different categories of AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_AI">Grok AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_Intelligence_Act">Artificial Intelligence Act - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Regulation`, `#Generative AI`, `#Deepfake`, `#AI Governance`

---

<a id="item-7"></a>
## [Microsoft Brings Gaming Copilot to Xbox 2026](https://www.cnbeta.com.tw/articles/game/1553460.htm) ⭐️ 7.0/10

Microsoft confirmed that its AI gaming assistant Gaming Copilot will officially launch on Xbox Series X|S consoles in 2026, after entering beta testing on PC, mobile, and ASUS ROG Xbox Ally handhelds starting October 2025. Xbox Gaming AI head Sonali Yadav announced the plan at the recent GDC conference, noting the service will expand to more player platforms over time. This launch marks Microsoft's first integration of a native AI assistant into its flagship console line, demonstrating the company's broader AI strategy for gaming hardware ahead of the next-generation Xbox release. It will likely reshape how players get game recommendations, strategies and in-game help, accelerating the adoption of AI tools in the consumer gaming industry. Gaming Copilot has three core functions: personalized game recommendations based on player history, in-game tips without leaving the game screen, and tactical advice to improve player performance, and it works by analyzing in-game screenshots and screen captures. The current beta version defaults to uploading captured screen content for AI model training, which raises privacy compliance concerns, and it remains unclear if this default enabled setting will be retained for the Xbox console launch.

telegram · AI_News_CN · Mar 14, 08:03

**Background**: Gaming Copilot is an AI-powered personal assistant Microsoft developed specifically for video game players. Project Helix is the codename for Microsoft's next-generation Xbox console, which is planned to launch around 2028 as a hybrid platform that supports both Xbox and PC games. GDPR is the General Data Protection Regulation, a strict privacy regulation enacted by the European Union that governs the collection and processing of personal user data in the EU region.

<details><summary>References</summary>
<ul>
<li><a href="https://www.xbox.com/en-US/gaming-copilot">Gaming Copilot (Beta): Your personal gaming sidekick | Xbox</a></li>
<li><a href="https://en.wikipedia.org/wiki/Project_Helix">Project Helix</a></li>
<li><a href="https://en.wikipedia.org/wiki/GDPR">GDPR</a></li>

</ul>
</details>

**Tags**: `#Gaming AI`, `#Microsoft Copilot`, `#Xbox`, `#AI Privacy`

---