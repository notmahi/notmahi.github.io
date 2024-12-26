---
date: 2022-10-11 20:00:00
layout: research
tags: semantic fields, detic, lseg, llms, vlms, clip, neural fields, semantic navigation, sentence-bert 
pills: semantic-scene-representation, large-pretrained-models
description: CLIP Fields
title: "CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory"
authors: "Nur Muhammad Mahi Shafiullah, Chris Paxton, Lerrel Pinto, Soumith Chintala, Arthur Szlam" 
paper_url: https://arxiv.org/abs/2210.05663
code_url: https://github.com/notmahi/clip-fields
project_site_url: https://mahis.life/clip-fields/
show_blog_link: false
show_card: true
research_type: long-term-memory
highlight: "Outstanding Paper Award"
venue: "Workshop on Language and Robot Learning, CoRL 2022; Robotics: Science and Systems (RSS) 2023"
local_video: assets/images/research/clip_fields.mp4
---

We propose CLIP-Fields, an implicit scene model that can be trained with no direct human supervision. This model learns a mapping from spatial locations to semantic embedding vectors. The mapping can then be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, and view localization. Most importantly, the mapping can be trained with supervision coming only from web-image and web-text trained models such as CLIP, Detic, and Sentence-BERT. When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of the examples. Finally, we show that using CLIP-Fields as a scene memory, robots can perform semantic navigation in real-world environments.
