---
title: Transformer Positional Embeddings and Encodings
description: How transformers encode information about token positions?
layout: post
categories: ml
image: /images/transformer-positional-embeddings.png
date: 2022-06-05
last_modified_at: 2022-06-11
permalink: /:categories/:title
redirect_from:
- /ml/transformer-positional-encodings
my_related_post_paths:
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
---



{% include mathjax.html %}

{% include shared_slides/positional-encodings-summary.md %}

{% include image.html src="/images/transformer-positional-embeddings.png" alt="positional embeddings in BERT architecture" %}


## Learned Positional Embeddings
- [Hierarchical Perceiver](https://arxiv.org/pdf/2202.10890.pdf) for high resolution inputs
  - learns low-dimensional positional [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) 
  - objective function is masked token prediction
  - embeddings are concatenated to input and used as a query for masked prediction
- [What Do Position Embeddings Learn?](https://arxiv.org/abs/2010.04903)
  - [sinusoidal embeddings below are not learned](#fourier-sinusoid-positional-encodings-in-bert)
  - GPT2 [learned positional embeddings as in GPT-1](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) have a very symmetrical structure
  - RoBERTa embeddings mildly similar to sinusoidal
  - BERT trained embeddings, up to position 128, are very similar to sinusoidal, but not elsewhere - likely training artefact
  - sinusoidal and GPT-2 were the best for classification

{% include image.html src="/images/visualization-of-cosine-similarity-of-position-embeddings.png" alt="Visualization of position-wise cosine similarity of different position embeddings" %}

## Positional Embeddings in Popular Models
- In [BERT](/ml/transformers-self-attention-mechanism-simplified), positional embeddings give first few tens of dimensions of the token embeddings meaning of relative positional closeness within the input sequence.
- In [Perceiver IO](/ml/cross-attention-in-transformer-architecture#cross-attention-in-perceiver-io) positional embeddings are concatenated to the input embedding sequence instead.
- In [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) the positional embeddings are learned feature of the RNN.


### Fourier (Sinusoid) Positional Encodings in BERT
- Positional embeddings are added to the word embeddings once before the first layer.
- Each position \\( t \\) within the sequence gets different embedding
  - if \\( t = 2i \\) is even then \\( P_{t, j} := \sin (p / 10^{\frac{8i}{d}})  \\)
  - if \\( t = 2i + 1 \\) is odd then \\( P_{t, j} := \cos (p / 10^{\frac{8i}{d}})  \\)
- This is similar to fourier expansion of Diracs delta
- dot product of any two positional encodings decays fast after first 2 nearby words
- average sentence has around 15 words, thus only first dimensions carry information
- the rest of the embeddings can thus function as word embeddings
- not translational invariant, only the [self-attention](/ml/transformers-self-attention-mechanism-simplified) key-query comparison is
- [in-practical work for high-resolution inputs](https://arxiv.org/pdf/2202.10890.pdf)

{% include image.html src="/images/position-embeddings-sinusoid.png" alt="Fourier (Sinusoid) Positional Encodings in BERT" %}

{% include shared_slides/rope-embeddings.md %}
