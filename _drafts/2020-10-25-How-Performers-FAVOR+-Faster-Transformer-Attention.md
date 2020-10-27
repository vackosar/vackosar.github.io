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

I described [a speed up using random features kernel approximation for word-movers distance](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents) in a previous post.
In this case, the Performer approximates Transformer attention by kernelizing the softmax using positive orthogonal random features.
Let's define the kernel as a resulting elements of the softmax result also called attention matrix values as a function of corresponding query and key vectors - rows of query and key matricies.

\\( k(Q_{i, \cdot }, K_{j, \cdot} ) = \\)

\\( \mathbf{softmax}(\frac{QK^\intercal}{\sqrt{d}})_{i, j} =  \\)

\\( \mathbf{softmax}( \frac{ Q_{i, \cdot }K^{\intercal}_{j, \cdot} }{\sqrt{d}} ) \\)



