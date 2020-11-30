---
layout: post
title: "Lambda Networks Transform Self-Attention"
date: 2020-11-29
categories: ml
description: Are they similar to self-attention in Transformer? Are their positional embeddings needed? LambdaResNet beats EfficientNet but does it loose to Performer?
image: /images/lambda-layer-thumb.png
permalink: /:categories/:title
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

[//]: # <iframe width="560" height="315" src="https://www.youtube.com/embed/xpys_xqB6qY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<img
    class="figure-img img-fluid rounded"
    style="width: 90%; max-width: 400px"
    alt="The Performer FAVOR+ attention on the right has linear complexity. The Transformer attention on the left has square complexity."
    src="/images/lambda-layer-thumb.png">


[Lambda Network](https://openreview.net/forum?id=xTJEN-ggl1b) head achieved SoTA, when sewed on decapitated Resnet50, outperforming EfficientNet and vanilla Transformer self-attention heads.
LambdaResNet also achieves ~4.5x speedup over EfficientNet at same accuracy.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="LambdaResNet also achieves ~4.5x speedup over EfficientNet at same performance"
        src="/images/lambda-layer-faster-than-efficientNet.png">
    <figcaption class="figure-caption">
        LambdaResNet also achieves ~4.5x speedup over EfficientNet at same performance
        (<a href="https://openreview.net/forum?id=xTJEN-ggl1b">source</a>).
    </figcaption>
</figure>


It however suffers from time-space complexity of sequence size squared and [Relu-Performer](/ml/Performers-FAVOR+-Faster-Transformer-Attention) could overtake it future.

The majority of model's performance comes from translation-invariant positional embeddings.
The positional embeddings are used similarly to a key matrix in a self-attention, but without any softmax function.
The embeddings are trained, but don't depend on the inputs (static).



## How similar are Lambda Interactions to Self-Attention?

Are there any similarities between Lambda Networks Interactions and Transformer or Performer attention?
Your thirst for knowledge will be satisfied here, friend!

In following \\( X \\) will denote input sequence of dimension \\( n \times d \\), where \\( d \\) is the token embedding dimension and \\( n \\) is the sequence length.
The interaction and attention context is the entire input sequence \\( X \\) for simplicity.
But for experiments with images the authors needed to limit the attention to image patches.


### Lambda Networks Interaction

Given \\( Q_l =  Q_{l, \cdot} \\),

\\( Q = (W_Q X) \in \mathbb{R}^{n \times k} \\),

\\( K =  (W_K X) \in \mathbb{R}^{n \times k} \\),

and \\( V =  (W_V X) \in \mathbb{R}^{n \times d} \\).

Positional embeddings are denoted by \\( E \in \mathbf{R}^{n \times n \times k} \\).
For each two positions in the input sequence there is an embedding vector.
Translational invariance \\( E_{i, j} = E_{t(i), t(j)}\\) is enforced by storing the embeddings in translation-invariant (relative) format.

Softmax applied along the dimension \\( n \\) is denoted by \\( \sigma \\).
The softmax serves here to strongly prefer select few of the value vectors indexed by \\( n \\).
However the selection factor (the logit) here is not the query-key match (dot product).
But rather to the key vector itself.
That may be the reason, why presence of \\( \sigma(K) \\) does not provide much performance gain (See the performance section).

In the paper the lambda layer is defined in a very unfamiliar form.
The left side of the equation below serves as a reference to the original paper.
On the left you can see a linear function \\( \lambda \\) parametrized by \\( l \\) projecting a query vector.
The resulting vector is transposed, such that the right side reminds you an self-attention vector.

\\( (\lambda_l Q_l)^\intercal = Q_l \odot_k (\sigma(K) + E_l )^{\intercal} \odot_n V \\)

The matrix multiplication subscript in above declares along which dimension it operates.
We omit the index \\( l\\) we obtain a format akin to self-attention.

\\( \mathrm{lambdaLayer} = Q (\sigma(K) + E)^\intercal V \\).

Note that the paper also mentions additional dimension called "intra-dimension" \\( u \\), which is set to 1 as it is not important.

### Transformer Self-Attention

Normalized softmax along dimension \\( n \\) is denoted by \\( \sigma \\).
Transformer positional encoding is denoted by \\( P \in \mathbf{R}^{n \times d} \\).
The positional embeddings are learned e.g. in case of BERT model.

Given
\\( Q = W_Q (X + P) \in \mathbb{R}^{n \times d}\\),

\\( K = W_K (X + P) \in \mathbb{R}^{n \times d}\\),

and \\( V = W_V (X + P) \in \mathbb{R}^{n \times d}\\).

Self-attention is defined as:

\\( \mathrm{selfAttention} = \sigma(QK^\intercal) V \\)


#### Performer Self-Attention Approximation

Kernel function approximating softmax via a feature function \\( \phi \in \mathbb{R}^{n \times d} \rightarrow \mathbb{R}^{k \times d} \\),
which maps to the smaller dimension \\( k \\).

The [Peformer](http://localhost:4000/ml/Performers-FAVOR+-Faster-Transformer-Attention) self-attention approximation is defined as:

\\( \mathrm{performerAttention} = \phi(Q) \phi(K)^\intercal V \\)


## How Is Lambda Doing in Space and Time Complexity?

The worst in terms of complexity is vanilla transformer self-attention.
For each batch item it requires \\( n^2 \\) time and space,
because it materializes attention matrix for each batch input.

The second place takes the Lambda Layer.
For entire batch it requires only \\( n^2 \\) time and space.
The savings come from positional embeddings having \\( n^2 \\) time and space size,
but being the same for entire batch.

The first places takes the Performer.
The Performer's time and space complexity is linear in both batch size and sequence length \\( n \\).
Additional time speed up in Performer comes from replacing the exponential with Relu in the kernel softmax approximation.


## How Lambda Layer Performs Compared to Self-Attention and Performer?

The paper compares Lambda layer to Transformer self-attention.
While Lambda layer out-performs self-attention, it does so by only a small margin.
For experimental specifics, please see the paper.
Note that in the experiment the lambda layer is not applied to the entire picture,
but rather to a small neighborhood of each pixel due to time and space complexity.

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

Comparison of the Relu-Performer and Lambda Network is not available as of 2020-11-30.
I think [Relu-Peformer](http://localhost:4000/ml/Performers-FAVOR+-Faster-Transformer-Attention) will likely outperform Lambda layer, although it needs to be tested first.


## Are Lambda's Positional Embeddings Required?

Could we possibly get rid of the positional embeddings, if they consume so much?
No, they drive most of the performance. That is at least in case of the image classification task.

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

If you remove the "content" part \\( \sigma(K) \\), that does not contribute much accuracy,
the lambda layer becomes: \\( Q E^\intercal V \\).

