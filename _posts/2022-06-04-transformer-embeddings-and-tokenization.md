---
title: Transformer Embeddings and Tokenization
description: How transformers convert words and other objects to vectors and back using tokenizers, positional encoders, embedders.
layout: post
categories: ml
image: /images/transformer-architecture-tokens-vs-embeddings.drawio.svg
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


## Tokenization vs Embedding
- input is [tokenized](/ml/Tokenization-in-Machine-Learning-Explained), the tokens then are [embedded](/ml/Embeddings-in-Machine-Learning-Explained)
- output text embeddings are classified back into tokens, which then can be decoded into text
- tokenization converts a text into a list of integers
- embedding converts the list of integers into a list of vectors (list of [embeddings](/ml/Embeddings-in-Machine-Learning-Explained))
- positional information about each token is added to embeddings using [positional encodings or embeddings](/ml/transformer-positional-embeddings-and-encodings)

## Tokenization

{% include shared_slides/tokenization-summary.md %}


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