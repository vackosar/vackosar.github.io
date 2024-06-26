---
title: Bits-Per-Byte and Bits-Per-Character
description: BPB and BPC are metrics used in compression and language modelling related to compression ratio.
layout: post
categories: ml
date: 2022-05-20
last_modified_at: 2023-05-25
image: /images/deflate-algorithm-operation.drawio.svg
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-05-14-neural-data-compression.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2017-12-03-Boundary-Control-Entity-Architecture--The-Pattern-to-Structure-Your-Classes.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
- _posts/2020-09-15-double-descent-contrary-to-bias-variance-trade-off.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
---



{% include mathjax.html %}


Bits-per-Byte measures **how many bits** a compression program needs to know **to guess the next symbol** on average.
For example, **if** the compression program is **perfect**, then the **next symbol is obvious** to it, and it needs **0 bits**, so \\( bpb = 0 \\).
Or, if it the worst possible, it needs to be given the exact next symbol from the vocabulary, so it needs as \\( bpb = log_2(\mathrm{vocabularySize}) \\).



## How BPB relates to compression ratio or cross-entropy?

Bits-per-Byte (BPB) and Bits-per-Character (BPC) are metrics related to compression ratio and cross-entropy, used in compression and language modeling, with BPC equaling BPB for ASCII Extended characters, and cross-entropy loss using log2 in character-level models equating to BPC.

{% include shared_slides/bits-per-byte.md %}

BPC corresponds to BPB for extended ASCII characters, and when using log2 in character-level models, the cross-entropy loss is equivalent to BPB.

{% include image.html src="/images/deflate-algorithm-operation.drawio.svg" alt="Deflate algorithm illustration with LZ77 and Huffman coding" %}


## Neural Data Compression
Data compression relies on ability to predict next symbol. Read more on [neural data compression and its applications in machine learning here](/ml/neural-data-compression).