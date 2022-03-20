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

## Cross-Attention in BERT Decoder
Cross-attention was described in the [Attention is All You Need (BERT) decoder](https://arxiv.org/pdf/1706.03762.pdf), but not named yet.
 
![Cross-Attention in the decoder of Attention is All You Need (BERT) paper](/images/cross-attention-in-bert-decoder.png)

### Cross-Attention in Perceiver IO
[Perceiver IO](https://arxiv.org/pdf/2107.14795.pdf) is a general-purpose architecture that uses extensively cross-attention for:
- merging input into the low dimensional latent transformer sequence
- merging output "query" or "command" to decode the output value
 
![Perceiver IO architecture](/images/cross-attention-perceiver-io.png)

## Cross-attention Algorithm
- Let us have embeddings (token) sequences S1 and S2
- sequences A and B lengths can differ
- Calculate Key and Value from sequence S1
- Calculate Queries from sequence S2
- Calculate [Attention matrix A](/ml/transformers-self-attention-mechanism-simplified) from Keys and Values
- Apply queries to the attention matrix A
- Output sequence has dimension and length of sequence S2


## Other Examples
- [DeepMind's RETRO Transformer uses cross-attention to incorporate the database retrived sequences](/ml/DeepMinds-RETRO-Transformer-Model)
- [Code example: HuggingFace BERT (key, value are from the encoder, while query is from the decoder)](https://github.com/huggingface/transformers/blob/198c335d219a5eb4d3f124fdd1ce1a9cd9f78a9b/src/transformers/models/bert/modeling_bert.py#L268)
- [CrossVit - here only simplified cross-attention is used](https://arxiv.org/pdf/2103.14899.pdf)



