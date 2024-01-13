---
title: Cross-Attention in Transformer Architecture
description: Merge two embedding sequences regardless of modality, e.g., image with text in Stable Diffusion U-Net.
layout: post
categories: ml
image: /images/cross-attention-in-transformer-architecture.png
video: NXjvcNVkX9o
date: 2021-12-28
last_modified_at: 2022-12-30
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2020-11-29-Lambda-Networks-Transform-Self-Attention.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2022-02-26-SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN.md
---



{% include load_video.html %}
{% include mathjax.html %}
{% include highlight-rouge-friendly.css.html %}

Cross attention is:
- an [attention mechanism in Transformer architecture](/ml/transformers-self-attention-mechanism-simplified) that mixes two different embedding sequences
- the two sequences must have the same dimension
- the two sequences can be of different modalities (e.g. text, image, sound)
- one of the sequences defines the output length as it plays a role of a query input
- the other sequence then produces key and value input

## Cross-attention Applications
- [image-text classification](/ml/Multimodal-Image-Text-Classification) with Perceiver
- machine translation: [cross-attention helps decoder predict next token](#cross-attention-in-transformer-decoder) of the translated text

## Cross-attention vs Self-attention

Except for inputs, cross-attention calculation is the same as [self-attention](/ml/transformers-self-attention-mechanism-simplified).
Cross-attention combines asymmetrically two separate embedding sequences of same dimension, in contrast self-attention input is a single embedding sequence.
One of the sequences serves as a query input, while the other as a key and value inputs.
Alternative [cross-attention in SelfDoc](#cross-attention-in-selfdoc), uses query and value from one sequence, and key from the other.

[The feed forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) is related to cross-attention, except the feed forward layer does use softmax and one of the input sequences is static.
[Augmenting Self-attention with Persistent Memory paper](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) shows that Feed Forward layer calculation made the same as self-attention.

{% include image.html src="/images/cross-attention-detail-perceiver-io.png" alt="cross-attention perceiver io detail" %}

## Cross-attention Algorithm
- Let us have embeddings (token) sequences S1 and S2
- Calculate Key and Value from sequence S1
- Calculate Queries from sequence S2
- Calculate [attention matrix](/ml/transformers-self-attention-mechanism-simplified) from Keys and Queries
- Apply queries to the attention matrix
- Output sequence has dimension and length of sequence S2

In an equation: \\( \mathbf{softmax}((W_Q S_2) (W_K S_1)^\intercal) W_V S_1 \\)


## Cross-attention Alternatives
[Feature-wise Linear Modulation Layer](/ml/Feature-wise-Linear-Modulation-Layer) is simpler alternative, which does not require the input to be a sequence and is linear complexity to to calculate.

## Cross-attention Implementation
Have a look at [CrossAttention implementation](https://github.com/huggingface/diffusers/blob/4125756e88e82370c197fecf28e9f0b4d7eee6c3/src/diffusers/models/cross_attention.py) in Diffusers library, which can generate images with **Stable Diffusion**.
In this case the cross-attention is used to **condition transformers inside a UNet layer with a text prompt for image generation**.
The constructor shows, how we can also have **different dimensions** and if you step through with a debugger, you will also see the **different sequence length between the two modalities** . 

```python
class CrossAttention(nn.Module):
    r"""
    A cross attention layer.

    Parameters:
        query_dim (`int`): The number of channels in the query.
        cross_attention_dim (`int`, *optional*):
            The number of channels in the encoder_hidden_states. If not given, defaults to `query_dim`.
        heads (`int`,  *optional*, defaults to 8): The number of heads to use for multi-head attention.
        dim_head (`int`,  *optional*, defaults to 64): The number of channels in each head.
        dropout (`float`, *optional*, defaults to 0.0): The dropout probability to use.
        bias (`bool`, *optional*, defaults to False):
            Set to `True` for the query, key, and value linear layers to contain a bias parameter.
    """
```

In particular at this part, where you can see how query, key, and value interact. This is [encoder-decoder](/ml/Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer) architecture, so query is created from [encoder](/ml/Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer) hidden states.

```python
        query = attn.to_q(hidden_states)
        query = attn.head_to_batch_dim(query)

        encoder_hidden_states = encoder_hidden_states if encoder_hidden_states is not None else hidden_states
        key = attn.to_k(encoder_hidden_states)
        value = attn.to_v(encoder_hidden_states)
        key = attn.head_to_batch_dim(key)
        value = attn.head_to_batch_dim(value)

        attention_probs = attn.get_attention_scores(query, key, attention_mask)
        hidden_states = torch.bmm(attention_probs, value)
```

## Cross-Attention in Popular Architectures
Cross-attention is widely used in [encoder-decoder](/ml/Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer) or multi-modality use cases.

### Cross-Attention in Transformer Decoder
Cross-attention was described in the [Transformer](/ml/transformers-self-attention-mechanism-simplified) paper, but it was not given this name yet.
Transformer decoding starts with full input sequence, but empty decoding sequence.
Cross-attention introduces information from the input sequence to the layers of the decoder,
such that it can predict the next output sequence token.
The [decoder](/ml/Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer) then adds the token to the output sequence, and repeats this autoregressive process until the EOS token is generated.

{% include image.html src="/images/cross-attention-in-transformer-decoder.png" alt="Cross-Attention in the Transformer decoder of Attention is All You Need paper" %}


### Cross-Attention in Stable Diffusion
Stable Diffusion uses cross-attention **for image generation to condition transformers with a text prompt** inside the denoising U-Net layer.

{% include image.html src="/images/stable-diffusion-architecture.png" alt="stable diffusion architecture with cross-attention" %}


### Cross-Attention in Perceiver IO

{% include shared_slides/perceiver-io.md %}


### Cross-Attention in SelfDoc

{% include image.html src="/images/selfdoc-cross-attention.png" alt="selfdoc cross-attention" %}

In [Selfdoc](https://arxiv.org/pdf/2106.03331.pdf), cross-attention is integrated in a special way.
First step of their Cross-Modality Encoder, instead uses value and query from sequence A and then key from the sequence B.

### Other Cross-Attention Examples
- [DeepMind's RETRO Transformer uses cross-attention to incorporate the database retrived sequences](/ml/DeepMinds-RETRO-Transformer-Model)
- [Code example: HuggingFace BERT (key, value are from the encoder, while query is from the decoder)](https://github.com/huggingface/transformers/blob/198c335d219a5eb4d3f124fdd1ce1a9cd9f78a9b/src/transformers/models/bert/modeling_bert.py#L268)
- [CrossVit - here only simplified cross-attention is used](https://arxiv.org/pdf/2103.14899.pdf)
- [On the Strengths of Cross-Attention in Pretrained Transformers for Machine Translation](https://arxiv.org/pdf/2104.08771v1.pdf)


