---
layout: post
title: "StarSpace Embedding"
categories: papers
date: 2020-05-08
description: To embed variety of entities into single vector space, this paper describes general-purpose neural embedding model.
image: https://github.com/facebookresearch/StarSpace/blob/master/examples/starspace.png
---

## Summary
1. Is general-purpose method to embed multi-class entities into single vector space e.g. words, documents, and users can be embedded into single space.
1. Requires discrete features e.g. user's features are docs that he liked.
1. Trains by summing bag-of-features and contrasting with k-negative samples.
1. In terms of quality the method performs competitively.
1. In terms of speed the method is on par with FastText.


## Source
"[StarSpace: Embed All The Things!](https://arxiv.org/abs/1709.03856)" with publication date 2017-11-21.
Authors are Ledell Wu, Adam Fisch, Sumit Chopra, Keith Adams, Antoine Bordes and Jason Weston.
Funding comes from Facebook AI Research.


## Method

The method is highly influenced by FastText, in comparison to which it is much more general, although slightly slower.
If I understand correctly, in contrast to Word2vec and FastText there is no word (input) vector concept, but only context (output) vector concept.

For each discrete feature, an embedding vector is fitted such that SGD minimizes the loss function below.
Embeddings of the composite entities are then constructed as a sum of their sub-entities (bag-of-features).
The loss function relies on having labels for positive (close) and non-positive (negative, distant) pairs.
Thanks to this very general notion of labels, the embeddings can be constructed in many different scenarios.

The loss is calculated using margin [ranking loss](https://gombru.github.io/2019/04/03/ranking_loss/) `max(0, m - sim(s, ps) + sim(s, ns[0]) + sim(s, ns[1]) ...`,
where `m` is margin, `s` is sample, `ps` is positive sample, `ns` is negative sample array.
Similarity function used was either dot product performing better in lower number of dimensions or cosine similarity being more suitable for higher dimensionality.

Embeddings for classes of entities higher in hierarchy are calculated by summing bag-of-words representations of its children.



## Applications
- text classification
- ranking entities
- collaborative filtering-based recommendation
- content-based recommendation
- word, sentence, dcoument, graph embedding
