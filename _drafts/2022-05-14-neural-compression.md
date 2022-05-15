---
title: "Neural Network-based Data Compression"
description: "Lossless data compression data via deep-learning predictions"
layout: post
categories: ml
date: 2022-05-14
permalink: /:categories/:title
---

{% include mathjax.html %}


- data compression means encoding into less bits
- lossless means without loosing any information
- compression is possible if some symbols are more likely than others given all previous symbols
- tradeoff between communication throughput, computation, and memory


## Morse Code Uses Huffman Coding Compression
- compresses 26 characters of english alphabet, not compressing white space
- each character is mapped to sequence of dots and dashes, space is mapped to space
- more frequent characters mapped to fewer dots and dashes
- this is done with static [Huffman coding](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf)
- encoding and decoding require minimal compute (human operator)

![A part of Morse Huffman tree](/images/morse-huffman-tree.drawio.svg)


## GZip's Deflate Data Compression
- GZip uses [Deflate](https://datatracker.ietf.org/doc/html/rfc1951) compression format
- a sliding widow of 32k bytes is used to detect duplicate strings
  - duplicate strings are referenced back with length and distance symbols
- this along with byte literals defines custom alphabet of symbols
- [Huffman coding](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf) maps frequent symbols to shorter bit sequences
- the Huffman trees used for bit-mapping stored in the output and sometimes refreshed

![Deflate algorithm illustration with LZ77 and Huffman coding](/images/deflate-algorithm-operation.drawio.svg) 


## Compression by Predicting Next Symbol
- Huffman coding predicts next symbol cheaply with symbol frequency
- we can trade more memory and computation by using more complex machine learning models
- [arithmetic coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/Rissanen__1976.pdf) maps high probability symbols into shorter bit sequences of length \\( -log_2(p) \\)
- model can be retrained based on already compressed data stream
- common benchmark is enwik8 dataset, but compression bpb metric is not comparable

![model predicting the next symbol from alphabet](/images/character-prediction-blabla.drawio.svg)


## NNCP: Lossless Data Compression with Neural Networks
- [NNCP](https://bellard.org/nncp/nncp.pdf) uses LSTM to predict next byte
  - model is not stored in the output - deterministically derived based on decompressed output
- newer [TRACE](https://dl.acm.org/doi/pdf/10.1145/3485447.3511987) uses faster Transformer
  - single layer transformer retrained less often 
  - regularly retrained during compression
- LSTM (large2) 10,000 times slower than GZip for 2.17x less bits per byte

![NNCP result](/images/nncp-enwik8-results.png)


## TRACE: A Fast Transformer-based General-Purpose Lossless Compressor Model
- [TRACE](https://dl.acm.org/doi/pdf/10.1145/3485447.3511987) is 1-layer transformer compression
- 3x speedup with competitive compression with NNCP, but still 1000x slower than GZip
- vocabulary is 256 bytes, 4 consecutive embeddings concatenated before input
- result below achieved on GPU - not practical for most applications 

![TRACE NNCP compression performance](/images/trace-nncp-compression-ratio-and-speed-comparison.png)


## Deep Neural Network Lossless Compression Applications
- as of 2022-05 seems unpractical - slow, small compression improvement 
  - could be practical as a side effect of other computation
- note that lossy compression of images and video seem more likely applied
- you can get more overview of the field [this paper](https://arxiv.org/pdf/2202.06533.pdf)
