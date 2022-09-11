---
title: "Embeddings in Machine Learning Explained"
description: "Embedding is a task specific lower dimensional vector representation of data like a word, image, document, or an user."
layout: post
categories: ml
date: 2022-09-11
image: /images/word2vec-10k-tensorflow-projector.png
last_modified_at: 2022-09-11 
permalink: /:categories/:title
---

- We want to represent data as numbers to compute our tasks.
- We start with simple high dimensional feature vectors created from input data e.g. vocabulary word index.
- Then we find lower dimensional vectors optimized for our task called embeddings.
- Common training tasks:
  - How similar are these two product images? (similarity e.g. student-teacher)
  - How similar is this image to this abstract product image class? (classification)


## Input Tokenization
- before representing the full data we often split data into meaningful parts
  - images are split into patches
  - text split into tokens (words) e.g. [transformer tokenization](/ml/transformer-embeddings-and-tokenization)
- these parts (tokens) have representations of their own e.g. word (token) embeddings, image patch (token) embeddings.
- progressively we pool the embeddings into full contextual data representation
- Common training task: predict the masked word (de-noising)

![tokenization and embeddings](/images/transformer-tokenization-and-embeddings.drawio.svg)


{% include shared_slides/representations.md %}


## Image Embeddings
- instead of tokens (words) we embed image patches
- convolutional networks embed overlapping patches and progressively pool them into a single image embedding
- [Vision Transformer (ViT)](https://arxiv.org/pdf/2010.11929.pdf) uses [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) and the output class token embedding is used as an image embedding

![vision transformer (ViT) architecture](/images/vision-transformer-vit-architecture.png)