---
title: Prompt Engineering for Large Language Models
description: Instantly instruct your GPT to generate the best tokens on the first shot.
categories: ml
date: 2023-06-08
last_modified_at: 2023-06-08
layout: post
permalink: /:categories/:title
---

- recording!

When **given input**, we want the model to correctly **generate output**.
Large language models (LLMs) like ChatGPT ([GPT-3](https://arxiv.org/pdf/2005.14165.pdf)), Claude, Bard are trained to predict text continuation with extra tuning for following conversations and instructions (RLHF).
We steer the model with a small additional textual context, such that it **learns in context** without large amount of training data.
This additional context is called prompt.
Systematic development of the prompt is called prompt engineering.


## Trade-offs in Prompting
- Longer the prompt the more expensive in terms of time and compute. For example, more examples provided, the longer prompt.
- If the model changes the prompt may stop being optimal, in that case there is little point over-optimizing it. For example, ChatGPT or GPT-4 is changed often by OpenAI.


## Task Instruction
(Zero-Shot Prompting)

Describe the task:
- intent (detect product review sentiment)
- audience (5 year old)
- persona (expert marketer)
- specific and precise terms, e.g., avoiding generic word "not".

![GPT-3 Zero-shot](/images/gpt-3-zero-shot-prompting.png)


## Input-Output Examples
(One-shot, Few-Shot prompting)

Provide examples such that
- Changing order of examples can change results. Recent examples are more likely to be reproduced.
- Representative ordered examples at least random - For multiple choice outputs you may want to debias the model to prevent repeating the last answer.
- Similar or relevant examples to the input - For an input search KNN clustering for finding semantically similar examples to provide into the prompt.
- Diverse examples between each other - If you have static prompt, instead select diverse examples with clustering.
- Difficult to answer examples - select most difficult questions for prompt based on difficulty to answer by the model.

![Language Models are Few-Shot Learners](/images/gpt-3-few-shot-prompting.png)


## Reasoning in Steps
([Chain-of-Thought (CoT) Prompting](https://arxiv.org/pdf/2201.11903.pdf))

Steer the model to generate text that will guide it towards the correct answer.
The reasoning steps increase interpretability.
Append instruction "Let's think step by step." or provide reasoning examples.
For example: multi-step arithmetic, commonsense logical reasoning.

![Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](/images/palm-chain-of-though-prompting.png)


## Majority Vote Reasoning Steps
(Self-consistency with Chain-of-Thought (CoT-SC))

Generate multiple reasoning paths (chains of thought), then return the most common answer.


## Self-evaluated Reasoning Search
([Tree of Thoughts Problem Solving (ToT)](https://arxiv.org/pdf/2305.10601.pdf))

Generate explicitly decomposable thoughts, evaluate progress of each unfinished thought chain, and efficiency explore with an search algorithm.


### Thought Decomposition

Designed problem-specific meaningful thought size and separation. For example a paragraph, or an equation.

![three of thought input, output, thoughts](/images/three-of-thought-input-output-thoughts-steps.png)


### Thought and Value Generation
Designed problem-specific prompts thought-prompt. Propose or sample generate depending on the output size.


### Evaluation-prompt
Designed problem-specific prompt for reflecting on the thoughts "state".
Either
- Value of state: Generate value of a specific step or "chain".
- Vote: across states: Based on all steps, the model compares and select the most promising.


### Search Algorithm
Explore the most promising paths until solution, bad state, or depth limit:
- Breadth-first search (BFS): Keep only most promising states, then generate to deeper the level for all, prune. Iterate.
- Depth-first search (DFS): Keep going deeper until solution, bad state, or depth limit. Then backtrack, exclude already visited.


### Examples

#### Game of 24
- Game of 24 is a mathematical reasoning challenge, where the goal is to use 4 numbers and basic arithmetic operations (+-*/) to obtain 24. For example, given input “4 9 10 13”, a solution output could be “(10 - 4) * (13 - 9) = 24”. We decompose by choosing the numbers from the left to the right.

![](/images/tree-of-thought-tot-game-of-24.png)

![](/images/tree-of-thought-tot-game-of-24-results.png)


##### Creative Writing

![](/images/tree-of-thought-tot-creative-writing-results.png)


## Generating Optimal Prompts
- TODO


## Tool Use
- TODO


## Fine-Tuning Training

When we have enough data, we can fine-tune the model weights to increase performance.
There are some cheaper methods like LoRA and more expensive methods.