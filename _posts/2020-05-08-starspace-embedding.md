---
layout: post
title: StarSpace - Embeddings For Documents, Users, and Words
date: 2020-05-08
categories: ml
description: Create vectors of various entities in a single space with this general-purpose embedding model from Facebook AI.
image: https://raw.githubusercontent.com/facebookresearch/StarSpace/master/examples/starspace.png
video: 0bSsAeT-N6w
permalink: /:categories/:title
redirect_from:
- /papers/2020/05/08/starspace-embedding.html
my_related_post_paths:
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2021-03-22-Automatically-Expanding-Taxonomy.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
---



{% include load_video.html %}
{% include mathjax.html %}

## Summary
"[StarSpace: Embed All The Things!](https://arxiv.org/abs/1709.03856)" with publication date 2017-11-21 from Facebook AI Research
2. Is general-purpose method to [embed](/ml/Embeddings-in-Machine-Learning-Explained) multi-class entities into single vector space e.g. words, documents, and users can be embedded into single space.
3. Requires discrete features e.g. user's features are docs that he liked.
4. Trains by summing bag-of-features and contrasting with k-negative samples.
5. In terms of quality the method performs competitively.
6. In terms of speed the method is on par with [FastText](/ml/FastText-Vector-Norms-And-OOV-Words).


## Method

![facebook starspace model method - sum](/images/starspace-sum.svg)

We train only the vectors directly without any other parameters.
In contrast to Word2vec and [FastText](/ml/FastText-Vector-Norms-And-OOV-Words) there is no word (input) vector concept, but only context (output) vector concept.
The method is highly influenced by FastText, in comparison to which it is much more general, although slightly slower.

For each discrete feature, an embedding vector is fitted such that SGD minimizes the loss function below.
Embeddings of the composite entities are then constructed as a sum of their sub-entities (bag-of-features).
The loss function relies on having labels for positive (close) and non-positive (negative, distant) pairs.
Thanks to this very general notion of labels, the embeddings can be constructed in many different scenarios.

\\( v_{\mathrm{document}} = \sum_{w \in \mathrm{document}} v_w \\)

The loss is calculated using margin [ranking loss](https://gombru.github.io/2019/04/03/ranking_loss/) `max(0, m - sim(s, ps) + sim(s, ns[0]) + sim(s, ns[1]) ...`,
where `m` is margin, `s` is sample, `ps` is positive sample, `ns` is negative sample array.
Similarity function used was either dot product performing better in lower number of dimensions or cosine similarity being more suitable for higher dimensionality.

Embeddings for classes of entities higher in hierarchy are calculated by summing bag-of-words representations of its children.


## Results

Text classification comparison with [FastText](/ml/FastText-Vector-Norms-And-OOV-Words):

![StarSpace text classification results comparison with fastText](/images/starspace-text-classification-results.png)

Content based document recommendation, each user is described by the bag-of-documents they like, while each document is described by its bag-of-words.

![StarSpace content-based recommendation results comparison with TF-IDF, word2vec, fastText](/images/starspace-content-based-recommendation-results.png)


## Applications
- text classification 
- ranking entities e.g. [Automatically Expanding Taxonomy](/ml/Automatically-Expanding-Taxonomy)
- collaborative filtering-based recommendation
- content-based recommendation
- word, sentence, document, graph embedding


## Beyond StarSpace
While StarSpace is computationally and memory-wise cheap, post 2017 the state of the art usually involves [Transfomer models](/ml/transformers-self-attention-mechanism-simplified).
If you don't understand [transformer or self-attention](/ml/transformers-self-attention-mechanism-simplified) yet, then [read more about it here](/ml/transformers-self-attention-mechanism-simplified).


## Quiz

Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=d0dfd88a-4712-42a6-bec3-68c86133d1ce">StarSpace Quiz</a>

