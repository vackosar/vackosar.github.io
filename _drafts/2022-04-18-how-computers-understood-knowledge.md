---
title: "How Computers Understood Humans"
description: "Introduction into deep natural language processing of 2022"
layout: post
categories: ml
date: 2022-04-18
permalink: /:categories/:title
last_modified_at: 2022-04-19
---

- instruct computer to perform tasks
- input and output interface
- represent knowledge in computers
- execute "thinking" process

<i style="color: blue">
by his contrivance, the most ignorant person, at a reasonable charge, and with a little bodily labour, might write books in philosophy, poetry, politics, laws, mathematics, and theology, without the least assistance from genius or study.
... He then commanded six-and-thirty of the lads, to read the several lines softly, as they appeared upon the frame; and where they found three or four words together that might make part of a sentence
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
- in ~1995 page rank counting links between documents

![Latent semantic analysis Wikipeadia](/images/latent-semantic-analysis-wiki.png)


## Non-Contextual Words Vectors
- vector is point in a multidimensional space
  - an array of numbers
- non-contextual word vectors:
- vocabulary 10k words
- count or train gradient based methods two vectors per word

![word2vec](/images/word2vec-10k-tensorflow-projector.png)


## Contextual Word Vectors
- word meaning based on context
- knowledge graph
- transformer architecture

![stars cosmos Hubble (NASA, ESA, Anton M. Koekemoer (STScI), Nick Scoville (Caltech))](/images/stars-cosmos.png)


- in a vocabulary
- counting methods
- gradient methods
- vector methods
  - Tao te Ching - every positive thought negative - direction and anti direction
- RNNs
- Transformers
- knowledge graph - what is knowledge
  - wikipedia is knowledge graph
  - knowledge graph is between database and training data samples
- softmax forces to make a decision, a collapse
- projection and subspaces
- last 230 iq person

- few shot vs zero shot?