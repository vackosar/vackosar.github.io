---
title: Synthetic Data
description: TBD.
categories: ml
date: 2024-02-11
last_modified_at: 2024-02-13
layout: post
permalink: /:categories/:title
---

[//]: # ({% include mermaidjs.html %})
{% include highlight-rouge-friendly.css.html %}

[//]: # ({% include image.html alt="Bellman Update and Synthetic Data in Q-Transformer" src="/images/bellman-update-q-transformer-thumb.png" %})



Here are my notes on synthetic data. Take it with grain of salt, as I am new in this area.


## Why synthetic data makes sense?
Here is a spectrum of increasingly less human involvement in the process or human leverage in the process or model development.

1. Fully manual: You would love to train on data from people that is fully manually written and verified.
2. Cleaned up manual data: The data is manually written, but rewritten, rephrased or cleaned by a machine, then verified.  
3. The data is entirely generated, but manually verified and select each sample and labelled.
4. The data is entirely generated, and rated by a machine. Trained model is evaluated on a small human labelled subset.
5. Fully autonomous: The data is entirely generated, and rated by a machine. Trained model is evaluated on a machine generated data.


## Papers
[Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/html/2312.09390v1)

