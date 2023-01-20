---
title: Superposition, Memorization, and Double Descent
description: 
categories: health
date: 2022-12-26
last_modified_at: 2022-12-26
layout: post
image: /images/psyllium-husk-black-beans.png
permalink: /:categories/:title
my_related_post_paths:
- _posts/2017-08-12-Fish-Roe-vs-Fish-Oil.md
- _posts/2016-07-16-Boost-Jog-Morale-Using-Mil-Cadence.md
- _posts/2017-12-25-Cheap-And-Tiny-Walking-Desk.md
---

## What is overfitting?

Overfitting refers to when model has **low training set loss, but high testing set loss**.
For example, if a model has sufficient capacity and "insufficient regularization", it may memorize training data.

**A decision tree is an if-else look up table** and with sufficient size without [pruning regularization](/ml/Neural-Network-Pruning-Explained) can **memorize training set**.
ReLU neuron can also "memorize", since each neuron represents a dot-product of input vector with weights vector.

## Superposition - Memorization in NNs 
A set of ReLU neurons can memorize more vectors than their count, which is called [superposition (Antropic)](https://transformer-circuits.pub/2022/toy_model/index.html).
We observe superposition when a ReLU network **can embed and recover more vectors than its dimension** (neurons).
ReLU network memory is greater than sum of its neurons or hidden dimension.
A similar effect was observed in [Transformers (Hopfield Networks is All You Need)](https://ml-jku.github.io/hopfield-layers/).
During stored vector reconstruction, hidden activations form vectors with maximally different directions (polytopes) from when it reconstructs other stored vectors.


## Generalization - Hidden Features

Instead of embeddings, we can look at weight vectors.
In [Superposition, Memorization, and Double Descent](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
**generalization was observed when weight vectors instead formed polytopes, while embeddings did not**.
Below increasing the training set size.


## Phase Change

- from memorization to rule memorization
- embeddings change from crystals into noise into clusters of discovered rules
