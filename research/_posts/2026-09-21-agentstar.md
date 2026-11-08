---
date: 2026-09-21 20:00:00
layout: research 
tags: object tracking, 3D reconstruction, articulated objects, vision-language models, agents, analysis-by-synthesis
pills: semantic-scene-representation, large-pretrained-models
description: "AgentSTAR: Agentic Shape Tracking and Reconstruction from Monocular Videos"
title: "AgentSTAR: Agentic Shape Tracking and Reconstruction from Monocular Videos"
authors: "Kirill Mazur, Nikita Karaev, Matthew Chang, Jitendra Malik, Nur Muhammad Mahi Shafiullah"
paper_url: https://arxiv.org/abs/2609.24487
code_url: https://github.com/makezur/agenticSTAR
project_site_url: https://agenticstar.github.io/
show_blog_link: false
research_type: imperfect-information
show_card: true
local_video: assets/images/research/agentstar.mp4
---

The problem of reconstructing and tracking arbitrary objects from monocular videos remains a challenging one -- primarily due to the wide variety in solid and articulated, textured and textureless objects in the wild. In this work, we present a method for shape reconstruction and tracking from video via agentic analysis-by-synthesis. Unlike prior methods which first estimate dense pixel correspondences and then recover object motion from them, our method infers a structured 3D object model, including its geometry and kinematic structure, and uses this model to optimise object track estimates over time. In our optimisation loop, a Vision-Language Model (VLM) agent iteratively refines shape or generalised pose through a render-and-compare loop, combining coarse visual reasoning with numerical pose optimisation for precise state estimation. This structured formulation enables our method to track through large motion, articulation, and severe occlusion without relying on pixel-matching objectives. Quantitatively, on ARCTIC, our method substantially outperforms state-of-the-art 3D point-tracking baselines for articulated objects, and on HOT3D it outperforms all evaluated rigid-object tracking baselines.
