---
title: Cross-Attention in Transformer Architecture
description: Cross-attention is a way to merge two embedding sequences e.g. image with text.
layout: post
categories: ml
image: /images/cross-attention-in-transformer-architecture.png
video: NXjvcNVkX9o
date: 2021-12-28
permalink: /:categories/:title
---

{% include mathjax.html %}
{% include load_video.html %}

Cross-attention is a very similar to self-attention, except we are putting together two sequences asymmetrically. One of the sequences serves as a query, while the other as a key and value.

- an [attention mechanism in Transformer architecture](/ml/transformers-self-attention-mechanism-simplified) that mixes two different embedding sequences
- the two sequences can be of different modalities (e.g. text, image, sound)
- one of the modalities defines the output dimensions and length by playing a role of a query
- similar to [the feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) where the other sequence is static
 
## Cross-attention Algorithm
- Let us have embeddings (token) sequences S1 and S2
- Calculate Key and Value from sequence S1
- Calculate Queries from sequence S2
- Calculate [attention matrix](/ml/transformers-self-attention-mechanism-simplified) from Keys and Queries
- Apply queries to the attention matrix
- Output sequence has dimension and length of sequence S2

In an equation: \\( \mathbf{softmax}((W_Q S_2) (W_K S_1)^\intercal) W_V S_1 \\)
- where the softmax output is the [attention matrix](/ml/transformers-self-attention-mechanism-simplified) 

## Cross-Attention in BERT Decoder
Cross-attention was described in the [Attention is All You Need (BERT) decoder](https://arxiv.org/pdf/1706.03762.pdf), but not named yet.
BERT decoding starts with full sized input sequence, but empty decoding sequence.
Cross-attention introduces information from the input sequence to the decoding layers,
such that the decoder can predict the next sequence token.
The next token is added to the output sequence and we repeat the decoding process.
 
![Cross-Attention in the decoder of Attention is All You Need (BERT) paper](/images/cross-attention-in-bert-decoder.png)

### Cross-Attention in Perceiver IO
[Perceiver IO](https://arxiv.org/pdf/2107.14795.pdf) is a general-purpose crossdomain architecture that can handle variety of inputs and outputs uses extensively cross-attention for:
- merging very long input sequences (e.g. images, audio) into the low dimensional latent embeddings sequence
- merging "output query" or "command" to decode the output value e.g. we can the model ask about a masked word

Advantage of this is that in general you can work with very high long sequences.
Architecture [Hierarchical Perceiver](https://arxiv.org/pdf/2202.10890.pdf) has ability to process even longer sequences by splitting into subsequences and then merging them.
Hierarchical Perceiver also learns the positional encodings with a separate training step with a reconstruction loss.
 
![Perceiver IO architecture](/images/cross-attention-perceiver-io.png)




## Other Examples
- [DeepMind's RETRO Transformer uses cross-attention to incorporate the database retrived sequences](/ml/DeepMinds-RETRO-Transformer-Model)
- [Code example: HuggingFace BERT (key, value are from the encoder, while query is from the decoder)](https://github.com/huggingface/transformers/blob/198c335d219a5eb4d3f124fdd1ce1a9cd9f78a9b/src/transformers/models/bert/modeling_bert.py#L268)
- [CrossVit - here only simplified cross-attention is used](https://arxiv.org/pdf/2103.14899.pdf)



