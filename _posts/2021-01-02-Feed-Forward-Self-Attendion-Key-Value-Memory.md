---
layout: post
title: Feed-Forward, Self-Attention & Key-Value
date: 2021-01-02
categories: ml
image: /images/transformer-feed-forward.png
video: NI7vFV_iOOA
description: Feed-forward (MLP) layer is similar to cross-attention as observed in SwiGLU and All-attention.
permalink: /:categories/:title
last_modified_at: 2022-04-24
redirect_from:
- /ml/Feed-Forward-Self-Attention-Key-Value-Memory
my_related_post_paths:
- _posts/2020-11-29-Lambda-Networks-Transform-Self-Attention.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2022-02-26-SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2021-02-07-submodularity-in-ranking-summarization-and-self-attention.md
---



{% include mathjax.html %}
{% include load_video.html %}


Have you forgotten about Transformer's feed-forward layer? [It eats 2/3 of the model params](https://arxiv.org/pdf/2012.14913v1.pdf)!
Feed-forward layer is sometimes also called MLP layer. 

[The last post on LambdaNetwork sketches self-attention as a differentiable query of a key-value store](/ml/Lambda-Networks-Transform-Self-Attention).
The [Transformer](/ml/transformers-self-attention-mechanism-simplified)'s feed-forward sublayer is similar to the  [cross-attention](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) attending to a separate sequence via key and value input.
So, it is a bit like differentiable key-value memory.

Can we gain more understanding of [Transformer model](/ml/transformers-self-attention-mechanism-simplified) operation by looking at the feed-forward layer?

## Where is Feed-Forward Layer?

Where is Feed-Forward layer within the architecture exactly?
Feed-forward layer camps within encoder and decoder layers as a sublayer just behind the self-attention sub-layer.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Transformer encoder layers. Feed-forward is a sub-layer after the self-attention."
        data-src="/images/feed-forward-sublayer-in-transformer.png"
        style="width: 300px"
    >
    <figcaption class="figure-caption">
        Transformer encoder layers. Feed-forward is a sub-layer after the self-attention (<a href="https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf">source</a>)
    </figcaption>
</figure>

## What is Feed-Forward Layer?
- It is a position-wise transformation that consists of linear transformation, ReLU, and another linear transformation.

- formula: \\( \mathrm{ffLayer} = \sum_i \mathrm{relu}(q_i k_i^\intercal + b_i) v_i + c\\)

- Don't forget the residual connections and their addition and normalization to outputs of both feed-forward and self-attention.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Transformer Feed-Forward Layer"
        data-src="/images/transformer-feed-forward.png"
        style="width: 400px"
>
    <figcaption class="figure-caption">
        Transformer Feed-Forward Layer 
    </figcaption>
</figure>



## Feed-Forward Layer vs Cross-Attention

Have you noticed that the feed-forward sublayer is akin to key-value memory of the self-attention except for non-linearity is ReLU and bias-terms \\( b, c \\)?

\\( \mathrm{keyValMemory} = \sum_i \mathrm{softmax}(q_i k_i^\intercal) v \\)

More specifically feed-forward layer is a bit like a [cross-attention](/ml/cross-attention-in-transformer-architecture) with a trainable embedding sequence.
[Augmenting Self-attention with Persistent Memory paper](https://arxiv.org/pdf/1907.01470.pdf) saw the similarity of feed-forward sublayer and self-attention and suggested an architecture simplification.
They restated the feed-forward layer, incorporated it into the self-attention sublayer, and named the new block "All-attention".
And they reportedly slightly outperformed the vanilla model on the next token prediction task.

![All-attention: feed-forward layer restated as self-attention](/images/all-attention-feed-forward-as-self-attention.png)

[Google's PaLM model](/ml/googles-pathways-language-model-and-chain-of-thought) authors adopted gated linear unit (GLU) based modification to their feed-forward layer, which is midly similar to cross-attention:

{% include shared_slides/swiglu-modified-feed-forward-layer.md %}


## Feed-Forward vs Softmax Linear Unit (SoLU)
- the definition is \\( x * \mathrm{softmax}(x) \\)
- SoLU uses Softmax instead of the ReLU
- SoLU reminds a gating mechanism similar to SwiGLU
- SoLU [learns more interpretable memories, the same metrics and speed (Layer norm not needed.)](https://transformer-circuits.pub/2022/solu/index.html)

But does the feed-forward sublayer really behave like key-value memory not only talk a talk?


## Feed-Forward Key-Value Memories - Empirical Study

In [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/pdf/2012.14913v1.pdf) authors show that feed-forward layer does walk the walk of a key-value store.

The paper studies activation of feed-forward keys for the last position of the input sequence.
The activated keys are  keys with top-n ReLU outputs for given feed-forward sublayer.
For most of the keys in the feed-forward sublayers the authors found one or more human-interpretable input text patterns for which the key in feed-forward was being activated.
Text patterns ranged from simple exact word matches (e.g. last word is "substitutes") to more complex topics (e.g. "one of", "part of", "among").
Authors also observed that the upper layers memorize more abstract patterns.

Unfortunately not all samples are provided in the pre-print.
Furthermore, they report they found more than one pattern per key.
Were those patterns referencing a single topic or disparate topics?
If single key was associated with multiple topics, can we still look at it as a memory cell?

Activated feed-forward values predicted model's next output tokens in higher layers only, but not in lower layers.
Typical example activated tens of memories which were then aggregated (non-zero coef mems).
The model output vector differed from all single memory predictions (single value vectors) 68% of the time.
Remaining 32% are perhaps stop words and a like.
The feed-forward residual connections predicted next output token increasingly in the higher layers.
Could be that the internal embedding space is changes between layers?
Is the model refining its prediction from layer to layer?

They additionally observed that top-1 predictions of sublayer residuals mostly not match feed-forward.
These sublayer-outputs seem to not agree but rather compose.
Does feed-forward dampen or "veto" residual vectors towards other candidates?
In 66% adding feed-forward to residuals changed prediction is to a semantically unrelated word.
Is this used by the model for predicted sequence re-arrangements?

## ROME method Feed-Forward Layers as Editable Memories
The [ROME paper](This) develops a technique for locating memories and associative rules in [GPT transformer](/ml/transformers-self-attention-mechanism-simplified) for specific facts ,e.g. Eiffel tower is in Paris.
Additionally, they introduce a technique for editing these memories without rest of the model.

## LambdaNet Positional Embeddings vs Feed-Forward Layer

[LambdaNet layer positional embeddings](/ml/Lambda-Networks-Transform-Self-Attention) are something between self-attention and feed-forward layer in transformer, but neither.
They are about querying pattern-values store.
The keys are constants like in feed-forward, but queries and values are derived from the input.
Whereas in the feed-forward the values are constants as well.


## Meet Other ML Enthusiasts One-on-One Online

Video-call each week an interesting person and break out of your remote isolation.
Network One-on-One Around Your Online Village with RandomMeets.

<a class="btn btn-info" style="text-decoration: none;" href="https://randommeets.com/invite/eyJncm91cF9pZCI6IjZhMzNkMTVjLTc0NjItNGFhMS1hNTc0LWM1NTUwMWQ4NWNkZiJ9.X76oug.2563ghpMTzbST9KPHerGeDqhXRY">
    Join Machine Learning @ RandomMeets
</a>
