---
title: Bash Tricks I Use
description: Treats for your Bash without bashing it too much!
categories: ml
date: 2024-06-09
last_modified_at: 2024-06-09
layout: post
permalink: /:categories/:title
---

{% include highlight-rouge-friendly.css.html %}


Multilingual models are not as common as English ones.

- Llama-3 is not intended for [use with other languages than English](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md), although authors report training on 30 languages, and possibility of fine-tuning the model on them.
- [Qwen2](https://qwenlm.github.io/blog/qwen2/) Qwen2-72B and various other sizes Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, Qwen2-57B-A14B. Primarily english and chinese, but 27 others.
- [Nemotron 4-15b](https://arxiv.org/html/2402.16819v2) or [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct)
- [EagleX 7B 2.25T](https://huggingface.co/RWKV/v5-EagleX-v2-7B-pth) has faster inference, but generally seems it has a bit lower quality.