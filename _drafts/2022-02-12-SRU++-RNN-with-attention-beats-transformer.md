---
title: "SRU++ Model Speedup Transformer with the Simple Recurrent Unit"
description: "Scaling Transformer with SRU, Terraformer, and "
layout: post
categories: book
tag: ml
date: 2022-02-26
permalink: /:categories/:title
---

{% include mathjax.html %}

<img src="/images/sru++-bits-per-character-on-enwik8.png" alt="SRU++ Simple Recurrent Unit on Enwik8 bits per character" />

Here are my notes on SRU, and thanks to the paper authors and Yannic's Discord meetup discussions.

- https://discord.com/channels/714501525455634453/780793106496880650/941342791349440514
- [Simple Recurrent Units for Highly Parallelizable Recurrence](https://arxiv.org/abs/1709.02755)
- [Sparse is Enough in Scaling Transformers](https://arxiv.org/pdf/2111.12763.pdf)

# Attention and Recurrence
- attention vs recurrence = graph vs sequence
- [original recurrent LSTM](https://www.bioinf.jku.at/publications/older/2604.pdf) is less parallelizable than [Transformer](https://arxiv.org/pdf/1706.03762v5.pdf)
  - because future steps in LSTM depend on the past?
  
# How SRU helps parallelization?
- while the state computation of SRU is time-dependent, each state dimension is independent
- time step: \\( t \\)
- input vector: \\( x_t \\)
- state vectors: \\( c_t \\)
- forget gate \\( f_t \\)
- typically: \\( f_t = \sigma(W_f x_t + V_f c_{t-1} + b_f) \\)
  - problem: both \\( c_t, f_t \\) depend on all dimensions \\( c_{t-1} \\) 
  - due to matrix-multiplication: \\( V_f c_{t-1} \\)
  - solution: point-wise multiplication \\( v_f \odot c_{t-1} \\)
  - gives parallel computation \\( c_t, f_t \\)
