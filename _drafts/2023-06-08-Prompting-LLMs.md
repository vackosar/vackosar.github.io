---
title: Instant Prompt Engineering for Large Language Models
description: Instruct your GPT to generate the best tokens on the first shot.
categories: ml
date: 2023-06-08
last_modified_at: 2023-06-08
layout: post
permalink: /:categories/:title
---

- recording!

When **given input**, we want the model to correctly **generate output**.
Language models are trained to predict text continuation with extract tuning for conversations and instruction following.
We steer the model with a small additional textual context, such that it **learns in context** without large amount of training data.
This additional context is called prompt.
Systematic development of the prompt is called prompt engineering.


## Task Instruction (Zero-Shot Prompting)
Describe the task:
- intent (detect product review sentiment)
- audience (5 year old)
- persona (expert marketer)
- specific and precise terms, e.g., avoiding generic word "not".


## Input-Output Examples (One-shot, Few-Shot prompting)
Provide examples such that
- Changing order of examples can change results. Recent examples are more likely to be reproduced.
- Representative ordered examples at least random - For multiple choice outputs you may want to debias the model to prevent repeating the last answer.
- Similar or relevant examples to the input - For an input search KNN clustering for finding semantically similar examples to provide into the prompt.
- Diverse examples between each other - If you have static prompt, instead select diverse examples with clustering.
- Difficult to answer examples - select most difficult questions for prompt based on difficulty to answer by the model.



## Reasoning in Steps (Chain-of-Thought (CoT) Prompting)
Steer the model to generate text that will guide it towards the correct answer.
Append instruction "Let's think step by step."



## Self-evaluated Reasoning Search (Tree of Thoughts Problem Solving (ToT))



