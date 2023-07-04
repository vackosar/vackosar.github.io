---
title: OpenAI's Image-Text Model CLIP
description: Encode image, and text into similar embedding vectors for multimodality.
categories: ml
date: 2023-07-03
last_modified_at: 2023-07-03
image: /images/clip-contrastive-pretraining.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
---

Since the initial release, the CLIP architecture entered the hall of fame.
One of the most performant versions now is likely H[/14 OpenCLIP variant trained on LAION-2B](https://laion.ai/blog/large-openclip/) achieving 78.0% zero shot top-1 accuracy on ImageNet and 73.4% on zero-shot image retrieval at Recall@5 on MS COCO.
Both vision and the text par of the CLIP architecture are available in various implementation, for example, vision encoder can be ViT or Renset-50.


{% include shared_slides/openais-clip.md %}
