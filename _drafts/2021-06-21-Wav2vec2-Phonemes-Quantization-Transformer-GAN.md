---
layout: post
title: "Wav2vec: Phonemes, Quantization, Transformer, GAN"
date: 2021-05-21
categories: ml
video: x6sxKHrPA2A
image: /images/pid-controller.webp
description: Proportional–integral–derivative controller calculates feedback to reduce the error in the next step.
permalink: /:categories/:title
redirect_from:
- /ml/PID-controller
---

{% include load_video.html %}
{% include mathjax.html %}

# There are many languages
- 7000 languages spoken today
- 195 sovereign states
- ~150 language groups
- lack labelled data
- humans learn without labels
- traditionally Hidden Markov Models

# Wav2vec 2.0
- [A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477.pdf)
- Facebook AI
- 22 Oct 2020
- Dataset Librispeech without labels
- ~800h unlabeled data 
- ~100h labeled data  
- SoTa in low-resource setting Libri-light

# Wav2vec 2.0 vs previous version
- learn quantizations together
- reduce WER ~33%

# Wav2vec 2.0 Architecture
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

# Wav2vec 2.0 Implementation
- mask the speech input
- contextualize via transformer  
- transformer output of the masked predicts its quantization vector
- contrastive learning used
- jointly learn quantizations
- diversity loss

# Wav2vec Results
  
# 
- wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data
- follow up to Wav2Vec1 https://arxiv.org/abs/1904.05862
- intro
	- raw audio
	- multi-layer convolutional neural network
	- masks spans of the resulting latent speech representations
	- Transformer network to build contextualized representations
	-  trained via a contrastive task to predict masked quantized latent
	-  learn discrete speech units via a gumbel softmax
	-  jointly learning discrete speech units with contextualized representations
	- more effective than non-quantized targets
	- fine-tuned on labeled data
![[Pasted image 20210621080353.png]]
      
## Connectionist Temporal Classification Loss
What is Connectionist Temporal Classification (CTC)?
- Calculates loss between a continuous (unsegmented) time series and a target sequence.
- CTCLoss sums over the probability of possible alignments of input to target, producing a loss value which is differentiable with respect to each input node. https://pytorch.org/docs/master/generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss
- Original Paper Graves https://www.cs.toronto.edu/~graves/icml_2006.pdf
	- network predicts phonemes, blank (null prediction / silence)
	- We do this by simply **removing all blanks** and **repeated labels** from the paths (e.g. B(a − ab−) = B(−aa − −abb) = aab). Intuitively, this corresponds to outputting a new label when the network switches from predicting no label to predicting a label, or from predicting one label to another.
	- We use B to define condiitonal probabilty of given labelling l as the sum of the probabilities of all the paths corresponding to it:
	- p(l|x) = \sum_{\pi \in B^{-1}(l)} p(\pi|x)
	
## Hugging Face model without quantization
- https://huggingface.co/transformers/model_doc/wav2vec2.html#overview
- class Wav2Vec2ForCTC
	- class Wav2Vec2Model
		- feature_extractor
			- conv layers applied to the audio input
		- feature_projection - projects conv_dim into hidden_dim
		- encoder: Wav2Vec2Encoder
			- positional embeddings, layer norm, dropout
			- attention layers Wav2Vec2EncoderLayer
			- no-loss is implemeneted here
		- no-loss is implemeneted here
	- linear lm_head maps  to vocabulary
	- ctc_loss for fine tuning

## Original Source Code
https://github.com/pytorch/fairseq/tree/master/examples/wav2vec
