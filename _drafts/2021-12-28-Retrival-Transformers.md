---
layout: post
title: "Transformers and Retrieval"
date: 2021-12-28
categories: ml
description: "-"
permalink: /:categories/:title
---

# DeepMind's Retrieval Transformer
- LM
- condition on document chunks
- retried based on similarity with preceding tokens
- same perf GPT-3 with 25x less params


# Training Dataset
- multilingual MassiveText
- SentencePiece tokenizer vocabulary of 128k tokens
- Retrieval database 1.75T tokens of text
- Chucks are consecutive 64 token sequences
- not retrieval from the same document during training
 
# Architecture
- Frozen BERT retriever on chunk level
- differentiable encoder conditioned on query
- chunked cross-attention


# Retriever
- database is key-value memory
- frozen BERT vectorizes the chunks
- values are two consecutive chunks
- keys are the first chunk
- 2T db queried in 10ms
- retrieval is part of the input dataset pipeline

# Encoding Retrieved Neighbours
- 


# Cross Attention
- Let us have sequence A and sequence B
- Attention matrix from sequence A is used to highlight in sequence B
- Queries from sequence A
- Keys and Values from another sequence B
- Similar [the feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory)
- sequences A and B lengths can differ
