---
title: "OpenAI's DALL-E 2 And DALL-E 1"
description: "Quick overview of DALL-E 2 background and related models CLIP, and GLIDE"
layout: post
categories: ml
date: 2022-04-13
permalink: /:categories/:title
---

{% include mathjax.html %}

DALL-E 1 uses discrete variational autoencoder, next token prediction, and CLIP model re-ranking,
while DALL-E 2 uses CLIP embedding directly, and decodes it via diffusion.


## OpenAI's CLIP
- [OpenAI blog on CLIP](https://openai.com/blog/clip/)
- trained on a 400M images with a caption text from the internet
- robust to distribution shift
- text and image have separate [transformer](/ml/transformers-self-attention-mechanism-simplified) encoders
- trained with contrastive learning making representations maximize cosine similarity
- trained on 256 GPUs for 2 weeks
- resulting image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)

### Architecture
- visual encoder is [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf) image [transformer](/ml/transformers-self-attention-mechanism-simplified)
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
- the fix length text embedding is extracted from \[EOS\] token position

<br>

## DALL-E 1

OpenAI DALL-E 1 introduced in [paper](https://arxiv.org/pdf/2102.12092.pdf) and [code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13).
DALL-E 1 generates images via variational autoencoder inspired by VA-VAE-2 and from textual input autoregressive on a discrete latent space.

### Training:
1. train encoder and decoder image of image into 32x32 grid of 8k possible code word tokens
2. concatenate encoded text tokens to image tokens and train to predict next image token
3. discard the image encoder

### Prediction:
1. encode input text
2. predict following image tokens
3. decode the image tokens using dVAE
4. select the best results using [CLIP model](#openais-clip-model) ranker

	
### Learning Visual Codebook
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

### Learning The Prior
- train transformer to predict next token of the concatenated text and image
  - text and image tokens as a single stream
  - (decoder only autoregressive model)
- learns how well text and image tokens match together
    - the prior distribution
	
![VQ-VAE-2 generation](/images/vq-vae-generation.png)

<br>

## OpenAI's GLIDE
Photo-like image generator introduced  in [paper](https://arxiv.org/pdf/2112.10741.pdf).
- a diffusion model
  - diffusion models reverse addition of gaussian noise to an image
  - an image arises from iterative denoising
  - training task is to predict the added noise with mean-squared error loss
  - similar to [normalizing flow models like OpenAI's Glow](/ml/openais-glow-flow-based-model-teardown) which are additionally single step and invertible
- [CLIP](#openais-clip-model) guided diffusion
  - task: "predict the added noise given that the image has this caption" 
  - training task is prediction of the noise and guidance towards the CLIP text embedding
  - training loss has additional term of gradient of dot-product with the CLIP text embedding
  - CLIP encoders are trained on noised images to stay in distribution
- text-conditional diffusion model
  - GLIDE diffusion model is a transformer ([ADM model](https://arxiv.org/pdf/2105.05233.pdf)))
  - text is embedded via another transformer
  - text embeddings are appended to the diffusion model sequence in each layer

<br>

## OpenAI's DALL-E 2

Introduced in [the paper](https://arxiv.org/pdf/2204.06125.pdf). Generates 1024 x 1024.

### Training
1. generate a [CLIP model](#openais-clip-model) embedding for text caption
2. prior generates CLIP image embedding from text embedding
3. diffusion decoder generates image from the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive


### Image Generation

![DALL-E 2 decoder](/images/dall-e-2-decoder.png)

#### Prior
- Prior decoder is to generate CLIP image embedding from text
- tested autoregressive and diffusion prior generation with similar results
- autoregressive prior uses quantization to discrete codes
- diffusion prior is more compute efficient
  - Gaussian diffusion model conditioned on the caption text
  
#### Decoder 
- diffusion decoder similar to [GLIDE](#openais-glide-model)
- additionally condition also on CLIP image embedding
  - projected as 4 extra tokens
  - in addition to the text present in the original GLIDE


## Results

Comparison:

![DALL-E 2 vs DALL-E 1 vs GLIDE](/images/dall-e-2-vs-dall-e-1-vs-GLIDE.png)

Sample ("A teddybear on a skateboard in Times Square."):

![samples from DALL-E “A teddybear on a skateboard in Times Square.”](/images/dall-e-2-random-images.png)