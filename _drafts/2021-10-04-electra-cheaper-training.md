---
layout: post
title: "Electra - Cheaper BERT Training"
date: 2021-10-04
categories: ml
description: Reducing training flops 4x by GAN-like discriminative task
permalink: /:categories/:title
---


# Why Is BERT Training Inefficient?
- vanilla BERT training masks some inputs
- then predicts them based on context
- but only a few tokens can be masked this way!
 
![img.png](/images/electra-masking.png)

# How To Improve?
- [Electra paper @ Stanford & Google Brain @ ICRL 2020](https://openreview.net/pdf?id=r1xMH1BtvB)
- smaller generator and big discriminator
- train big model
- smaller generator is jointly trained
- the generator is trained with masked language modeling (MLM) 
- for masked positions generator samples tokens
- these corrupted tokens are detected by the big model
- true or fake token?
 
![img.png](/images/electra-generator-discriminator.png) 

# Specifics
- generator and discriminator same architecture
- only embeddings are shared
- generator has 4x - 2x less layers
- trained jointly otherwise discriminator fails to learn
 

- Weight sharing only embeddings or tokens and positional.
- Generator 2x - 4x smaller


# Results

![img_1.png](/images/electra-results-glue.png)

![img.png](/images/electra-results-squad.png)

- Follow up paper improves on this with contrastive https://scholarphi.semanticscholar.org/?file=https://arxiv.org/pdf/2106.00139v1.pdf 
    - they report time comparison and not compute comparison with electra
- also MC-BERT multi-choice cloze
    - https://arxiv.org/pdf/2006.05744.pdf


# TODO Ideals
- bit like gradient boosting
- main idea image 

