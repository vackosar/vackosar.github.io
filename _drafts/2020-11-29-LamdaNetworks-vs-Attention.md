---
layout: post
title: "LambdaNetwork Transforms the Attention"
date: 2020-10-25
categories: ml
description: LambdaResNets beats EfficientNets but does it loose to Performer?
image: /images/performer-thumb.png
permalink: /:categories/:title
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

[//]: # <iframe width="560" height="315" src="https://www.youtube.com/embed/xpys_xqB6qY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


https://openreview.net/forum?id=xTJEN-ggl1b


## Comparison with Attention and Performer Attention

Are there any similarities between Lambda Networks Interactions and Transformer or Performer attention?
In following \\( X \\) will denote input sequence of dimension \\( n \times d \\), where \\( d \\) is the embedding dimension and \\( n \\) is the sequence length.
The interaction and attention context is the entire input sequence \\( X \\) for simplicity.


### Lambda Networks Interaction

Given \\( Q_n =  Q_{\cdot, n}  = (W_Q X)_{\cdot, n} \\),

\\( K =  (W_K X) \in \mathbb{R}^{n \times k} \\),

and \\( V =  (W_V X) \in \mathbb{R}^{n \times k} \\).

Positional embeddings is denoted by \\( E \in \mathbf{R}^{n \times n \times k} \\).
Softmax in the dimension \\( k \\) is denoted by \\( \sigma \\).

Then single lambda interaction (lambda head) is defined as following:

\\( \lambda_n Q_n = (\sigma(K) + E_n ) \odot_k Q_n \odot_n V^\intercal \\)

Where the matrix multiplication subscript declares which dimension it operates across.
Note that here we focus on case, where the context is entire input sequence and intra-dimension is 1.

If we reindex, we can rewrite this into more akin to transformer head with attention:

\\( \mathrm{head} = Q (\sigma(K) + E)^\intercal V \\).


### Transformer Head

Transformer positional encoding is denoted by \\( P \in \mathbf{R}^{n \times d} \\).
Normalized softmax in the dimension \\( d \\) is denoted by \\( \sigma \\).

Given
\\( Q = W_Q (X + P) \in \mathbb{R}^{n \times d}\\),

\\( K = W_K (X + P) \in \mathbb{R}^{n \times d}\\),

and \\( V = W_V (X + P) \in \mathbb{R}^{n \times d}\\)

then transformer head with attention is defined as:

\\( \mathrm{head} = \sigma(QK^\intercal) V \\)

#### Performer Head

Kernel function approximating softmax via a feature function \\( \phi \in \mathbb{R}^{n \times d} \rightarrow \mathbb{R}^{k \times d} \\),
which maps to the smaller dimension \\( k \\).

Performer transformer head with attention is then defined as:

\\( \mathrm{head} = \phi(Q) \phi(K)^\intercal V \\)

- Positional encodings drive the results
- LambdaNetworks vs Performers on ImageNet


## Complexity

The worst in terms of complexity is vanilla transformer head.
It needs for each batch item it requires \\( n^2 \\) time and space,
because it materializes attention matrix for each batch input.

The second place takes the Lambda Head.
For entire batch it requires \\( n^2 \\).
The savings come from positional embeddings having \\( n^2 \\) time and space size,
but being the same for entire batch.

The first places takes the Performer.
The Performer is time and space is linear both in batch size and sequence length \\( n \\).
Additional time speed up in performer may come from adoption of relu replacing the exponential in the kernel softmax approximation.

## Performance

Comparison of the Relu-Performer and Lambda Network is not available. So we have to compare only Lambda layer and self-attention.
While Lambda layer out-performs self-attention, it is by a small margin.
The Performer will likely be able to outperform Lambda layer, although it needs to be tested first.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="Lambda layer vs self-attention on ImageNet with a Resnet50 architecture"
        src="/images/lambda-layer-vs-self-attention.png">
    <figcaption class="figure-caption">
        Lambda layer vs self-attention on ImageNet with a Resnet50 architecture
        (<a href="https://openreview.net/forum?id=xTJEN-ggl1b">source</a>).
    </figcaption>
</figure>

Could we possibly get rid of the positional embeddings, if they consume so much?
No, they drive most of the performance at least in case of the image classification task.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="Lambda layer with and without positional embeddings on ImageNet"
        src="/images/lambda-layer-w-and-wo-positional-interactions.png">
    <figcaption class="figure-caption">
        Lambda layer with and without positional embeddings on ImageNet
        (<a href="https://openreview.net/forum?id=xTJEN-ggl1b">source</a>).
    </figcaption>
</figure>

