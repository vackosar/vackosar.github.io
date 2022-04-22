---
title: "OpenAI's DALL-E 2 And DALL-E 1"
description: "Quick overview of DALL-E 2 background and related models CLIP, and GLIDE"
layout: post
categories: ml
image: /images/dall-e-2-decoder.png
date: 2022-04-13
permalink: /:categories/:title
last_modified_at: 2022-04-22
---

{% include mathjax.html %}

[DALL-E 1](#openais-dall-e-1) uses [discrete variational autoencoder (dVAE)](#discreet-variational-auto-encoder-dvae), next token prediction, and [CLIP model](#openais-clip) re-ranking,
while [DALL-E 2](#openais-dall-e-2) uses CLIP embedding directly, and decodes it via diffusion similar to [GLIDE](#openais-glide).


## OpenAI's CLIP
- [paper](https://openai.com/blog/clip/): encodes image, and text to similar embeddings
- trained on a 400M various images with a caption text from the internet
- trained with contrastive learning, maximizing cosine similarity of corresponding image and text
- image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)


### CLIP Architecture
- text and image have separate [transformer](/ml/transformers-self-attention-mechanism-simplified) encoders
- visual encoder is [ViT](https://arxiv.org/pdf/2010.11929.pdf) (vision [transformer](/ml/transformers-self-attention-mechanism-simplified))
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
- the fix length text embedding is extracted from \[EOS\] token position
- trained on 256 GPUs for 2 weeks

![CLIP architecture](/images/clip-architecture.png)

<br>

## Variational Auto-encoder (VAE) Models
- model the image distribution via lower bound on [maximum likelihood](http://paulrubenstein.co.uk/variational-autoencoders-are-not-autoencoders/)
- encode each image as a gaussian distribution on the latent space
- random sampling from latents not differentiable
  - => re-parametrization trick \\( z = \sigma * r + \mu \\) where \\( r \\) is random vector
- loss is to reconstruct (L2) the image and latents to have normal distribution (KL)

![variational autoencoder](/images/variational-autoencoder.drawio.svg)


## Discreet Variational Auto-Encoder (dVAE)
- introduced in [VQ-VAE 1](https://arxiv.org/pdf/1711.00937.pdf) and [VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf) (dVAE, up-scaling)
- image encoder maps to latent 32x32 grid of embeddings
- vector quantization maps to 8k code words (visual codebook)
- decoder maps from quantized grid to the image
- copy gradients from decoder input z to the encoder output

![Discreet Variational Auto-Encoder VQ-VAE 1](/images/vq-vae-encoding-decoding.png)


<br>

## OpenAI's DALL-E 1

OpenAI DALL-E 1 introduced in [paper](https://arxiv.org/pdf/2102.12092.pdf) and [code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13).
DALL-E 1 generates images via [dVAE](#discreet-variational-auto-encoder-dvae) inspired by VA-VAE-2 and from textual input autoregressive on a discrete latent space.


### Training:
1. train encoder and decoder image of image into 32x32 grid of 8k possible code word tokens ([dVAE](#discreet-variational-auto-encoder-dvae))
2. concatenate encoded text tokens with image tokens into single array
3. train to predict next image token from the preceding tokens (autoregressive transformer)
4. discard the image encoder, keep only image decoder and next token predictor


### Prediction:
1. encode input text to tokens
2. iteratively predict next image token from the learned codebook
3. decode the resulting image tokens using [dVAE](#discreet-variational-auto-encoder-dvae)
4. select the best image using [CLIP model](#openais-clip) ranker

![DALL-E-1 generates tokens](/images/dall-e-1-generate.drawio.svg)

	
### Discreet Variational Auto-Encoder (dVAE) in DALL-E 1
- instead of copying gradients annealing ([categorical reparameterization with gumbel-softmax](https://arxiv.org/pdf/1611.01144.pdf))
- promote codebook utilization using higher KL-divergence weight
- decoder is conv2d, decoder block (4x relu + conv), upsample (tile bigger array), repeat


### DALL-E 1 Results
- Human evaluation vs DF-GAN, zero-shot
 
![DALL-E 1 results](/images/dall-e-1-results.png)


### DALL-E 1 Examples

![dall-e 1 examples](/images/dall-e-1-examples.png)

<br>

## Diffusion Models
  - [diffusion models](https://arxiv.org/pdf/2006.11239.pdf) reverse addition of gaussian noise to an image
  - an image arises from iterative denoising e.g. after 100 steps
  - training task is to predict the added noise with mean-squared error loss
  - similar to [normalizing flow models like OpenAI's Glow](/ml/openais-glow-flow-based-model-teardown) which are additionally single step and invertible

![diffusion model - progressive denoising examples steps (Denoising Diffusion Probabilistic Models)](/images/diffusion-model-example-steps.png)

## OpenAI's GLIDE
[Diffusion](#diffusion-models) image generator introduced  in [paper](https://arxiv.org/pdf/2112.10741.pdf).
- [CLIP](#openais-clip-model) guided diffusion
  - task: "predict the added noise given that the image has this caption" 
  - training task is prediction of the noise and guidance towards the CLIP text embedding
  - training loss has additional term of gradient of dot-product with the CLIP text embedding
  - CLIP encoders are trained on noised images to stay in distribution
- text-conditional diffusion model
  - GLIDE diffusion model is a transformer ([ADM model](https://arxiv.org/pdf/2105.05233.pdf))
  - text is embedded via another transformer
  - text embeddings are appended to the diffusion model sequence in each layer

<br>

## OpenAI's DALL-E 2

Introduced in [the paper](https://arxiv.org/pdf/2204.06125.pdf). Generates 1024 x 1024. Diffusion based.

### DALL-E 2 Training
1. generate a [CLIP model](#openais-clip) text embedding for text caption
2. "prior" network generates CLIP image embedding from text embedding
3. diffusion decoder generates image from the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive


### DALL-E 2 Image Generation

![DALL-E 2 decoder](/images/dall-e-2-decoder.png)

#### DALL-E 2 "Prior" Network
- Prior decoder generates CLIP image embedding from text
- tested autoregressive and diffusion prior generation with similar results
- autoregressive prior uses quantization to discrete codes
- diffusion prior is more compute efficient
  - Gaussian diffusion model conditioned on the caption text
  
#### DALL-E 2 Decoder 
- diffusion decoder similar to [GLIDE](#openais-glide)
- additionally condition also on CLIP image embedding
  - projected as 4 extra tokens
  - in addition to the text present in the original GLIDE

## DALL-E 2 Evaluation Results 

[dall-e 2 human eval results preference](/images/dall-e-2-results.png)

### DALL-E 2 Examples

Comparison:

![DALL-E 2 vs DALL-E 1 vs GLIDE](/images/dall-e-2-vs-dall-e-1-vs-GLIDE.png)

Sample ("A teddybear on a skateboard in Times Square."):

![samples from DALL-E “A teddybear on a skateboard in Times Square.”](/images/dall-e-2-random-images.png)