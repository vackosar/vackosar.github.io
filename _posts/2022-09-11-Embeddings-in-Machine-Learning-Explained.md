---
title: Embeddings in Machine Learning Explained
description: Embedding is a task specific lower dimensional vector representation of data like a word, image, document, or an user.
layout: post
categories: ml
date: 2022-09-11
image: /images/word2vec-10k-tensorflow-projector.png
last_modified_at: 2022-09-11
permalink: /:categories/:title
my_related_post_paths:
- _posts/2020-05-08-starspace-embedding.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
---



- We want to represent data as numbers to compute our tasks.
- We start with simple high dimensional feature vectors created from input data e.g. vocabulary word index.
- Then we find lower dimensional vectors optimized for our task called embeddings.
- Common training tasks:
  - How similar are these two product images? (similarity e.g. student-teacher)
  - How similar is this image to this abstract product image class? (classification)
- Before representing the full data we often split data into meaningful parts called tokens


## Input Tokenization

{% include shared_slides/tokenization-summary.md %}


## Embedding Tokens
- tokens are then mapped to their representations e.g. word (token) embeddings, image patch (token) embeddings.
- progressively we pool the sequences of embeddings into full contextual data representation


{% include shared_slides/representations.md %}


## Image Embeddings
- instead of tokens (words) we embed image patches
- convolutional networks embed overlapping patches and progressively pool them into a single image embedding
- [Vision Transformer (ViT)](https://arxiv.org/pdf/2010.11929.pdf) uses [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) and the output class token embedding is used as an image embedding

![vision transformer (ViT) architecture](/images/vision-transformer-vit-architecture.png)