---
title: Encoder-Only vs Decoder-Only vs Encoder-Decoder Transformer
description: Wrap your head around the main Transformer variants in 5 minutes.
layout: post
image: /images/transformer-encoder-decoder.png
categories: ml
date: 2023-10-29
last_modified_at: 2023-10-29
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2021-10-04-electra-4x-cheaper-bert-training.md
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
---

![Transformer encoder-decoder model diagram (Attention is all you need)](/images/transformer-encoder-decoder.png)


People keep asking me about, what is the difference between encoder, decoder, and normal [transformer (with self-attention)](/ml/transformers-self-attention-mechanism-simplified).
It is a simple thing, you can master quickly.

### Encoder-only (BERT)
[BERT](https://aclanthology.org/N19-1423/) has Encoder-only architecture.
Input is text and output is sequence of [embeddings](/ml/Embeddings-in-Machine-Learning-Explained).
Use cases are sequence classification (class token), token classification.
It uses bidirectional attention, so the model can see forwards and backwards.

![bidirectional attention in BERT vs unidirectional (causal) attention in GPT](/images/bert-vs-GPT.png)


### Decoder-only (GPT4)
[GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) has Decoder-only architecture.
Input is text and output is the next word (token), which is then appended to the input.
Use cases are mostly text generation (autoregressive), but with [prompting](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM) we can do many things including sequence classification.
The attention is almost always causal (unidirectional), so the model can see only previous tokens (prefix). 



### Encoder-Decoder T5
![T5 encoder-decoder multi-task visualization](/images/t5-text-to-text.png)

[T5](https://arxiv.org/abs/1910.10683) has [Encoder-Decoder or Full-Transformer](https://arxiv.org/abs/1706.03762).
Input is text and output is the next word (token), which is then appended to the decoder-input.
Encoder decoder uses cross-attention to introduce information from the encoder into the decoder.


### Decoder-Only vs Encoder-Decoder
The intuition is that, the decoder model just appends text, so if we have significant distribution difference between the input and the output, for example completely different set of tokens, we can expect that encoder-decoder would work better. And the decoder (prefix model) and sees only the past, and so any task that involves seeing entire text context and addressing specific tokens is a bit more complex for it. However, decoder-only is simpler architecture than Encoder-decoder, and it is already [Turing-complete](https://arxiv.org/pdf/2305.17026.pdf) and size of the model and training is likely the biggest factor in most cases ([The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)). 

To make relevant apples to apples comparison, we can compare these in latency or compute-matched or parameter-match way, but it is hard to get rid of major differences in training objectives, which likely play the decisive role.

In the [Flan-UL2 paper](https://arxiv.org/abs/2205.05131), authors attempted to reduce training differences by reformulating fill-in-the-blank task (denoising) into generative (autoregressive or prefix-language modelling setting) - this is called Mixture of Denoisers. Furthermore, they seem to use the same encoder-decoder model in both decoder-only way and encoder-decoder way. Also in [Flan-UL2 paper](https://arxiv.org/abs/2205.05131), their best model was 20b parameter encoder-decoder.

Futhermore, Compute matched encoder-decoder models in UL2 paper have approximately twice the number of parameters as the decoder models but similar speeds and accuracy. This indicates that encoder-decoder may have [more sparsity that may be taken out with some pruning](/ml/Neural-Network-Pruning-Explained) or distillation techniques to eventually outperform.


![UL2 formulation of masking tasks in a autoregressive way](/images/mixture-of-denoisers-for-UL2-formulated-auto-regressively.png)


In this older pre-RLHF paper, [Encoder-decoder models trained with masked language modeling achieve the best zero-shot performance after multitask finetuning](https://arxiv.org/pdf/2204.05832.pdf).


For details, there is [a difference between decoder-only causal and prefix LM](https://arxiv.org/pdf/1910.10683.pdf). Prefix-LM has a section that has non-causal (bidirectional attention) token dependencies like BERT:
![encoder-decoder-language-model-prefix-lm.png](/images/encoder-decoder-language-model-prefix-lm.png)


### How to Choose?
Personally, I will choose based on what pretrained model is available and how easy is it to adopt it for the task at hand.
It is unclear what architecture may be the best from the start. Perhaps minor consideration could be following:

- decoder-only: strong at text generation tasks (models for prompting, chatting)
- encoder-decoder: strong for natural language understanding (NLU). For example translation, question answering, summarization.

