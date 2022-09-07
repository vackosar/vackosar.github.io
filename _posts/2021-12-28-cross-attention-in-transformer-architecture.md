---
title: Cross-Attention in Transformer Architecture
description: Cross-attention is a way to merge two embedding sequences e.g. image with text.
layout: post
categories: ml
image: /images/cross-attention-in-transformer-architecture.png
video: NXjvcNVkX9o
date: 2021-12-28
last_modified_at: 2022-08-07
permalink: /:categories/:title
---

{% include mathjax.html %}
{% include load_video.html %}

Cross attention is:
- an [attention mechanism in Transformer architecture](/ml/transformers-self-attention-mechanism-simplified) that mixes two different embedding sequences
- the two sequences must have the same dimension
- the two sequences can be of different modalities (e.g. text, image, sound)
- one of the sequences defines the output length as it plays a role of a query input
- the other sequence then produces key and value input

## Cross-attention Applications
- [image-text classification](/ml/Multimodal-Image-Text-Classification) with Perceiver
- machine translation: [cross-attention helps decoder predict next token](#cross-attention-in-transformer-decoder) of the translated text

## Cross-attention vs Self-attention
![cross-attention perceiver io detail](/images/cross-attention-detail-perceiver-io.png)

Except for inputs, cross-attention calculation is the same as [self-attention](/ml/transformers-self-attention-mechanism-simplified).
Cross-attention combines asymmetrically two separate embedding sequences of same dimension, in contrast self-attention input is a single embedding sequence.
One of the sequences serves as a query input, while the other as a key and value inputs.
Alternative [cross-attention in SelfDoc](#cross-attention-in-selfdoc), uses query and value from one sequence, and key from the other.

[The feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) is related to cross-attention, except the feed forward layer does use softmax and one of the input sequences is static.
[Augmenting Self-attention with Persistent Memory paper](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) shows that Feed Forward layer calculation made the same as self-attention.

## Cross-attention Algorithm
- Let us have embeddings (token) sequences S1 and S2
- Calculate Key and Value from sequence S1
- Calculate Queries from sequence S2
- Calculate [attention matrix](/ml/transformers-self-attention-mechanism-simplified) from Keys and Queries
- Apply queries to the attention matrix
- Output sequence has dimension and length of sequence S2

In an equation: \\( \mathbf{softmax}((W_Q S_2) (W_K S_1)^\intercal) W_V S_1 \\)


## Cross-Attention in Popular Architectures

### Cross-Attention in Transformer Decoder
Cross-attention was described in the [Transformer](/ml/transformers-self-attention-mechanism-simplified) paper, but it was not given this name yet.
Transformer decoding starts with full input sequence, but empty decoding sequence.
Cross-attention introduces information from the input sequence to the layers of the decoder,
such that it can predict the next output sequence token.
The decoder then adds the token to the output sequence, and repeats this autoregressive process until the EOS token is generated.

![Cross-Attention in the Transformer decoder of Attention is All You Need paper](/images/cross-attention-in-transformer-decoder.png)

### Cross-Attention in Perceiver IO

{% include shared_slides/perceiver-io.md %}


### Cross-Attention in SelfDoc

![selfdoc cross-attention](/images/selfdoc-cross-attention.png)

In [Selfdoc](https://arxiv.org/pdf/2106.03331.pdf), cross-attention is integrated in a special way.
First step of their Cross-Modality Encoder, instead uses value and query from sequence A and then key from the sequence B.

### Other Cross-Attention Examples
- [DeepMind's RETRO Transformer uses cross-attention to incorporate the database retrived sequences](/ml/DeepMinds-RETRO-Transformer-Model)
- [Code example: HuggingFace BERT (key, value are from the encoder, while query is from the decoder)](https://github.com/huggingface/transformers/blob/198c335d219a5eb4d3f124fdd1ce1a9cd9f78a9b/src/transformers/models/bert/modeling_bert.py#L268)
- [CrossVit - here only simplified cross-attention is used](https://arxiv.org/pdf/2103.14899.pdf)
- [On the Strengths of Cross-Attention in Pretrained Transformers for Machine Translation](https://arxiv.org/pdf/2104.08771v1.pdf)


