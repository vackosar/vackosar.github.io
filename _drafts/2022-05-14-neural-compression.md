---
title: "Neural Network-based Data Compression"
description: "How to losslessly compress data with deep-learning predictions."
layout: post
categories: ml
date: 2022-05-14
permalink: /:categories/:title
---

- data compression means encoding into less bits
- lossless means without loosing any information
- compression is possible if some symbols are more likely than others given all previous symbols
- tradeoff between communication throughput, computation, and memory


## Morse Code Compression
- compresses 26 characters of english alphabet, not compressing white space
- each character is mapped to sequence of dots and dashes, space is mapped to space
- more frequent characters mapped to fewer dots and dashes
- this is done with static [Huffman coding](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf)
- human can encode and decode


## GZip's Deflate Data Compression
- GZip uses [Deflate](https://datatracker.ietf.org/doc/html/rfc1951) compression format
- a sliding widow of 32k bytes is used to detect duplicate strings
  - duplicate strings are referenced back with length and distance symbols
- this along with byte literals defines custom alphabet of symbols
- [Huffman coding](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf) maps frequent symbols to shorter bit sequences
- the Huffman trees used for bit-mapping stored in the output and sometimes refreshed


## Compression by Predicting Next Symbol
- Huffman coding predicts next symbol cheaply with symbol frequency
- we can trade more memory and computation by using more complex machine learning models
- arithmetic coding maps high probability symbols into shorter bit sequences 
- model can be retrained based on already compressed data stream
- common benchmark is enwik8 dataset


## Lossless Data Compression with Neural Networks
- [NNCP](https://bellard.org/nncp/nncp.pdf) uses LSTM to predict next byte
  - model is not stored in the output, is deterministically derived based on decompressed output
- newer [TRACE](https://dl.acm.org/doi/pdf/10.1145/3485447.3511987) uses faster Transformer
  - single layer transformer retrained less often 
- both still too expensive
- TODO comparison