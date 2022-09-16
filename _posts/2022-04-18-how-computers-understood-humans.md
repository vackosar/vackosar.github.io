---
title: How Computers Understood Humans
description: Catch on with this 7-slide introduction to deep natural language processing of 2022, featuring TF-IDF, Word2vec, knowledge graphs, and transformers.
layout: post
categories: ml
image: /images/how-computers-understood-humans-thumb.png
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2022-05-21
video: Jo-IQjdFfnw
my_related_post_paths:
- _posts/2020-05-08-starspace-embedding.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
---



{% include load_video.html %}

- ideas existed at least since 1700s, but not enough compute and computer science
- Current computers do almost what was predicted, but how?
- How to instruct computer to perform tasks?
- How represent knowledge in computers?
- How to generate the answers?

<p style="color: blue">
by his contrivance, the most ignorant person, at a reasonable charge, and with a little bodily labour, <b>might write books</b> in philosophy, poetry, politics, laws, mathematics, and theology, without the least assistance from genius or study.
... <b>to read the several lines softly, as they appeared upon the frame</b>
(Gulliver's Travels, by Jonathan Swift 1726, making fun of <a href="https://www.researchgate.net/publication/221502602_Llull_as_Computer_Scientist_or_Why_Llull_Was_One_of_Us">Ramon Llull 1232</a>)
</p>


## Prompt as an Interface
- 2001: A Space Odyssey HAL 9000
- input textual instructions e.g. explain a riddle
- based on its knowledge computer generates the answer text 

![2001 A Space Odyssey HAL-9000 Interface](/images/2001-A-Space-Odyssey-HAL-9000-Interface-3.png)


{% include shared_slides/representations.md %}


## Big Transformer Models
- generate by predicting input text continuation
- $10M transformers trained on large amount of text from the internet in 2022
- can solve wide variety of problems like explaining jokes, sometimes with human level performance
- examples: [PaLM (2022)](/ml/googles-pathways-language-model-and-chain-of-thought), [RETRO (2021)](/ml/DeepMinds-RETRO-Transformer-Model), [GPT-3](https://arxiv.org/pdf/2005.14165.pdf), ...

![transformer next token prediction](/images/transformer-from-word2vec-next-token.jpg)
