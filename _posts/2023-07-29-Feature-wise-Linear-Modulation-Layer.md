---
title: Feature-wise Linear Modulation Layer
description: Guide models with FiLM layers via a simple linear transformation conditioning.
categories: ml
date: 2023-07-27
image: /images/film-layer-feature-wise-linear-transformation-layer-cnn.png
last_modified_at: 2023-07-27
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
---


{% include image.html src="/images/film-layer-feature-wise-linear-transformation-layer-cnn.png" alt="Feature-wise Linear Modulation (sourced from paper)" %}

[Feature-wise Linear Modulation](https://arxiv.org/pdf/1709.07871.pdf) (FiLM) layer is used to change outputs of a general model with some specific conditioning input.

FiLM input is one input feature and a conditioning feature.
The conditioning is trained to **change model's behavior on demand** (changes output probability distribution).
For example you **condition [diffusion model](/ml/openai-dall-e-2-and-dall-e-1) with words** "brown cat" to generate images of brown cats.
The conditioning has smaller impact than the input feature and overall model training, but is very important for the model application.

## FiLM Implementation
Example FiLM applied to U-Net [implementation is here](https://github.com/gabolsgabs/cunet/blob/562103321e6324e816549d66cdbdeba5ed7ec1a7/cunet/train/models/cunet_model.py#L23).

- [Feature-wise transformations](https://distill.pub/2018/feature-wise-transformations/) conditions each input feature separately.
- Multiplicative conditioning seems to be more useful.
  - But to avoid loss of generality conditioning with addition and multiplication (affine transformation) is used.
- This affine conditioning is called Feature-wise Linear Modulation (FiLM) layer.
- Conditioning is often applied across multiple layers.
- [Cross-attention](/ml/cross-attention-in-transformer-architecture) is more complex feature-wise transformation, where the feature is an input sequence. Cross-attention has quadratic complexity.


## FiLM Application

### Reinforcement Learning

[Q-Transformer](/ml/Bellman-Update-and-Synthetic-Data-in-Q-Transformer) applies FiLM to a visual EfficientNet to condition with embeddings of textual instructions to predict Q-values.


### Try-on in Fashion 
{% include image.html src="/images/film-layer-u-net-virtual-try-on-tryondiffusion.png" alt="FiLM layer in U-Net in TryOnDiffusion for virtual try on clothes" %}

[TryOnDiffusion: A Tale of Two UNets](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_TryOnDiffusion_A_Tale_of_Two_UNets_CVPR_2023_paper.pdf) is using FiLM layers to condition U-Net to generate new image given an input person image but wearing a shirt from another conditioning image.

FiLM layer relies on the ability to [disentangle attributes](/ml/manipulate-item-attributes-via-disentangled-representation) about the input features and change them using the conditioning.

