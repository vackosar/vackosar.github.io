---
layout: post
title: "Double Descent for Neural Network and Multiple Descent for Linear Regression"
date: 2020-09-15
categories: ml
description: The test loss as a function of number of parameters in a special case of linear regression can show arbitrary multiple-descent.
image: /images/double-descent-nn-mnist.webp
permalink: /:categories/:title
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="/images/double-descent-nn-mnist.webp"
        alt="Double Descent for fully connected NN on MNIST."/>
    <figcaption class="figure-caption">Double Descent for fully connected NN on MNIST. <a href="https://arxiv.org/abs/1812.11118">Source: Belkin 2019</a></figcaption>
</figure>


Bias-variance trade-off hypothesis implies that lowering train loss by increasing model size will lead to higher test loss.
Empirically this can be observed for example in case of decision tree, which beyond some size will achieve zero train loss, while test loss will rise.

But in general, bias-variance trade-off is not applicable.
Any kind of regularization of the optimizer, which is part of the model, will force model to look for "simple" solution, despite having capacity to fully fit the training data.
Behaviour of the optimiser can have big impact on the resulting test loss (generalization error).

## Over-parameterized

- no precise definition
- it can mean test loss zero
- usually means #params > #samples
- most modern machine learning works in over parametrized regime and uses various regularization methods

## Generalization Curve

- Defined as the test loss as a function of number of parameters of the model family.
- The test loss is usually normalized by the number of parameters.

##  Multiple Descent: Design Your Own Generalization Curve

In the Multiple Descent paper, the test loss as a function of number of parameters of special case of linear regression is highly controlled for in both under-parametrized and over-parametrized regimes.

### Authors rigorously prove:
- Existence of multiple descent in the generalization curve.
- That the number of descents can be designed.

### How it works?

The problem is linear regression without regularization with true linear model of zero.
Where all labels contain an error \\( y_i = 0 + \epsilon_i \\), which is normally distributed around zero.

However the features have all different distribution.
The authors select them, such that they can control the generalization curve.
Each feature \\( x_i \\) is distributed either as a Gaussian mixture \\( N^{mix}_{\sigma_1, 1} \\) or as a standard Gaussian \\( N(0, \sigma) \\) .
The data dimension is the feature count.

The model parameter count is increased by adding new features and corresponding labels to the data.
Note that for given generated data and labels, the optimal linear model can be calculated in a single step.
Authors then draw generalization curve as average test-loss normalized by the feature count (dimension) as a function of feature count.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="/images/double-descent-generalization-curve.webp"
        alt="Double Descent for fully connected NN on MNIST."/>
    <figcaption class="figure-caption">Bugged image - N_mix should be first, then N_0. Multiple Descent generalization curve (dimension normalized test loss as a function of number of parameters). Source TODO</figcaption>
</figure>


