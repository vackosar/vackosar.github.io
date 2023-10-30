---
title: Tokenization in Machine Learning Explained
description: Tokenization is splitting the input data into a sequence of meaningful parts e.g. pice data like a word, image patch, document sentence.
layout: post
categories: ml
date: 2022-09-16
image: /images/transformer-tokenization-and-embeddings.drawio.svg
last_modified_at: 2022-09-16
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2022-05-14-neural-data-compression.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
---


{% include shared_slides/tokenization-summary.md %}


### Tokenization in NLP
- Input data text is split using a dictionary into character chunks called tokens
- The vocabulary contains around 100k most common sequences from the training text.
- Tokens often correspond to words of 4 characters long with prepended whitespace or special characters.
- common tokenization algorithms are [BPE](/ml/Tokenization-in-Machine-Learning-Explained#bpe-tokenizer), [WordPiece](/ml/Tokenization-in-Machine-Learning-Explained#wordpiece-vs-bpe-tokenizer), [SentencePiece](/ml/Tokenization-in-Machine-Learning-Explained#sentencepiece-vs-wordpiece-tokenizer)
- Text tokens can be converted back to text, but sometimes there is a loss of information.
- Tokenization in NLP is a form of [compression - dictionary coding](/ml/neural-data-compression).

![tokenization and embedding layer for transformer](/images/transformer-tokenization-and-embeddings.drawio.svg)


### Is NLP Tokenization Slow?
Does tokenization take up resources?

Tokenization is low resource CPU operation.
It is a much lower resource intensive than the model inference, which on contrary is performed on the GPU and involves large matrix multiplications.
Tokenization can be around 1% of the BERT model inference time.

Tokenization is mostly splitting text on space characters and sometimes further using a dictionary lookup.
For example, [tiktoken library](https://github.com/openai/tiktoken) can process (throughput) Mega Bytes per second of text with a single CPU core.


### Tokenization In Continuous Modalities Vision or Speech
- Tokenizers are not quite present in modalities like image or speech.
- Instead, the images or audio is split into a matrix of patches without dictionary equivalent as in case of the text.
- Image architectures [Vision Transformer (ViT)](https://arxiv.org/pdf/1909.02950.pdf), Resnets split image into overlapping patches and then encode these.
- Outputs [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) of these can then be passed to ,e.g., [transformer](/ml/transformers-self-attention-mechanism-simplified) ([CMA-CLIP or MMBT](/ml/Multimodal-Image-Text-Classification#amazons-cma-clip-model))

![tokenization and embedding in Vision Transformer ViT](/images/vision-transformer-vit-architecture.png)


#### Quantization

{% include shared_slides/quantization.md %}


## The Most Common Tokenizers in NLP

A list of commonly used tokenizers sorted by their date of introduction.


### FastText Tokenizer
- Older models like Word2vec, or [FastText](/ml/FastText-Vector-Norms-And-OOV-Words) used simple tokenizers, that after some preprocessing simply split the text on whitespace characters.
  These chunks are often words of a natural language.
- Then, if the character sequence chunk is present in a dictionary of most common chunks, and return an index in the dictionary.
- If not found, most tokenizers before FastText returned a special token called the unknown token. FastText solved this problem by additional split on the word level into fixed size "subwords", but to find out [more details about FastText read this post](/ml/FastText-Vector-Norms-And-OOV-Words).
- BPE never returns unknown token, and instead composes the out-of-vocab words from parts up to individual characters.

### BPE Tokenizer
Byte-Pair-Encoding (BPE) algorithm:
1. [BPE](https://arxiv.org/abs/1508.07909) pre-tokenizes text by splitting on spaces
2. start with only characters as token
3. merge the highest frequency token pair from the text
4. stop if max vocabulary size reached, otherwise loop to previous step


### WordPiece vs BPE Tokenizer
- [WordPiece](https://static.googleusercontent.com/media/research.google.com/ja//pubs/archive/37842.pdf) merges token pair with highest `count(ab) / count(a)count(b)`
- Used for [BERT](/ml/transformers-self-attention-mechanism-simplified), DistilBERT, [Electra](/ml/electra-4x-cheaper-bert-training)


### Unigram Tokenizer
- [Unigram](https://arxiv.org/pdf/1804.10959.pdf) construction instead of merging and adding to a vocabulary like [BPE](#bpe-tokenizer), it removes tokens
- A vocabulary loss is constructed as expectation maximization loss summing over all tokenizations of all corpus' subsequences.
  - The probability of each token is approximated as independent of other tokens.
- Starts with a very large vocabulary and removes fixed number symbols such that the vocabulary loss increase minimally
- Stop if vocabulary size reached, otherwise loop to previous step


### SentencePiece vs WordPiece Tokenizer
- Japanese, Korean, or Chinese languages don't separate words with a space
- [SentencePiece](https://arxiv.org/pdf/1808.06226.pdf) removes pre-tokenization (splitting on spaces)
- instead tokenizes text stream with usually with [Unigram](#unigram-tokenizer) or alternatively with [BPE](#bpe-tokenizer)
- T5, ALBERT, XLNet, MarianMT use SentencePiece with [Unigram](#unigram-tokenizer)

