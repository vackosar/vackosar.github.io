---
title: Transformer Embeddings and Tokenization
description: How transformers convert words and other objects to vectors and back.
layout: post
categories: ml
image: /images/transformer-architecture-embeddings.drawio.svg
date: 2022-06-05
last_modified_at: 2022-06-18
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2022-04-18-how-computers-understood-humans.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
---



- [transformer (e.g. BERT)](/ml/transformers-self-attention-mechanism-simplified) is sequence to sequence neural network architecture
- input text is encoded with tokenizers to sequence of integers
- input tokens are mapped to sequence of embeddings via embeddings layer 
- output [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) can be classified to a sequence of tokens
- output tokens can then be converted back to the text

![embeddings in transformer architecture](/images/transformer-architecture-embeddings.drawio.svg)


## Tokenizers
- Input text is split into character chunks called tokens present in a dictionary.
- Vocabulary of the token dictionaries contain around 100k most common sequences from the training text
- Tokens often correspond to words of 4 characters long with prepended whitespace or special characters.
- Embedding layers map tokens to vectors in other words to sequence of numbers.
- Input and output embeddings layer often share the same token-vector mapping.
- common tokenization algorithms are [WordPiece](https://static.googleusercontent.com/media/research.google.com/ja//pubs/archive/37842.pdf), [SentencePiece](https://arxiv.org/pdf/1808.06226.pdf)

![tokenization and embedding layer for transformer](/images/transformer-tokenization-and-embeddings.drawio.svg)


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
- [Unigram](https://arxiv.org/pdf/1804.10959.pdf) instead of merging and adding like BPE, it removes
- starts with a very large vocabulary and removes fixed number symbols such that a vocabulary loss increase minimally 
- stop if vocabulary size reached, otherwise loop to previous step
- to disambiguate tokenization a probability of token occurrence is used, and packaged with the tokenizer


### SentencePiece vs WordPiece Tokenizer
- Japanese, Korean, or Chinese languages don't separate words with a space
- [SentencePiece](https://arxiv.org/pdf/1808.06226.pdf) removes pre-tokenization (splitting on spaces)
- instead tokenizes text stream with usually with [Unigram](#unigram-tokenizer) or alternatively with [BPE](#bpe-tokenizer)
- T5, ALBERT, XLNet, MarianMT use SentencePiece with [Unigram](#unigram-tokenizer)


## Tokenizers vs Encoders 
- Tokenizers are not suitable for modalities like image or speech.
- Image architectures like [Vision Transformer (ViT)](https://arxiv.org/pdf/1909.02950.pdf) or [MMBT](/ml/Multimodal-Image-Text-Classification#facebooks-mmbt-model) encode input without a tokenizer.
- Inputs to transformer can be encoded with a another neural network.
- Output of the encoding layer has to be a sequence of embeddings for the transformer.


## [Positional Encodings](/ml/transformer-positional-embeddings-and-encodings) add Token Order Information

{% include shared_slides/positional-encodings-summary.md %}


## Explore Yourself
Try out BERT BPE tokenizer and its embeddings using Transformers package.

{% include highlight-rouge-friendly.css.html %}

```python
# pip install transformers && pip install torch

from transformers import DistilBertTokenizerFast, DistilBertModel

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
tokens = tokenizer.encode('This is a input.', return_tensors='pt')
print(tokens)
for token in tokens[0]:
    print(tokenizer.decode([token]))

model = DistilBertModel.from_pretrained("distilbert-base-uncased")
print(model.embeddings.word_embeddings(tokens))
for e in model.embeddings.word_embeddings(tokens)[0]:
    print(e)
```