---
title: Understand Large Language Models like ChatGPT
description: In 9 slides from TF-IDF, Word2vec, knowledge graphs, and transformers to LLMs and ChatGPT basics explained.
layout: post
categories: ml
image: /images/man-talking-to-a-big-robot-head-small.png
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2023-06-11
video: Jo-IQjdFfnw
redirect_from:
- /ml/how-computers-understood-humans
my_related_post_paths:
- _posts/2023-06-08-Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2023-03-24-Symbolic-vs-Connectionist-Machine-Learning.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
---



{% include load_video.html %}

The presentation explains the development of **large language models like ChatGPT**, which can generate text by predicting input text continuation. The idea of a talking machine has been around since the 1700s, but it wasn't until the development of **powerful computers and computer science** that it became a reality. Simple document representations, such as **counting word occurrences**, were used to create [sparse matrices](/ml/sparse-matrix-why-and-when) as feature vectors in methods like **term frequency–inverse document frequency and latent semantic analysis**. Non-contextual word vectors were created using **word2vec**, which trained embeddings to sum up close to the middle word vector. Later, **contextual word vectors** were created using [transformer architecture](/ml/transformers-self-attention-mechanism-simplified), which consumes the entire input sequence and is state-of-the-art in 2022.



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

{% include image.html src="/images/2001-A-Space-Odyssey-HAL-9000-Interface-3.png" alt="2001 A Space Odyssey HAL-9000 Interface" %}


{% include shared_slides/representations.md %}


## Large Language Models
- generate by predicting input text continuation
- $10M transformers trained on large amount of text from the internet in 2022
- can solve wide variety of problems like explaining jokes, sometimes with human level performance
- examples: [PaLM (2022)](/ml/googles-pathways-language-model-and-chain-of-thought), [RETRO (2021)](/ml/DeepMinds-RETRO-Transformer-Model), [hybrids with algorithms](/ml/Symbolic-vs-Connectionist-Machine-Learning)
- ChatGPT additionally trained to chat using [RLHF alignment method](https://arxiv.org/abs/2009.01325)

{% include image.html src="/images/transformer-from-word2vec-next-token.jpg" alt="transformer next token prediction" %}



## Future: Hybridizing Text with Algorithms
- ChatGPT and other Large Language Models hallucinate despite alignment with [RLHF](https://arxiv.org/abs/2009.01325)
- If neural network has a intuition, what is repetition, search, self-reflection?
- Read more about [reasoning without hallucinations hybridizing neural networks with code](/ml/Symbolic-vs-Connectionist-Machine-Learning)
- Also: [understanding image and text regardless of a language](/ml/Multimodal-Image-Text-Classification)


{% include image.html src="/images/hybrid-symbolic-connectionist-papers.png" alt="hybridizing neural networks with code" %}



## Instructing ChatGPT and Large Language Models
- [Prompting is asking the LLMs right questions](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM)
- [Common prompting techniques](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM): being specific, provide examples, allow thinking step by step, self-reflecting
- Use cases: question answering, coding, form filling, data schema extraction, knowledge graph construction 

{% include image.html src="/images/palm-chain-of-though-prompting.png" alt="chain-of-thought prompting technique" %}