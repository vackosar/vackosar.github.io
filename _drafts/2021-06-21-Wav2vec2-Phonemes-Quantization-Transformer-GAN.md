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
- 22 Oct 2020
- Dataset Librispeech without labels
- pretrain on ~800h unlabeled data
- fine-tune ~100h labeled data
- SoTa in low-resource setting Libri-light


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
- fine-tuning uses [CTC loss](#connectionist-temporal-classification-ctc-loss)
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

## Wav2vec Results - REMOVE?
- wav2vec 2.0 is SoTa on 100 hour subset of Librispeech
- fine-tuned on labeled data

	
