---
layout: post
title: "Double Descent for Neural Network and Multiple Descent for Linear Regression"
date: 2020-09-15
categories: ml
description: The test loss as a function of number of parameters in a special case of linear regression can show arbitrary multiple-descent.
image: /images/double-descent-nn-mnist.webp
permalink: /:categories/:title
---

<script src="/js/polyfill.min.js"></script>
<script id="MathJax-script" async src="/js/tex-mml-chtml.js"></script>


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


# Bias-Variance Trade-off for L2 Norm

In case of L2 norm, the train loss can be rewritten as a sum of bias term and variance term.

- A prediction function \\( f \\) was fitted on the training data \\( D = \lbrace (x_1, y_1), (x_2, y_2), ..., (x_n, y_n) \rbrace \\).
- A single the test sample \\( (x, y) \\) has a noisy label \\( y = Ey + \varepsilon \\), but the mean label \\( Ey \\) is the true value.
- Because the test label noise is independent of the training data, the fitted function has zero covariance with the test label noise: \\( E \varepsilon f = 0 \\).

Then the expected L2 test loss \\( E(y-f)^2 \\) below is conditioned on a test sample \\( x \\). The expectation is calculated over all draws of train samples \\( D \\) and label noise \\( \varepsilon \\).

\\( E(y-f)^2 \\)

\\( = E(y - Ey + Ey - f)^2 \\)

\\( = E (Ey - f)^2 + 2 E \varepsilon (Ey - f) + \sigma^2\\)

\\( = E (Ey - f)^2 + \sigma^2 \\)

\\( = (Ey - Ef)^2 + E(Ef - f)^2 + \sigma^2 \\).

Terms in above equation in given order represent:

<table border="1" class="dataframe">
<thead>
    <tr>
        <th scope="col">
            Term
        </th>
        <th scope="col">
            Description
        </th>
        <th scope="col">
            Name
        </th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>
            $$ (Ey - Ef)^2 $$
        </td>
        <td>The model's ability to fit the true training data.</td>
        <td>bias</td>
    </tr>
    <tr>
        <td>$$ E(Ef - f)^2 $$</td>
        <td>the model's ability to resist the training label noise, predict mostly the same outputs on same inputs, and thus generalize</td>
        <td>variance</td>
    </tr>
    <tr>
        <td>$$ \sigma^2 $$</td>
        <td>the test label noise</td>
        <td>irreducible error</td>
    </tr>
</tbody>
</table>
        
However, above decomposition does not explicitly prove how the individual components behave.
So, it is no prove of the proposed dilemma.

## Over-parameterized

- no precise definition
- it can mean test loss zero
- usually means #params > #samples
- modern ML models are over-parametrized and use various regularization methods

## Generalization Curve

- Defined as the test loss as a function of number of parameters of the model family.
- The test loss is usually normalized by the number of parameters.

##  Multiple Descent: Design Your Own Generalization Curve

In the [Multiple Descent paper](https://arxiv.org/abs/2008.01036), the test loss as a function of number of parameters of special case of linear regression is highly controlled for in both under-parametrized and over-parametrized regimes.

### Authors prove:
- Existence of multiple descent in the generalization curve.
- That the number of descents can be designed.

### How it works?

The problem is linear regression without regularization with true linear model of zero.
Where all labels contain an error \\( y_i = 0 + \varepsilon_i \\), which is normally distributed around zero.

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
    <figcaption class="figure-caption">This image is wrong: \\( N_mix \\) should be first, then \\( N_0 \\). Multiple Descent generalization curve (dimension normalized test loss as a function of number of parameters). [Source](https://arxiv.org/abs/2008.01036)</figcaption>
</figure>

There is an bug in the generalization curve image above.
The paper proves that the generalization curve can be pushed up if we introduce a gaussian mixture feature right after a standard gaussian.
That makes sense, as gaussian mixture is easier to "mis-learn" than standard gaussian.

While this is completely artificial model, it still interesting that we can have arbitrary number of descents contrary to the bias-variance dilemma.
