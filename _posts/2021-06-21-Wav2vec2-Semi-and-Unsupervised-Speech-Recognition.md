---
layout: post
title: 'Wav2vec: Semi-supervised and Unsupervised Speech Recognition'
date: 2021-06-21
categories: ml
description: Word2vec for audio quantizes phonemes, transforms, GAN trains on text and audio from Facebook AI.
permalink: /:categories/:title
video: PHIKbgMJq4c
image: /images/wav2vec-thumb.png
redirect_from:
- /ml/PID-controller
last_modified_at: 2022-09-17
my_related_post_paths:
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2021-10-04-electra-4x-cheaper-bert-training.md
---



{% include mathjax.html %}
{% include load_video.html %}

Wav2vec is fascinating in that it combines several neural network architectures and methods:
CNN, [transformer](/ml/transformers-self-attention-mechanism-simplified),
quantization, and GAN training.
I bet you'll enjoy this guide through Wav2vec papers solving the problem of speech to text.


## There are many languages
- want to convert audio to text
- 7000 languages spoken today
  - 195 sovereign states
  - ~150 language groups
- lack labelled data
- humans learn without labels


## Wav2vec 2.0
- Paper [A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477.pdf) from Facebook AI 2020
- pretrain on ~800h unlabeled data and fine-tune ~100h labeled data
- SOTA in low-resource setting Libri-light
  - (all SOTA info is as of the paper discussed)
  - by a lot on WER clean test 100h labeled: others ~4 vs theirs ~2.5
  - WER = word-level, word-count normalized edit distance
- SOTA on high-resource noisy data (3.3 vs 3.4)
  - close to SOTA on clean data
- uses [quantization](#quantization) as inductive bias for [phonemes](#phoneme)

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Wav2vec 2.0 results on 100h-labels Libri-Light"
        data-src="/images/wav2vec-results.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Wav2vec 2.0 results on 100h-labels Libri-Light (<a href="https://arxiv.org/pdf/2006.11477.pdf">source</a>).
    </figcaption>
</figure>


## Phoneme
- a unit of sound in spoken languages approximately [100ms long](https://www.scitepress.org/Papers/2013/45035/45035.pdf)
- for example in IPA: /sɪn/ (sin) and /sɪŋ/ (sing)
- English ~40 phonemes


## Quantization

{% include  shared_slides/quantization.md %}


## Wav2vec Quantization works
- codewords = product of 2 codebooks of 320 gives 100k
- codewords dimension of 256 (128 for both sub-codebooks)
- there is a high co-occurence of certain codebook items and phoneme sounds

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



### Wav2vec 2.0 Architecture
- pre-trained unsupervised, and then fine-tuned on supervised speech transcription task
- raw audio [tokenized via splitting into 25ms pieces](/ml/Tokenization-in-Machine-Learning-Explained) fed into 7-layer convolution network
- output quantized into a fixed sized codebook
- contextualize [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) via 12-block [transformer](/ml/transformers-self-attention-mechanism-simplified)
- [original source here](https://github.com/pytorch/fairseq/tree/master/examples/wav2vec), [HuggingFace (pretraining not possible as of 2021-06)](https://huggingface.co/transformers/model_doc/wav2vec2.html#overview)

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


### Wav2vec 2.0 Training
- unsupervised pre-training:
  - mask spans of the latent embeddings
  - predict masked quantization via [contrastive learning on quantized targets](#wav2vec-20-vs-previous-version)
  - ablations showed quantization helps
- fine-tuning
  - add output layer to predict characters
  - uses [CTC loss](#connectionist-temporal-classification-ctc-loss)


### Connectionist Temporal Classification (CTC) Loss
- between a unsegmented time series and a target sequence
- CTCLoss sums probability of all possible alignments of input to target
- differentiable with respect to each input node
- [Original CTC paper (Graves 2016)](https://www.cs.toronto.edu/~graves/icml_2006.pdf), [pytorch docs](https://pytorch.org/docs/master/generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss)
  - network returns probabilities of phonemes and blanks for each position
  - **remove all blanks** and **repeated labels** from the possible sequences
  - for example \\( B(a − ab−) = B(−aa − −abb) = aab \\)
  - this maps many paths to one output sequence \\( \pi \in B^{-1}(l) \\)
  - probability of label \\( l \\) is sum of matching the sequences \\( \pi \in B \\)
  - \\( p(l  \| x) = \sum_{\pi \in B^{-1}(l)} p(\pi \| x) \\)
  - efficiently calculated with [dynamic programming (Forward–backward algorithm)](https://en.wikipedia.org/wiki/Forward%E2%80%93backward_algorithm)


### Wav2vec 2.0 vs vq-wav2vec
- jointly learn quantizations instead of separately in constrat to [vq-wav2vec](https://arxiv.org/pdf/1910.05453.pdf)
- contrastive loss for quantizations:
  - [transformer](/ml/transformers-self-attention-mechanism-simplified) output compared to the embeddings in the codebook
  - contractive distractors are other masked time steps
  - \\( - \log \frac{exp(sim(c_t, q_t) / \kappa }{ \sum_{q \in Q_t } \exp (sim(c_t, q) / \kappa) } \\)
- diversity loss for codebook:
  - encourage even use of the whole codebook
  - loss is entropy of average softmax for the batch over the codebook
- reduced [word error rate (WER)](https://en.wikipedia.org/wiki/Word_error_rate) ~33% compared to vq-wav2vec


## Wav2vec-U
- ["Unsupervised Speech Recognition"](https://arxiv.org/pdf/2105.11084.pdf)
- On Arxiv on 24 May 2021
- trains without any labeled data
- inspired by other adversarial approaches
- SOTA in unsupervised setting
- not competitive with current supervised models
  - perhaps with models from 2018


### Wav2vec-U Architecture
- segment representations k-means clustering and mean-pool clusters into single phoneme unit embedding
- Generator is single layer CNN: ~90k params, kernel size 4, 512 dimensions
- Generative adversarial (GAN) training involves only the CNN
- discriminator is also an CNN

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


### Wav2vec-U Training
- amazing! no-labels needed
- discriminator
  - fed phonemized natural text and generator output
  - tries to recognize which input is which
  - generator wins over-time
  - easier to generate correct transcription
  - compared to hallucinating incorrect transcription

## Discussions
- [Hackernews](https://news.ycombinator.com/item?id=27722333)


## Still not sure how [the transformer model](/ml/transformers-self-attention-mechanism-simplified) really works?
The [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) stormed the ML world including computer vision thanks to its generality and GPU parallizability on shorter sequences.
[Finally understand it over here](/ml/transformers-self-attention-mechanism-simplified), and if you still don't get it, ask me a question!