---
title: "Sparce Matrix Why and When?"
description: "Sparce matrices like CSR, LOL, COO are extremely useful for matrices with more than half zero values"
layout: post
categories: ml
date: 2022-03-20
permalink: /:categories/:title
---

Sparse matrix format compresses matrices with more than half zero values and speeds up certain operations on them.
There are two main groups of the sparce matrix representations: 
- efficient for construction and modification DOK, LIL, COO
- efficient for access and operations CSR, CSC e.g. 

There are several types of sparse matrix representations, where each has an advantage in different situations.
- DOK: Dictionary of Keys format:
  - row, column pairs map to value,
  - `dict((i, j): matrix[i, j] for i in matrix.shape[0] for j in matrix.shape[1])`
- LOL: List of Lists format:
  - each row has one list of tuples of column and value
  - example `[[(j, matrix[i,j]) for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]`
- COO: COOrdinate format (aka IJV, triplet format): sorted list of row, column, value tuples `[(i, j, val) for i, j in ...]`
- CSC: Compressed Sparse Row format: Combination of LOL and COO
    - stores matrix in 3 lists
    - "row list" for each row contains a number that is references a position in the value and column lists, where the row's column and values start
    - "column list" contains column indexes and is indexed by the row list
    - "value list" contains values and is indexed by the row list
    - to access a row `i` retrieve `indexes = range(row_list[i], row_list[i+1])`, then build row's list of list representation `row_lol = [(i, column_list[j], value_list[j]) for j in indexes]`
    - fast matrix vector product e.g. useful for KNN
    - [converting to Scipy's CSR](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html) with `tocsr` method
- and more: Compressed Sparse Row, Block Sparse Row format, Diagonal, ...

You can use [Scipy library for sparce matrixes](https://docs.scipy.org/doc/scipy/reference/sparse.html#usage-information).

