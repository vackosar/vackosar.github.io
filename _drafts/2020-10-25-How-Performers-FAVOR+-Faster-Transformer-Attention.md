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

<div class="image-container">
    <img alt="The Performer FAVOR+ attention on the right has linear complexity. The Transformer attention on the left has square complexity." style="width: 90%; max-width: 500px" src="/images/performer-attention-complexity.jpg">
    <div class="centered">The Performer FAVOR+ attention on the right has linear complexity. The Transformer attention on the left has square complexity.</div>
</div>

<!--
<iframe width="560" height="315" src="https://www.youtube.com/embed/uuNLz6eT_tg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

The attention mechanism is the kingpin of the Tranformer model. It drives the results, but runs the memory and time racket of \\( O(L^2d) \\), where \\( L \\) is input token count and \\( d \\) is the latent representation dimension.

[The Reformer](https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html), [Longformer](https://arxiv.org/abs/2004.05150) and others attempted to topple it with \\( O(L \log L \\).
But only recently published [Performer](https://ai.googleblog.com/2020/10/rethinking-attention-with-performers.html) done the job with \\( O(L d^2 \log d ) \\).

How was that done? Read on, traveller! I will tell you a great story. 

# Original Attention

\\( softmax(QK^\intercal)V \\)

# Not Paying for the Attention

I described [a speed up using random features kernel approximation for word-movers distance](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents) in a previous post.
The Performer approximates Transformer attention by kernelizing the softmax using positive orthogonal random features.

