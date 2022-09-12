---
layout: post
title: 'Word Mover''s Embedding: Cheap WMD For Documents'
date: 2020-06-19
categories: ml
description: What is Word Mover's Embedding for documents and how it approximates Word Mover's Distance between documents.
image: /images/word-movers-embedding.png
video: uuNLz6eT_tg
permalink: /:categories/:title
redirect_from:
- /ml/Word-Movers-Embedding
my_related_post_paths:
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
---



{% include mathjax.html %}
{% include load_video.html %}


Word Mover's Distance captures the semantic similarity between documents [more accurately than the cosine similarity between word vector averages](#word-movers-distance-vs-word-embedding-weighted-average-cosine-similarity). 
However, vanilla WMD has cubic computational complexity, which makes it impractical in many applications. How WMD works? Why is it so good? Is there any low complexity approximation of WMD?

### What is Earth Mover's Distance?

It is minimum amount of dirt multiplied by distance needed to transform one pile of dirt into another pile of dirt.

<img alt="Earth Mover's Distance is amount multiplied by distance." style="width: 90%; max-width: 500px" src="/images/earth-movers-distance.png">

Despite the earth in the name, better analogy is that of a transportation problem. 
Good example of transportation problem is cost optimization of transportation of gold ore from mines to refineries, where each refinery can accept only certain percentage of the ore.

Earth Movers Distance is also a distance metric between probability distributions.
So the problem above can be restated into following question. How to transform the this geographical distribution of gold ore to this geographical distribution for the least hauling cost?

Earth mover distance computational complexity is super-cubic as can be found in [Network Flows: Theory, Algorithms, and Applications](https://www.amazon.com/Network-Flows-Theory-Algorithms-Applications/dp/013617549X).
There are papers on approximating EMD with [quadratic complexity](http://proceedings.mlr.press/v37/kusnerb15.pdf) in general case and [linear complexity](http://proceedings.mlr.press/v97/atasu19a/atasu19a.pdf) in document search if pre-computation is allowed.

### Earth Movers Distance vs Optimal Transport

Earth movers distance differs from optimal transport in that optimal transport disallows splitting and summing of the transported amount at each point.
So optimal transport can be defined by only transforming the support of the distribution and often may not match the target distribution.


### What is Word Mover's Distance (WMD)?
Word Mover's Distance is like [Earth Movers Distance](#what-is-earth-movers-distance) but between text documents.
We use word vectors like for example Word2vec, [FastText](/ml/FastText-Vector-Norms-And-OOV-Words), or [StarSpace](/ml/starspace-embedding) embeddings.

- The probability distribution's
  - support is over word vectors of the document's words
  - value is normalized frequency of unique words in the document or TF-IDF
- The distance between word vectors can be [a cosine similarity ("Word Rotators Distance" argues for cosine similarity)](https://arxiv.org/pdf/2004.15003.pdf) or euclidean distance.

Word movers distance solves similar task to [word alignment](/ml/monolingual-word-alignment-for-sentence-similarity#word-alignment), but in word alignment the mapping is one-to-one.
Speculative reason for cosine similarity seems to be that [Word2vec (or FastText) vector norm behaves a bit like TF-IDF](/ml/FastText-Vector-Norms-And-OOV-Words#word2vec-vector-norms), but with document size of 10 words.
Since we want to use our TF-IDF and not the word2vec's, then we use cosine similarity.

### Word Mover's Distance vs Word Embedding Weighted Average Cosine Similarity

Cosine similarity is a way how to compare two vectors, which is especially useful in high dimensions, where euclidean distance does not give useful results.
Cosine similarity measures cosine of the angle between the two vectors, so maximum value is 1 and minimum is -1.
Cosine similarity is calculated as a dot-product of two normalized vectors.
In natural language processing, the cosine similarity can we used to compare embedding of two distinct words.

Word Embedding Weighted Average Embedding is a document vector calculated as frequency weighted average of word vectors (embeddings) in the document.
Using the resulting WEWA document vectors can be compared using cosine similarity.

<img alt="Average of two vectors." style="width: 90%; max-width: 300px" src="/images/vector-average.png">

We can compare Word Mover's Distance vs Cosine similarity of WEWA vectors 
- WMD uses more detailed information and captures move semantics than WEWA.
- WMD has much higher complexity of \\( O(L^3 \log(L)) \\) compared to WEWA's \\( O(L) \\), where \\( L \\) is document length.

### Word Mover's Distance vs BERT Similarity

It would be interesting to compare [BERT transformer model](/ml/transformers-self-attention-mechanism-simplified) sentence embedding computational complexity to WMD.
If I understand correctly, BERT is of linear complexity in the length of the document, although total running time may be still in many cases be longer for BERT.
[SentenceBert](https://arxiv.org/pdf/1908.10084.pdf) is simple model that is fine-tuned for sentence similarity task.
Its main embedding is created by averaging output sequence embeddings.

While direct comparison is not possible, results on [STS 15 for WMD](https://arxiv.org/pdf/2004.15003.pdf) of Pearson score 0.7161 indicate that SentenceBert with Spearman 0.8185 likely strongly outperforms.
Specially modified version of the [WME paper below called WRD](https://arxiv.org/pdf/2004.15003.pdf) achieves 0.7785, which seems quite close to SentenceBert.

### Word Mover's Embedding

In oversimplified terms, [Word Mover's Embedding](https://arxiv.org/abs/1811.01713) is a vector embedding of a document such that its dot product
with documents in a collection approximates Word Mover's Distance between the documents for less computational cost.

To address the main computational complexity, we need to cut cost of WMD calculation.
Could we make one of the documents in each side of WMD calculation smaller?
For small constant size \\( D \\) document \\( \omega \\), the complexity of WMD would be nearly linear \\( O(L \log(L)) \\) instead of \\( O(L^3 \log(L)) \\)!
So if we could compare all documents not against each other but rather against \\(R \\) much smaller documents, we could get complexity down to \\( O(NRL \log(L)) \\) from \\( O(N^2 L^3 \log(L)) \\)!

#### Random Encounters
Let's borrow the spirit of [Random Projections method for LSH](https://www.cs.princeton.edu/courses/archive/spr04/cos598B/bib/CharikarEstim.pdf) to save ourselves computation.
Let's define j-th dimension of an embedding as WMD distance to a "randomly generated document" \\( \omega_j \\). 

\\( \mathit{WME}(x)_j = \\) 
\\( \frac{1}{\sqrt{R}} \exp[ - \gamma \mathit{WMD}(x, \omega_j) ] \\)

And let's for a moment assume we know how to randomly generate documents. Why would above make sense?

As teased above, the dot product of the embeddings is dominated by a random document that lies on the shortest path between the documents.
Note that the random document can only be close to the shortest path between the documents if it is "rich enough".

\\( \mathit{WME}(x) \cdot \mathit{WME}(y) = \\)
\\( \frac{1}{R} \sum_j \exp[ - \gamma (\mathit{WMD}(x, \omega_j) + \mathit{WMD}(y, \omega_j)) ] \\)
\\( \approx \frac{1}{R} exp[ - \gamma (WMD(x, \omega_k) + WMD(y, \omega_k)) ] \\)
\\( \approx \frac{1}{R} \exp [- \gamma \mathit{WMD}(x, y) ] \\)

<img alt="Word Mover's Distance dominated by single common random document distance." style="width: 90%; max-width: 900px" src="/images/word-movers-distance-vs-embedding.png">


### Rich Random Documents

You are rightly skeptical about generating random documents. 
Don't we need to generate too many, which would defeat our attempt to speed up the calculation?
And how do we generate documents anyway?


#### Random Words
To generate documents we only need to generate enough random word vectors to represent words.
Perhaps for the purposes of the proof or to have an ability to generate "mixed-words", [the WME paper](https://arxiv.org/abs/1811.01713) generate random vectors instead of random words from a dictionary and then drawing words for them.

The paper [cites an observation](https://arxiv.org/pdf/1502.03520.pdf) that Word2vec and GloVe words vector direction distribution is approximately isotropic.
That means that normalized word vectors are uniformly distributed on a unit sphere.
We can generate these by uniformly sampling from a hyper-cube and then normalizing the results.

\\( v_j \approx \mathit{Uniform}[v_{min}, v_{max}] \\)

Read more about [distribution of norms of Word2vec and FastText words vectors in another post of mine](/ml/FastText-Vector-Norms-And-OOV-Words).


#### Exclusive Document Collection

But how many words per random document is enough?
If we generate too large documents, we will not obtain any speed up!
So far, I haven't mentioned any restrictions on the document collection we would like to embed. Here it comes.

The paper observed that the number of random words on the order of _the number of topics_ in the collection of the documents is enough.
So if we have document collection with small enough topic count, we should obtain good accuracy, while reducing time complexity.


#### How Many Rando-Docs?

Thanks to fast convergence the paper found that the count on the order of thousands is enough, which was also on the order of number of documents they had in their testing datasets.
I am not sure, how many would be needed in the document count in the collection would be bigger than that.


#### Algo
Full algorithm is following:

- Generate \\( R \\) random docs:
    - Generate random document size \\( D \\).
    - Generate \\( D \\) random words. 
    - For all input documents calculate Word Mover's Embedding projection to just generated document as store it to matrix \\( Z \\).
- Return matrix \\( Z \\) containing the embeddings.


#### Kernel Of Approximate Truth

The approximation is motivated by analytical proof of convergence of _Word Mover's Kernel_ defined below to the WMD.
The proof utilizes theory of Random Features to show convergence of the inner product between WMEs to a positive-definite kernel that can interpreted as a soft version of WMD.

\\( k(x, y) = \\)
\\( \int p(\omega) \phi_{\omega}(x) \phi_{\omega}(y) \mathbf{d}\omega \\),

where \\( \phi_{\omega}(x) := \exp [- \gamma \mathit{WMD}(x, \omega) ] \\)

Random features are a popular method.
For example Transformer language model's [attention matrix was approximated random features kernels (FAVOR+) in the paper introducing Performers](/ml/Performers-FAVOR+-Faster-Transformer-Attention).
Read the linked post to get more context on this method.


#### Word Movers Embedding vs KNN-WMD

The method complexity is \\( O(NRL \log(L)) \\) when the random documents size (topic count) is constant. That stands in contrast to KNN-WMD variant \\( O(N^2L^3log(L)) \\).
Additionally, [WME slightly outperformed KNN-WMD in classification accuracy](https://arxiv.org/abs/1811.01713).


### 1-Minute Quiz

Without active recall, you won't remember anything from the above. Take at least one round of the quiz below. You can also subscribe to get revision reminders or generate your own quizzes there.<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=83f9d7dd-0cbf-461d-a835-cbfc2024940a">1-Minute Word Mover's Distance Quiz</a>

