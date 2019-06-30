---
layout: post
title: "FastText Vector Norm And OOV Words"
date: 2019-06-30
---

![standard_norm-tf](https://raw.githubusercontent.com/vackosar/fasttext-vector-norms-and-oov-words/master/results/standard_norm-tf.png)

I had a look at norms of FastText embeddings and written paper-like formatted post. [Full post and code is here](https://github.com/vackosar/fasttext-vector-norms-and-oov-words/blob/master/README.md).

#### Abstract

Word embeddings, trained on large unlabeled corpora are useful for many natural language processing tasks. FastText model introduced in [(Bojanowski et al., 2016)](https://arxiv.org/abs/1607.04606) in contrast to Word2vec model accounts for sub-word information by embedding also sub-word n-grams. FastText word representation is whole word vector plus sum of n-grams contained in it.
Word2vec vector norms have been show in [(Schakel & Wilson, 2015)](http://arxiv.org/abs/1508.02297) to be correlated to word significance. This blog post visualize vector norms of FastText embedding and evaluates use of FastText word vector norm multiplied with number of word n-grams for detecting non-english OOV words.


