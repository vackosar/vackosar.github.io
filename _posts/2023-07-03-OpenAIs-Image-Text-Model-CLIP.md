---
title: OpenAI's Image-Text Model CLIP
description: Encode image, and text into similar embedding vectors for multimodality.
categories: ml
date: 2023-07-03
last_modified_at: 2023-07-03
image: /images/clip-contrastive-pretraining.png
layout: post
permalink: /:categories/:title
---

Since the initial release, the CLIP architecture entered the hall of fame.
One of the most performant versions now is likely H[/14 OpenCLIP variant trained on LAION-2B](https://laion.ai/blog/large-openclip/) achieving 78.0% zero shot top-1 accuracy on ImageNet and 73.4% on zero-shot image retrieval at Recall@5 on MS COCO.
Both vision and the text par of the CLIP architecture are available in various implementation, for example, vision encoder can be ViT or Renset-50.


{% include shared_slides/openais-clip.md %}
