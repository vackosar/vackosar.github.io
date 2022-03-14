---
title: "DeepMind's RETRO Transformer Model"
description: "Retrieval-Enhanced Language Model cross-attends trillions of tokens for SoTA on Wikitext103 and The Pile with 25x fewer parameters."
image: /images/retrieval-transformer-thumb.png 
video: -93KBOg77Sg
layout: post
categories: ml
date: 2021-12-29
permalink: /:categories/:title
---

{% include load_video.html %}

- next token (~word) prediction = autoregressive language model
- full name = Retrieval-Enhanced Transformer (RETRO) 
- paper = DeepMind's [Improving Language Models by Retrieving from Trillions of Tokens (2021)](https://arxiv.org/pdf/2112.04426v1.pdf), [Deep Mind Blog](https://deepmind.com/research/publications/2021/improving-language-models-by-retrieving-from-trillions-of-tokens)
- retrieves from [kNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) database [Bert](https://arxiv.org/pdf/1706.03762.pdf)-similar to the current text-chunk
- conditions on retrieved chunk and its continuation chunk
- so attends to previously encountered "future texts"
- SoTA on [Wikitext103](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/) and [the Pile](https://pile.eleuther.ai/) datasets
- Competitive on QA same perf [GPT-3](https://arxiv.org/pdf/2005.14165.pdf) with 25x less params
- model performs even when low train-test overlap
- retrieval reduces hallucinations and increases interpretability
- merges symbolic with deep learning similar to [Dream Coder program learning](/ml/dreamcoder-ai-wake-sleep-program-learning)


## Other Retrieval Architectures
- historically inverted index matching [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) and BM25
- latent topic modelling e.g. [LDA (2003)](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)
- [edit-distance search for translation (2018)](https://arxiv.org/pdf/1705.07267.pdf)
- [kNN-LM (2020)](https://openreview.net/forum?id=HklBjCEKvH)
  - search context LM embedding in database
  - linearly interpolate with LM predictions
- [DPR (2020)](https://aclanthology.org/2020.emnlp-main.550.pdf)
  - trains one [Bert (2017)](https://arxiv.org/pdf/1706.03762.pdf) for keys and one for values
  - uses contrastive loss
- RETRO in contrast uses
  - longer sequences
  - [cross-attention](/ml/cross-attention-in-transformer-architecture) allowing for multiple retrievals
  - bigger database

![retrieval transformer comparison](/images/retrieval-transformer-comparison.png)


## Training Dataset
- 10-lingual [MassiveText dataset](https://storage.googleapis.com/deepmind-media/research/language-research/Training%20Gopher.pdf)
- SentencePiece tokenizer vocabulary of 128k tokens
- Retrieval database 1.75T tokens
- 1 token ~ 4 characters ~ 1 word
- Chucks are 64 token sequences
- database ~13B records? 
- not retrieval from the same document during training

![MassiveText dataset composition table](/images/retrieval-transformer-massive-text.png)

 
## Architecture
- Frozen BERT retriever on chunk level
- differentiable encoder conditioned on query
- chunked [cross-attention](/ml/cross-attention-in-transformer-architecture) with previous chunk retrieval set 
- ablations show retrieval helps

![retriever transformer achitecture](/images/retriever-transformer-architecture.png)


## Retriever
- database is key-value memory of chunks
- each value is two consecutive chunks (128 tokens)
- each key is the first chunk from its value (first 64 tokens)
- each key is time-averaged BERT embedding of the first chunk
- key-vectors stored in k-nearest neighbors (similarity) [ScaNN db](https://github.com/google-research/google-research/tree/master/scann)
- db stores entire MassiveText train set during evaluation
  - training on 600B train subset
  - test set leakage into train set is controlled via a 13-gram Jaccard similarity
- 1.7T token database queried in 10ms
- retrieval is part of the input dataset pipeline
- optimum number of neighbors between 2 and 40 


## Encoding Retrieved Neighbours
- all retrieved values: 128 consecutive tokens
- are first passed through a bi-directional transformer encoder
- differentiably modulates retrieved chunks
- conditioning on query-chunks via [cross-attention](/ml/cross-attention-in-transformer-architecture) 
  - query-chunks hidden representations serves as key and value
  - encoded representations serve as queries
  - at the last layer before first [cross-attention](/ml/cross-attention-in-transformer-architecture)
- output is called retrieval set


## Chunked Cross Attention
- take previous chunk retrieval set to be autoregressive
- add relative positional encodings to each retrieved 
- concatenate into time dimension
- use hidden representation at the layer as query
- [cross-attend](/ml/cross-attention-in-transformer-architecture)

![retrieval transformer](/images/retrieval-transformer-cross-attention.png)


## RETRO Results
- SoTA on Wikitext103 and Pile
- on Pile with 7B params outperforms Jurassic-1 and Gopher
  - strongly outperforms on Github - repetitive dataset?
  - weakly outperforms on [HackerNews](https://news.ycombinator.com/)
  - underperforms on Math - not in MassiveText, poor search?
- comparable with GPT-3 when 25x less params
- generates on-topic and coherent text likely thanks to long memories
- underperforms specialized QA models

![RETRO on Pile](../images/retrieval-transformer-results-on-pile.png)

![RETRO generated text keeps on topic thanks to longer sequences](/images/retrieval-transformer-generated-text.png)

![RETRO question answering results](/images/retrieval-transformer-qa-results.png)

![RETRO Wikitext103](/images/retrieval-transformer-wikitext103-results.png)


## How to Use RETRO Ideas
- freeze any pre-trained transformer
- add and train chunked cross-attention and the encoder
- tune number of neighbours between 2 and 40 to your model size
- results should get close to training whole from scratch
- see "Retro-fitting baseline models" section
- Retro source code not published yet
