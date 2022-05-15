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


## GZip Data Compression
- GZip uses [Deflate](https://datatracker.ietf.org/doc/html/rfc1951) compression format
- a sliding widow of 32k bytes is used to detect duplicate strings
  - duplicate strings are referenced back with length and distance symbols
- this along with byte literals defines custom alphabet of symbols
- [Huffman coding](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf) assigns to more frequent symbols shorter bit sequences
- the Huffman tree used for the mapping to bit codes is stored with the compressed output
- multiple Huffman trees can be used during compression


