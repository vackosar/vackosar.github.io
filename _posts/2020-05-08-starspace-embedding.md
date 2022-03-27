---
layout: post
title: "StarSpace Embedding - United and universal spaces of vectors"
date: 2020-05-08
categories: ML
description: To embed variety of entities into single vector space, this paper describes general-purpose neural embedding model.
image: https://raw.githubusercontent.com/facebookresearch/StarSpace/master/examples/starspace.png 
video: 0bSsAeT-N6w
permalink: /:categories/:title
redirect_from:
  - /papers/2020/05/08/starspace-embedding.html 
---

{% include load_video.html %}

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

We train only the vectors directly without any other parameters.
In contrast to Word2vec and FastText there is no word (input) vector concept, but only context (output) vector concept.
The method is highly influenced by FastText, in comparison to which it is much more general, although slightly slower.

For each discrete feature, an embedding vector is fitted such that SGD minimizes the loss function below.
Embeddings of the composite entities are then constructed as a sum of their sub-entities (bag-of-features).
The loss function relies on having labels for positive (close) and non-positive (negative, distant) pairs.
Thanks to this very general notion of labels, the embeddings can be constructed in many different scenarios.

The loss is calculated using margin [ranking loss](https://gombru.github.io/2019/04/03/ranking_loss/) `max(0, m - sim(s, ps) + sim(s, ns[0]) + sim(s, ns[1]) ...`,
where `m` is margin, `s` is sample, `ps` is positive sample, `ns` is negative sample array.
Similarity function used was either dot product performing better in lower number of dimensions or cosine similarity being more suitable for higher dimensionality.

Embeddings for classes of entities higher in hierarchy are calculated by summing bag-of-words representations of its children.


## Results


Text classification comparison with FastText:

![StarSpace text classification results comparison with fastText](/images/starspace-text-classification-results.png)

Content based document recommendation, each user is described by the bag-of-documents they like, while each document is described by its bag-of-words.

![StarSpace content-based recommendation results comparison with TF-IDF, word2vec, fastText](/images/starspace-content-based-recommendation-results.png)


## Applications
- text classification
- ranking entities
- collaborative filtering-based recommendation
- content-based recommendation
- word, sentence, dcoument, graph embedding

## Quiz

Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=d0dfd88a-4712-42a6-bec3-68c86133d1ce">StarSpace Quiz</a>


