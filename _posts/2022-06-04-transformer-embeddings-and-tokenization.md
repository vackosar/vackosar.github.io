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
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
---



- [Transformer](/ml/transformers-self-attention-mechanism-simplified) is sequence to sequence neural network architecture
- input text is encoded with tokenizers to sequence of integers called input tokens
- input tokens are mapped to sequence of vectors (word [embeddings](/ml/Embeddings-in-Machine-Learning-Explained)) via embeddings layer 
- output vectors ([embeddings](/ml/Embeddings-in-Machine-Learning-Explained)) can be classified to a sequence of tokens
- output tokens can then be decoded back to a text

![embeddings in transformer architecture](/images/transformer-architecture-tokens-vs-embeddings.drawio.svg)


## Tokenization and Tokenizers
- Input text is split using a dictionary into character chunks called tokens
- The vocabulary contains around 100k most common sequences from the training text.
- Tokens often correspond to words of 4 characters long with prepended whitespace or special characters.
- common tokenization algorithms are [BPE](#bpe-tokenizer), [WordPiece](#wordpiece-vs-bpe-tokenizer), [SentencePiece](#sentencepiece-vs-wordpiece-tokenizer)

![tokenization and embedding layer for transformer](/images/transformer-tokenization-and-embeddings.drawio.svg)


### FastText Tokenizer
Older models like Word2vec, or [FastText](/ml/FastText-Vector-Norms-And-OOV-Words) used simple tokenizers, that after some preprocessing simply split the text on whitespace characters.
These chunks are often words of a natural language.
Then, if the character sequence chunk is present in a dictionary of most common chunks, we treat it as a token.
Otherwise, most tokenizers before FastText returned an unknown token.
FastText solved this problem by additional split on the word level into fixed size "subwords", but to find out [more details about FastText read this post](/ml/FastText-Vector-Norms-And-OOV-Words).
Other tokenizers, continued to have these issues until [SentencePiece](#sentencepiece-vs-wordpiece-tokenizer), which keep a dictionary including single characters and almost never returns unknown token.


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
- Tokenizers are not quite present in modalities like image or speech.
- Instead, the images or audio is split into a matrix of patches without dictionary equivalent as in case of the text.
- Image architectures [Vision Transformer (ViT)](https://arxiv.org/pdf/1909.02950.pdf), Resnets split image into overlapping patches and then encode these.
- Outputs [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) of these can then be passed to a transformer e.g. in [CMA-CLIP or MMBT](/ml/Multimodal-Image-Text-Classification#amazons-cma-clip-model)


## [Positional Encodings](/ml/transformer-positional-embeddings-and-encodings) add Token Order Information

{% include shared_slides/positional-encodings-summary.md %}


## Word Embeddings
- Embedding layers map tokens to word vectors (sequence of numbers) called word [embeddings](/ml/Embeddings-in-Machine-Learning-Explained).
- Input and output embeddings layer often share the same token-vector mapping.
- Embeddings contain semantic information about the word.


## Explore Yourself
Try out BERT BPE tokenizer and its embeddings using Transformers package.

{% include highlight-rouge-friendly.css.html %}

```python
# pip install transformers && pip install torch

from transformers import DistilBertTokenizerFast, DistilBertModel

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
tokens = tokenizer.encode('This is a input.', return_tensors='pt')
print("These are tokens!", tokens)
for token in tokens[0]:
    print("This are decoded tokens!", tokenizer.decode([token]))

model = DistilBertModel.from_pretrained("distilbert-base-uncased")
print(model.embeddings.word_embeddings(tokens))
for e in model.embeddings.word_embeddings(tokens)[0]:
    print("This is an embedding!", e)
```