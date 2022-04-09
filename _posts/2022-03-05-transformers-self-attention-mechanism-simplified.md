---
title: "Transformer's Self-Attention Mechanism Simplified"
description: "Understand quickly successful architecture used in GPT, BERT, and other famous transformer models."
layout: post
image: /images/transformer-full-model.png
categories: ml
date: 2022-03-05
permalink: /:categories/:title
---

{% include mathjax.html %}

![BERT full model diagram](/images/transformer-full-model.png)

The prototypical example of the Transformer architecture is the Bidirectional Encoder Representations from Transformers (BERT) model. The BERT Transformer model was introduced in a [Attention Is All You Need paper](https://arxiv.org/abs/1706.03762).

While [self-attention](#self-attention-in-transformer) is the central part of the Transformer architecture, it is not the whole picture.
Transformer architecture is a composite of following parts:
- [Positional encodings inject input word-position information](#positional-embeddings)
- [Self-attention contextually encodes the input sequence information](#self-attention-in-transformer)
- [Feed forward layer which operates bit like a static key-value memory](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory). FF layer is similar to self-attention except it does not use softmax and one of the input sequences is a constant.
- [Cross-attention decodes output sequence](/ml/cross-attention-in-transformer-architecture) of different inputs and modalities.

## Self-Attention in Transformer
<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/self-attention-calculation-visualisation.png"
        alt="self-attention calculation visualization"/>
    <figcaption class="figure-caption">Output and input have the same sequence length and dimension. Weight each value by similarity of the corresponding query and key. For each sequence position output sum up the weighted values.</figcaption>
</figure>

Transformer's self-attention layer computes differentiable key-value search and summation on the input sequence.

- input \\( X \in \mathbf{R}^{L \times d} \\) is a sequence of embeddings of dimension \\( d \\) of length \\( L \\)
- output \\( Y \in \mathbf{R}^{L \times d} \\) has the same shape as input
- project \\( X \\) into 3 matrices of the same shape
  - query \\( X^Q := W^Q X \\),
  - key \\( X^K := W^K X \\)
  - value \\( X^V := W^V X \\)
- calculate "soft sequence-wise nearest neighbor search"
  - "search" all \\( L \times L \\) combinations of sequence elements of \\( X^K \\) and \\( X^Q \\)
  - for each sequence position \\( m \\): output more of \\( X^V_{o} \\) the more is \\( X^K_o \\) similar to \\( X^Q_{m} \\)
  - this is done by weighting the value with a softmax of a dot-product and summing the values
  - in pseudo-code: \\( Y = \mathrm{matmul}_L(\mathrm{softmax}_L(\mathrm{matmul_d}(X_q, X_k^\intercal)), X_v) \\)
  - in equation: \\( Y = \mathbf{softmax}(QK^\intercal)V \\)
- More details in [Attention Is All You Need paper](https://arxiv.org/abs/1706.03762) e.g.: dot-product is "scaled", residual connection, layer normalization

## Word Embeddings

Input text is split into character chunks called tokens.
Tokens are mostly words around 4 characters long with prepended whitespace, but can represent special characters.
Embeddings layers map tokens to vectors in other words to sequence of numbers.
Input and output embeddings layer share the same mapping.
  
### Multi-Head Attention
Instead of basic self-attention above, BERT implements special more complicated layer:
1. for each key, value, and query multiplies by additional projection weight matrix
2. then splits each resulting embedding into 8 equal sized vectors,
3. applies separate 1/8th dimensional self-attention mechanism to each of them,
4. concatenates the result.
 
Each separate self-attention in above is called self-attention head.
As a whole this layer is called multi-head attention.
Multi-head attention allows each head to focus on a subspace, with different meaning.
Experiments show that each head attends to tokens of different semantic or syntactic meaning.
Splitting vector representation into subspaces is related to [disentangled representation training](/ml/manipulate-item-attributes-via-disentangled-representation),
where we train model to give selected subspaces specific meaning.

<small>
Most heads don't [attend to the same sequence position](https://aclanthology.org/W19-4828.pdf),
probably because residual connection always adds current position embedding to the result.
Special tokens are used by some heads to "attend" to nothing.
</small>

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

### Self-Attention Computational Complexity
- complexity is quadratic in sequence length \\( O(L^2) \\)
- because we need to calculate \\( L \times L \\) attention matrix \\( \mathbf{softmax}(\frac{QK^\intercal}{\sqrt{d}}) \\)
- but context size is crucial for some tasks e.g. character-level models
- multiple speedup approaches already exits
- for example [Performer](/ml/Performers-FAVOR+-Faster-Transformer-Attention), [Expire-Span](/ml/expire-span-scaling-transformer-by-forgetting), [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) are architectures reducing transformer computational complexity.
  - In [Perceiver IO, cross-attention](/ml/cross-attention-in-transformer-architecture#cross-attention-in-perceiver-io) is used to reduce dimensionality and thus the complexity.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Attention Complexity"
        data-src="/images/expire-span-attention-complexity.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Attention Complexity (<a href="https://arxiv.org/pdf/2009.14794.pdf">source</a>).
    </figcaption>
</figure>

## Positional Embeddings

![positional embeddings in BERT architecture](/images/transformer-positional-embeddings.png)

In BERT, positional embeddings give first few tens of dimensions of the token embeddings meaning of relative positional closeness within the input sequence.
In [Perceiver IO](/ml/cross-attention-in-transformer-architecture#cross-attention-in-perceiver-io) positional embeddings are concatenated to the input embedding sequence instead.
In [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) the positional embeddings are learned feature of the RNN.


### Fourier Positional Encodings in BERT
- Positional embeddings are added to the word embeddings once before the first layer.
- Each position \\( t \\) within the sequence gets different embedding
  - if \\( t = 2i \\) is even then \\( P_{t, j} := \sin (p / 10^{\frac{8i}{d}})  \\)
  - if \\( t = 2i + 1 \\) is odd then \\( P_{t, j} := \cos (p / 10^{\frac{8i}{d}})  \\)
- This is similar to fourier expansion of Diracs delta
- dot product of any two positional encodings decays fast after first 2 nearby words
- average sentence has around 15 words, thus only first dimensions carry information
- the rest of the embeddings can thus function as word embeddings


## Training a Transformer
Transformers are usually pre-trained with self-supervised tasks like masked language modelling or next-token prediction on large datasets.
Pre-trained models are often very general and publicly distributed e.g. on HuggingFace.
Big transformer models are usually trained on multiple GPUs.
While there are various approaches to speedup transformer itself, there are also ways to improve its training.
For example [ELECTRA training scheme speeds up training](/ml/electra-4x-cheaper-bert-training) by using GAN-like setting using a loss over entire sequence.

Then fine-tuning training is used to specialize the model for a specific task on using a small labelled dataset.
For example model like BART are fine-tuned for summarization tasks.
Sometimes we fine-tune twice, as authors did with [BART model equipped with diminishing self-attention to increase summarization coverage (read my summary)](/ml/submodularity-in-ranking-summarization-and-self-attention).

Beware of possibility of the [double descent of test accuracy contrary to bias-variance trade-off hypothesis (read my summary)](/ml/double-descent-contrary-to-bias-variance-trade-off).


## Serving Transformer in Kubernetes Cluster in Cloud

While you can train and predict with small transformers on for example [Thinkpad P52 graphics card (see my review)](/electronics/Thinkpad-P52-vs-HP-Zbook-15-G5-vs-Dell-Precision-7530),
to run bigger models, or deploy your models to production, you will need to a bit of MLOps and DevOps, so read:
- [store your trained models e.g. using Quilt Data in S3 (read more here)](/ml/Quilt-data-versioning-review-how-to)
- [deploy to Kubernetes (read more here on Cortex, BentoML, and Helm)](/ml/BentoML-vs-Cortex.dev-ML-Serving-Showdown)


## Example Transformer Models

- [Wav2vec uses Transformer with quantization to predict phonemes](/ml/Wav2vec2-Semi-and-Unsupervised-Speech-Recognition)
- [Diminishing self-attention improves summarization coverage](/ml/submodularity-in-ranking-summarization-and-self-attention)
- [DeepMind's RETRO Transformer uses cross-attention to incorporate the database retrived sequences](/ml/DeepMinds-RETRO-Transformer-Model)
- [Expire-Span uses attention with forgetting](/ml/expire-span-scaling-transformer-by-forgetting)
- [SRU++ fuses of RNN and Self-attention](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN)
- [Performer uses random kernel features to speedup attention](/ml/Performers-FAVOR+-Faster-Transformer-Attention)
- [Lambda Networks introduce self-attention modification](/ml/Lamda-Networks-Transform-Self-Attention)
- For similarity task, you may also consider [lightweight approximation of word movers distance - WM embedding](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents)


## Transformer vs Word2vec Continuous Bag-of-Words

![Word2vec CBOW](/images/transformer-and-word2vec-cbow.png)

Word2vec was used in many state-of-the-art models between 2013-2015.
It was gradually replaced by more advanced variants like [FastText](/ml/FastText-Vector-Norms-And-OOV-Words), and [StarSpace a general-purpose embeddings](/ml/starspace-embedding), and more sophisticated models like LSTM and transformers. 
[Word2vec Continuous Bag-of-Words](https://arxiv.org/pdf/1301.3781.pdf) predicts word using its surrounding 10-word context by:
1. summing the input embeddings corresponding to the input context words
2. finding maximum a dot-product with all output embeddings
 
Note average sentence length is about 15 words.
Word2vec uses 2 sets of embeddings: input and output (context) embeddings.
Word2vec CBOW (w2v CBOW) model is similar to an extremely simplified a single layer transformer.

If we use:
- a single self-attention (remove the feed forward layer and layer normalization)
- single attention head
- [fourier positional encodings \\( p_j \\)](#fourier-positional-encodings-in-bert) 
  - that behave as if concatenated: for all embeddings and positional encodings \\( p_j^\intercal e_w \approx 0 \\)
  - decay fast after relative distance of 4: \\( p_j^\intercal p_i \approx \delta_{ |i-j| <= 4 } \\)
- identity key, query linear transformations  \\( W_K = W_Q = 1 \\).
- masked word vector has the same dot-product with all embeddings \\( e_{mask}^\intercal e_w \approx C \\)

Then we approximately:
\\( (e_w + p_w)^\intercal (e_{mask} + p_{mask}) \approx \\)
\\( e_w^\intercal e_{mask} + p_w^\intercal p_{mask} = \\)
\\(  C + \delta_{|i-j| <= 4} \\) 

And if we define output embeddings via the value projection matrix multiplied with embeddings:
\\( W_V E \\)

Then the Transformer output for a masked word is close to summation of the surrounding word vectors like in CBOW Word2vec.
The positional embeddings probably do not behave as concatenated.
The term above would contain relative and absolute positional terms, which are not present in Word2vec.
So the transformer result would still be more expressive.

But if we would additionally not use positional encodings, and use sliding context window of size matching Word2vec's context size, then the results would be even closer to the Word2vec.

## Transformer vs FastText

Transformer architecture cannot really be compared to [FastText](/ml/FastText-Vector-Norms-And-OOV-Words) well in other things than performance.
That is because apart from whole words [FastText trains also on sub-words or n-grams](/ml/FastText-Vector-Norms-And-OOV-Words),
while Transformer always trains only on the word tokens.
