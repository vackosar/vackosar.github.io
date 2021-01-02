---
layout: post
title: "Transformer Queries a Key-Value Memory After the Attention"
date: 2021-01-02
categories: ml
description: Transformer model looks up not only in the input sequence via an attention, but also in a memory of feed-forward layer.
permalink: /:categories/:title
---
[comment]: <> (image: /images/lambda-layer-thumb.png)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

[comment]: <> (<iframe width="560" height="315" src="https://www.youtube.com/embed/SYxm3R5VAsw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>)

Have you forgotten about Transformer's feed-forward layer? It eats 2/3 of the model params!

In the post on [LambdaNet I mentioned that self-attention is differentiable querying of an key-value store](https://vaclavkosar.com/ml/Lamda-Networks-Transform-Self-Attention).
LambdaNet layer positional embeddings are more like querying pattern-values store. The keys are static, but queries and values are derived from the input.
The Transformer's feed-forward layer is similar to the LambaNet's positional embeddings except values are independent of the input as well!
FF layer is like self-attention with static keys and values.
It is like differentiable key-value memory!

[A 2019 Facebook paper Augmenting Self-attention with Persistent Memory](https://arxiv.org/pdf/1907.01470.pdf) noticed this and suggested an architecture simplification.
They squashed feed-forward layer into the key-value memory pressed it into the attention layer and even slightly outperformed the vanilla model on next token prediction.
Note that FF are quite like key-value stores except for non-linearity is RELU and bias-terms \\( b, c \\) are non-zero.

\\( \mathrm{keyValMemory} = \sum_i \mathrm{softmax}(q k^\intercal) v \\)

\\( \mathrm{ffLayer} = \sum_i \mathrm{relu}(q k_i^\intercal + b_i) v_i + c\\)


But does the feed-forward layer really behave like key-value memory not only talk a talk?
In [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/pdf/2012.14913v1.pdf)
authors show that FF does walk the walk of a key-value store

The paper explains that:
- input-key matches correlate with human-interpretable input patterns
    - Text prefixes in which last token \\( x_j \\) representation has big projection with a key.
    - But Figure 3 shows that the last token is the most impacting which is in line.
    - The data is not part of the pre-print :(
- Upper layers memorize more abstract patterns
- Key-match examples next tokens correlate with max-value probability only in the higher layers and not lower layers
- Typical example triggers tens of memories which are then aggregated (non-zero coef mems)
- Output is not from single memory 68% of the time. Remaining 32% could be stop words and a like.
- Probability of output token based on residual outputs increases with layer count. Could be that the internal embeddings are different?
- Model may be refining from layer to layer.
    - residuals and ff mostly compose and not agree
    - ff seems to after dampen parts of the rediual towards other candidate
    - in 66% the changed prediction is to semantically unrelated word - perhaps sequence shift?


## Meet Other ML Enthusiasts One-on-One Online

Video-call each week an interesting person and break out of your remote isolation.
Network One-on-One Around Your Online Village with RandomMeets.

<a class="btn btn-info" style="text-decoration: none;" href="https://randommeets.com/invite/eyJncm91cF9pZCI6IjZhMzNkMTVjLTc0NjItNGFhMS1hNTc0LWM1NTUwMWQ4NWNkZiJ9.X76oug.2563ghpMTzbST9KPHerGeDqhXRY">
    Join Machine Learning @ RandomMeets
</a>
