---
date: 2022-10-19 20:00:00
layout: research 
tags: real robots, real home, imitation learning, home robotics, learning from demonstration, robotics dataset,  robot foundational model
pills: home-robotics, behavior-cloning-algorithms, visual-representation-learning
description: On Bringing Robots Home
title: "On Bringing Robots Home"
authors: "Nur Muhammad (Mahi) Shafiullah, Anant Rai, Haritheja Etukuru, Yiqian Liu, Ishan Misra, Soumith Chintala, Lerrel Pinto"
paper_url: https://arxiv.org/abs/2311.16098
code_url: https://github.com/notmahi/dobb-e
project_site_url: https://dobb-e.com/
show_blog_link: false
show_card: true
highlight: "Best Demo Finalist"
venue: "International Conference in Robotics and Automation (ICRA) 2024"
local_video: assets/images/research/dobb-e-thumbnail.mp4
---

Throughout history, we have successfully integrated various machines into our homes. Dishwashers, laundry machines, stand mixers, and robot vacuums are a few recent examples. However, these machines excel at performing only a single task effectively. The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - has long been a goal in robotics that has been steadily pursued for decades. In this work, we initiate a large-scale effort towards this goal by introducing Dobb-E, an affordable yet versatile general-purpose system for learning robotic manipulation within household settings. Dobb-E can learn a new task with only five minutes of a user showing it how to do it, thanks to a demonstration collection tool ("The Stick") we built out of cheap parts and iPhones. We use the Stick to collect 13 hours of data in 22 homes of New York City, and train Home Pretrained Representations (HPR). Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb-E can reliably solve the task on the Stretch, a mobile robot readily available on the market. Across roughly 30 days of experimentation in homes of New York City and surrounding areas, we test our system in 10 homes, with a total of 109 tasks in different environments, and finally achieve a success rate of 81%. Beyond success percentages, our experiments reveal a plethora of unique challenges absent or ignored in lab robotics. These range from effects of strong shadows, to variable demonstration quality by non-expert users. With the hope of accelerating research on home robots, and eventually seeing robot butlers in every home, we open-source Dobb-E software stack and models, our data, and our hardware designs on our website: [https://dobb-e.com](https://dobb-e.com).