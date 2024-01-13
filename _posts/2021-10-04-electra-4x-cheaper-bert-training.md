---
layout: post
title: ELECTRA - How to Train BERT 4x Cheaper
date: 2021-10-04
categories: ml
description: Reducing training flops 4x by GAN-like discriminative task compared to RoBERTa-500K transformer model.
permalink: /:categories/:title
image: /images/electra-thumb.png
video: svDvV97wuiE
my_related_post_paths:
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2021-12-29-DeepMinds-RETRO-Transformer-Model.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
---



{% include load_video.html %}

Can you afford to fully train and retrain your own BERT language model?
Training costs is important part of machine learning production as [transformer language models](/ml/transformers-self-attention-mechanism-simplified) get bigger.
ELECTRA model is being adopted by the industry to reduce training expenses. For example [reportedly used in a web search engine Seznam](https://www-root-cz.translate.goog/clanky/rychla-oprava-dotazu-ve-vyhledavaci-pomoci-neuronovych-siti/?_x_tr_sl=cs&_x_tr_tl=en&_x_tr_hl=cs&_x_tr_pto=nui),
which capable to locally compete with Google in the Czech Republic.
ELECTRA is also available on [HuggingFace](https://huggingface.co/transformers/model_doc/electra.html) including a model for pre-training.


## Why Is BERT Training Inefficient?
- [BERT is transformer model](/ml/transformers-self-attention-mechanism-simplified)
- Uses unsupervised pre-training
- Encodes text into WordPiece tokens 
- pre-training task is masked language modeling (MLM) 
  - Pre-training replaces 15% inputs with "[MASK]" token,
  - Then predicts original token ids based on context
- __Every step costs me__,
- But __only a few tokens are masked in each step__!

{% include image.html src="/images/electra-bert.png" alt="BERT model pre-training and fine-tuning" %}


## BERT vs ELECTRA Training
How to get difficult enough task for all tokens instead of just the tokens masked?
- enter [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators ](https://openreview.net/pdf?id=r1xMH1BtvB)
  - ELECTRA = Efficiently Learning an Encoder that Classifies Token Replacements Accurately
  - Stanford & Google Brain
  - ICRL 2020, Not SoTA
- ELECTRA trains in GAN-like setting:
- trained BERT model is the discriminator
- smaller generator has [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) also
  - Jointly train the generator and discriminator
  - The generator is trained with masked language modeling (MLM) 
  - For each masked position generator samples one token
- The big model discriminates true or fake token
- Not exactly GAN setup: Generator is trained for MLM
 
{% include image.html src="/images/electra-generator-discriminator.png" alt="ELECTRA model generator discriminator pre-training diagram" %} 


## ELECTRA Model Architecture and Methods
- Generator and discriminator same architecture
  - only embeddings or tokens and positional are shared
  - sharing more was not helping
- Generator 2x - 4x smaller
  - bigger are not helping
  - compute more expensive
  - perhaps bigger too difficult task
- Both trained jointly otherwise discriminator fails to learn
  - otherwise, the discriminator fails to learn
  - generator selects harder cases
  - but must not be too much better than discriminator
- mildly resembles [DINO's momentum teacher-student](https://ai.facebook.com/blog/dino-paws-computer-vision-with-self-supervised-transformers-and-10x-more-efficient-training)
  
![ELECTRA model loss is sum of generator masked language modeling and discriminator loss](../images/electra-loss.png)

{% include image.html src="/images/electra-generator-size.png" alt="ELECTRA model generator size and GLUE benchmark performance" %}


## ELECTRA vs BERT vs RoBERTA vs XLNext Performance Results
- Datasets:
  - GLUE: natural understanding benchmark
  - SQuAD: questions answering benchmark
- RoBERTa = BERT with better training and dataset
  - longer training, bigger batches, more data
  - remove next sentence objective
  - train on longer sequences
  - dynamically changing masking pattern
- XLNet = BERT with permutation language modelling
  - maximizes likelihood of the original sequence
  - compared to all other permutations
  - next-token prediction task
- ELECTRA-400K on par with RoBERTa-500K with 4x less FLOPs

{% include image.html src="/images/electra-results-glue.png" alt="ELECTRA model performance on GLUE benchmark" %}

{% include image.html src="/images/electra-results-squad.png" alt="ELECTRA model performance on SQuAD benchmark" %}


## ELECTRA Source of The Improvement
- compared alternative tasks on GLUE score
- results:
  - loss over all inputs is important
  - masking is worse than replacing tokens

<table class="table">
  <thead>
    <tr><th>Task</th><th>Description</th><th>GLUE score</th></tr>
  </thead>
  <tbody>
    <tr><td>BERT</td><td>MLM with [MASK] token</td><td>82.2</td></tr>
    <tr><td>Replace MLM</td><td>masked tokens replaced with generated + LM</td><td>82.4</td></tr>
    <tr><td>Electra 15%</td><td>Discriminator over 15% of the tokens</td><td>82.4</td></tr>
    <tr><td>All-Tokens MLM</td><td>Replace MLM on all tokens + copy mechanism</td><td>84.3</td></tr>
    <tr><td>Electra</td><td>Discriminator over all tokens</td><td>85.0</td></tr>
  </tbody>
</table>


## Personal Speculations:
- ELECTRA could be suitable for low-resource settings
  - Since ELECTRA converges faster
  - perhaps [less data is needed](https://arxiv.org/pdf/2010.08127.pdf)
- ELECTRA training is like augmentation:
  - samples again from generator on each epoch

## Follow up - MC-BERT
- [MC-BERT Paper](https://arxiv.org/pdf/2006.05744.pdf)
- Contrastive instead of discriminative
 
![MC-BERT model extension of ELECTRA diagram](../images/electra-mcbert.png)


## Follow Up - TEAMS
- also contrastive
- shares more weights

![TEAMS model extension of ELECTRA diagram](../images/electra-teams.png)


## Read More About BERT
Read more about [BERT, transformer architecture, self-attention, training, and deployment](/ml/transformers-self-attention-mechanism-simplified)