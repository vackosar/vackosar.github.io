---
title: How Deep Neural Networks Learn
description: Notes that pull together Superposition, Memorization, Double Descent, Ensembling to get insights.
categories: ml
image: /images/classroom-neural-network-training.png
date: 2023-08-25
last_modified_at: 2023-08-27
layout: post
permalink: /:categories/:title
---

![neural network drawn on a blackboard in a class room](/images/classroom-neural-network-training.png)

Deep neural networks have multi-layer structure.
Gradient descent is used to propagate corrections backwards through the layers.

## Gradient Descent Intuition
Gradient descent calculates weight corrections (gradients) with backpropagation algorithm.
Backpropagation takes the distance from the correct results, and calculates gradients (derivatives) starting from the results and iterating through neural network layers back.
Because deep neural networks have layered structure, backpropagation uses chain-rule and analytical derivatives for known functions.
Backpropagation increases or decreases reliance on neuron outputs in proportion to their influence on pointing towards the true label.


## What is Overfitting and Memorization?

Overfitting refers to when model has **low training set loss, but high testing-set loss**.
For example, if a model has sufficient capacity and "insufficient regularization", it may memorize training data.
Read more about [overfitting and double descent here](/ml/double-descent-contrary-to-bias-variance-trade-off).

**A decision tree is an if-else look up table** and with sufficient size without [pruning regularization](/ml/Neural-Network-Pruning-Explained) can **memorize training set**.
That is because the tree can create an individual bin for each dataset input, and then recover desired training set label.

If ReLU neuron activates, we can say that the neuron memorized to respond.
Each neuron represents a dot-product of input vector with weight vector, and the dot-product is positively valued, the neuron outputs non-zero.
Because we can have a bias values, this is not only direction but a hyperplane.
In this way, we can see that a neural network of sufficient size can also learn to split hyperspace into planes, such that for each input there is a bin into which a hidden representation will fall and which will activate a neuron corresponding to a label.


## Memorization in Neural Networks via Superposition

Let's consider a fully connected neural network with a lower internal dimension than input and output.
In a way, this is auto-encoder configuration.

This set of ReLU neurons can memorize more vectors than their count, which is called [superposition (Anthropic)](https://transformer-circuits.pub/2022/toy_model/index.html).
In other words, ReLU network **can embed and recover more vectors than its dimension** (neurons), thanks to superposition.
Or, ReLU network memory is greater than a sum of its neurons or hidden dimension because of the non-linearity.

This means that internal embeddings of features are not fully orthogonal and have a small non-zero dot-product
During reconstruction ReLU will only activate for the original feature to be reconstructed, thanks to bias weights preventing activation.

A similar effect was observed in [Transformers (Hopfield Networks is All You Need)](https://ml-jku.github.io/hopfield-layers/).
During stored vector reconstruction, hidden activations form vectors with maximally different directions (polytopes) from when it reconstructs other stored vectors.


## Generalization is Finding Hidden Rules
Instead of embeddings, we can look at weight vectors.
In [Superposition, Memorization, and Double Descent](https://transformer-circuits.pub/2023/toy-double-descent/index.html)
**generalization was observed when weight vectors instead formed polytopes, while embeddings did not**.


### Frequency Leads to Memorization
In the toy model, they observed that those often repeated patterns where memorized, instead of generalized.


### Phase Change from Memorization to Abstraction
When memorization is no longer possible, generalization will happen.
The [testing set error may get worse for some time (double descent)](/ml/double-descent-contrary-to-bias-variance-trade-off).

- from data memorization to rule memorization
- embeddings change from crystals into noise into clusters of discovered rules


## Individually Trained Networks Overfit on First Discovered Features

From paper: [Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning](https://openreview.net/forum?id=Uuf2q9TfXGA),
which compares average ensembling, ensemble knowledge distillation, training averaged models, and individual models on classification problems.


### Random Feature Mapping
The Theory of random feature mapping (RFM) cannot explain deep learning neural network ensembling behavior as these are too different models.
They also behave different.

Random feature maps in machine learning are techniques used for dimensionality reduction and feature extraction.
RFM is based on sampling random matrices, which have been found to often preserve dot product well.
For example, Gaussian Random Projections a simple element wise matrix sampling.
After these random features are sampled, then we can employ, for example, gradient boosting on them.
Similar methods are used by [Performer Transformer](/ml/Performers-FAVOR+-Faster-Transformer-Attention) and [word mover's embedding](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents).


### Ensemble Distillation
Ensemble is a combination of several models to make a prediction.
Ensemble distillation is much better for DL and performs similar to ensemble, contrary to random feature mapping.
Training a model that is average of output of 10 models does not improve results in case of deep learning,
because once a simple solution is found in one of the models, the gradients will prevent further exploration in the other models. 
On the other hand, in RFM this does not seem to be a problem, because gradient descent is not used?


### Input Data Distribution
Note that, input statistical distribution matters for the results of every machine learning algorithm.
Fortunately, most real world problems deal with a similar class of distributions.
In the case of Gaussian mixture, deep learning ensembling does not help, because test variance tends to go down, despite not test accuracy.

They define a multi-view assumption as compositional of the samples with smaller features.
If these features appear together, they trigger classification class.
Authors indicate this as possible because of explainable visualizations.


### Neural Networks with Gradient Descent Find Only Some Features
Then authors show that each model learns these local features differently and at different speeds.
And because they get the simplest features first, it becomes difficult to find the other features.
Then the model overfits and is not able to learn the other feature and rather learns a noise in the small number of samples.

Perhaps the layered nature of deep neural networks explains why some features are forgotten across the layers, if not reinforced enough.
This is what multiple separate training helps to prevent.
Random feature mapping and boosting as it is more shallow and has access to all the features, but then fails to optimize very well.

I wonder if:
- deduplication and better sampling of the training data help by preventing overfitting, because deduplication reduces repetition.
- dropout, which randomly prevents usage of specific features and helps with overfitting, but is turned off in inference mode.
- more data increase diversity and thus again reduce repetition and encourage generalization


### Ensemble Distillation Allows Learning More Features
Distillation works for DL because the network has a signal that there must be feature that it has to find it.
The model has the capacity, and with the additional signal, it can learn to detect all the features.


## My Questions
I wonder if:
- deduplication and better sampling of the training data help by preventing overfitting, because deduplication reduces repetition.
- regularization like Dropout, which randomly prevents usage of specific features and helps with overfitting, but is turned off in inference mode.
- more data increase diversity and thus again reduce repetition and encourage generalization

This post is related to capsule networks, which explicitly looks for find specific configurations of discovered features.

## Other topics

Other topics in training neural networks:
- optimization algorithms (SGD, Adam) and their parameters like learning rate
- initialization, e.g., [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)
