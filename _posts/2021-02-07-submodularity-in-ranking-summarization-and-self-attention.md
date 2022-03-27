---
layout: post
title: "Submodularity in Ranking, Summarization, and Self-attention"
date: 2021-02-07
categories: ml
description: Diminishing returns with a budget constraint in problems of coverage and results diversification.
permalink: /:categories/:title
image: /images/submodularity-main.png
video: fLAYeDYqhag
---

{% include mathjax.html %}
{% include load_video.html %}


### Submodular function models diminishing returns

A submodular function is a set function whose value, has the property that the difference in the incremental value of the function that a single element makes when added to an input set decreases as the size of the input set increases.

<div>
\( S_1 \subset S_2 \), 
\(i \notin S_2 \),
\( F(\lbrace i \rbrace \cup S_1) - F(S_1) \geq F(\lbrace i \rbrace \cup S_2) - F(S_2) \)
</div>
<br>

We encounter this property during shopping in form of quantity discount.
The discount of addition of on more item to the purchase cart, decreases with the size of the cart.
This priciple is called diminishing returns.

For example the price per product price as a function of set of purchased products \\( S \\) could be dependent on the product count \\( \| S \| \\). 
From following, we then observe diminishing discount of adding an extra product into the cart.

<div>
  \( \mathrm{price}(S) = \exp(-|S|) \)<br>

  \( S_1 \subset S_2 \implies | S_1 | \leq | S_2 | \)<br>

  \( \mathrm{price}(S_1 + \lbrace x \rbrace) - \mathrm{price}(S_1) \geq \)
  \( \mathrm{price}(S_2 + \lbrace x \rbrace) - \mathrm{price}(S_2) \),<br>
  because
  \( \exp(- | S_1 | )(e^{-1} - 1) \geq \exp(- | S_2 | )(e^{-1} - 1) \)
</div>
<br>

Submodular functions appear also in maximization problems where they model notions of diversity, information and coverage.
For example one would like a document summary to cover all important and relevant concepts in the document,
but avoid topic repetition at the same time as repeating a fact has a diminishing return.

[Submodular functions can be seen as discrete convexity](https://web.cs.elte.hu/~lovasz/scans/submodular.pdf) e.g.
- polynomial time algo for finding minimum-set.
- for non-negative submodular function maximum-set under a budget constraint is approximable with polynomial time greedy algorithm 
- Submodular functions can be combined, and the resulting function is still submodular.


### Maximum-Marginal-Relevance re-ranks for diversity of results
[Maximum-Marginal-Relevance for re-ranking (1998)](https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf)
trades off redundancy of query results for small decrease relevance of results for already ranked documents or phrases.
It make the trade off using the following greedy algorithm.

- \\( V \\) = a set of documents
- \\( S \\) = a subset of documents in V already selected
- \\( \lambda \\) = a constant in range of \\( ( 0, 1 ) \\) 

<div>
\( \mathrm{nextDoc}(S) = \)
\( \mathrm{argmax}_{i \in V \setminus S } ( \lambda \mathrm{sim}_1 (i, Q) - (1 - \lambda) \mathrm{max}_{j \in S} \mathrm{sim}_2 (i, j)) \),
</div>

- The first part of equation growths with document similarity with the query.
- The second part decreases with the document similarity with already selected documents.



### Summarization as budgeted submodularity maximization

[Multi-document Summarization via Budgeted Maximization of Submodular Functions](https://www.aclweb.org/anthology/N10-1134.pdf)
formulates summarization as the problem of maximizing a submodular function under a budget constraint,
where \\( V \\) is set of all sentences, \\( S \\) are selected sentences, \\( c_i \\) is word count, \\( f \\) is submodular function, \\( B \\) is the word budget, then:

\\( S_{max} = \max_{S \subset V} f(S) : \sum_{i \in S} c_i \leq B \\)


The paper proposes MMR alternative that is submodular if the similarity is non-negative:

\\( f = \sum_{i \in V \setminus S} \sum_{j \in S} \mathrm{sim}(i,j) - \lambda \sum_{i,j \in S: i \neq j} \mathrm{sim}(i,j) \\)

- The first part grows as selected sentences \\( S \\) become more similar to all sentences \\( V \\).
- The second part decreases as selected sentences become more similar between each other.

For which they present greedy algorithm with near-optimality guarantee. The algo repeatedely finds documents maximizing:

\\( \mathrm{nextDoc}(S) = \mathrm{argmax_i} \frac{f(S \cup \lbrace i \rbrace) - f(S)}{c_i^r} \\)

until the budget is reached. The algo Details are presented in [the paper](https://www.aclweb.org/anthology/N10-1134.pdf).

How is this related exactly to the MMR? If the costs for each item is the same e.g. \\( c_i = 1 \\), then we get:

<div>
\(  f(S \cup \lbrace k \rbrace ) - f(S) = \)
\(  \sum_{i \in V \setminus \lbrace k \rbrace} \mathrm{sim} (i, k) - 2 (1 + \lambda) \sum_{i \in S} \mathrm{sim}(i, k) \).
</div>
<br>

<div style="font-size: 10px">
  <b>Proof:</b>

  <div>
  \( f_1 := \sum_{i \in V \setminus S, j \in S } \mathrm{sim} (i, j) \),<br>

  \( f_1(S \cup \lbrace k \rbrace ) - f_1(S) = - \sum_{j \in S} \mathrm{sim}(k, j) + \sum_{i \in V \setminus (S \cup \lbrace k \rbrace )} \mathrm{sim}(i, k) = \)
  \( \sum_{j \in V \setminus \lbrace k \rbrace} \mathrm{sim}(k, j) - 2 \sum_{j \in S} \mathrm{sim}(k, j) \)
  <br>

  \( f_2 := \sum_{i,j \in S : i \neq j } \mathrm{sim} (i, j) \),<br>

  \( f_2(S \cup \lbrace k \rbrace )  - f_2(S) = 2 \sum_{j \in S} sim(k, j) \),<br>

  \( f = f_1 - \lambda f_2 \)

  </div>

</div>
<br>

The equation is very much like the Maximum-Marginal-Relevance equation, except \\( \lambda \\) the diversity term has always non-zero weight.
The cost \\( c_k \\), can then be added back to rescale according to the sentence length.

- The first part grows with the sentence \\(k \\) similarity to all sentences in \\( V \\) i.e. with sentence centrality in the whole document.
- The second part decreases with sentence similarity to the already selected sentences.

This setup with idf-modified-cosine similarity matrix achieved SoTA outperforming PageRank based centrality summarization algorithms like [LexRank](https://arxiv.org/pdf/1109.2128.pdf).
LexRank applies PageRank to the idf-modified-cosine similarity matrix to get the centrality scores for the sentences.
The LexRank paper mentions use MMR as a re-ranker, making the comparison with the submodularity solution fair.


### Wiki term disambiguation for wiki using topic hierarchy coverage

[Summarization of Multi-Document Topic Hierarchies using Submodular Mixtures (2015)](https://www.aclweb.org/anthology/P15-1054.pdf)
suggested generating Wikipedia disambiguation pages using custom crafted submodularity function maximizing disambiguation topics specificity, clarity, relevance, and more.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Wiki disambiguation problem and submodularity"
        data-src="/images/submodularity-wiki-disambiguation.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Wiki disambiguation problem and submodularity (<a href="https://www.aclweb.org/anthology/P15-1054.pdf">source</a>) 
    </figcaption>
</figure>

Wiki articleas are organized into a topic hierarchy. The article looks for the best small subset of topics for an informative disambiguation page.
The submodular function is constructed as optimal linear combination of multiple hand-constructed submodular functions.

- \\( V \\) all topics organized into a hierarchy
- Collection of D documents associated with one or more topics
- \\( S \\) selected topics 
- \\( B \\) topic count budget
- \\( f_i \\) custom monotone submodular functions for selection of the best topics. For example:
    - Weighted set cover function \\( f(S) = \sum_d \omega_d  \\) with weights based on relative importance.
    - topic specificity - distance from root
    - topic clarity: fraction of descendats that cover one or more docs
    - topic relevance: min number of hops needed
- \\( \omega_i \geq 0 \\) the best linear combination of the custom functions

We solve:

<div>
\( S_{best} = \mathrm{argmax}_{S \subset V : |S| \leq B} \sum_i \omega_i f_i(S) \)
</div>
<br>


### Diminishing self-attention improves summarization coverage

The paper [Resurrecting Submodularity for Neural Text Generation](https://arxiv.org/abs/1911.03014) optimizes summarization and translation coverage with diminishing attentions with submodular functions.

End-to-end trained neural encoder-decoder summarizers suffer from repetition and insufficient information coverage.
Previous papers added coverage requirements into the loss.
This paper instead modifies the attention weights using the principle of diminishing returns using a submodular function.

[comment]: <> (At each decoding step for one self-attention head there is single attention vector which is used for the next token prediction.)
Given decoder step (position) \\( t \\),
encoder sequence position \\( i \\),
attention matrix \\( a_{i, t} \\),
concave non-decreasing function \\( F \\) with \\( F(0) = 0 \\) e.g. ,
then diminishing attention is defined as:

\\( DimAtt_{i,t} = F(\sum_{\tau = 0}^{t} a_{i, \tau}) - F(\sum_{\tau = 0}^{t - 1} a_{i, \tau}) \\)


<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Diminishing attention via submodularity"
        data-src="/images/submodularity-diminishing-attention.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Diminishing attention via submodularity (<a href="https://arxiv.org/abs/1911.03014">source</a>) 
    </figcaption>
</figure>


This relatively increases attention to the parts of input text that were not yet used for decoding.
With a slightly more sofisticated approach they call "Dynamic Dimishing Attention" they then achive SoTA
with underlying summarization models Pointer-Generator and BART ([BERT](/ml/transformers-self-attention-mechanism-simplified)-based model).


<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Results of diminishing attention"
        data-src="/images/diminishing-attention.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Results of diminishing attention (<a href="https://arxiv.org/abs/1911.03014">source</a>) 
    </figcaption>
</figure>


## Meet Other ML Enthusiasts One-on-One Online

Video-call each week an interesting person in the machine learning field and break out of your remote isolation.
Network One-on-One Around Your Online Village with RandomMeets.

<a class="btn btn-info" style="text-decoration: none;" href="https://randommeets.com/invite/eyJncm91cF9pZCI6IjZhMzNkMTVjLTc0NjItNGFhMS1hNTc0LWM1NTUwMWQ4NWNkZiJ9.X76oug.2563ghpMTzbST9KPHerGeDqhXRY">
    Join Machine Learning @ RandomMeets
</a>
