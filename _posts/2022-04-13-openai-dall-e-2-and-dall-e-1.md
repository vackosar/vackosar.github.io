---
title: OpenAI's DALL-E 2 and DALL-E 1 Explained
description: Compare of text-to-image generation models DALL-E 1, 2, and understand related models VQ-VAE, CLIP, and GLIDE
layout: post
categories: ml
image: /images/dalle-2-1-thumb.png
date: 2022-04-13
permalink: /:categories/:title
last_modified_at: 2022-04-22
video: cYeH45VOI3w
my_related_post_paths:
- _posts/2023-07-03-OpenAIs-Image-Text-Model-CLIP.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2021-10-04-electra-4x-cheaper-bert-training.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
---



{% include mathjax.html %}
{% include load_video.html %}

[DALL-E 1](#openais-dall-e-1) uses [discrete variational autoencoder (dVAE)](#discreet-variational-auto-encoder-dvae), next token prediction, and [CLIP model](#openais-clip) re-ranking,
while [DALL-E 2](#openais-dall-e-2) uses CLIP embedding directly, and decodes images via diffusion similar to [GLIDE](#openais-glide).


{% include shared_slides/openais-clip.md %}

<br>

## Variational Auto-encoder (VAE) Models
- model the image distribution via lower bound on [maximum likelihood](http://paulrubenstein.co.uk/variational-autoencoders-are-not-autoencoders/)
- encode each image as a gaussian distribution on the latent space
- random sampling from latents not differentiable
  - => re-parametrization trick \\( z = \sigma * r + \mu \\) where \\( r \\) is random vector
- loss is to reconstruct (L2) the image and latents to have normal distribution (KL)
- sample, or interpolate from the latent normal distribution and generate images - may find [disentangled representations](/ml/manipulate-item-attributes-via-disentangled-representation)

{% include image.html src="/images/variational-autoencoder.drawio.svg" alt="variational autoencoder" %}


## Quantization
{% include shared_slides/quantization.md %}


## Discreet Variational Auto-Encoder (dVAE)
- introduced in [VQ-VAE 1](https://arxiv.org/pdf/1711.00937.pdf) and [VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf) (dVAE, up-scaling)
- image encoder maps to latent 32x32 grid of [embeddings](/ml/Embeddings-in-Machine-Learning-Explained)
- vector quantization maps to 8k code words (visual codebook)
- decoder maps from quantized grid to the image
- copy gradients from decoder input z to the encoder output

{% include image.html src="/images/vq-vae-encoding-decoding.png" alt="Discreet Variational Auto-Encoder VQ-VAE 1" %}


<br>

## OpenAI's DALL-E 1

- OpenAI introduced DALL-E 1 text-to-image generator in introduced in [paper](https://arxiv.org/pdf/2102.12092.pdf) and [code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13).
- generates 256×256 images from text via [dVAE](#discreet-variational-auto-encoder-dvae) inspired by [VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf).
- autoregressive-ly generates image tokens from textual tokens on a discrete latent space.


### DALL-E 1 Training:
1. train encoder and decoder image of image into 32x32 grid of 8k possible code word tokens ([dVAE](#discreet-variational-auto-encoder-dvae))
2. concatenate encoded text tokens with image tokens into single array
3. train to predict next image token from the preceding tokens (autoregressive transformer)
4. discard the image encoder, keep only image decoder and next token predictor


### DALL-E 1 Prediction:
1. encode input text to text tokens
2. iteratively predict next image token from the learned codebook
3. decode the image tokens using [dVAE](#discreet-variational-auto-encoder-dvae) decoder
4. select the best image using [CLIP model](#openais-clip) ranker

{% include image.html src="/images/dall-e-1-generate.drawio.svg" alt="DALL-E-1 generates tokens" %}

	
### DALL-E 1 Discreet Variational Auto-Encoder (dVAE)
- instead of copying gradients annealing ([categorical reparameterization with gumbel-softmax](https://arxiv.org/pdf/1611.01144.pdf))
- promote codebook utilization using higher KL-divergence weight
- decoder is conv2d, decoder block (4x relu + conv), upsample (tile bigger array), repeat


### DALL-E 1 Results
- competitive in zero-shot fashion, preferred 90% time by humans
- Human evaluation which is preferred DALL-E vs DF-GAN, zero-shot
 
{% include image.html src="/images/dall-e-1-results.png" alt="DALL-E 1 results" %}


### DALL-E 1 Examples

{% include image.html src="/images/dall-e-1-examples.png" alt="dall-e 1 examples" %}

<br>

## Diffusion Models
- [Diffusion models](https://arxiv.org/pdf/2006.11239.pdf) reverse addition of gaussian noise to an image.
- An image arises from iterative denoising e.g. after 100 steps.
- Training task is to predict the added noise with mean-squared error loss.
- Similar to [normalizing flow models like OpenAI's Glow](/ml/openais-glow-flow-based-model-teardown) which are additionally single step and invertible.
- Diffusion model can be formulated as [an ODE solution](https://arxiv.org/pdf/2011.13456.pdf), where de-noising step represents time dimension step.
The **training image data form a manifold**. **Adding noise to the images expands** the manifold volume. **The expansion direction and step size of the expansion define the ODE**.
The ODE's solution is the probability density function. We link gradient of the density function to the L2 loss of denoising function.
The step size is scaled with a function dependent on the noise level.

{% include image.html src="/images/diffusion-model-example-steps.png" alt="diffusion model - progressive denoising examples steps (Denoising Diffusion Probabilistic Models)" %}


## OpenAI's GLIDE
- [Diffusion](#diffusion-models) text-to-image (256 × 256) generator introduced  in [paper](https://arxiv.org/pdf/2112.10741.pdf).
- GLIDE outperforms on human preference DALL-E 1.
- [CLIP](#openais-clip-model) guided diffusion
  - task: "predict the added noise given that the image has this caption" 
  - training task is prediction of the noise and guidance towards the CLIP text embedding
  - training loss has additional term of gradient of dot-product with the CLIP text embedding
  - CLIP encoders are trained on noised images to stay in distribution
- text-conditional diffusion model
  - GLIDE diffusion model is a [transformer](/ml/transformers-self-attention-mechanism-simplified) ([ADM model](https://arxiv.org/pdf/2105.05233.pdf))
  - text is embedded via another transformer
  - text embeddings are appended to the diffusion model sequence in each layer

<br>


## OpenAI's DALL-E 2

- OpenAI introduced DaLL-E-2 in [the paper](https://arxiv.org/pdf/2204.06125.pdf)
- model name is unCLIP while DALL-E 2 is seems to be a marketing name
- generates 1024 x 1024 images from text using diffusion models.
- generates more diverse and higher resolution images than [GLIDE](#openais-glide).

### DALL-E 2 Training
1. generate a [CLIP model](#openais-clip) text embedding for text caption
2. "prior" network generates CLIP image embedding from text embedding
3. diffusion decoder generates image from the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive


### DALL-E 2 Image Generation

{% include image.html src="/images/dall-e-2-decoder.png" alt="DALL-E 2 decoder" %}

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
DALL-E 2 competitive photo-realism while more diverse images than GLIDE

{% include image.html src="/images/dall-e-2-results.png" alt="dall-e 2 human eval results preference" %}


### DALL-E 2 Examples

Comparison:

{% include image.html src="/images/dall-e-2-vs-dall-e-1-vs-GLIDE.png" alt="DALL-E 2 vs DALL-E 1 vs GLIDE" %}

Sample ("A teddybear on a skateboard in Times Square."):

{% include image.html src="/images/dall-e-2-random-images.png" alt="samples from DALL-E “A teddybear on a skateboard in Times Square.”" %}