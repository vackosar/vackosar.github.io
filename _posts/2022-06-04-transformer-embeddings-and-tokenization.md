---
title: "Transformer Embeddings and Tokenization"
description: "How transformers convert words and other objects to vectors and back."
layout: post
categories: ml
image: /images/transformer-architecture-embeddings.drawio.svg
date: 2022-06-05
permalink: /:categories/:title
---

- [transformer (e.g. BERT)](/ml/transformers-self-attention-mechanism-simplified) is sequence to sequence neural network architecture
- input text is encoded with tokenizers to sequence of integers
- input tokens are mapped to sequence of embeddings via embeddings layer 
- output embeddings can be classified to a sequence of tokens
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


## Tokenizers vs Encoders 
- Tokenizers are not suitable for modalities like image or speech.
- Architectures like [Vision Transformer (ViT)](https://arxiv.org/pdf/1909.02950.pdf) or [MMBT](https://arxiv.org/pdf/1909.02950.pdf) encode input without a tokenizer.
- Inputs to transformer can be encoded with a another neural network.
- Output of the encoding layer has to be a sequence of embeddings for the transformer.


## [Positional Encodings](/ml/transformer-positional-embeddings-and-encodings) add Token Order Information

{% include shared_slides/positional-encodings-summary.md %}


## Explore Yourself

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