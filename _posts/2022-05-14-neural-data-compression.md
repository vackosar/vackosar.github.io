---
title: Neural Data Compression
description: 'Lossless bit reduction with machine learning by minimizing cross-entropy. Examples: NNCP and TRACE models.'
layout: post
categories: ml
image: /images/neural-data-compression-thumb.png
date: 2022-05-14
video: hRvhG4GWAhE
permalink: /:categories/:title
last_modified_at: 2023-11-03
my_related_post_paths:
- _posts/2022-05-20-bits-per-byte-and-bits-per-character.md
- _posts/2022-10-23-Neural-Network-Pruning-Explained.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2023-03-24-Symbolic-vs-Connectionist-Machine-Learning.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
---



{% include mathjax.html %}


- data compression means encoding into less bits
- lossless means without loosing any information
- trade-off between communication throughput, computation, and memory
- can compress if some symbols are more likely than others 
- better symbol prediction => lower cross-entropy => higher compression

{% include load_video.html %}


## Dictionary Coder
- Also called Substitution coder
- Replaces long frequently occurring strings with a shorter references in a dictionary.
- Applied in [Gzip](#gzips-deflate-data-compression) and in [natural language processing tokenization (e.g. BPE)](/ml/Tokenization-in-Machine-Learning-Explained) compression


## Morse Code Uses Huffman Coding Compression
- compresses 26 characters of english alphabet, not compressing white space
- character mapped to sequence of dots and dashes, space mapped to space
- more frequent characters mapped to fewer dots and dashes
- this is [Huffman coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf) with a static tree
- encoding and decoding requires minimal compute and memory

{% include image.html src="/images/morse-huffman-tree.drawio.svg" alt="A part of Morse Huffman tree" %}


## GZip's Deflate Data Compression
- [GZip](https://datatracker.ietf.org/doc/html/rfc1952) uses [Deflate](https://datatracker.ietf.org/doc/html/rfc1951) compression format ([ZIP](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) also)
  1. a sliding widow of 32k bytes is used to detect duplicate strings
    - duplicate strings are referenced back with length and distance symbols (similar to [dictionary coding](#dictionary-coder))
    - this along with byte literals defines custom alphabet of symbols
  2. [Huffman coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf) maps frequent symbols to shorter bit sequences
    - bit-mapping trees stored in the output and sometimes refreshed

{% include image.html src="/images/deflate-algorithm-operation.drawio.svg" alt="Deflate algorithm illustration with LZ77 and Huffman coding" %} 


## Arithmetic Coding vs Huffman Coding
- [arithmetic coding](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/Rissanen__1976.pdf) has higher compression ratio than Huffman, but slower
- maps symbol of probability \\( q \\) to length \\( -log_2 q \\) in contrast to Huffman
- defined by split of \\( (0, 1) \\) into subintervals of the probability size, sorted by the size.
- encodings are numbers within the subintervals in binary format
- transmit enough digits so all fractions that fall within interval (prefix code)

{% include image.html src="/images/aritmetic-coding-intervals-visualization.drawio.svg" alt="aritmetic coding interval visualization" %}
 

## Entropy and Cross-Entropy in Compression
- Let true next symbol probability given previous symbols: \\( p(x \mid x_i, x_{i-1}, ...) \\)
  - estimated next symbol probability given previous symbols: \\( q(x \mid x_i ,... ) \\)
  - arithmetic coding encodes to length \\( - \log_2 q(x) \\)
- then average compressed message bit-length is cross-entropy: \\( - \sum_x p(x) \log_2 q(x) \\)
  - and optimal minimum bits for next symbol is entropy: \\( - \sum_x p(x) \log_2 p(x) \\)
  - [optimal due to "Shanon's 1948 source coding theorem"](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
- Cross-Entropy minimization equals likelihood maximization: \\( \frac{1}{N} \log ( \prod_k q_k^{N_k p_k} ) \\)


## Bits-per-byte (bpb) and Bits-per-Character (bpc)
{% include shared_slides/bits-per-byte.md %}


## Compression by Predicting Next Symbol
- Huffman coding predicts next symbol cheaply with symbol frequency
- can trade more memory and computation with complex probability modeling with ML
- ML model can be trained on already compressed data stream deterministically
- common benchmarks are enwik8, and enwik9 datasets with [bits-per-byte (bpb)](/ml/bits-per-byte-and-bits-per-character)
- bpb not comparable to language modeling results: single-pass, extra overhead, compressing entire dataset

{% include image.html src="/images/character-prediction-blabla.drawio.svg" alt="model predicting the next symbol from alphabet" %}


## Language Modelling is Compression
- [Language model's training objective](/ml/How-Deep-Neural-Networks-Learn) is to predict the next symbol
- Any [text compressor can be used for text generation including GZIP](https://arxiv.org/pdf/2309.10668.pdf)


## NNCP: Lossless Data Compression with Neural Networks
- model is not stored in the output. It is deterministically derived based on decompressed output
- model is regularly retrained during compression
- creates a [tokenization](/ml/Tokenization-in-Machine-Learning-Explained) dictionary (16k symbols like Cmix) during the first pass
- tokenization is [dictionary coding](#dictionary-coder)
- [NNCP 1](https://bellard.org/nncp/nncp.pdf) uses multi-layer LSTM to predict next symbol
- [NNCP v2](https://bellard.org/nncp/nncp_v2.1.pdf) Transformer beats Cmix on enwik9


## NNCP v2 Results vs Cmix
- results of NNCP v2 on enwik9 below. LSTM (large2) is ...
- 10,000 times slower than GZip for 2.8x less bits-per-byte
- faster, simpler, better than [Cmix](http://www.byronknoll.com/cmix.html) (complex w/ LSTM) on enwik9
- worse than Cmix on enwik8

{% include image.html src="/images/nncpv2-enwik9.png" alt="NNCP v2, CMIX, LSTM compression performance" %}


## TRACE Model 1-layer Transformer 
- [TRACE](https://arxiv.org/abs/2203.16114) is 1-layer transformer compression
- predicts the next byte instead of dictionary symbol (token)
- vocabulary size is 256 too little compared to the hidden dimension
  - so 4 consecutive embeddings concatenated before input
- retrained less often (adaptive) than NNCP, but starts randomly initialized

{% include image.html src="/images/trace-model-architecture.png" alt="TRACE model architecture" %}


## TRACE Model Results Faster Data Compression Than NNCP
- 3x speedup with competitive compression with NNCP, but still 1000x slower than GZip
- worse on text but on-par on other due to not using tokenization dictionary
- result on enwik9 below for Cmix, NNCP, [Dzip](https://arxiv.org/pdf/1911.03572.pdf) required GPU

{% include image.html src="/images/trace-nncp-compression-ratio-and-speed-comparison.png" alt="TRACE, NNCP, CMIX, Dzip compression performance" %}


## Deep Neural Network Lossless Compression Applications
- other compression algos: Cmix ([HutterPrice](http://prize.hutter1.net/) 2021 SoTA), [Dzip](https://arxiv.org/pdf/1911.03572.pdf)
- as of 2022-05 seems unpractical - slow, small compression improvement 
  - could be practical as a side effect of other computation
- note that lossy compression of images and video seem more likely applied
- more overview of the field in [this paper](https://arxiv.org/pdf/2202.06533.pdf)


## Abstraction is Lossy Compression
- [abstraction is a set of generalization rules and concepts](/ml/How-Deep-Neural-Networks-Learn) derived from the usage and classification
- transformation from concrete to abstract is lossy compression - [taxonomy](/ml/Automatically-Expanding-Taxonomy)
- from properties of the abstract, can derive properties for all concrete
- not have to repeat this for each concrete - compression


## Autoencoders and Variational Autoencoders are Lossy Compressors
- if finite precision encoding into less latent dimensions
- compressed representations may be used for interpolation
- interpretable features may be [disentangled](/ml/manipulate-item-attributes-via-disentangled-representation)