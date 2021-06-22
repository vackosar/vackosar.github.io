---
layout: post
title: "Wav2vec: Semi and Unsupervised Speech Recognition"
date: 2021-06-21
categories: ml
description: Quantize phonemes from audio, transform, GAN the text.
permalink: /:categories/:title
video: PHIKbgMJq4c
image: /images/wav2vec-thumb.png
redirect_from:
- /ml/PID-controller
---

{% include mathjax.html %}
{% include load_video.html %}

# There are many languages
- want to convert audio to text
- 7000 languages spoken today
  - 195 sovereign states
  - ~150 language groups
- lack labelled data
- humans learn without labels


# Wav2vec 2.0
- [A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477.pdf)
- Facebook AI
- On Arxiv 22 Oct 2020
- pretrain on ~800h unlabeled data
- fine-tune ~100h labeled data
- SoTa in low-resource setting Libri-light
  - by a lot on WER clean test 100h labeled: others ~4 vs theirs ~2.5
  - WER = word-level, word-count normalized edit distance
- SoTa on high-resource noisy data (3.3 vs 3.4)
  - close to SoTa on clean data
- uses [quantization](#quantization) as inductive bias for [phonemes](#phoneme)


# Phoneme
- a unit of sound in spoken languages
- for example in IPA: /sɪn/ (sin) and /sɪŋ/ (sing)
- English ~40 phonemes


# Quantization
- replaces with vector from a finite set
- the set of vectors is "codebook"
- forward pass selects single quantization vector
- backward pass uses Gumbal softmax over the codebook
- product quantization:
  - concatenation of several quantizations
  - then linear transformation

# Wav2vec Quantization works
- codewords = product of 2 codebooks of 320 gives 100k
- codewords dimension of 256 (128 for both sub-codebooks)

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Co-occurrence between phonemes on y-axis and quantizations on x-axis"
        data-src="/images/wav2vec-phonemes-quantization-co-occurence.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Co-occurrence between phonemes on y-axis and quantizations on x-axis (<a href="https://arxiv.org/pdf/2006.11477.pdf">source</a>).
        Discrete representation is coded in presence of one phoneme most of the time.
    </figcaption>
</figure>



## Wav2vec 2.0 Architecture
<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Wav2vec-U architecture: GAN CNN phonemes segment representations"
        data-src="/images/wav2vec-quantization.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Wav2vec-U architecture (<a href="https://arxiv.org/pdf/2105.11084.pdf">source</a>)
    </figcaption>
</figure>


## Wav2vec 2.0 Implementation
- 7-layer convolution to raw audio
- mask spans of the latents
- contextualize via 12-block transformer
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
  - efficiently calculated with dynamic programming


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
- not competitive with current supervised models
  - perhaps with models from 2018


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
  - Generative adversarial (GAN) training involves only the CNN
- discriminator is also an CNN