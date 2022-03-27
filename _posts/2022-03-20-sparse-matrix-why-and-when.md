---
title: "Sparse Matrix Why and When?"
description: "Sparce matrix formats like CSR, LOL, COO compress and speed up certain operations on mostly zero matrices"
layout: post
categories: ml
image: /images/sparse-matrix-csr.png
date: 2022-03-20
permalink: /:categories/:title
---

Hi, this is a draft of a post, but it could be already useful.

## Dense Matrix Multiplication Example
The simplest the most common formats used.

![Dense matrix multiplication example](../images/sparse-matrix-dense-example.png)


## CSR Sparse Matrix Multiplication Example
A very common sparse format that is useful in situations described in below.

![Compressed Sparce Row sparse matrix matrix multiplication](/images/sparse-matrix-csr.png)


## Sparse Matrix Formats
Sparse matrix format compresses matrices with more than half zero values and speeds up certain operations on them.
There are two main groups of the sparce matrix representations: 
- efficient for incremental construction and modification DOK, LIL, COO
- efficient for access and operations CSR, CSC

There are several types of sparse matrix representations, where each has an advantage in different situations.
- DOK: Dictionary of Keys format:
  - row, column pairs map to value,
  - `dict((i, j): matrix[i, j] for i in matrix.shape[0] for j in matrix.shape[1])`
- LOL: List of Lists format:
  - each row has one list of tuples of column and value
  - example `[[(j, matrix[i,j]) for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]`
- COO: COOrdinate format (aka IJV, triplet format):
  - sorted list of row, column, value tuples
  - `[(i, j, matrix[i, j]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1])]`
- CSC: Compressed Sparse Row format: COO 
    - stores matrix in 3 lists
    - "row list" for each row contains a number that is references a position in the value and column lists, where the row's column and values start
    - "column list" contains column indexes and is indexed by the row list
    - "value list" contains values and is indexed by the row list
    - to access a row `i` retrieve `indexes = range(row_list[i], row_list[i+1])`, then build row's list of list representation `row_lol = [(i, column_list[j], value_list[j]) for j in indexes]`
    - fast matrix to vector multiplication (product) thus useful for [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
    - [converting to Scipy's CSR](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html) with `tocsr` method
- and more: Compressed Sparse Row, Block Sparse Row format, Diagonal, ...

You can use [Scipy library for sparce matrixes](https://docs.scipy.org/doc/scipy/reference/sparse.html#usage-information).
The main image is from [this study](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.140.9761&rep=rep1&type=pdf).
