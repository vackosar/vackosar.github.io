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
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
- _posts/2023-07-03-OpenAIs-Image-Text-Model-CLIP.md
---



- Want to represent data as numbers to compute our tasks.
- Start with simple high dimensional feature vectors created from input data e.g. vocabulary word index.
- Then find lower dimensional vectors optimized for our task called embeddings.
- Can train with both unsupervised, and supervised tasks:
  - How similar are these two product images? (similarity e.g. student-teacher)
  - How similar is this image to this abstract image class? (classification)
- Before representing the full data we often split data into meaningful parts called tokens


## Input Tokenization

{% include shared_slides/tokenization-summary.md %}


## Embedding Tokens
- Map Tokens to their representations e.g. word (token) embeddings, image patch (token) embeddings.
- Step by step pool the sequences of embeddings into shorter sequences, until we get a single full contextual data representation for the output.
- Can pool via averaging, summation, segmentation, or just take a single sequence position output embedding (class token).


{% include shared_slides/representations.md %}


## Image Embeddings
- instead of tokens (words) we embed image patches
- convolutional networks embed overlapping patches and progressively pool them into a single image embedding
- [Vision Transformer (ViT)](https://arxiv.org/pdf/2010.11929.pdf) uses [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) and the output class token embedding is used as an image embedding

![vision transformer (ViT) architecture](/images/vision-transformer-vit-architecture.png)


## Reusing Embeddings
- Embeddings are trained to represent data such that it makes the training task easy
- Embeddings perform often better than the input feature vectors on at least related tasks
- some tasks are more related than others: [multi-task learning](https://ai.googleblog.com/2021/10/deciding-which-tasks-should-train.html)
- speculation: Because of high number precision, smoothness of the neural network layers, and random weight initialization, most input information is preserved within the output embeddings
  - that would explain why neural networks can improve by training
- for example Word2vec or BERT embeddings are trained on a word prediction tasks, but their embeddings are useful for e.g. text classification tasks
 
![inter-task affinity for multi-task learning task grouping](/images/disentangle-multi-task.png)
