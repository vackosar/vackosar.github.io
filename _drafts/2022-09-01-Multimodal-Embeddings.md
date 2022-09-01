---
title: "Multimodal embeddings"
description: "Multimodal embeddings as seen in CMA-CLIP and CoCa models"
layout: post
categories: ml
date: 2022-09-01
last_modified_at: 2022-09-01 
permalink: /:categories/:title
---

- extracting information from multiple-modalities


[//]: # (TODO change CLIP into reusable slides)

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
- the fixed-length text embedding is extracted from \[EOS\] token position, token embeddings also available
- trained on 256 GPUs for 2 weeks

![CLIP architecture](/images/clip-architecture.png)


### CLIP Applications
- [DALL-E 1](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-1) uses
  - [discrete variational autoencoder (dVAE)](/ml/openai-dall-e-2-and-dall-e-1#discreet-variational-auto-encoder-dvae), next token prediction,
  - and CLIP model for re-ranking,
- [DALL-E 2](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-2)
  - uses CLIP embedding directly,
  - and decodes images via diffusion similar to [GLIDE](/ml/openai-dall-e-2-and-dall-e-1#openais-glide).
- in image classification:
  - create for each class a text -> embedding
  - cosine similarity between image and text embeddings
- in image text classification


## Amazon's CMA-CLIP Model
- image-text classification task model
- [CMA-CLIP: Cross-Modality Attention CLIP for Image-Text Classification](https://arxiv.org/pdf/2112.03562v2.pdf) from Amazon on Dec 2021
- image and text modalities fuses with task-wise attention for multi-task classification
- beats two stream (global image embedding):
  - CLIP (keeps modalities separate and only shallow head is used) on Amazon's proprietary MRWPA dataset,
  - [MMBT](https://arxiv.org/pdf/1909.02950.pdf) (concat Resnet linear projections and BERT token embeddings) on Food101.
- beats one-stream (local fine-grained selected image patches)
  - [KaleidoBERT](https://arxiv.org/abs/2103.16110) (pretrains with aligning image tokens with text tokens, then [transformer](/ml/transformers-self-attention-mechanism-simplified)) on Fashion-Gen dataset

![CMA-CLIP architecture](/images/cma-clip-architecture.png)


### CMA-CLIP Architecture
- split image into patches, and embed with CLIP into sequence
- embed text with CLIP into sequence of text token embeddings
- concatenate both embeddings into single sequence into a transformer
- the transformer outputs aggregate (global) image and text embedding
- modality-wise attention per task: learned weighted sum of the two embeddings
  - the weight is a softmax of a dot product to a learned vector \\( w \\)
  - speculation: it helps to avoid noise

![CMA-CLIP](/images/cma-clip-architecture.png)


### CMA-CLIP Datasets
- Amazon's proprietary MRWPA dataset contains labels for Color, Pattern, and Style

![CMA-CLIP datasets](/images/cma-clip-datasets.png)

### CMA-CLIP Results
- modality wise attention helps the most on Style labels , then Pattern, then Color
- likely because (the text feature is irrelevant to relevant in this order)

![CMA-CLIP results](/images/cma-clip-results.png)


![CMA-CLIP results](/images/cma-clip-ablation-modality-wise-attention-sequence-wise-attention.png)




## CoCa Model
- state-of-the-art model on ImageNet’s image classification reported on is image-text model CoCa
- [CoCa](https://arxiv.org/abs/2205.01917)