---
title: MassiveText Dataset introduced for pre-training of DeepMind's Gopher
description: Private diverse 10-lingual textual dataset composed of web, Github, news, Wikipedia, Books, C4.
layout: post
image: /images/retrieval-transformer-massive-text.png
categories: ml
date: 2022-03-20
permalink: /:categories/:title
last_modified_at: 2022-05-14
my_related_post_paths:
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
---



<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/retrieval-transformer-massive-text.png"
        alt="MassiveText dataset composition table"/>
    <figcaption class="figure-caption">MassiveText dataset composition table</figcaption>
</figure>

- Introduced in [DeepMind's Scaling Language Models: Methods, Analysis & Insights from Training Gopher](https://storage.googleapis.com/deepmind-media/research/language-research/Training%20Gopher.pdf)
- Disk size is 10.5 TB.
- Token count is around 5T tokens.
- Document count is 2.32B with average 2k tokens per document.
- Dataset is **private** - not open-source licenced as of 2022-03-20.
- Similar but public dataset is [The Pile (diverse 800GB text dataset)](https://pile.eleuther.ai/)

## MassiveText Contents
- Dataset language composition: 99% English, then 10 other languages.
- Google SafeSearch filter
- Dataset is composed of subsets: web, Github, news, Wikipedia, Books, [C4 (web-text)](https://arxiv.org/abs/1910.10683)

![MassiveText non-english composition](/images/massivetext-non-english-composition.png)


## Papers Using MassiveText
- Since it is private only DeepMind uses the dataset
- [DeepMind's RETRO Transformer used multi-lingual version of the dataset](/ml/DeepMinds-RETRO-Transformer-Model)
- [DeepMind's Gopher used only english version of the dataset](https://storage.googleapis.com/deepmind-media/research/language-research/Training%20Gopher.pdf)


## Don't Confuse MassiveText with Amazon Massive Dataset
- [Amazon Massive](https://github.com/alexa/massive) is not MassiveText
- Amazon Massive is:
  - released by Amazon on 2022-04-20
  - multilingual natural-language understanding 
  - 51-language dataset
