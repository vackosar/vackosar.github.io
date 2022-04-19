---
title: "How Computers Understood Humans"
description: "Introduction into deep natural language processing of 2022"
layout: post
categories: ml
image: /images/gullivers-travels-swift.png
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2022-04-19
---

- instruct computer to perform tasks
- input and output interface
- represent knowledge in computers
- execute "thinking" process

<i style="color: blue">
by his contrivance, the most ignorant person, at a reasonable charge, and with a little bodily labour, <b>might write books</b> in philosophy, poetry, politics, laws, mathematics, and theology, without the least assistance from genius or study.
... He then commanded six-and-thirty of the lads, to read the several lines softly, as they appeared upon the frame; and where they found three or four <b>words together that might make part of a sentence</b>
(Gulliver's Travels, by Jonathan Swift 1726, making fun of [Ramon Llull 1232](https://www.researchgate.net/publication/221502602_Llull_as_Computer_Scientist_or_Why_Llull_Was_One_of_Us))
</i>

## Prompt as an Interface
- input textual instructions
- computer generates output based on its knowledge

![2001 A Space Odyssey HAL-9000 Interface](/images/2001-A-Space-Odyssey-HAL-9000-Interface-3.jpg)


## How To Represent Knowledge
- textual documents in a database
- counting word occurrences on documents level into [sparce matrices](/ml/sparse-matrix-why-and-when)
- methods: TF*IDF, Latent semantic analysis
- search by list of words (query) ~1970s

![Latent semantic analysis - CC BY-SA 4.0 Christoph Carl Kling](/images/latent-semantic-analysis-wiki.png)


## Non-Contextual Words Vectors
- each of 10k words gets one general vector
- vector is point in a multidimensional space - an array of numbers
- global (non) contextual word vectors - no disambiguation (flowering) vs fruit (food)

![word2vec](/images/word2vec-10k-tensorflow-projector.png)


## Word2vec
- count (GloVe) or train (word2vec - two vectors per word)
- word2vec (Mikolov 2013), or counting co-occurrence (GloVe)
- word strings should be just 

![word2vec operation](/images/word2vec.jpg)


## Contextual Word Vectors
- word meaning based on context
- recurrent neural networks (LSTM, GRU) - sequential with memory
- [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) (Vaswani 2017)
  - calculates on entire input sequence
   
![transformer from word2vec](/images/transformer-from-word2vec.jpg)


## Knowledge Graph's Nodes Are Disambiguated
- knowledge graph e.g. Wikidata: each node is specific fruit (flowering) vs fruit (food)
- imperfect tradeoff between database and training data samples
- Wikipedia and internet is between knowledge graph and set of documents
- random walk ~ valid "sentences", link prediction ~ generating text

![knowledge graph visualization from wikipedia](/images/knowledge-graph.jpg)