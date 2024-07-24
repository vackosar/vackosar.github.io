---
title: Multilingual Open LLMs
description: A list of good open multilingual large language models.
categories: ml
date: 2024-06-22
last_modified_at: 2024-07-18
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2024-05-06-Llama-3.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2024-02-20-Synthetic-Data-for-LLM-Training.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
---

{% include highlight-rouge-friendly.css.html %}


Multilingual models are not as common as English ones. Note that this list is evolving and may not be up-to-date.



| Name                                                                              | Description                                                                                                                                                                                                                             | Primary languages        | Languages with likely a good support                                                                                |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Llama 3.1](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/)                                                                     | Version 405B is likely the best as of 2024-07-24 Close to GPT-4o performance in English, but quite in other languages yet.                                                                                                                | EN, DE, FR, IT, PT, HI, ES, TH | Likely a wide support. Speak more coherently in CS.                                                                 |
| [Mistral-Nemo-Instruct-2407](https://mistral.ai/news/mistral-nemo/)               | 12B model trained for multilingualism. Seems to generate well in CS if prompted for.                                                                                                                                                    | EN, CN, IT, FR, DE, ES, RU | Likely a wide support. Perhaps 85% of all languages have some support.                                              |
| [Qwen2](https://qwenlm.github.io/blog/qwen2/)                                     | Qwen2-72B and various other sizes Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, Qwen2-57B-A14B.                                                                                                                                                     | EN, ZH                   | EN, ZH, DE, FR, ES, PT, IT, NL, RU, CS, PL, AR, FA, HE, TR, JA, KO, VI, TH, ID, MS, LO, MY, CEB, KM, TL, HI, BN, UR |
| [Gemma 2](https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf) | It seems to be capable in Czech (CS), which a small language. I have seen similar reports for some other languages. Probably all more frequent languages than CS are supported. Based on the Whisper dataset these _could be_ following | EN                       | ZH, DE, ES, RU, FR, PT, KO, JA, TR, PL, IT, SV, NL, CA, FI, ID, AR, UK, VI, HE, EL, DA, MS, HU, RO, NO, TH, CS.     |
| [Llama-3](https://github.com/meta-llama/llama3)                                   | Llama-3 is a multilingual model trained on over 100 languages. It is not intended for use with other languages than English.                                                                                                            | EN                       | EN, FR, DE, ES, KO, AF, IT, CA, RO, CY, TJ, DA, VI.                                                                 |
| [Nemotron 4](https://arxiv.org/html/2402.16819v2)                                 | Nemotron-4-15b, or [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct). I haven't tested this model.                                                                                                     | EN                       | ES, ID, NL, PL, FR, RU, IT, DE, VI, JA, TR, EL, RO, CS, AR, SV, FA, ZH, HU, KO, UK, NO, FL, HI, DA, BG, HR, SK, TH  |
| [EagleX 7B 2.25T](https://huggingface.co/RWKV/v5-EagleX-v2-7B-pth)                | Faster inference, but generally a bit lower quality. Not available on OpenRouter. I haven't tested this model much.                                                                                                                     | EN                       |                                                                                                                     |
