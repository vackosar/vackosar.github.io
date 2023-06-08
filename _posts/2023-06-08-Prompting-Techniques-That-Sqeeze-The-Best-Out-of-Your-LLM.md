---
title: Prompting Techniques That Squeeze the Best Out of Your LLM
description: From the simplest to the most advanced, instruct your GPT for the best generation.
categories: ml
image: /images/squeeze-robot-hand-orange.png
date: 2023-06-08
last_modified_at: 2023-06-08
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2016-07-16-Boost-Jog-Morale-Using-Mil-Cadence.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2020-07-05-Transfigure-Stress-Into-Energy.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
---

![squeeze-robot-hand-orange](/images/squeeze-robot-hand-orange.png)


For **given input**, you want the model to correctly **generate output**.
There is natural path from the simplest to the most advanced approaches, up to final tuning of the model.
This post guides your through these techniques in a simple way.

[Large language models (LLMs)](/ml/Understand-Large-Language-Models-like-ChatGPT) like ChatGPT ([GPT-3](https://arxiv.org/pdf/2005.14165.pdf)), Claude, Bard are trained to predict text continuation with extra tuning for following conversations and instructions (RLHF).
We steer the model with a small additional textual context, such that it **learns in context** without large amount of training data.
This additional context is called prompt.
Systematic development of prompts using metric evaluation is called prompt engineering.


## Trade-offs in Prompting
- Longer the prompt the more expensive in terms of time and compute. For example, more examples provided, the longer prompt. Training a specific model may be
- If the model changes the prompt may stop being optimal, in that case there is little point over-optimizing it. For example, ChatGPT or GPT-4 is changed often by OpenAI. The models are meant to be general not specific to your problem.
- Control guardrails vs creative hallucinations. Certain prompts may be prone to more hallucinations over others.


## Task Instruction
Also called Zero-Shot Prompting.

Describe the task:
- intent (detect product review sentiment)
- audience (5 year old)
- persona (expert marketer)
- specific and precise terms, e.g., avoiding generic word "not".

![GPT-3 Zero-shot](/images/gpt-3-zero-shot-prompting.png)


## Input-Output Examples
Also called One-shot, Few-Shot prompting.

Provide examples such that
- Changing order of examples can change results. Recent examples are more likely to be reproduced.
- Representative ordered examples at least random - For multiple choice outputs you may want to debias the model to prevent repeating the last answer.
- Similar or relevant examples to the input - For an input search KNN clustering for finding semantically similar examples to provide into the prompt.
- Diverse examples between each other - If you have static prompt, instead select diverse examples with clustering.
- Difficult to answer examples - select most difficult questions for prompt based on difficulty to answer by the model.

![Language Models are Few-Shot Learners](/images/gpt-3-few-shot-prompting.png)


## Reasoning in Steps
Also called [Chain-of-Thought (CoT) Prompting](https://arxiv.org/pdf/2201.11903.pdf).

Your step-by-step instruction creates a momentum such that the model generates a text that guides it towards the correct answer.
The reasoning steps increase interpretability.
Append instruction "Let's think step by step." or provide reasoning examples.
For example: multi-step arithmetic, commonsense logical reasoning.
Model's ability to use [CoT increases with model size (see PaLM and its ability to explain jokes)](/ml/googles-pathways-language-model-and-chain-of-thought).

![Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](/images/palm-chain-of-though-prompting.png)


## Majority Vote Reasoning Steps
Also called Self-consistency with Chain-of-Thought (CoT-SC).

Generate multiple reasoning paths (chains of thought), then return the most common answer.


## Self-evaluated Reasoning Search
Also called [Tree of Thoughts Problem Solving (ToT)](https://arxiv.org/pdf/2305.10601.pdf).

Generate explicitly decomposable thoughts, evaluate progress of each unfinished thought chain, and efficiency explore with an search algorithm.
This has analogies to [AlphaZero](https://arxiv.org/pdf/1712.01815.pdf) for playing chess.

My criticism is that the evidence is low with only 3 toy examples and the technique requires additional problem specific edits.

![Tree of Thoughts Problem Solving comparison with Chain-of-Thought](/images/tree-of-thought-tot-comparison-cot.png)


### Thought Decomposition in ToT
Designed problem-specific meaningful thought size and separation. For example a paragraph, or an equation.

![three of thought input, output, thoughts](/images/three-of-thought-input-output-thoughts-steps.png)


### Thought and Value Generation in ToT
Designed problem-specific prompts thought-prompt. Propose or sample generate depending on the output size.


### Evaluation-prompt in ToT
Designed problem-specific prompt for reflecting on the thoughts "state".
Either:
- Value of state: Generate value of a specific step or "chain".
- Vote: across states: Based on all steps, the model compares and select the most promising.


### Search Algorithm in ToT
Explore the most promising paths until solution, bad state, or depth limit:
- Breadth-first search (BFS): Keep only most promising states, then generate to deeper the level for all, prune. Iterate.
- Depth-first search (DFS): Keep going deeper until solution, bad state, or depth limit. Then backtrack, exclude already visited.


### Examples in ToT

#### Game of 24
- Game of 24 is a mathematical reasoning challenge, where the goal is to use 4 numbers and basic arithmetic operations (+-*/) to obtain 24. For example, given input “4 9 10 13”, a solution output could be “(10 - 4) * (13 - 9) = 24”. We decompose by choosing the numbers from the left to the right.

![](/images/tree-of-thought-tot-game-of-24.png)

![](/images/tree-of-thought-tot-game-of-24-results.png)


##### Creative Writing

![](/images/tree-of-thought-tot-creative-writing-results.png)


## Generating Optimal Prompts
Models can be used to generate their own optimal prompts.
- TODO


## Tool Use
Models can use external tools by generating API calls, when it is advantageous.
For example, if there is a question for some sort of calculation. [Toolformer method](https://arxiv.org/abs/2302.04761) can use a small training sets, you can teach it to call a calculate function, which it can use to do the calculation for it. It will get the results as into the text and instead of predicting the function output, it would get the output from the tool. It would sort of stop predicting for a couple tokens and get the result. With this you can improve actual performance on dedicated tasks for, you can do retrieval for question answering.
- TODO


## Fine-Tuning Training

When we have enough data, we can fine-tune the model weights to increase performance.
There are some cheaper methods like LoRA and more expensive methods.