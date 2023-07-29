---
title: "Feature-wise Linear Modulation Layer"
description: "Guide models with FiLM layers via a simple linear transformation conditioning."
categories: ml
date: 2023-07-27
image: /images/film-layer-feature-wise-linear-transformation-layer-cnn.png
last_modified_at: 2023-07-27
layout: post
permalink: /:categories/:title
---


![Feature-wise Linear Modulation (sourced from paper)](/images/film-layer-feature-wise-linear-transformation-layer-cnn.png)

[Feature-wise Linear Modulation](https://arxiv.org/pdf/1709.07871.pdf) (FiLM) layer is used to change outputs of a general model with some specific conditioning input.

FiLM input is one input feature and a conditioning feature.
The conditioning is trained to **change model's behavior on demand** (changes output probability distribution).
For example you **condition diffusion model with words** "brown cat" to generate images of brown cats.
The conditioning has smaller impact than the input feature and overall model training, but is very important for the model application.

## Implementation
Example FiLM applied to U-Net [implementation is here](https://github.com/gabolsgabs/cunet/blob/562103321e6324e816549d66cdbdeba5ed7ec1a7/cunet/train/models/cunet_model.py#L23).

- Feature-wise transformations conditions each input feature separately.
- Multiplicative conditioning seems to be more useful.
  - But to avoid loss of generality conditioning with addition and multiplication (affine transformation) is used.
- This affine conditioning is called Feature-wise Linear Modulation (FiLM) layer.
- Conditioning is often applied across multiple layers.
- [Cross-attention](/ml/cross-attention-in-transformer-architecture) is more complex feature-wise transformation, where the feature is an input sequence.


## Application

![FiLM layer in U-Net in TryOnDiffusion for virtual try on clothes](/images/film-layer-u-net-virtual-try-on-tryondiffusion.png)

[TryOnDiffusion: A Tale of Two UNets](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhu_TryOnDiffusion_A_Tale_of_Two_UNets_CVPR_2023_paper.pdf) is using FiLM layers.


You can read more on feature-wise transformations [here](https://distill.pub/2018/feature-wise-transformations/).