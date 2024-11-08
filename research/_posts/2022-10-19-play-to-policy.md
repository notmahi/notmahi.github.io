---
date: 2022-10-19 20:00:00
layout: research 
tags: play data, transformers, behavior transformers, real robot experiments, play kitchen
pills: supervised-policy-learning
description: Play to Policy
title: "From Play to Policy: Conditional Behavior Generation from Uncurated Robot Data"
authors: "Zichen Jeff Cui, Yibin Wang, Nur Muhammad (Mahi) Shafiullah, Lerrel Pinto"
paper_url: https://arxiv.org/abs/2210.10047
code_url: https://github.com/jeffacce/play-to-policy
project_site_url: https://play-to-policy.github.io/
show_blog_link: false
show_card: true
highlight: "Top 5% (Oral)"
venue: "International Conference of Learning Representations (ICLR) 2023"
local_video: assets/images/research/play_to_policy.mp4
---

While large-scale sequence modeling from offline data has led to impressive performance gains in natural language and image generation, directly translating such ideas to robotics has been challenging. One critical reason for this is that uncurated robot demonstration data, i.e. play data, collected from non-expert human demonstrators are often noisy, diverse, and distributionally multi-modal. This makes extracting useful, task-centric behaviors from such data a difficult generative modeling problem. In this work, we present Conditional Behavior Transformers (C-BeT), a method that combines the multi-modal generation ability of Behavior Transformer with future-conditioned goal specification. On a suite of simulated benchmark tasks, we find that C-BeT improves upon prior state-of-the-art work in learning from play data by an average of 45.7%. Further, we demonstrate for the first time that useful task-centric behaviors can be learned on a real-world robot purely from play data without any task labels or reward information. Robot videos are best viewed on our project website: [https://play-to-policy.github.io](https://play-to-policy.github.io).