---
layout: post
title: "Double Descent for NN and Multiple Descent for Linear Regression"
date: 2020-09-15
categories: ml
description: The test loss as a function of number of parameters in a special case of linear regression can show arbitrary multiple-descent.
image: /images/double-descent-nn-mnist.webp
permalink: /:categories/:title
---

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="/images/double-descent-nn-mnist.webp"
        alt="Double Descent for fully connected NN on MNIST."/>
    <figcaption class="figure-caption">Double Descent for fully connected NN on MNIST. <a href="https://arxiv.org/abs/1812.11118">Source: Belkin 2019</a></figcaption>
</figure>


Bias-variance trade-off hypothesis implies that increasing model size will lead to a lower train loss, but also a higher test loss.
Empirically this can be observed for example in case of decision tree, which beyond some size will achieve zero train loss, while increasing test loss.
In case of a [linear regression, bias-variance tradeoff](http://www.dam.brown.edu/people/geman/Homepage/Essays%20and%20ideas%20about%20neurobiology/bias-variance.pdf) can be expressed via an equation.

\\( E [ (y - f(x, D))^2 |x, D] = E [ (y - E[y|x])^2 | x, D] + (f(x, D) - E[y | x])^2 \\)

Where first element represents the bias and second the variance.


But in general, bias-variance trade-off is not applicable.
Any kind of regularization of the optimizer, which is part of the model, will force model to look for "simple" solution, despite having capacity to fully fit the training data.
Behaviour of the optimiser can have big impact on the resulting test loss (generalization error).


