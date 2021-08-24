---
layout: post
title: "Expire-Span: Scaling Transformer by Predicting Token Forgetting"
date: 2021-08-24
categories: book
description: Reducing computational costs by differentiably dropping tokens from self-attention context.
permalink: /:categories/:title
------------------------------

{% include mathjax.html %}

## Self-Attention Complexity
- \\( \mathbf{softmax}(\frac{QK^\intercal}{\sqrt{d}})V \\)
- quadratic in sequence length \\( O(L^2) \\)
- but context size is crucial for some tasks e.g. character-level models
- multiple approaches already exits

## Previous Approaches

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


## Expire-Span
![expire-span-attention](/images/expire-span-attention.png)

