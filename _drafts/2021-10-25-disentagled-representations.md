---
layout: post
title: "Disentangled Representations"
date: 2021-10-25
categories: ml
description: TDO
permalink: /:categories/:title
---

# Why Disentangled
- attribute manipulation, conditional similirity e.g. the same with different change color
- complementary item e.g. complete fashion outfit

# What is disentangled
- Goal change 
- Entangled representation = hard to to preserve some attributes and change others
- Disentangled: Attibutes have separate dimensions applied to them of there is known orthogonality

# Unsupervised Disentangling Methods
- GANs (has encoder and decoder) e.g. [DNA-GAN: Learning Disentangled Representations from Multi-Attribute Images](https://arxiv.org/pdf/1711.05415.pdf),
- Auto-encoders (mutual information between latents, total correlation) e.g. unsupervised [Relevance factors VAE](https://arxiv.org/pdf/1902.01568v1.pdf)
- Flow-Based models e.g. [Glow](/ml/openais-glow-flow-based-model-teardown) (1-1 encodes into independent gaussian factors)

# Unsupervised Disentangled Representations
- Google 2019 paper [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://ai.googleblog.com/2019/04/evaluating-unsupervised-learning-of.html)
- a large-scale evaluation of various unsupervised methods (12k models)
- On dataset Shape3D try to separate all attributes of the scene into 10 dimensions 
- No model disentangled reliably
- theorem assumptions about the data have to be incorporated into the model (inductive bias)
- so each unsupervised model needs to be at least specialized to some type of data
 
![Shape3D dataset for disentagling factors: floor color, wall color, object color, object size, camera angle](../images/disentangled-shape3d.png)

# Attribute-driven Disentangled Representations

- Amazon 2021 paper [Learning Attribute-driven Disentangled Representations for Interactive Fashion Retrieval](https://openaccess.thecvf.com/content/ICCV2021/papers/Hou_Learning_Attribute-Driven_Disentangled_Representations_for_Interactive_Fashion_Retrieval_ICCV_2021_paper.pdf)
- SoTA on the fashion tasks
- supervised disentangled represantions learning
  - all attribute values are of fixed count
  - multi-task training
  - store prototype embeddings of each attribute value in memory module
  - prototypes can then be swapped for items attribute vector

![disentangled representation using attribute-specific encoder](../images/disentangled-encoder.png)


## Architecture

- image representation (?which)
- per attribute:
  - fully-connected two-layer network
  - map into attributed-specific subspace
  - producing image's attribute embedding
- together it is disentangled representation
- called Attribute-Driven Disentangled Encoder (ADDE)
- memory block
  - stores prototype embeddings for all values of the attributes
  - e.g. each color has one prototype embeddings
  - stored in a matrix that forces small non-block diagonal elements
  - trained via triplet loss
    - randomly generate manipulation vectors to other attribute values
  - Why we cannot extract these from the classifier - not the same dimension or reprez?

## Loss
- Memory block loss
- Compositional triplet loss
- Consistency loss
- Label triplet loss


## Experiments and Results
- 

