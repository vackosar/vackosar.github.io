---
layout: post
title: "Feed-Forward, Self-Attention & Key-Value"
date: 2021-01-02
categories: ml
image: /images/transformer-feed-forward.png
description: Transformer model queries values of keys in the self-attention and in the feed-forward memories.
permalink: /:categories/:title
---
[comment]: <> (image: /images/lambda-layer-thumb.png)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<iframe width="560" height="315" src="https://www.youtube.com/embed/NI7vFV_iOOA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Have you forgotten about Transformer's feed-forward layer? [It eats 2/3 of the model params](https://arxiv.org/pdf/2012.14913v1.pdf)!

[The last post on LambdaNetwork sketches self-attention as a differentiable query of a key-value store](https://vaclavkosar.com/ml/Lamda-Networks-Transform-Self-Attention).
The Transformer's feed-forward sublayer is similar to the self-attention except values and keys are independent of the input.
It is like differentiable key-value memory!

Can we gain more understanding of Transformer model operation by looking at the FF?

## Where and what is Feed-Forward?

Where is Feed-Forward layer within the architecture exactly?
FF camps within encoder and decoder layers as a sublayer just behind the self-attention sub-layer.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="Transformer encoder layers. Feed-forward is a sub-layer after the self-attention."
        src="/images/transformer-layers-encoder.jpg"
    >
    <figcaption class="figure-caption">
        Transformer encoder layers. Feed-forward is a sub-layer after the self-attention (<a href="https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf">source</a>)
    </figcaption>
</figure>

And what is FF layer precisely?
It is a position-wise transformation that consists of linear transformation, ReLU, and another linear transformation.

\\( \mathrm{ffLayer} = \sum_i \mathrm{relu}(q_i k_i^\intercal + b_i) v_i + c\\)


<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="Transformer Feed-Forward Layer"
        src="/images/transformer-feed-forward.png">
    <figcaption class="figure-caption">
        Transformer Feed-Forward Layer 
    </figcaption>
</figure>

Don't forget the residual connections and their addition and normalization to outputs of both FF and self-attention.


## Key-Value Memory vs Feed-Forward Layer

Have you noticed that the FF sublayer is akin to key-value memory except for non-linearity is ReLU and bias-terms \\( b, c \\)?

\\( \mathrm{keyValMemory} = \sum_i \mathrm{softmax}(q_i k_i^\intercal) v \\)

[Augmenting Self-attention with Persistent Memory paper](https://arxiv.org/pdf/1907.01470.pdf) saw the similarity of feed-forward sublayer and self-attention and suggested an architecture simplification.
They restated the FF as key-value memory and incorporated it into the self-attention sublayer. And they reportedly slightly outperformed the vanilla model on the next token prediction task.

But does the feed-forward sublayer really behave like key-value memory not only talk a talk?


## The Memory of The Feed-Forward

In [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/pdf/2012.14913v1.pdf) authors show that FF does walk the walk of a key-value store.

The paper studies activation of FF keys for the last position of the input sequence.
The activated keys are  keys with top-n ReLU outputs for given FF sublayer.
For most of the keys in the feed-forward sublayers the authors found one or more human-interpretable input text patterns for which the key in FF was being activated.
Text patterns ranged from simple exact word matches (e.g. last word is "substitutes") to more complex topics (e.g. "one of", "part of", "among").
Authors also observed that the upper layers memorize more abstract patterns.

Unfortunately not all samples are provided in the pre-print.
Furthermore, they report they found more than one pattern per key.
Where those patterns on a single topic or disparate topics?
If single key was associated with multiple topics, can we still look at it as a memory cell?

Activated FF-values predicted model's next output tokens in higher layers only, but not in lower layers.
Typical example activated tens of memories which were then aggregated (non-zero coef mems).
The model output vector differed from all single memory predictions (single value vectors) 68% of the time.
Remaining 32% are perhaps stop words and a like.
The FF-residual connections predicted next output token increasingly in the higher layers.
Could be that the internal embedding space is changes between layers?
Is the model refining its prediction from layer to layer?

They additionally observed that top-1 predictions of sublayer residuals mostly not match FF.
These sublayer-outputs seem to not agree but rather compose.
Does FF dampen or "veto" residual vectors towards other candidates?
In 66% adding FF to residuals changed prediction is to a semantically unrelated word.
Is this used by the model for predicted sequence re-arrangements?

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
