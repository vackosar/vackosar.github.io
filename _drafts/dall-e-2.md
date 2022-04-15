---
title: "OpenAI DALL-E 2 vs DALL-E 1, and CLIP"
description: "TODO"
layout: post
categories: ml
date: 2022-04-13
permalink: /:categories/:title
---

{% include mathjax.html %}

DALL-E 1 uses quantization and next token predition while DALL-E 2 uses CLIP model and diffusion.


## OpenAI's CLIP Model
- [OpenAI blog](https://openai.com/blog/clip/)
- trained on a 400M images with a caption text from the internet
- robust to distribution shift
- text and image have separate [transformer](/ml/transformers-self-attention-mechanism-simplified) encoders
- trained with contrastive learning making representations maximize cosine similarity
- trained on 256 GPUs for 2 weeks
- resulting image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)

### OpenAI's CLIP Model Architecture
- visual encoder is [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf) image [transformer](/ml/transformers-self-attention-mechanism-simplified)
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
- the fix length text embedding is extracted from \[EOS\] token position


## DALL-E 1

OpenAI DALL-E 1 introduced in [paper](https://arxiv.org/pdf/2102.12092.pdf) and [code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13).
DALL-E 1 generates images via variational autoencoder inspired by VA-VAE-2 and from textual input autoregressive on a discrete latent space.

### DALL-E 1 Training:
1. train encoder and decoder image of image into 32x32 grid of 8k possible code word tokens
2. concatenate encoded text tokens to image tokens and train to predict next image token
3. discard the image encoder

### DALL-E 1 Prediction:
1. encode input text
2. predict following image tokens
3. decode the image tokens using dVAE
4. select the best results using [CLIP model](#clip) ranker

	
### Learning visual codebook
- similar to [VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf)
- train discrete variational autoencoder (dVAE)
	- train image encoder to a latent 32x32 grid of 8k code words
	- train a decoder back to image
- VAE model the image distribution via lower bound on maximum likelihood
    - encodes to a simple latent space of gaussian distributions
    - re-parametrization trick \\( z = \sigma * r + \mu \\)
    - how dVAE does this?
- tune the decoder with a weight on the KL divergence term
- decoder is conv2d, decoder block (4x relu + conv), upsample (tile bigger array), repeat
- start with uniform prior over the codebook
- maximize evidence lower bound (ELB)

### Learning the prior
- train transformer to predict next token of the concatenated text and image
  - text and image tokens as a single stream
  - (decoder only autoregressive model)
- learns how well text and image tokens match together
    - the prior distribution
	
![VQ-VAE-2 generation](/images/vq-vae-generation.png)



## DALL-E 2
Operation
1. generates a CLIP embedding from text
2. decoder generates image the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive

### Diffusion models
- generative modelling framework
