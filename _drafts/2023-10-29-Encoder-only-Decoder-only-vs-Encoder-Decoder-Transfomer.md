---
title: Encoder-Only vs Decoder-Only vs Encoder-Decoder Transformer
description: Wrap your head around the main Transformer variants in 5 minutes.
layout: post
image: /images/transformer-encoder-decoder.png
categories: ml
date: 2023-10-29
last_modified_at: 2023-10-29
permalink: /:categories/:title
---

![Transformer encoder-decoder model diagram](/images/transformer-encoder-decoder.png)


People keep asking me about, what is the difference between encoder, decoder, and normal transformer.
It is a simple thing, you can master quickly.

### Encoder-only (BERT)
[BERT](https://aclanthology.org/N19-1423/) has Encoder-only architecture.
Input is text and output is sequence of [embeddings](/ml/Embeddings-in-Machine-Learning-Explained).
Use cases are sequence classification (class token), token classification.
It uses bidirectional attention, so the model can see forwards and backwards.


### Decoder-only (GPT4)
[GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) has Decoder-only architecture.
Input is text and output is the next word (token), which is then appended to the input.
Use cases are mostly text generation (autoregressive), but with [prompting](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM) we can do many things including sequence classification.
The attention is almost always causal (unidirectional), so the model can see only previous tokens (prefix). 



### Encoder-Decoder T5
![](/images/t5-text-to-text.png)

[T5](https://arxiv.org/abs/1910.10683) has [Encoder-Decoder or Full-Transformer](https://arxiv.org/abs/1706.03762).
Input is text and output is the next word (token), which is then appended to the decoder-input.
Encoder decoder uses cross-attention to introduce information from the encoder into the decoder.

Cross-attention is unidirectional information flow  both the source sequence and the target sequence simultaneously, less and less attention will be focused on the source sequence as the target sequence length grows. This is the attention degeneration problem.
https://arxiv.org/pdf/2304.04052.pdf



### Decoder-Only vs Encoder-Decoder
The intuition is that, the decoder model just appends text, so if we have significant distribution difference between the input and the output, for example completely different set of tokens, we can expect that encoder-decoder would work better. And the decoder (prefix model) and sees only the past, and so any task that involves seeing entire text context and addressing specific tokens is a bit more complex for it. However, decoder-only is simpler architecture than Encoder-decoder, and it is already [Turing-complete](https://arxiv.org/pdf/2305.17026.pdf) and size of the model and training is likely the biggest factor in most cases ([The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)). 

To make relevant apples to apples comparison, we can compare these in compute-matched or parameter-match way, but it is hard to get rid of major differences in training objectives, which likely play the decisive role.

In the [Flan-UL2 paper](https://arxiv.org/abs/2205.05131), authors attempted to reduce training differences by reformulating fill-in-the-blank task (denoising) into generative (autoregressive or prefix-language modelling setting) - this is called Mixture of Denoisers. Furthermore, they seem to use the same encoder-decoder model in both generative way (autoregressive) and encoder-decoder way. Also in [Flan-UL2 paper](https://arxiv.org/abs/2205.05131), their best model was 20b parameter encoder-decoder.


![](/images/mixture-of-denoisers-for-UL2-formulated-auto-regressively.png)


In this older pre-RLHF paper, [Encoder-decoder models trained with masked language modeling achieve the best zero-shot performance after multitask finetuning](https://arxiv.org/pdf/2204.05832.pdf).


For details, there is [a difference between decoder-only causal and prefix LM](https://arxiv.org/pdf/1910.10683.pdf):
![encoder-decoder-language-model-prefix-lm.png](/images/encoder-decoder-language-model-prefix-lm.png)


### How to Choose?
Personally, I will choose based on what pretrained model is available and howeasy is it to adopt it for the task at hand.
It is unclear what architecture may be the best from the start. Perhaps minor consideration could be following:

- decoder-only: strong at text generation tasks (models for prompting, chatting)
- encoder-decoder: strong for natural language understanding (NLU). For example translation, question answering, summarization.

