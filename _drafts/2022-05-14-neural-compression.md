---
title: "Neural Network-based Data Compression"
description: "How to losslessly compress data with deep-learning predictions."
layout: post
categories: ml
date: 2022-05-14
permalink: /:categories/:title
---

- data compression means encoding into less bits
- compression is only possible if statistical redundancy
- lossless means without loosing any information


## Popular Data Compression
- GZip uses Deflate compression format
- Deflate uses 2 methods:
  - encodes bytes into shorter sequence of bits represent 
  - duplicate string elimination LZ77
  - bit reduction via Huffman coding on bytes into bit-codes
  - https://www.w3.org/Graphics/PNG/RFC-1951