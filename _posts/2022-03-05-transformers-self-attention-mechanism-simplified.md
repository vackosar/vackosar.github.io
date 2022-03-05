---
title: "Transformer's Self-Attention Mechanism Simplified"
description: "Understand quickly successful architecture used in GPT, BERT, and other famous models."
layout: post
image: /images/self-attention-calculation-visualisation.png
categories: ml
date: 2022-03-05
permalink: /:categories/:title
---

{% include mathjax.html %}

![self-attention calculation visualization](/images/self-attention-calculation-visualisation.png)


- input \\( X \in \mathbf{R}^{L \times d} \\) is a sequence of embeddings of dimension \\( d \\) of length \\( L \\)
- output \\( Y \in \mathbf{R}^{L \times d} \\) has the same shape as input
- project \\( X \\) into 3 matrices of the same shape
  - query \\( X^Q := W^Q X \\),
  - key \\( X^K := W^K X \\)
  - value \\( X^V := W^V X \\)
- calculate "soft sequence-wise nearest neighbor search"
  - "search" all \\( L \times L \\) combinations of sequence elements of \\( X^K \\) and \\( X^Q \\)
  - for each sequence position \\( m \\): output more \\( X^V_{o} \\) when \\( X^K_o \\) is more similar to \\( X^Q_{m} \\)
  - in pseudo-code: \\( Y = \mathrm{matmul}_L(\mathrm{softmax}_L(\mathrm{matmul_d}(X_q, X_k^\intercal)), X_v) \\)
  - in equation: \\( Y = \mathbf{softmax}(QK^\intercal)V \\)
- More details in [Attention Is All You Need paper](https://arxiv.org/abs/1706.03762)

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Scaled Dot-Product Attention"
        data-src="/images/expire-span-attention-recap.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Scaled Dot-Product Attention (<a href="https://arxiv.org/pdf/1706.03762.pdf">source</a>).
    </figcaption>
</figure>


## Cross-Attention

Cross-attention is used layer to combine different sequences. [Read more here](/ml/cross-attention-in-transformer-architecture).