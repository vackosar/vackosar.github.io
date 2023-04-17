---
title: Understand Large Language Models like ChatGPT
description: In 7 slides from TF-IDF, Word2vec, knowledge graphs, and transformers to LLMs and ChatGPT basics explained.
layout: post
categories: ml
image: /images/how-computers-understood-humans-thumb.png
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2023-04-17
video: Jo-IQjdFfnw
redirect_from:
- /ml/how-computers-understood-humans
my_related_post_paths:
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2020-05-08-starspace-embedding.md
---



{% include load_video.html %}



## Dream of a Talking Machine
- Idea of a talking machine since 1700s, but weak computers and computer science
- ChatGPT does almost what was predicted, but how?
- How to instruct large language model to perform tasks?
- How represent knowledge in computers?
- How to generate the answers?

<p style="color: blue">
by his contrivance, the most ignorant person, at a reasonable charge, and with a little bodily labour, <b>might write books</b> in philosophy, poetry, politics, laws, mathematics, and theology, without the least assistance from genius or study.
... <b>to read the several lines softly, as they appeared upon the frame</b>
(Gulliver's Travels, by Jonathan Swift 1726, making fun of <a href="https://www.researchgate.net/publication/221502602_Llull_as_Computer_Scientist_or_Why_Llull_Was_One_of_Us">Ramon Llull 1232</a>)
</p>


## Text Prompt as an Interface
- For example 2001: A Space Odyssey HAL 9000
- input textual instructions e.g. explain a riddle
- based on its knowledge computer generates the answer text 

![2001 A Space Odyssey HAL-9000 Interface](/images/2001-A-Space-Odyssey-HAL-9000-Interface-3.png)


{% include shared_slides/representations.md %}


## Large Language Models
- generate by predicting input text continuation
- $10M transformers trained on large amount of text from the internet in 2022
- can solve wide variety of problems like explaining jokes, sometimes with human level performance
- examples: [PaLM (2022)](/ml/googles-pathways-language-model-and-chain-of-thought), [RETRO (2021)](/ml/DeepMinds-RETRO-Transformer-Model), [hybrids with algorithms](/ml/Symbolic-vs-Connectionist-Machine-Learning), ChatGPT ...

![transformer next token prediction](/images/transformer-from-word2vec-next-token.jpg)


## Future: Hybridizing Text with Algorithms
- ChatGPT and other Large Language Models hallucinate.
- If neural network has a intuition, what is repetition, search, self-reflection?
- Read more about [reasoning without hallucinations hybridizing neural networks with code](/ml/Symbolic-vs-Connectionist-Machine-Learning)
- Also: [understanding image and text regardless of a language](/ml/Multimodal-Image-Text-Classification)


![hybridizing neural networks with code](/images/hybrid-symbolic-connectionist-papers.png)