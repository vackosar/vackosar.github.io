---
title: How Deep Neural Networks Learn
description: Notes that pull together Superposition, Memorization, Double Descent, Ensembling to get insights.
categories: ml
date: 2023-08-25
last_modified_at: 2023-08-25
layout: post
permalink: /:categories/:title
---

## What is overfitting?

Overfitting refers to when model has **low training set loss, but high testing set loss**.
For example, if a model has sufficient capacity and "insufficient regularization", it may memorize training data.

**A decision tree is an if-else look up table** and with sufficient size without [pruning regularization](/ml/Neural-Network-Pruning-Explained) can **memorize training set**.
ReLU neuron can also "memorize", since each neuron represents a dot-product of input vector with weights vector.

## Superposition - Memorization in Neural Networks

A set of ReLU neurons can memorize more vectors than their count, which is called [superposition (Antropic)](https://transformer-circuits.pub/2022/toy_model/index.html).
ReLU network **can embed and recover more vectors than its dimension** (neurons), thanks to superposition.
ReLU network memory is greater than sum of its neurons or hidden dimension.
A similar effect was observed in [Transformers (Hopfield Networks is All You Need)](https://ml-jku.github.io/hopfield-layers/).
During stored vector reconstruction, hidden activations form vectors with maximally different directions (polytopes) from when it reconstructs other stored vectors.


## Generalization - Hidden Features
Instead of embeddings, we can look at weight vectors.
In [Superposition, Memorization, and Double Descent](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
**generalization was observed when weight vectors instead formed polytopes, while embeddings did not**.

## Frequency Leads to Memorization
In the toy model they observed that those often repeated patterns where memorized, instead of generalized.

## Phase Change
When memorization is no longer possible, generalization will happen.
The [testing set error may get worse for some time (double descent)](/ml/double-descent-contrary-to-bias-variance-trade-off).

- from memorization to rule memorization
- embeddings change from crystals into noise into clusters of discovered rules

"Another interesting property is that ReLU makes negative interference free in the 1-sparse case. This explains why the solutions we've seen prefer to only have negative interference when possible. Further, using a negative bias can convert small positive interferences into essentially being negative interferences."



## Individually Trained Networks Overfit on First Discovered Features

From paper: [Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning | OpenReview](https://openreview.net/forum?id=Uuf2q9TfXGA),
which compares average ensembling, emsamble knowledge distillation, training averaged models, and individual models on classification problems.


### Random Feature Mapping
Theory of random feature mapping (RFM) cannot explain deep learning neural network ensembling behaviour as these are too different models. They also behave different.

Random feature maps in machine learning are techniques used for dimensionality reduction and feature extraction.
RFM is based on sampling random matrices, which have been found to often preserve dot product well.
For example Gaussian Random Projections a simple element wise matrix sampling.
After these random features are sampled, then we can employ for example gradient boosting on them.
This method of approximation was also used in [Performer Transformer](/ml/Performers-FAVOR+-Faster-Transformer-Attention) and [word mover's embedding](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents).


### Ensemble Distillation
Ensemble distillation is much better for DL and performs similar to ensemble, in contrary to random feature mapping.
Training of average of 10 models does not work for DL, because once a simple solution is found in one of the models, the gradients will prevent futher exploration in the other models
On the other hand in RFM this does not seem to be problem, because gradient descent is not used?


### Input Data Distribution
Note that, input distribution matters for the results.
For Gaussian mixture ensemble for DL does not help.
Test variance can go down, despite not test accuracy.

They define multi-view assumption as compositional of the samples with smaller features, which if they appear together they trigger classification.
They indicate this as possible because of explainability visualizations.


### Neural Networks with Gradient Descent Find Only Some Features
Then they show that each model learns these local features differently and at different speed.
And because they get the simplest features first, it becomes difficult to find the other features.
Then the model overfits and is not able to learn the other feature and rather learns a noise in the small amount of samples.

Perhaps the layered nature of deep neural networks explains why some of features are forgotten across the layers, if not reinforced enough.
This is what multiple separate training helps to prevent.
Random feature mapping and boosting as it is more shallow and has access to all the features, but then fails to optimize very well.

I wonder if:
- deduplication and right sampling of the training data helps by preventing overfitting.
- dropout, which randomly prevents usage of specific features and helps with overfitting, but is turned off in inference mode.


### Ensemble Distillation Allows To Learn Multiple Features
Distillation works for DL because the network has a signal that there must be feature that it has to find it.
The model has the capacity and with the additional signal, it can learn to detect all the features.


## Capsule Networks
Above is related to capsule networks, which explicitly looks for find specific configurations of discovered features.


