---
layout: post
title: "Electra - Cheaper BERT Training"
date: 2021-10-04
categories: ml
description: Increase efficiency training by GAN-like contrastive
permalink: /:categories/:title
---


# Why Is BERT Training Inefficient?
- vanilla BERT training masks some inputs
- then predicts them based on context
- but only a few tokens can be masked this way!
 
![img.png](/images/electra-masking.png)

# How To Improve?
- We 


Increases efficiency of training BERT-like model via GAN-like discriminator task.
- But major efficiency gain is in that the discriminator model has a task across entire sequence and not few masked tokens - corrupt or not corrupt.
- Trains small MLM generator on maximum likelihood jointly with big BERT discriminator.
- Weight sharing only embeddings or tokens and positional.
- Generator has to be 2x - 4x smaller and  to gain efficiency.
- learn ML electra https://openreview.net/pdf?id=r1xMH1BtvB
- Follow up paper improves on this with contrastive https://scholarphi.semanticscholar.org/?file=https://arxiv.org/pdf/2106.00139v1.pdf 
	- they report time comparison and not compute comparison with electra
- also MC-BERT multi-choice cloze
	- https://arxiv.org/pdf/2006.05744.pdf


# TODO Ideals
- bit like gradient boosting
- main idea image 


