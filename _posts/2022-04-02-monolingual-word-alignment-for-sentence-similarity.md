---
title: Word Alignment for Sentence Similarity
description: Semantic similarity increases with similar semantic units of similar semantic contexts in the monolingual word alignment.
layout: post
categories: ml
image: /images/word-alignment-for-sentence-similarity-thumb.png
video: sb8qJ5XVGP4
date: 2022-04-02
permalink: /:categories/:title
my_related_post_paths:
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
---



{% include load_video.html %}

In 2015, LSTM wasn't widely used and [Transformer](/ml/transformers-self-attention-mechanism-simplified) haven't existed yet.
How people even did their sentence similarity back then?
This post is about application of word alignment to semantic similarity.
It is about a super simple word aligner based solely on dependency parsing and a word database that achieved 1st place in 2014, 5th in 2015, in SemEval STS
In 2017, the aligner itself dropped to 10th place, but it still lived on as a subsystem in the winning system in an autoencoder system and other spots are taken by LSTM models.

- The monolingual aligner paper: [Back to Basics for Monolingual Alignment (2014)](https://aclanthology.org/Q14-1018.pdf)
- The aligner-based sentence similarity paper: [DLS@CU](https://aclanthology.org/S14-2039.pdf)
- The aligner source: [Sultan et al. 2014 aligner source code](https://github.com/ma-sultan/monolingual-word-aligner)
- State-of-the-art 2014 on sentence word alignment task
- Winner (DSL-CU) of [SemEval 2014 STS (sentence similarity)](https://aclanthology.org/S14-2010.pdf), [results only](https://alt.qcri.org/semeval2014/task10/index.php?id=results)
- Fifth place in [SemEval 2015 STS](https://aclanthology.org/S15-2045.pdf) - [2020 overview of the sentence similarity evolution](https://arxiv.org/pdf/2004.13820.pdf)


## Word Alignment
In word alignment we have two similar sentences and look for a correspondence mapping between the words that correspond to the same meaning within the context.
To evaluate this task we need to have labelled corpus.
Word alignment task is related to [word movers distance (read more)](/ml/Word-Movers-Embedding-Cheap-WMD-For-Documents),
in that both first map between the words, but alignment has to be zero-or-one while in case of WMD we can distribute the word weights in a fuzzy way.

{% include image.html src="/images/dataset-MSR-Brockett-2007.png" alt="word alignment example" %}

## Word Alignment vs Semantic Similarity
In 2015, top positions in sentence similarity task were occupied by corpus-based word-alignment models that used simple algorithms together with word databases or word embeddings e.g. word2vec.
How word alignment relates to semantic similarity?
Semantic similarity increases with similar semantic units of similar semantic contexts in the word alignment.

Now, to say how similar word-aligned sentences are, we need to calculate the similarity score.
The score for similarity of sentence A to sentence B is a fraction of aligned words divided by number of words in sentence A.
This measure is made symmetric by taking harmonic mean of both directions.
Stop word alignment is not used for sentence similarity task.

But, how to align the words?

 
## The Sultan 2014 Aligner Algorithm
{% include image.html src="/images/word-alignment.png" alt="alignment pipeline diagram" %}

In each step below we increasingly align more words: 
1. align identical word sequences (high precision)
1. align named entities before other content words to enable alignment of entity mentions of different lengths
1. align similar words with similar dependency-tree context (higher precision then the next step)
1. align similar word with similar with 3 to the left and 3 to the right
1. align stop words depending on existing content word alignments


### Identical Word Sequences
Aligning identical words in sequences of length `n` containing at least one content word.
This simple heuristic demonstrates a high precision (≈ 97%) on the MSR alignment dev set for `n ≥ 2`

### Named Entities
The algorithm uses GNU licenced [Stanford Named Entity Recognizer (Finkel et al., 2005)](https://nlp.stanford.edu/software/CRF-NER.html) to align all first character acronyms in the texts.

### Content Words
- word similarity: via [Paraphrase Database (PPDB)](https://aclanthology.org/P15-2070.pdf)
- exact word or lemma match, returns similarity score of `1`
- if found as match in the PPDB, returns a similarity score `ppdbSim=0.9`
  - a tuned parameter `0 <= ppdbSim <= 1`

### Dependency-based Alignment Process

{% include image.html src="/images/syntactic-dependencies-for-similarity.png" alt="Dependency-based Alignment Process" %}

Dependency context alignment is limited by accuracy of the dependency parser.
Without the dependency alignment the model performed almost the same (see ablations).
To align the dependency context, the dependency types were aligned custom lists to only find similar syntactic patterns.

Operation:
- for each potentially alignable pair, the dependency-based context is extracted, and context similarity is calculated as the sum of the word similarities of the context word pairs
- alignment score a weighted sum of word similarity and contextual similarity
- then aligns pairs with non-zero evidence in decreasing order of this score (greedy)


### Alignment Based on Similarities in The Textual Neighborhood
- extract the context, which is a set of neigh-boring content word pairs (3 left, 3 right)
- The contextual similarity is the sum of the similarities of these pairs
- the alignment score is a weighted sum of word similarity and contextual similarity
- The alignment score is then used to make one-to-one word alignment decisions


## Datasets

- [MSR Brockett 2007 Corpus (aligned sentences)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-77.pdf):
 
{% include image.html src="/images/dataset-MSR-Brockett-2007-2.png" alt="MSR Brockett 2007 Corpus example" %}

- SemEval 2014 STS [SemEval 2014 STS (sentence similarity)](https://aclanthology.org/S14-2010.pdf):
 
{% include image.html src="/images/semeval-2014-sts-task-10-dataset-examples.png" alt="semeval 2014 sts task 10 dataset examples" %}

## Results
- state-of-the-art 2014 on word alignment
 
{% include image.html src="/images/word-alignment-for-sentence-similarity-results.png" alt="Monolingual Word Alignment for Sentence Similarity results" %}


Winner of SemEval 2014 STS [SemEval 2014 STS (sentence similarity)](https://aclanthology.org/S14-2010.pdf):

{% include image.html src="/images/semeval-2014-sts-results.png" alt="SemEval 2014 STS (sentence similarity) results" %}

Winner of [SemEval 2015 STS](https://aclanthology.org/S15-2045.pdf) (DLS@CU-S1) with pearson mean result of 0.8015.
While Word Mover's Embeddings paper gets 64.2. 

Unfortunately for the other papers spearman correlation is used. So they are not directly comparable.
[SentenceBert achieved 0.8099](https://arxiv.org/pdf/1908.10084.pdf). Top score as of writing is [0.8863 from Trans-Encoder-RoBERTa-large-cross](https://arxiv.org/pdf/2109.13059v4.pdf).
