---
layout: post
title: "Disentangled Representations"
date: 2021-10-25
categories: ml
description: TDO
permalink: /:categories/:title
---

# What is disentangled
- Goal change 
- Entangled representation = hard to to preserve some attributes and change others
- Disentangled: Attibutes have separate dimensions applied to them of there is known orthogonality

# Unsupervised Disentangled Representations
- Google 2019 Paper [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://ai.googleblog.com/2019/04/evaluating-unsupervised-learning-of.html)
- a large-scale evaluation of various unsupervised methods (12k models)
- On dataset Shape3D try to separate all attributes of the scene into 10 dimensions 
- No model disentangled reliably
- theorem assumptions about the data have to be incorporated into the model (inductive bias)
- so each unsupervised model needs to be at least specialized to some type of data
 
![Shape3D dataset for disentagling factors: floor color, wall color, object color, object size, camera angle](../images/disentangled-shape3d.png)

