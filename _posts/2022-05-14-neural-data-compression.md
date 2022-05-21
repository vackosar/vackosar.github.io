---
title: "Neural Data Compression"
description: "Losslessly reducing bits with deep-learning by minimizing cross-entropy of NNCP and TRACE models."
layout: post
categories: ml
image: /images/neural-data-compression-thumb.png
date: 2022-05-14
video: hRvhG4GWAhE
permalink: /:categories/:title
last_modified_at: 2022-05-21
---

{% include mathjax.html %}


- data compression means encoding into less bits
- lossless means without loosing any information
- trade-off between communication throughput, computation, and memory
- can compress if some symbols are more likely than others 
- better symbol prediction => lower cross-entropy => higher compression

{% include load_video.html %}


## Morse Code Uses Huffman Coding Compression
- compresses 26 characters of english alphabet, not compressing white space
- character mapped to sequence of dots and dashes, space mapped to space
- more frequent characters mapped to fewer dots and dashes
- this is [Huffman coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf) with a static tree
- encoding and decoding requires minimal compute and memory

![A part of Morse Huffman tree](/images/morse-huffman-tree.drawio.svg)


## GZip's Deflate Data Compression
- GZip uses [Deflate](https://datatracker.ietf.org/doc/html/rfc1951) compression format
  1. a sliding widow of 32k bytes is used to detect duplicate strings
    - duplicate strings are referenced back with length and distance symbols
    - this along with byte literals defines custom alphabet of symbols
  2. [Huffman coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf) maps frequent symbols to shorter bit sequences
    - bit-mapping trees stored in the output and sometimes refreshed

![Deflate algorithm illustration with LZ77 and Huffman coding](/images/deflate-algorithm-operation.drawio.svg) 


## Arithmetic Coding vs Huffman Coding
- [arithmetic coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/Rissanen__1976.pdf) has higher compression ratio than Huffman, but slower
- maps symbol of probability \\( q \\) to length \\( -log_2 q \\) in contrast to Huffman
- defined by split of \\( (0, 1) \\) into subintervals of the probability size, sorted by the size.
- encodings are numbers within the subintervals in binary format
- transmit enough digits so all fractions that fall within interval (prefix code)

![aritmetic coding interval visualization](/images/aritmetic-coding-intervals-visualization.drawio.svg)
 

## Entropy and Cross-Entropy in Compression
- Let true next symbol probability given previous symbols: \\( p(x \mid x_i, x_{i-1}, ...) \\)
  - estimated next symbol probability given previous symbols: \\( q(x \mid x_i ,... ) \\)
  - arithmetic coding encodes to length \\( - \log_2 q(x) \\)
- then average compressed message bit-length is cross-entropy: \\( - \sum_x p(x) \log_2 q(x) \\)
  - and optimal minimum bits for next symbol is entropy: \\( - \sum_x p(x) \log_2 p(x) \\)


## Bits-per-byte (bpb) and Bits-per-Character (bpc)
{% include shared_slides/bits-per-byte.md %}


## Compression by Predicting Next Symbol
- Huffman coding predicts next symbol cheaply with symbol frequency
- can trade more memory and computation with complex probability modeling
- model can be trained on already compressed data stream deterministically
- common benchmarks are enwik8, and enwik9 dataset with [bits-per-byte (bpb)](/ml/bits-per-byte-and-bits-per-character)
- bpb not comparable to language modeling results: single-pass, extra overhead, compressing entire dataset

![model predicting the next symbol from alphabet](/images/character-prediction-blabla.drawio.svg)


## NNCP: Lossless Data Compression with Neural Networks
- [NNCP](https://bellard.org/nncp/nncp.pdf) uses LSTM to predict next byte
  - model is not stored in the output - deterministically derived based on decompressed output
  - model regularly retrained during compression
- LSTM (large2) 10,000 times slower than GZip for 2.17x less bits-per-byte
- results on enwik9 below for Gzip, [Cmix](http://www.byronknoll.com/cmix.html)

![NNCP, CMIX, LSTM compression performance](/images/nncp-enwik8-results.png)


## TRACE: Faster Data Compression Than NNCP
- [TRACE](https://dl.acm.org/doi/pdf/10.1145/3485447.3511987) is 1-layer transformer compression
- 3x speedup with competitive compression with NNCP, but still 1000x slower than GZip
- vocabulary size is 256, so 4 consecutive embeddings concatenated before input
- retrained less often than NNCP, but starts randomly initialized
- result below for Cmix, NNCP, [Dzip](https://arxiv.org/pdf/1911.03572.pdf) required GPU

![TRACE, NNCP, CMIX, Dzip compression performance](/images/trace-nncp-compression-ratio-and-speed-comparison.png)


## Deep Neural Network Lossless Compression Applications
- other compression algos: Cmix, Dzip, 
- as of 2022-05 seems unpractical - slow, small compression improvement 
  - could be practical as a side effect of other computation
- note that lossy compression of images and video seem more likely applied
- more overview of the field in [this paper](https://arxiv.org/pdf/2202.06533.pdf)


## Abstraction is Lossy Compression
- abstraction is general rules and concepts derived from the usage and classification
- transformation from concrete to abstract is lossy compression - [taxonomy](/ml/Automatically-Expanding-Taxonomy)
- from properties of the abstract, can derive properties for all concrete
- not have to repeat this for each concrete - compression


## Autoencoders and Variational Autoencoders are Lossy Compressors
- if finite precision encoding into less latent dimensions
- compressed representations may be used for interpolation
- interpretable features may be [disentangled](/ml/manipulate-item-attributes-via-disentangled-representation)