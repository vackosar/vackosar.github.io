---
layout: post
title: "Submodularity TODO"
date: 2021-01-02
categories: ml
description: TODO
permalink: /:categories/:title
---

[comment]: <> (image: /images/transformer-feed-forward.png)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


# Submodular function

A submodular function is a set function whose value, has the property that the difference in the incremental value of the function that a single element makes when added to an input set decreases as the size of the input set increases. Submodular functions model diminishing returns like costs of items. There is often a larger discount, with an increase in the items one buys. In maximization problems, they model notions of diversity, information and coverage.

<div>
\( x \notin A \subset B \), 
\( F(\lbrace x \rbrace \cup A) - F(A) \geq F(\lbrace x \rbrace \cup B) - F(B) \)
</div>

For example, in document summarization, one would like the summary to cover all important and relevant concepts in the document.

[Maximum-Marginal-Relevance for re-ranking (1998)](https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf) tries to reduce the redundancy of results while at the same time maintaining query relevance of results for already ranked documents or phrases.

<div>
\( \mathrm{mmr} = \)
\( \mathrm{argmax}_{i \in R \setminus S } ( \lambda \mathrm{sim} (D_i, Q) - (1 - \lambda) \mathrm{max}_{j \in S} \mathrm{sim} (D_i, D_j)) \),
</div>

where \\( R \setminus S \\) are unselected documents
- D = Set of documents related to Query Q 
- S = Subset of documents in R already selected 
- R\S = set of unselected documents in R 
- \\( \lambda \\) = Constant in range [0–1], for diversification of results

Submodular functions can be efficiently combined together, and the resulting function is still submodular.

Very efficient algorithms for optimization. For example, a simple greedy algorithm admits a constant factor guarantee

[Summarization of Multi-Document Topic Hierarchies using Submodular Mixtures (2015)](https://www.aclweb.org/anthology/P15-1054.pdf)
suggested generating Wikipedia disambiguation pages using combination of search and summarization.

Given a DAG-structured topic hierarchy and asubset of objects, we investigate the problem offinding a subset of DAG-structured topics that areinduced by that subset (of objects).
summarize such large sets of labels into a smaller and more meaningful label sets usinga DAG-structured topic hierarchy
finding the most representa-tive subset of topic nodes from a DAG-Structuredtopic hierarchy. We argue that many formulationsof this problem are natural instances of submodularmaximization, and provide a learning frameworkto create submodular mixtures to solve this prob-lem.