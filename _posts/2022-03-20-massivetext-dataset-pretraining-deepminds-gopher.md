---
title: "MassiveText Dataset introduced for pre-training of DeepMinds Gopher"
description: "Private diverse 10-lingual textual dataset composed of web, Github, news, Wikipedia, Books, C4."
layout: post
image: /images/retrieval-transformer-massive-text.png
categories: ml
date: 2022-03-20
permalink: /:categories/:title
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
- Similar dataset [The Pile (diverse 800GB text dataset)](https://pile.eleuther.ai/)
- Google SafeSearch filter
- Licence is private.
- Dataset is composed of subsets: web, Github, news, Wikipedia, Books, [C4 (web-text)](https://arxiv.org/abs/1910.10683)
- Dataset language composition: 99% English, then 10 other languages.
- Dataset is as of 2022-03-20 *private*.

![MassiveText non-english composition](/images/massivetext-non-english-composition.png)

## Related Papers
- [DeepMind's RETRO Transformer used multi-lingual version of the dataset](/ml/DeepMinds-RETRO-Transformer-Model)
- [DeepMind's Gopher used only english version of the dataset](https://storage.googleapis.com/deepmind-media/research/language-research/Training%20Gopher.pdf)