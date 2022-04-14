---
title: "OpenAI DALL-E 2 vs DALL-E 1, and CLIP"
description: "Understand quickly successful architecture used in GPT, BERT, and other famous transformer models."
layout: post
image: /images/transformer-full-model.png
categories: ml
date: 2022-03-05
permalink: /:categories/:title
---


DALL-E 1 uses quantization and next token predition while DALL-E 2 uses CLIP model and diffusion.

## DALL-E 1

OpenAI DALL-E introduced in [blog](https://openai.com/blog/dall-e/) and [code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13).

Training:
1. train encoder and decoder image of image into 32x32 grid of 8k possible code word tokens
2. concatenate encoded text tokens to image tokens and train to predict next token
3. discard the image encoder

Prediction:
1. encode input text
2. predict following image tokens
3. decode the image tokens
4. select the best results using [CLIP model](#clip) ranker

	
### Learn visual codebook:
- similar to [VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf)
- trains image encoder to a 32x32 grid of 8k code words  and decoder back to image
	- discrete variational autoencoder (dVAE) to "compress" 
	- explicit goal of VAE is not to really compress, but 
	- VAEs goal is to create model that estimates maximum likelihood
	- so it may collapse into single gaussian distribution
	- re-parametrization trick \\( z = \sigma * r + \mu \\)
	- tune the decoder with a weight on the KL divergence term
- compress into 32x32 grid of 8k code words
- decoder is conv2d, decoder block (4x relu + conv), upsample (tile bigger array), repeat
- start with uniform prior over the codebook
- maximize evidence lower bound (ELB)

### Learning the prior
- train transformer to predict next token of the concatenated text and image
  - text and image tokens as a single stream
  - (decoder only autoregressive model)
- learns how well text and image tokens match together
    - the prior distribution
	
### Sample generation
- re-rank samples drawn from the transformer
- use the decoder from dVAE to generate an image
- candidate text and image are ranked by [CLIP model](#clip) to select the best
	- language-guided search

![VQ-VAE-2 generation](/images/vq-vae-generation.png)


## CLIP
- [OpenAI blog](https://openai.com/blog/clip/)
- trained on a 400M images with and text from the internet
- robust to distribution shift
- separate text and image [transformer](/ml/transformers-self-attention-mechanism-simplified) encoder
- contrastive training for representations to correspond
- maximize cosine similarity
- generative methods not worked so well - too much text variety
- trained on 256 GPUs for 2 weeks
- resulting image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)

### CLIP Architecture
- visual encoder is [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf) image [transformer](/ml/transformers-self-attention-mechanism-simplified)
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
	- embeddings is extracted from \[EOS\] token position


## DALL-E 2
Operation
1. generates a CLIP embedding from text
2. decoder generates image the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive

### Diffusion models
- generative modelling framework
