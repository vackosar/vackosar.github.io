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

Let's say you have a generative AI (generative machine learning) problem, so you have some input data, and some corresponding output data.
But you have only a small quantity of this data.

Synthetic data helps where you need to add missing hard to collect data needed for your predictions.
This data could be something people never write down or say.
For example human thoughts when problem-solving usually don't get written down.

The rarer and more important the data the more important this data can be.

If nothing like this data was present during the model pretraining, you won't be able to prompt-instruct the model to perform this.
Few shot examples can help, but the more complex the problem, the more likely you will need more examples, which are costly to write by hand.


## Why synthetic data makes sense?
Real data costs human time and synthetic data can be a way around that.
But you cannot create the required data out of thin air synthetically.

You need:
1. either more general model that was essentially trained one something similar to the target data needed,
2. or you need a real data that is close to the required data, and perform only an easy modification to match the required data distribution.


## Verification of Synthetic Data
Garbage-in implies garbage-out.
The more difficult data to generate or more distant to the real training data, the harder it is to synthesize correct data to train on.

In some problems verification is easier that generation, so in these cases you can remove the invalid data out of the generated data.

Fo example, the goal may be to solve simple addition problems given in a textual format, which is easily machine-extractable.
In this case, it is very easy to verify that the generated summation is correct.


## Levels of Synthetic Data
Here is a spectrum of increasingly less human involvement in the process or human leverage in the process or model development.

1. Fully manual: You would love to train on data from people that is fully manually written and verified.
2. Cleaned up manual data: The data is manually written, but rewritten, rephrased or cleaned by a machine, then verified.  
3. The data is entirely generated, but manually verified and select each sample and labelled.
4. The data is entirely generated, and rated by a machine. Trained model is evaluated on a small human labelled subset.
5. Fully autonomous: The data is entirely generated, and rated by a machine. Trained model is evaluated on a machine generated data.


## Examples of Synthetic Data Uses

### [DSPy](https://github.com/stanfordnlp/dspy?tab=readme-ov-file) (Python Library)
Fine-tune smaller models on using small amount of labelled examples and prompting to generate synthetic fine-tuning data. 


### [Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/html/2312.09390v1)
Smaller model teacher model, generates inputs, and labels.
The bigger model can learn to outperform the smaller teacher, if allowed to be "over-confident".
However, I think this approach is not generally proven for all situations and still seems to show upper performance limit.


### [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
A math reasoning dataset.
