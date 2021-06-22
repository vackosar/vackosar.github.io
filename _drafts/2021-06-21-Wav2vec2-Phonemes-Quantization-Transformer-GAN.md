---
layout: post
title: "Wav2vec: Phonemes, Quantization, Transformer, GAN"
date: 2021-06-21
categories: ml
description: Unsupervised speech
permalink: /:categories/:title
redirect_from:
- /ml/PID-controller
---

{% include mathjax.html %}

# There are many languages
- 7000 languages spoken today
- 195 sovereign states
- ~150 language groups
- lack labelled data
- humans learn without labels
- traditionally Hidden Markov Models

# Phoneme
- a unit of sound in spoken languages
- English ~40 phonemes
- for example in IPA: /sɪn/ (sin) and /sɪŋ/ (sing)

# Quantization
- replaces with vector from a finite set
- the set of vectors is "codebook"
- forward pass selects single quantization vector
- backward pass uses Gumbal softmax over the codebook
- product quantization:
	- concatenation of several quantizations
  	- then linear transformation


# Wav2vec 2.0
- [A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477.pdf)
- Facebook AI
- On Arxiv 22 Oct 2020
- Dataset Librispeech without labels
- pretrain on ~800h unlabeled data
- fine-tune ~100h labeled data
- SoTa in low-resource setting Libri-light
  - by a lot on WER clean test 100h labeled: others ~4 vs theirs ~2.5
- SoTa on large-resource noisy data (3.3 vs 3.4)
  - close to SoTa on clean data
- codewords = product of 2 codebooks of 320 gives 100k
- inner dimension of 256 (128 for both sub-codebooks)


## Wav2vec 2.0 Architecture
<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Wav2vec 2.0 architecture"
        data-src="/images/wav2vec-quantization.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Wav2vec 2.0 architecture (<a href="https://arxiv.org/pdf/2006.11477.pdf">source</a>)
    </figcaption>
</figure>

## Wav2vec 2.0 Implementation
- multi-layer convolve to raw audio
- mask spans of the latents
- contextualize via transformer  
- transformed token predicts quantized input
- [contrastive learning on quantized targets](#wav2vec-20-vs-previous-version)
- ablations showed quantization helps
- unsupervised, and then fine-tuned on supervised
- fine-tuning
  - add output layer to predict characters
  - uses [CTC loss](#connectionist-temporal-classification-ctc-loss)
- [original source](https://github.com/pytorch/fairseq/tree/master/examples/wav2vec),
- [HuggingFace (pretraining not possible as of 2021-06)](https://huggingface.co/transformers/model_doc/wav2vec2.html#overview)

## Connectionist Temporal Classification (CTC) Loss
- between a unsegmented time series and a target sequence
- CTCLoss sums probability of all possible alignments of input to target
- differentiable with respect to each input node
- [pytorch docs](https://pytorch.org/docs/master/generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss)
- [Original CTC paper (Graves 2016)](https://www.cs.toronto.edu/~graves/icml_2006.pdf)
  - network returns probabilities of phonemes and blanks for each position
  - **remove all blanks** and **repeated labels** from the possible sequences
  - for example \\( B(a − ab−) = B(−aa − −abb) = aab \\)
  - this maps many paths to one output sequence \\( \pi \in B^{-1}(l) \\)
  - probability of label \\( l \\) is sum of matching the sequences \\( \pi \in B \\)
  - \\( p(l  \| x) = \sum_{\pi \in B^{-1}(l)} p(\pi \| x) \\)

## Wav2vec 2.0 vs previous version
- previous version vq-wav2vec
- jointly learn quantizations instead of separately
- contrastive loss:
  - from transformer output to the codebook
  - uses similarity
  - distractors are other masked time steps
  - \\( - \log \frac{exp(sim(c_t, q_t) / \kappa }{ \sum_{q \in Q_t } \exp (sim(c_t, q) / \kappa) } \\)
- diversity loss:
  - encourage even use of the codebook
  - entropy of average softmax for the batch over the codebook
- reduced WER ~33% compared to vq-wav2vec


# Wav2vec-U
- [Unsupervised Speech Recognition](https://arxiv.org/pdf/2105.11084.pdf)
- On Arxiv on 24 May 2021
- trains without any labeled data
- inspired by other adversarial approaches
- SoTa in unsupervised setting

## Wav2vec-U Architecture

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Wav2vec-U architecture: GAN CNN phonemes segment representations"
        data-src="/images/wav2vec-gan.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Wav2vec-U architecture (<a href="https://arxiv.org/pdf/2105.11084.pdf">source</a>)
    </figcaption>
</figure>

- segment representations mean pooled clusters
- Generator is single layer CNN
  - ~90k params
  - kernel size 4
  - 512 dimension
  - GAN training involves only the CNN
- Distriminator is also an CNN

