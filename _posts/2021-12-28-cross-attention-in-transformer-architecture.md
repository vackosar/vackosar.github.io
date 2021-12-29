---
title: Cross-Attention in Transformer Architecture
description: Cross-attention is a way add activations from another embedding sequence into transformer layers.
layout: post
categories: ml
image: /images/cross-attention-in-transformer-architecture.png
date: 2021-12-28
permalink: /:categories/:title
---

![Cross-Attention in Transformer Architecture](/images/cross-attention-in-transformer-architecture.png)

- an [attention mechanism](https://vaclavkosar.com/ml/expire-span-scaling-transformer-by-forgetting#self-attention-simplified-recap) that mixes usually different modalities
- one of the modalities defines the output dimensions and length by playing a role of a query
- This is similar [the feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) where the other sequence is static

## Description
- Let us have sequence A and sequence B
- Attention matrix from sequence A is used to highlight in sequence B
- Queries from sequence A
- Keys and Values from another sequence B
- sequences A and B lengths can differ


## Examples
- [DeepMind's RETRO Transformer](/ml/DeepMinds-RETRO-Transformer-Model)
- [CrossVit](https://arxiv.org/pdf/2103.14899.pdf)
