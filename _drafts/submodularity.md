---
layout: post
title: "Submodularity TODO"
date: 2021-01-19
categories: ml
description: TODO
permalink: /:categories/:title
---

[comment]: <> (image: /images/transformer-feed-forward.png)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


### Submodular function

A submodular function is a set function whose value, has the property that the difference in the incremental value of the function that a single element makes when added to an input set decreases as the size of the input set increases.

<div>
\( A \subset B \), 
\(x \notin B \),
\( F(\lbrace x \rbrace \cup A) - F(A) \geq F(\lbrace x \rbrace \cup B) - F(B) \)
</div>
<br>

We encounter this property during shopping in form of quantity discount.
The discount of addition of on more item to the purchase cart, decreases with the size of the cart.
This priciple is called diminishing returns.

Submodular functions appear also in maximization problems where they model notions of diversity, information and coverage.
For example one would like a document summary to cover all important and relevant concepts in the document,
but avoid topic repetition at the same time as repeating a fact has a diminishing return.

[Submodular functions can be seen as discrete convexity](https://web.cs.elte.hu/~lovasz/scans/submodular.pdf) e.g.
- polynomial time algo for finding minimum-set.
- for non-negative submodular function with budget (each element has a cost) maximum-set is approximable with polynomial time greedy algorithm
- Submodular functions can be combined, and the resulting function is still submodular.


### Maximum-Marginal-Relevance
[Maximum-Marginal-Relevance for re-ranking (1998)](https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf)
reduces the redundancy of query results while at the same time maintaining query relevance of results for already ranked documents or phrases.
Greedy algoritm which makes trade-off between relevance and diversity.

- V = set of documents
- S = Subset of documents in V already selected
- \\( \lambda \\) = Constant in range [ 0–1 ], for diversification of results

<div>
\( \mathrm{nextDoc} = \)
\( \mathrm{argmax}_{i \in V \setminus S } ( \lambda \mathrm{sim}_1 (i, Q) - (1 - \lambda) \mathrm{max}_{j \in S} \mathrm{sim}_2 (i, j)) \),
</div>
<br>



### Summarization as Submodularity Maximization

[Multi-document Summarization via Budgeted Maximization of Submodular Functions](https://www.aclweb.org/anthology/N10-1134.pdf)
formulates summarization as the problem of maximizing a submodular function under budget constraint,
where \\( V \\) is set of all sentences, \\( S \\) are selected sentences, \\( c_i \\) is word count, \\( f \\) is submodular function, \\( K \\) is the word budget, then:

\\( \max_{S \subset V} f(S) : \sum_{i \in S} c_i \leq K \\)


The paper proposes MMR alternative that is submodular if the similarity is non-negative:

\\( f = \sum_{i \in V \setminus S} \sum_{j \in S} \mathrm{sim}(i,j) - \lambda \sum_{i,j \in S: i \neq j} \mathrm{sim}(i,j) \\)

For which they present greedy algorithm with near-optimality guarantee. The algo repeatedely finds documents maximizing:

\\( \mathrm{nextDoc} = \mathrm{argmax_i} \frac{f(G \cup \lbrace i \rbrace) - f(G)}{c_i^r} \\)

until the budget is reached. The algo Details are presented in [the paper](https://www.aclweb.org/anthology/N10-1134.pdf).

How is this related exactly to the MMR? If the costs for each item is the same e.g. \\( c_i = 1 \\), then we get:

<div>
\(  f(S \cup \lbrace k \rbrace ) - f(S) = \)
\(  \sum_{i \in V \setminus \lbrace k \rbrace} \mathrm{sim} (i, k) - 2 \lambda \sum_{i \in S} \mathrm{sim}(i, k) \).
</div>
TODO double check above.

Where the first element corresponds to the sentence's centrality,
and the second element to the sentence dissimilarity to the already selected sentences.
Above equation is very much like the Maximum-Marginal-Relevance equation.

The cost \\( c_k \\), can then be added back to rescale according to the sentence length.

Above setup with idf-modified-cosine similarity matrix achieved SoTA outperforming PageRank based centrality summarization algorithms like [LexRank](https://arxiv.org/pdf/1109.2128.pdf).
LexRank applies PageRank to the idf-modified-cosine similarity matrix to get the centrality scores for the sentences.
The LexRank paper mentions use MMR as a re-ranker, making the comparison with the submodularity solution fair.


### Wiki-Topic Hierarchies Notes TODO

[Summarization of Multi-Document Topic Hierarchies using Submodular Mixtures (2015)](https://www.aclweb.org/anthology/P15-1054.pdf)
suggested generating Wikipedia disambiguation pages using combination of search and summarization.

Given a DAG-structured topic hierarchy and asubset of objects, we investigate the problem offinding a subset of DAG-structured topics that areinduced by that subset (of objects).
summarize such large sets of labels into a smaller and more meaningful label sets usinga DAG-structured topic hierarchy
finding the most representa-tive subset of topic nodes from a DAG-Structuredtopic hierarchy. We argue that many formulationsof this problem are natural instances of submodularmaximization, and provide a learning frameworkto create submodular mixtures to solve this prob-lem.

- Given a (ground set) collection V of topics organized into DAG
- Collection of D documents associated with one or more topics
- K topics
- Transitive cover \\( C(t) \\) = all subtopics of t, truncated \\( C^\alpha \\) where path cannot be longer than \\( \alpha \\)
- Set of categories \\( S \\)

We solve:

<div>
\( \mathrm{argmax}_{S \subset V : |S| \leq K} \sum_i \omega_i f_i(S) \)
</div>
where \\( f_i \\) are monotone submodule mixture components, \\( \omega_i \geq 0 \\) are associated weights.

- Weighted set cover function \\( f(S) = \sum_d \omega_d  \\) with weights based on relative importance.
- topic specificity - distance from root
- topic clarity: fraction of descendats that cover one or more docs
- topic relevance: min number of hops needed

They do small modifications and combine these losses into single submodularity optimizing loss function?


### Submodularity and Self-Attention

The paper [Resurrecting Submodularity for Neural Text Generation](https://arxiv.org/abs/1911.03014) optimizes summarization and translation coverage with diminishing attentions with submodular functions.

The neural encoder-decoder summarizers trained end-to-end suffer from repetition and insufficient information coverage.
Mechanism to improve coverage by adding coverage requirements into the loss.
The paper introduces instead modifies to the attentions using the priciple of diminishing returns using submodular function.
No additional modification to the loss function or extra params are needed.

[comment]: <> (At each decoding step for one self-attention head there is single attention vector which is used for the next token prediction.)
Given decoder step (position) \\( t \\),
encoder sequence position \\( i \\),
attention matrix \\( a_{i, t} \\),
concave non-decreasing function \\( F \\) with \\( F(0) = 0 \\) e.g. ,
then diminishing attention is defined as:

\\( DimAtt_{i,t} = F(\sum_{\tau = 0}^{t} a_{i, \tau}) - F(\sum_{\tau = 0}^{t - 1} a_{i, \tau}) \\)


This relatively increases attention to part not used for decoding in previous steps.

Slighly improved approach call Dynamic Dimishing Attention then achived SoTA when used in models Pointer-Generator and BART models.


<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        alt="Results of diminishing attention"
        src="/images/diminishing-attention.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Results of diminishing attention (<a href="https://arxiv.org/abs/1911.03014">source</a>) 
    </figcaption>
</figure>
