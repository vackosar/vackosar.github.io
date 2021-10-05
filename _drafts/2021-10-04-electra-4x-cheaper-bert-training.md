---
layout: post
title: "Electra - 4x Cheaper BERT Training"
date: 2021-10-04
categories: ml
description: Reducing training flops 4x by GAN-like discriminative task compared to RoBERTa
permalink: /:categories/:title
---


# Why Is BERT Training Inefficient?
- [BERT = Bidirectional Encoder Representations from Transformers](https://arxiv.org/pdf/1810.04805.pdf)
- Uses unsupervised pre-training
- Encodes text into WordPiece tokens 
- Pre-training replaces 15% inputs with "[MASK]" token,
- Then predicts original token ids based on context
- Every step costs me,
- But only a few tokens can be masked this way!

![img_1.png](/images/electra-bert.png)


# How To Improve?
- How to get difficult enough task for all tokens?
- [Electra paper @ Stanford & Google Brain @ ICRL 2020, Not SoTA](https://openreview.net/pdf?id=r1xMH1BtvB)
- Smaller generator and big discriminator
- Jointly train the generator and discriminator
- The generator is trained with masked language modeling (MLM) 
- For each masked position generator samples one token
- The big model discriminates true or fake token
 
![img.png](/images/electra-generator-discriminator.png) 


# The Architecture and Methods
- Generator and discriminator same architecture
  - only embeddings or tokens and positional are shared
  - sharing more was not helping
- Generator 2x - 4x smaller
  - bigger are not helping
  - compute more expensive
  - perhaps bigger too difficult task
- Trained jointly otherwise discriminator fails to learn
  - otherwise, the discriminator fails to learn
  
![img.png](../images/electra-loss.png)

![img.png](/images/electra-generator-size.png)


# Results
- Datasets:
  - GLUE: natural understanding benchmark
  - SQuAD: questions answering benchmark
- RoBERTa = BERT with better training and dataset
  - longer training, bigger batches, more data
  - remove next sentence objective
  - train on longer sequences
  - dynamically changing masking pattern
- XLNet = BERT with permutation language modelling
  - maximizes likelihood of the original sequence
  - compared to all other permutations
  - next-token prediction task

![img_1.png](/images/electra-results-glue.png)

![img.png](/images/electra-results-squad.png)


# Source of The Improvement
- compared alternative tasks on GLUE score

<table class="table">
  <thead>
    <tr><th>Task</th><th>Description</th><th>GLUE score</th></tr>
  </thead>
  <tbody>
    <tr><td>BERT</td><td>MLM with [MASK] token</td><td>82.2</td></tr>
    <tr><td>Replace MLM</td><td>masked tokens replaced with generated + LM</td><td>82.4</td></tr>
    <tr><td>Electra 15%</td><td>Discriminator over 15% of the tokens</td><td>82.4</td></tr>
    <tr><td>All-Tokens MLM</td><td>Replace MLM on all tokens + copy mechanism</td><td>84.3</td></tr>
    <tr><td>Electra</td><td>Discriminator over all tokens</td><td>85.0</td></tr>
  </tbody>
</table>

- Speculations:
  - loss over all inputs is important
  - masking causes pre-train to fine-tune mismatch
  - personally: some similarity to gradient boosting


# Follow up - MC-BERT
- [MC-BERT Paper](https://arxiv.org/pdf/2006.05744.pdf)
- Contrastive instead of discriminative
 
![img.png](../images/electra-mcbert.png)


# Follow Up - TEAMS
- also contrastive
- shares more weights

![img.png](../images/electra-teams.png)


