Both Dall-e version use CLIP model, but in different ways.

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
- TODO finish

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)

## CLIP Architecture
- visual encoder [ViT](https://arxiv.org/pdf/2010.11929.pdf) image [transformer](/ml/transformers-self-attention-mechanism-simplified)
- text encoder [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)

## DALL-E 

[blog](https://openai.com/blog/dall-e/)
[code](https://github.com/openai/DALL-E/blob/5be4b236bc3ade6943662354117a0e83752cc322/dall_e/decoder.py#L13)

	
### Learn visual codebook:
- train discrete variational autoencoder (dVAE) to "compress" images
	- explicit goal of VAE is no to really compress, but 
	- VAEs goal is to create model that estimates maximum likelihood and not compress
	- so it may collapse into single gaussian distribution
	- re-parametrization trick \\( z = \sigma * r + \mu \\)
	- tune the decoder with a weight on the KL divergence term
- trains encoder and decoder
- compress into 32x32 grid of 8k code words
- decoder is conv2d, decoder block (4x relu + conv), upsample (tile bigger array), repeat
- start with uniform prior over the codebook
- maximize evidence lower bound (ELB)

### Learning the prior
- only decoder is used 
- learn distribution over text + image tokens
- use autoregressive transformer (guess next token)
	- "the text and image tokens are concatenated and modeled autoregressively as a single stream of data."
	
### Sample generation
- re-rank samples drawn from the transformer

## DALL-E-2
Operation
1. generates a CLIP embedding from text
2. decoder generates image the image embedding

- Can vary images while preserving style and semantics in the embeddings
- Authors found diffusion models more efficient and higher quality compared to autoregressive

### Diffusion models
- generative modelling framework
