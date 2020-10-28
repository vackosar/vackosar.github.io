---
layout: post
title: "How Performers FAVOR+ Faster Transformer Attention"
date: 2020-10-25
categories: ml
description: The Performer model attention approximation has linear time & space complexity of input token count in contrast to vanilla Transformer's square complexity.
image: /images/performer-attention-complexity.jpg
permalink: /:categories/:title
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="The Performer FAVOR+ attention on the right has linear complexity. The Transformer attention on the left has square complexity."
        src="/images/performer-attention-complexity.jpg">
    <figcaption class="figure-caption">The Performer FAVOR+ attention on the right has linear complexity. The Transformer attention on the left has square complexity (<a href="https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html">source</a>).</figcaption>
</figure>

<!--
<iframe width="560" height="315" src="https://www.youtube.com/embed/uuNLz6eT_tg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

The attention mechanism is the kingpin of the Tranformer model. It drives the results, but runs the memory and time racket of \\( O(L^2d) \\), where \\( L \\) is input token count and \\( d \\) is the latent representation dimension.

[The Reformer](https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html), [Longformer](https://arxiv.org/abs/2004.05150) and others attempted to topple it with \\( O(L \log L ) \\).
But only recently published [Performer](https://ai.googleblog.com/2020/10/rethinking-attention-with-performers.html) done the job with \\( O(L d^2 \log d ) \\).

How was that done? Read on, traveller! I will tell you a great story. 


### Not Paying for the Attention

Original attention is a value vector weighted by softmax applied to dot product of key and query.

\\( a_{\mathbf{orig}} = \mathbf{softmax}(\frac{QK^\intercal}{\sqrt{d}})V \\)

The expensive part is the matrix multiplication of key and query with softmax. Can we get a cheap estimate of that operation?


#### Kernel Approximation
I described [a speed up using random features kernel approximation for word-movers distance](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents) in a previous post.
In this case, the Performer approximates Transformer attention by kernelizing the softmax using positive orthogonal random features.
Let's define the kernel as a resulting elements of the softmax result also called attention matrix values as a function of corresponding query and key vectors - rows of query and key matricies.

\\( k(Q_{i, \cdot }, K_{j, \cdot} ) = \\)
\\( \mathbf{softmax}(\frac{Q K^\intercal}{\sqrt{d}})_{i, j} =  \\)

\\( \mathbf{softmax}( \frac{ Q_{i, \cdot } K^{\intercal}_{j, \cdot} }{\sqrt{d}} ) \\)

If we rescale the variables, we are looking to estimate exponential value of a dot product of two vectors.

\\( \exp(x^\intercal y) = \\)
\\( \exp(- \frac{\lVert x \rVert^2 + \lVert y \rVert^2}{2}) \exp(\frac{\lVert x+y \rVert^2}{2}) \\)

The common way to estimate above function is using trigonometrical functions of random projection into vectors around zero.
That runs into issues as the approximation has high variance around zero and can lead to negative values.

The authors of the paper instead propose alternative approximation using hyperbolical function, which are non-negative and don't suffer from high variance.
I give below a taste of derivation of the approximation.

How to draw random vectors in order to estimate the exponential of the dot product above?

\\( \exp(\frac{\lVert x+y \rVert^2}{2}) = \\)
\\( \exp(\frac{\lVert x+y \rVert^2}{2}) \int \exp(- \lVert \omega - (x+y) \rVert^2 / 2 ) \mathbf{d} \omega (2\pi)^{-d/2} = \\)
\\( \int \exp(\omega^\intercal (x + y)) \exp(- \lVert \omega \rVert^2 /2) \mathbf{d} \omega (2\pi)^{-d/2} = \\)
\\( \mathbb{E}_{\omega \~ N(0, 1)} \exp(\omega^\intercal (x+y)) \\),

where \\( \mathbb{E} \\) is an expected over random vectors from a standard normal distribution.

Next, the proof uses isotropy of the standard normal distribution to invert sign of \\( \omega \\) on one half of the exponential,
which results into hyperbolic cosine.

\\( \mathbb{E} \exp(\omega^\intercal u)  = \\)
\\( \mathbb{E} \frac{ \exp(\omega^\intercal u) + \exp(- \omega^\intercal u)}{2} = \\)
\\( \mathbb{E} \cosh (\omega^\intercal u) \ \\)

#### How Many Random \\( \omega \\) to FAVOR+?

So do we just start sampling of the distro and hope for the best? No!
If we make sure our [random vectors (features) are orthogonal, while still being drawn from standard normal distribution](https://arxiv.org/pdf/1703.00864.pdf).
The paper does this by drawing uniformly random orthogonal basis and then normalizing each row properly.

I am not clear however on the specifics here.
But I think we first draw uniformly random vector components,
removing the new vector projection to previously drawn vectors (Gramm-Schmidt orthogonalization method),
and then normalize the vectors to make their squared norms match standard normal distribution vector norm (Maxwell-Boltzman distribution).

Doing this, the authors arrived at stronger guarantees of fast convergence and unbiasedness of the softmax estimate.
The whole mechanism was then called FAVOR+.


