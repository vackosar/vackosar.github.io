---
title: Transformer Encoder-Only vs Decoder-Only vs Full Transformer
description: Wrap your head around the main Transformer variants in 5 minutes.
layout: post
image: /images/transformer-full-model.png
categories: ml
date: 2023-10-29
last_modified_at: 2023-10-29
permalink: /:categories/:title
---

![Transformer full model diagram](/images/transformer-full-model.png)


People keep asking me about, what is the difference between encoder, decoder, and normal transformer.
It is a simple thing, you can master quickly.

### Encoder-only (BERT)
[BERT](https://aclanthology.org/N19-1423/) has Encoder-only architecture.
Input is text and output is sequence of [embeddings](/ml/Embeddings-in-Machine-Learning-Explained).
Use cases are sequence classification (class token), token classification.
It uses bidirectional attention.


### Decoder-only (GPT4)
[GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) has Decoder-only architecture.
Input is text and output is the next word (token), which is then appended to the input.
Use cases are mostly text generation, but with [prompting](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM) we can do many things including sequence classification.



### Encoder-Decoder T5
[T5](https://arxiv.org/abs/1910.10683) has [Encoder-Decoder or Full-Transformer](https://arxiv.org/abs/1706.03762).
Input is text and output is the next word (token), which is then appended to the decoder-input.
Encoder decoder uses cross-attention to introduce information from the encoder into the decoder.

Cross-attention is unidirectional information flow  both the source sequence and the target sequence simultaneously, less and less attention will be focused on the source sequence as the target sequence length grows. This is the attention degeneration problem.
https://arxiv.org/pdf/2304.04052.pdf



### Which to Choose When?
The decoder model just appends text, so if we have significant distribution difference between the input and the output, for example completely different set of tokens, we can expect that encoder-decoder would work better.


- decoder-only: strong at text generation tasks (models for prompting, chatting)
- encoder-decoder: strong for NLU. For example translation, question answering, summarization.
  - In this older pre-RLHF paper,  


[We find that pretrained non-causal decoder models can be adapted into performant generative causal decoder models, using autoregressive language modeling as a downstream task. Furthermore, we find that pretrained causal decoder models can be efficiently adapted into non-causal decoder models, ultimately achieving competitive performance after multitask finetuning.](https://arxiv.org/abs/2204.05832)

