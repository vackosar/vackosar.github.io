---
title: "Multimodal Image-text Classification"
description: "Understand the top deep learning image and text classification models CMA-CLIP, CLIP, CoCa, and MMBT used in e-commerce."
layout: post
categories: ml
date: 2022-09-01
image: /images/multimodal-image-text-classification.png
last_modified_at: 2022-09-02 
permalink: /:categories/:title
---

- input is image and text pair (multiple modalities) and output a class or embedding vector
- used in product classification to [product taxonomies](/ml/Automatically-Expanding-Taxonomy) e.g. [Google product taxonomy](https://vaclavkosar.com/software/google-product-taxonomy-viewer)
- multi-modal models are increasingly important e.g. [CoCa achieved SoTA on ImageNet](#coca-results)

![mutlimodal image-text classification](/images/multimodal-image-text-classification.png)


## OpenAI's CLIP
- [CLIP: Connecting Text and Images (Jan 2021)](https://openai.com/blog/clip/): encodes image, and text to similar embeddings
- trained on a proprietary WebImageText (WIT don't confuse with Wikipedia-based Image Text Dataset (WIT))
  - 400M of various images with a caption text from the internet
- trained with contrastive learning, maximizing cosine similarity of corresponding image and text
- image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)


### CLIP Architecture
- text and image have separate [transformer](/ml/transformers-self-attention-mechanism-simplified) encoders
- visual encoder is [ViT](https://arxiv.org/pdf/2010.11929.pdf) (vision [transformer](/ml/transformers-self-attention-mechanism-simplified))
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
- the fixed-length text embedding is extracted from \[EOS\] token position,
- text token embeddings and image patch embeddings also available
- trained on 256 GPUs for 2 weeks

![CLIP architecture](/images/clip-architecture.png)


### CLIP Applications
- [DALL-E 1](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-1) uses
  - [discrete variational autoencoder (dVAE)](/ml/openai-dall-e-2-and-dall-e-1#discreet-variational-auto-encoder-dvae), next token prediction,
  - and CLIP model for re-ranking,
- [DALL-E 2](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-2)
  - uses CLIP embedding directly,
  - and decodes images via diffusion similar to [GLIDE](/ml/openai-dall-e-2-and-dall-e-1#openais-glide).
- zero-shot image classification:
  - create for each class a text -> embedding
  - cosine similarity between image and text embeddings
- supervised image-text classification training on the embeddings


## Amazon's CMA-CLIP Model
- image-text classification task model
- [CMA-CLIP: Cross-Modality Attention CLIP for Image-Text Classification](https://arxiv.org/pdf/2112.03562v2.pdf) from Amazon on Dec 2021
- image and text modalities fuses with task-wise attention for multi-task classification
- beats two stream (global image embedding):
  - CLIP (keeps modalities separate and only shallow head is used) on Amazon's proprietary MRWPA dataset,
  - [MMBT model (see below)](#facebooks-mmbt-model) on Food101 by +1%
  - no comparison with [EmbraceNet (see below)](#embracenet-model)
- strongly beats one-stream (local fine-grained selected image patches)
  - [KaleidoBERT](https://arxiv.org/abs/2103.16110) (pretrains with aligning image tokens with text tokens, then [transformer](/ml/transformers-self-attention-mechanism-simplified)) on Fashion-Gen dataset

![CMA-CLIP model architecture](/images/cma-clip-architecture.png)


### CMA-CLIP Architecture
- split image into patches, and embed with CLIP into sequence
- embed text with CLIP into sequence of text token embeddings
- concatenate both embeddings into single sequence into a transformer
- the transformer outputs aggregate (global) image and text embedding
- modality-wise attention per task: learned weighted sum of the two embeddings
  - asks: is this input relevant?
  - the weight is a softmax of a dot product to a learned vector
  - speculation: it helps to avoid noise

![CMA-CLIP model architecture](/images/cma-clip-architecture.png)


### CMA-CLIP Datasets
- Amazon's proprietary MRWPA dataset contains labels for Color, Pattern, and Style
- [Fashion-Gen Dataset](https://arxiv.org/pdf/1806.08317v2.pdf) with 325k images, 78k texts, single-label, and 41 categories.
- [UPMC-Food101 Dataset](https://hal.archives-ouvertes.fr/hal-01196959/file/CEA_ICME2015.pdf) with 90k images, 86k texts, 101 categories.

![CMA-CLIP datasets](/images/cma-clip-datasets.png)


### CMA-CLIP Results
- WIT in below is proprietary WebImageText
- Vaclav: Parameter count comparison is missing
 
![CMA-CLIP model results](/images/cma-clip-results.png)


### CMA-CLIP Ablation Results
- modality wise attention helps the most on Style labels, then Pattern, then Color
- likely because (the text feature is irrelevant to relevant in this order)

![CMA-CLIP ablation results](/images/cma-clip-ablation-modality-wise-attention-sequence-wise-attention.png)


## Google's CoCa Model
- [CoCa: Contrastive Captioners are Image-Text Foundation Models](https://arxiv.org/abs/2205.01917)
- State-of-the-art model many image and image-text tasks
- Combines a contrastive loss (similar to CLIP) with captioning task

![CoCa model pretraining](/images/coca-pretraining.png)


### CoCa Results
- achieved SoTA on ImageNet!

![CoCa results](/images/coca-results.png)


## Facebook's MMBT Model
- [Supervised Multimodal Bitransformers for Classifying Images and Text](https://arxiv.org/pdf/1909.02950.pdf)
- concatenate linear projections of Resnet output with BERT token embeddings into a sequence as Transformer input

![MMBT model architecture](/images/mmbt-architecture.png)


## EmbraceNet Model
- [EmbraceNet: A robust deep learning architecture for multimodal classification](https://arxiv.org/pdf/1904.09078.pdf) 2019
- feature fusion via a weighted summation with a normalizatin and "feature dropout"

![EmbraceNet model architecture](/images/embracenet-architecture.png)