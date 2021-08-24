---
layout: post
title: "Expire-Span: Scaling Transformer by Predicting Token Forgetting"
date: 2021-08-24
categories: ml
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
- a combination of above + global attention e.g. [Longformer](https://arxiv.org/pdf/2004.05150.pdf)

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

## Transformer-XL
- [Transformer-XL (Extra Long): Attentive Language Models Beyond a Fixed-Length Context](https://aclanthology.org/P19-1285.pdf)
- first self-attention model better than RNN on both char & word level LM
- auto-regressive: attention is backward only not bi-directional like BERT
- instead of recalculating tokens for each fixed span
- rather memorize previous token results
- because previous results saw context not available in the next step
- this effectively increases context
- positional embeddings must be relative

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Transformer-XL uses memory of previously calculated results to increase span"
        data-src="/images/transformer-xl-memory-attention.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Transformer-XL uses memory of previously calculated results to increase span
        (<a href="https://aclanthology.org/P19-1285.pdf">source</a>)
    </figcaption>
</figure>


## Compressive Transformer
- [Compressive Transformers for Long-Range Sequence Modelling](https://arxiv.org/pdf/1911.05507.pdf)
- maps several past tokens into one
- compressed tokens are appended into the context
- less flexibility due to fixed compression window size

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Compressive transformer"
        data-src="/images/expire-span-compressive-transformer.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Compressive transformer (<a href="https://arxiv.org/pdf/1911.05507.pdf">source</a>).
    </figcaption>
</figure>


## Adaptive Span
- learns to increase context length when needed
- similar to [Expire-Span](#expire-span-attention)
- except predicts span length instead of memory forgetting


## Expire-Span Attention
- Facebook AI Paper: [Not All Memories are Created Equal: Learning to Forget by Expiring](https://arxiv.org/abs/2105.06548)
- [Source](https://github.com/facebookresearch/transformer-sequential/blob/main/models/expire_span.py)
- uses memory ala Transformer-XL
- has default minimal span of size \\( K \\)
- \\( L \\) is maximum span
- for each input (memory) \\( h_i \\) into each layer compute once scalar \\( e_i \in [0, L] \\)
- \\( e_i \\) is called expire-span (expiration time span)
- \\( e_i = L \mathbf{\sigma}(w^\intercal h_i + b) \\)
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

## Expire-Span Loss
- Penalize higher memory usage with auxiliary term
- \\( \alpha > 0 \\) is a compression parameter
- \\( L_{total} = L_{task} + \alpha \sum_{i \in \lbrace 1, 2, ..., L \rbrace} e_i / T \\)
- randomly shorten memory for regularization


## Results on Enwik8
- better performance, less memory, faster
- LM metric bits per byte (or character) = average negative log base-2 probability of the target label

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Expire-span, Trans-XL, Adapt-Span, Compressive transformer parameters count and bits-per-byte on Enwik8"
        data-src="/images/expire-span-results-enwik8-summary.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Expire-span, Trans-XL, Adapt-Span, Compressive transformer bpb, memory, speed on Enwik8
        (<a href="https://arxiv.org/abs/2105.06548">source</a>)
    </figcaption>
</figure>


<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Expire-span, Trans-XL, Adapt-Span, Compressive transformer performance in bits-per-byte (bps) vs memory size on Enwik8"
        data-src="/images/expire-span-results-enwik8.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Expire-span, Trans-XL, Adapt-Span, Compressive transformer performance in bits-per-byte (bps) vs memory size on Enwik8
        (<a href="https://arxiv.org/abs/2105.06548">source</a>)
    </figcaption>
</figure>




<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Expire-span, Trans-XL, Adapt-Span, Compressive transformer parameters count and bits-per-byte on Enwik8"
        data-src="/images/expire-span-results-enwik8-2.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Expire-span, Trans-XL, Adapt-Span, Compressive transformer parameters count and bpb on Enwik8
        (<a href="https://arxiv.org/abs/2105.06548">source</a>)
    </figcaption>
</figure>

