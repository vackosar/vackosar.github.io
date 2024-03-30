---
title: Sparse Matrix Why and When?
description: Sparce matrix formats like CSR, LOL, COO compress and speed up certain operations on mostly zero matrices
layout: post
categories: ml
image: /images/sparse-matrix-csr.png
date: 2022-03-20
last_modified_at: 2024-03-30
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-05-14-neural-data-compression.md
- _posts/2022-10-23-Neural-Network-Pruning-Explained.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
---

Sparse matrices are a special type of matrices that have a significant number of zero values. They are used in machine learning and other scientific computations due to their ability to reduce memory usage and computation time.

For example, a dense matrix of size 1000x1000 with only 10% non-zero 8-bit values would require 8 MB of memory, while its sparse equivalent would require only a 10% of that.

Apart from **saving memory, sparse matrices also speed up certain operations**, such as matrix multiplication, by skipping over the zero values. In fact, the performance gain can be dramatic: a sparse matrix multiplication can be up to 100x faster than its dense counterpart.

Overall, using sparse matrices can greatly improve the efficiency and scalability of machine learning algorithms, especially when dealing with zero-valued data.


## Where Are Sparse Matrices Used?
Sparse representations are more used in symbolic systems like recommendation systems (item-item or item-user matrix). Or examples are adjacency matrices, word counting methods.

In area of neural networks, **dense representations** are the most common. For example, [word2vec or FastText](/ml/FastText-Vector-Norms-And-OOV-Words) are [dense representations (embeddings)](/ml/Embeddings-in-Machine-Learning-Explained) of words. Or in case of the [Transformer architecture](/ml/transformers-self-attention-mechanism-simplified). Even after [neural network connection pruning](/ml/Neural-Network-Pruning-Explained), the activations remain rather dense. But recently, sparse representations also appeared in the **Sparse Mixture-of-Experts** deep-learning architecture exemplified by widely-used Mixtral model. In each [feed-forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) of Mixtral model, only 2 of 8 (25%) get activated during inference.    

<blockquote class="blockquote" style="font-style: italic">
Mixtral is a sparse mixture-of-experts network. It is a decoder-only model where the feedforward block picks from a set of 8 distinct groups of parameters. At every layer, for every token, a router network chooses two of these groups (the “experts”) to process the token and combine their output additively.
<footer class="blockquote-footer"><a href="https://mistral.ai/news/mixtral-of-experts/">Mistral.ai</a></footer>
</blockquote>


## Dense Matrix Multiplication Example
The simplest the most common formats used.

{% include image.html src="../images/sparse-matrix-dense-example.png" alt="Dense matrix multiplication example" %}


## CSR Sparse Matrix Multiplication Example
A very common sparse format that is useful in situations described in below.

{% include image.html src="/images/sparse-matrix-csr.png" alt="Compressed Sparce Row sparse matrix matrix multiplication" %}


## Sparse Matrix Formats
Sparse matrix format compresses matrices with more than half zero values and speeds up certain operations on them.
There are two main groups of the sparce matrix representations: 
- efficient for incremental construction and modification DOK, LIL, COO
- efficient for access and operations CSR, CSC
There are several types of sparse matrix representations, where each has an advantage in different situations.
 

### DOK: Dictionary of Keys format:
- row, column pairs map to value,
- `dict((i, j): matrix[i, j] for i in matrix.shape[0] for j in matrix.shape[1])`


### LOL: List of Lists format:
- each row has one list of tuples of column and value
- example `[[(j, matrix[i,j]) for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]`
  

### COO: COOrdinate format (aka IJV, triplet format):
- sorted list of row, column, value tuples
- `[(i, j, matrix[i, j]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1])]`
 

### CSR: Compressed Sparse Row format
- stores matrix in 3 lists
  - "row list" for each row contains a number that is references a position in the value and column lists, where the row's column and values start
  - "column list" contains column indexes and is indexed by the row list
  - "value list" contains values and is indexed by the row list
- to access a row `i` retrieve `indexes = range(row_list[i], row_list[i+1])`, then build row's list of list representation `row_lol = [(i, column_list[j], value_list[j]) for j in indexes]`
- fast matrix to vector multiplication (product) thus useful for [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- fast CSR + CSR, CSR * CSR, CSR * Dense
- fast row slicing
- slow transpose
- [converting to Scipy's CSR](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html) with `tocsr` method


### CSC: Compressed Sparse Column format
- similar to CSR except columns and rows switch their role
 
### Other formats
Block Sparse Row format, Diagonal, ...


## How to Use Sparse Matrices
You can use [Scipy library for sparce matrixes](https://docs.scipy.org/doc/scipy/reference/sparse.html#usage-information).
The main image is from [this study](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.140.9761&rep=rep1&type=pdf).

