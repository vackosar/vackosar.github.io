---
layout: post
title: "Expire-Span: Scaling Transformer by Predicting Token Forgetting"
date: 2021-08-24
categories: book
description: Reducing computational costs by differentiably dropping tokens from self-attention context.
permalink: /:categories/:title
---

{% include mathjax.html %}

## Self-Attention Complexity
- \\( \mathbf{softmax}(\frac{QK^\intercal}{\sqrt{d}})V \\)
- quadratic in sequence length \\( O(L^2) \\)
- but context size is crucial for some tasks e.g. character-level models
- multiple approaches already exits

## Previous Approaches
- approximate softmax e.g. [Performer](/ml/Performers-FAVOR+-Faster-Transformer-Attention)
- sparsify attention e.g. [BigBird](https://arxiv.org/pdf/2007.14062.pdf)
- sliding span (window attention) e.g. [Multi-passage BERT](https://aclanthology.org/D19-1599.pdf)
- a combination of above e.g. [Longformer](https://arxiv.org/pdf/2004.05150.pdf)
- [compressive transformer](https://arxiv.org/pdf/1911.05507.pdf)
  - maps several past tokens into one
  - compressed tokens are appended into the span
  - fixed compression window
- adaptively increase span e.g. [Adaptive-Span]
  - similar to this paper
  - except predicts span length instead of token forgetting

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Longformer self-attention patterns comparison"
        data-src="/images/longformer-attention-patterns.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Longformer self-attention patterns comparison (<a href="https://arxiv.org/pdf/2004.05150.pdf">source</a>).
    </figcaption>
</figure>


## Expire-Span Attention
- Paper: [Not All Memories are Created Equal: Learning to Forget by Expiring](https://arxiv.org/abs/2105.06548)
- \\( L \\) is maximum span
- for each input (memory) \\( h_i \\) into each layer compute once scalar \\( e_i \in [0, L] \\)
- \\( e_i \\) is called expire-span (expiration time span)
- \\( e_i = L \mathbf{softmax}(w^\intercal h_i + b) \\)
- The model slides over the text with time steps.
- \\( t \\) denotes time-step.
- if \\( r_{ti} := e_i - (t-i) < 0 \\) then memory input is forgotten
- For differentiability linearly phase-out attention output:
  - \\( m_{ti} := \max(0, \min(1, 1 + \frac{r_{ti}}{R})) \\)
  - \\( a^\prime_{ti} := \frac{ m_{ti} a_{ti} }{ \sum_j m_{tj} a_{tj} } \\)

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Expire-span attention: For every sequence input h_i it calculates expiration time span e_i."
        data-src="/images/expire-span-attention.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Expire-span attention: For every sequence input h_i it calculates expiration time span e_i.
        (<a href="https://arxiv.org/abs/2105.06548">source</a>)
    </figcaption>
</figure>


