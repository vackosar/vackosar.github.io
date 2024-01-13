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
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
- _posts/2021-10-04-electra-4x-cheaper-bert-training.md
---

{% include image.html src="/images/squeeze-robot-hand-orange.png" alt="squeeze-robot-hand-orange" %}


For **given input**, you want the model to correctly **generate output**.
There is a natural path from the simplest most crude to the most advanced fine-tuning of the model.
This post guides your through these techniques in a simple way.

[Large language models (LLMs)](/ml/Understand-Large-Language-Models-like-ChatGPT) like ChatGPT ([GPT-3](https://arxiv.org/pdf/2005.14165.pdf)), Claude, Bard are trained to predict text continuation with extra tuning for the following conversations and instructions (RLHF).
We steer the model with a small additional textual context, such that it **learns in context** without a large amount of training data.
This additional context is called prompt.
Systematic development of prompts using **metric evaluation is called prompt engineering**.

## Trade-offs in Prompting
- Longer prompts are the more expensive in terms of **latency and compute**. For example, more examples provided, the longer prompt. Training a specific model or selecting samples intelligently are possible solutions.
- More complex and longer the prompt, less likely the model will be able to follow all the rules. Try to break the problem to simpler problems with simpler instructions.
- If the **model changes** the prompt may stop being optimal, in that case, there is little point **over-optimizing** it. For example, ChatGPT or GPT-4 is often changed by OpenAI. The models are meant to be general not specific to your problem.
- Control guardrails vs creative hallucinations. Certain prompts may be prone to more hallucinations over others. Can you verify the results? Can you measure performance of the model?
- Prompts are a crude tool without nuance and can be "over prompted" (prompt injection) with user's own instructions, whereas fine-tuning requires more initial investment, data, and is complicated. 


## Task Instruction
Also called Zero-Shot Prompting.

Describe the task:
- intent (detect product review sentiment)
- audience (5-year-old)
- persona (expert marketer)
- specific and precise terms, e.g., avoiding generic word "not".

{% include image.html src="/images/gpt-3-zero-shot-prompting.png" alt="GPT-3 Zero-shot" %}


## Input-Output Examples
Also called One-shot, Few-Shot prompting. The examples, can be described within the system message, or in separate messages input in user's message and output in assistant's messages.

Provide examples such that
- Changing order of examples can change results. Recent examples are more likely to be reproduced.
- Representatively ordered examples at least random - For multiple choice outputs you may want to debias the model to prevent repeating the last answer.
- Similar or relevant examples to the input - For an input search KNN clustering for finding semantically similar examples to provide into the prompt.
- Diverse examples between each other - If you have static prompt, instead select diverse examples with clustering.
- Difficult to answer examples - select most difficult questions for prompt based on difficulty to answer by the model.

{% include image.html src="/images/gpt-3-few-shot-prompting.png" alt="Language Models are Few-Shot Learners" %}


## [TELeR Prompting Taxonomy](https://arxiv.org/pdf/2305.11430.pdf)
{% include image.html src="/images/TELeR-prompt-taxonomy-levels-turn-expression-level-of-details-role.png" alt="TELeR paper prompt-taxonomy-levels-turn-expression-level-of-details-role" %}

## Level 5 prompt
Level 5 prompt is a complex directive prompt that includes the following in the order of detail:
1. Description of high-level goal
2. A detailed bulleted list of sub-tasks
3. An explicit statement asking LLM to explain its own output
4. Few-shot examples and description of good and bad output
5. Retrieved information from external sources based on the specific input

In Level 6 prompt, the paper recommends appending also asking LLM to explain its own output.


### Key Dimensions in Prompting
1. Turn: Single or multi-turn based on interaction length.
2. Expression: Question-style or instruction-style based on directive form.
3. Role: System-role defined or undefined before prompting.
4. Level of Details: Seven levels (0-6) indicating directive specificity and clarity.


## Key Factors in Prompting
1. Clear Goals: Define precise objectives to guide the model's understanding.
2. Associated Data: Clarify if the prompt includes data and distinguish it from instructions.
3. Distinct Sub-Tasks: Outline multiple steps as separate items for clarity and organization.
4. Evaluation Criteria/Few-Shot Examples: Provide examples of input-output pairs for learning.
5. Additional Information Retrieval: Use real-time data to enhance model responses.
6. Explanation Seeking: Request explicit explanations for model outputs when necessary.
7. Context Definition: Supply background information for more accurate model responses.
8. Expression Style: Decide between question or instruction format for directives.
9. Interaction Style: Choose between single-turn or multi-turn interactions for prompt delivery.


## The Top Principles for Improving Prompts
From paper: [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://browse.arxiv.org/html/2312.16171v1).


### Principle 14: Allow Asking Back
Allow the model to ask for specific details or requirements until there is enough information to generate the response.
Example: “From now on, I would like you to ask me questions to…”


### Principle 17: Use Delimiters
Use delimiters to separate the examples, instructions, or relevant information from each other. For example, one or more line breaks to separate instructions, examples, questions, context, and input data.

Example prompt:
- `###Instruction###`
- `###Example###` or `###Question###`.
- present your content.

### Principle 25: Keywords, Regulations, Hint, or Instructions
Provide directly and clearly keywords, regulations, hint, or instructions to follow.


### Principles 3, 12, 19
Reduce task complexity with a sequence of simple prompts, “think step by step”, combine reasoning in steps (Chain-of-thought) with examples (few-Shot). 


## Reasoning in Steps
Also called [Chain-of-Thought (CoT) Prompting](https://arxiv.org/pdf/2201.11903.pdf).

Your step-by-step instruction creates a momentum such that the model generates a text that guides it towards the correct answer.
The reasoning steps increase interpretability.
Append instruction "Let's think step by step." or provide reasoning examples.
For example, multistep arithmetic, commonsense logical reasoning.
Model's ability to use [CoT increases with model size (see PaLM and its ability to explain jokes)](/ml/googles-pathways-language-model-and-chain-of-thought).

{% include image.html src="/images/palm-chain-of-though-prompting.png" alt="Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" %}


## Majority Vote Reasoning Steps
Also called Self-consistency with Chain-of-Thought (CoT-SC).

Generate multiple reasoning paths (chains of thought), then return the most common answer.


## Self-evaluated Reasoning Search
Also called [Tree of Thoughts Problem Solving (ToT)](https://arxiv.org/pdf/2305.10601.pdf).

Generate explicitly decomposable thoughts, evaluate progress of each unfinished thought chain, and efficiency explore with an search algorithm.
This has analogies to [AlphaZero](https://arxiv.org/pdf/1712.01815.pdf) for playing chess.

Criticism is that the evidence is low with only 3 toy examples, additional model generation is required for evaluation operations, and the technique requires additional problem-specific human inputs.

{% include image.html src="/images/tree-of-thought-tot-comparison-cot.png" alt="Tree of Thoughts Problem Solving comparison with Chain-of-Thought" %}


### Thought Decomposition in ToT
Designed problem-specific meaningful thought size and separation. For example a paragraph, or an equation.

{% include image.html src="/images/three-of-thought-input-output-thoughts-steps.png" alt="three of thought input, output, thoughts" %}


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

{% include image.html src="/images/tree-of-thought-tot-game-of-24.png" alt="Tree of Thought ToT: Game of 24 results" %}

{% include image.html src="/images/tree-of-thought-tot-game-of-24-results.png" alt="Tree of Thought ToT: Game of 24 results" %}


#### Creative Writing

{% include image.html src="/images/tree-of-thought-tot-creative-writing-results.png" alt="Tree of Thought ToT: Creative Writing" %}

## [Graph of Thoughts](https://arxiv.org/pdf/2308.09687.pdf)
Tree of Thoughts with the human-specified ability to combine thoughts on top of Scoring & Ranking Thoughts.
Core idea in both methods is reusing the already generated thoughts, but graph of thoughts has aggregation ability.


## Generating Optimal Prompts
Models can be used to generate their own optimal prompts.
For example, [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409).



## Tool Use
Models can use external tools by generating API calls, when it is advantageous.
For example, if there is a question for some sort of calculation. [Toolformer method](https://arxiv.org/abs/2302.04761) can use a small training sets, you can teach it to call a calculate function, which it can use to do the calculation for it. It will get the results as into the text and instead of predicting the function output, it would get the output from the tool. It would sort of stop predicting for a couple tokens and get the result. With this you can improve actual performance on dedicated tasks for, you can do retrieval for question answering.
- TODO


## Fine-Tuning Training

Nuanced behavior and stronger prompt injection protection can be only trained via fine-tuning. 
When we have enough data and compute, we can fine-tune the model weights to increase performance.


### Parameter Efficient Methods
Cheaper to train, and switch between, and help to prevent catastrophic forgetting. 
Can help against catastrophic forgetting also.

Additive:
- Soft prompts: training a section of input sequence embeddings.
- Adapters

Re-parametrization:
- LoRA: Low-Rank Adaptation



## Other Resources
Get more information from leading model providers:
- [OpenAI's GPT best practices](https://platform.openai.com/docs/guides/gpt-best-practices/strategy-split-complex-tasks-into-simpler-subtasks?utm_source=vaclavkosar.com)
- [Anthropic's Prompt Design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design?utm_source=vaclavkosar.com)