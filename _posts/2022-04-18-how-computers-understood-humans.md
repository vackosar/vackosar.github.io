---
title: "How Computers Understood Humans"
description: "7-slide introduction into deep natural language processing of 2022 featuring TF-IDF, Word2vec, knowledge graphs, transformers"
layout: post
categories: ml
image: /images/how-computers-understood-humans-thumb.png
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2022-04-23
video: Jo-IQjdFfnw
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


## How To Represent Knowledge
- library ~> textual documents in a database
- search by list of words (query) ~1970s, find topics ~1980
- counting word occurrences on documents level into [sparce matrices](/ml/sparse-matrix-why-and-when)
- methods: TF*IDF, Latent semantic analysis

![Latent semantic analysis - CC BY-SA 4.0 Christoph Carl Kling](/images/latent-semantic-analysis-wiki.png)


## Non-Contextual Words Vectors
- document -> sentence or small running window of 10 words
- vector is point in a multidimensional space - an array of numbers
- each of 10k words gets one general vector in 300 dimensional space
- each vector has to fit in "only" 300 dimensions - much less than 10k words
- global (non) contextual word vectors - no disambiguation (flowering) vs fruit (food)

![word2vec](/images/word2vec-10k-tensorflow-projector.png)


## Word2vec: Word To a Global Vector
- count co-occurrence in a 10 word window [GloVe (Pennington 2014)](https://nlp.stanford.edu/pubs/glove.pdf)
- [word2vec (Mikolov 2013)](https://arxiv.org/pdf/1301.3781.pdf): 10 surrounding words sum close to the middle word vector
- words appearing in similar context are close in the 300 dimensional space
- disambiguation - word strings should be just name not an id!

![word2vec operation](/images/word2vec.jpg)


## Knowledge Graph's Nodes Are Disambiguated
- knowledge graph e.g. Wikidata: each node is specific fruit (flowering) vs fruit (food)
- imperfect tradeoff between database and training data samples
- Wikipedia and internet is between knowledge graph and set of documents
- random walk ~ valid "sentences", link prediction ~ generating text

![knowledge graph visualization from wikipedia](/images/knowledge-graph.jpg)


## Transformer: Contextual Word Vectors
- word meaning based on context of 100s of words.
- [recurrent neural networks (LSTM, GRU)](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) - sequential with memory
- [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) (Vaswani 2017)
  - calculates on entire input sequence

![transformer from word2vec](/images/transformer-from-word2vec.jpg)


## Big Transformer Models
- generate by predicting input text continuation
- $10M transformers trained on large amount of text from the internet in 2022
- can solve wide variety of problems like explaining jokes, sometimes with human level performance
- examples: [PaLM (2022)](/ml/googles-pathways-language-model-and-chain-of-thought), [RETRO (2021)](/ml/DeepMinds-RETRO-Transformer-Model), [GPT-3](https://arxiv.org/pdf/2005.14165.pdf), ...

![transformer next token prediction](/images/transformer-from-word2vec-next-token.jpg)
