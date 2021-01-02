---
layout: post
title: "Transformer Queries a Key-Value Memory After the Attention"
date: 2021-01-02
categories: ml
description: Transformer model looks up not only in the input sequence via an self-attention, but also in a static memory via a feed-forward layer.
permalink: /:categories/:title
---
[comment]: <> (image: /images/lambda-layer-thumb.png)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

[comment]: <> (<iframe width="560" height="315" src="https://www.youtube.com/embed/SYxm3R5VAsw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>)

Have you forgotten about Transformer's feed-forward layer? It eats 2/3 of the model params!

In the post on LambdaNet, [I described self-attention as a differentiable query of a key-value store](https://vaclavkosar.com/ml/Lamda-Networks-Transform-Self-Attention).
The Transformer's feed-forward layer is similar to the LambaNet's positional embeddings except values are independent of the input as well!
FF layer is like self-attention with static keys and values.
It is like differentiable key-value memory!

## Feed-Forward Layer vs Key-Value Memory
[A 2019 Facebook paper Augmenting Self-attention with Persistent Memory](https://arxiv.org/pdf/1907.01470.pdf) noticed this and suggested an architecture simplification.
They squashed feed-forward layer into the key-value memory pressed it into the attention layer and even slightly outperformed the vanilla model on next token prediction.
Note that FF are quite like key-value stores except for non-linearity is RELU and bias-terms \\( b, c \\) are non-zero.

\\( \mathrm{keyValMemory} = \sum_i \mathrm{softmax}(q_i k_i^\intercal) v \\)

\\( \mathrm{ffLayer} = \sum_i \mathrm{relu}(q k_i^\intercal + b_i) v_i + c\\)

But does the feed-forward layer really behave like key-value memory not only talk a talk?
In [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/pdf/2012.14913v1.pdf)
authors show that FF does walk the walk of a key-value store

## Feed-Forward Layer Memories

For most of the keys in the feed-forward layers the author were able to find one or more human-interpretable input text patterns for which the key was being activated.
Text patterns ranged from simple exact word matches (e.g. last word is "substitutes") to more complex topics (e.g. "one of", "part of", "among").
The activation was studied for the "channel" of the last provided token of the input sequence.
Thanks to self-attention the other tokens influenced the last vector via self-attention providing context.
That is also why the last token had the biggest impact on the memory change in the first layers, but not the later once.
Authors also observed that the upper layers memorize more abstract patterns.
Unfortunately not all samples are provided in the pre-print. :(

Individual activated values predicted next tokens in higher layers only, but not in lower layers.
Typical example activated tens of memories which are then aggregated (non-zero coef mems).
The model output vector differed from all single memory predictions (single value vectors) 68% of the time.
Remaining 32% are perhaps stop words and a like.

Probability of the next token based on residual outputs increased in higher layers.
Could be that the internal embedding space is different?
Is the model refining its prediction from layer to layer?
- Residuals and FF top-1 predictions mostly do not match. Their output seem to rather compose and not agree.
- FF seems to after dampen or "veto" residual vector towards other candidates.
- In 66% adding FF to residuals changed prediction is to a semantically unrelated word. Is this for sequence re-arrangement?

## LambdaNet Positional Embeddings vs Transformer FF

LambdaNet layer positional embeddings are something between self-attention and FF, but neither.
They are about querying pattern-values store.
The keys are constants like in FF, but queries and values are derived from the input.
Whereas in the FF the values are constants as well.


## Meet Other ML Enthusiasts One-on-One Online

Video-call each week an interesting person and break out of your remote isolation.
Network One-on-One Around Your Online Village with RandomMeets.

<a class="btn btn-info" style="text-decoration: none;" href="https://randommeets.com/invite/eyJncm91cF9pZCI6IjZhMzNkMTVjLTc0NjItNGFhMS1hNTc0LWM1NTUwMWQ4NWNkZiJ9.X76oug.2563ghpMTzbST9KPHerGeDqhXRY">
    Join Machine Learning @ RandomMeets
</a>
