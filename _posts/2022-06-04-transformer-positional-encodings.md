---
title: "Transformer Positional Encodings"
description: "How transformers encode information about token positions?"
layout: post
categories: ml
image: /images/transformer-positional-embeddings.png
date: 2022-06-05
last_modified_at: 2022-06-11
permalink: /:categories/:title
---

{% include mathjax.html %}

{% include shared_slides/positional-encodings-summary.md %}

![positional embeddings in BERT architecture](/images/transformer-positional-embeddings.png)


## Positional Embeddings in Popular Models
- In [BERT](/ml/transformers-self-attention-mechanism-simplified), positional embeddings give first few tens of dimensions of the token embeddings meaning of relative positional closeness within the input sequence.
- In [Perceiver IO](/ml/cross-attention-in-transformer-architecture#cross-attention-in-perceiver-io) positional embeddings are concatenated to the input embedding sequence instead.
- In [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) the positional embeddings are learned feature of the RNN.


### Fourier Positional Encodings in BERT
- Positional embeddings are added to the word embeddings once before the first layer.
- Each position \\( t \\) within the sequence gets different embedding
  - if \\( t = 2i \\) is even then \\( P_{t, j} := \sin (p / 10^{\frac{8i}{d}})  \\)
  - if \\( t = 2i + 1 \\) is odd then \\( P_{t, j} := \cos (p / 10^{\frac{8i}{d}})  \\)
- This is similar to fourier expansion of Diracs delta
- dot product of any two positional encodings decays fast after first 2 nearby words
- average sentence has around 15 words, thus only first dimensions carry information
- the rest of the embeddings can thus function as word embeddings


{% include shared_slides/rope-embeddings.md %}
