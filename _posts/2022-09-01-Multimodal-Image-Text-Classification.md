---
title: Multimodal Image-text Classification
description: Understand the top deep learning image and text classification models CMA-CLIP, CLIP, CoCa, and MMBT used in e-commerce.
layout: post
categories: ml
date: 2022-09-01
video: Oj3OqUgYL3Y
image: /images/multimodal-image-text-classification.png
last_modified_at: 2022-09-07
permalink: /:categories/:title
my_related_post_paths:
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2022-04-18-how-computers-understood-humans.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
---



- input is image and text pair (multiple modalities) and output a class or embedding vector
- used in product classification to [product taxonomies](/ml/Automatically-Expanding-Taxonomy) e.g. [Google product taxonomy](https://vaclavkosar.com/software/google-product-taxonomy-viewer)
- multi-modal models are increasingly important e.g. [CoCa achieved SoTA on ImageNet](#coca-results)

{% include load_video.html %}


{% include shared_slides/openais-clip.md %}

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
  - resists noise and missing data better similar to [EmbraceNet feature dropout](#embracenet-model)

![CMA-CLIP model architecture](/images/cma-clip-architecture.png)


### CMA-CLIP Datasets
- Amazon's proprietary MRWPA dataset contains labels for Color, Pattern, and Style
- [Fashion-Gen Dataset](https://arxiv.org/pdf/1806.08317v2.pdf) with 325k images, 78k texts, single-label, and 41 categories.
- [UPMC-Food101 Dataset](https://hal.archives-ouvertes.fr/hal-01196959/file/CEA_ICME2015.pdf) with 90k images, 86k texts, 101 categories.

![CMA-CLIP datasets](/images/cma-clip-datasets.png)



### CMA-CLIP Results
- Overall CMA-CLIP slightly better than MMBT, but speculatively could outperform on multitasking
- Parameter count comparison is missing
 
![CMA-CLIP model results](/images/cma-clip-results.png)


#### CMA-CLIP vs KaleidoBERT vs ImageBERT on Fashion-Gen 
- CMA-CLIP outperforms KaleidoBERT vs ImageBERT, and other models.
- There is no benchmark avaiabale for MMBT or CLIP on Fashion-Gen 

![CMA-CLIP vs KaleidoBERT vs ImageBERT on Fashion-Gen](/images/cma-clip-vs-kaleidobert-vs-imagebert-on-fashion-gen.png)


#### CMA-CLIP vs MMBT vs CLIP on Food101
- CMA-CLIP outperforms MMBT and CLIP
- MMBT significantly outperforms CLIP likely due to the tuned transformer head
- BERT does better than ViT on this dataset

![cma-clip vs mmbt vs clip vs bert vs vit on Food101](/images/cma-clip-vs-mmbt-vs-clip-vs-bert-vs-vit.png)


#### CMA-CLIP Results on MRWPA dataset
- WIT in below is proprietary WebImageText
- Since CMA-CLIP has more parameters, the performance is expected
- Multitask learning classification usable for [learning disentangled representations](/ml/manipulate-item-attributes-via-disentangled-representation)

![CMA-CLIP vs CLIP Results on MRWPA dataset](/images/cma-clip-vs-clip-on-MRWPA.png)


#### CMA-CLIP Image-text Alignment on MRWPA dataset
Text-to-image attention map alignment suggest CMA-CLIP can find cross-modality correlations.

![CMA-CLIP text-image token attention map](/images/cma-clip-text-token-image-token-attention-map.png)



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
- MMBT has similar architecture to [CMA-CLIP](#cma-clip-architecture) except for the CLIP backbone and modality-wise attention useful in multitasking

![MMBT model architecture](/images/mmbt-architecture.png)


## EmbraceNet Model
- [EmbraceNet: A robust deep learning architecture for multimodal classification](https://arxiv.org/pdf/1904.09078.pdf) 2019
- feature fusion via a weighted summation with a normalizatin and "feature dropout"
- model has similar performance to concatenation, but performs better when some modalities are missing due to noisy data
- We used it in [GLAMI-1M dataset](https://github.com/glami/glami-1m)

![EmbraceNet model architecture](/images/embracenet-architecture.png)


## DeepMind's Perceiver Model

{% include shared_slides/perceiver-io.md %}


## Multilingual Image-Text Classification
A lot of **room for research left** our new [13-lingual dataset GLAMI-1M](https://github.com/glami/glami-1m).
The task requires a **multilingual language encoder**, while images usually are international by default.
Language distribution requires additional consideration.
