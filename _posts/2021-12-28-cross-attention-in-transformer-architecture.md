---
title: Cross-Attention in Transformer Architecture
description: Cross-attention is a way to merge activations two embedding sequence in transformer architecture.
layout: post
categories: ml
image: /images/cross-attention-in-transformer-architecture.png
date: 2021-12-28
permalink: /:categories/:title
---

![Cross-Attention in Transformer Architecture](/images/cross-attention-in-transformer-architecture.png)

Cross-attention is a very similar to self-attention, except we are putting together two sequences asymmetrically. One of the sequences serves as a query, while the other as a key and value.

- an [attention mechanism in Transformer architecture](/ml/transformers-self-attention-mechanism-simplified) that mixes two different embedding sequences
- the two sequences can be of different modalities (e.g. text, image, sound)
- one of the modalities defines the output dimensions and length by playing a role of a query
- similar to [the feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) where the other sequence is static
- described in the [Attention is All You Need (BERT) decoder](https://arxiv.org/pdf/1706.03762.pdf), but named yet
 
![Cross-Attention in the decoder of Attention is All You Need (BERT) paper](/images/cross-attention-in-bert-decoder.png)


## Description
- Let us have sequence A and sequence B
- Attention matrix from sequence A is used to highlight in sequence B
- Queries from sequence A
- Keys and Values from another sequence B
- sequences A and B lengths can differ


## Examples
- [HuggingFace BERT code (key, value are from the encoder, while query is from the decoder)](https://github.com/huggingface/transformers/blob/198c335d219a5eb4d3f124fdd1ce1a9cd9f78a9b/src/transformers/models/bert/modeling_bert.py#L268)
- [DeepMind's RETRO Transformer](/ml/DeepMinds-RETRO-Transformer-Model)
- [CrossVit - here only simplified cross-attention is used](https://arxiv.org/pdf/2103.14899.pdf)


### Perceiver IO
[Perceiver IO](https://arxiv.org/pdf/2107.14795.pdf) uses extensively cross-attention:

![Perceiver IO architecture](/images/cross-attention-perceiver-io.png)
