---
title: Multilingual Open LLMs
description: A list of good open multilingual large language models.
categories: ml
date: 2024-06-22
last_modified_at: 2024-06-22
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2024-05-06-Llama-3.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2024-02-20-Synthetic-Data-for-LLM-Training.md
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
---

{% include highlight-rouge-friendly.css.html %}


Multilingual models are not as common as English ones. Note that this list is evolving and may not be up-to-date.

- [Llama-3](/ml/Llama-3) is not intended for [use with other languages than English](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md), although authors do report training on 30 languages with over 5% of the dataset, and possibility of fine-tuning the model on them. There seems to be support [based on tokenization](https://www.icodeformybhasa.com/p/exploring-multilingual-aspects-and) for: EN, FR, DE, ES, KO, AF, IT, CA, RO, CY, TJ, DA, VI. But people use it even for more languages.
- [Qwen2](https://qwenlm.github.io/blog/qwen2/) Qwen2-72B and various other sizes Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, Qwen2-57B-A14B. Primarily english and chinese, but 27 others. Primarily: DE, FR, ES, PT, IT, NL, RU, CS, PL, AR, FA, HE, TR, JA, KO, VI, TH, ID, MS, LO, MY, CEB, KM, TL, HI, BN, UR
- [Nemotron 4-15b](https://arxiv.org/html/2402.16819v2) or [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct). I haven't tested this model. Primarily: ES, ID, NL, PL, FR, RU, IT, DE, VI, JA, TR, EL, RO, CS, AR, SV, FA, ZH, HU, KO, UK, NO, FL, HI, DA, BG, HR, SK, TH
- [EagleX 7B 2.25T](https://huggingface.co/RWKV/v5-EagleX-v2-7B-pth) has faster inference, but generally seems it has a bit lower quality. Not available on OpenRouter.  I haven't tested this model much.


