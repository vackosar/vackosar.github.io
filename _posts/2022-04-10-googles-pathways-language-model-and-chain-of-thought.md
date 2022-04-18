---
title: "Google's Pathways Language Model and Chain-of-Thought"
description: "Pathways Language Model (PaLM), the largest model of early 2022, outperforms average human on grade school logic and math (BIG-bench) by simulating reasoning steps."
layout: post
categories: ml
date: 2022-04-10
last_modified_at: 2022-04-18
image: /images/palm-thumb.png
permalink: /:categories/:title
---

{% include mathjax.html %}

![palm thumbnail](/images/palm-thumb.png)

- training task: Given this text, predict the next word (token).
- the biggest dense [transformer](/ml/transformers-self-attention-mechanism-simplified) (540B) and likely the most expensive (~$10B) as of early 2022 
- highly efficient training on 6k chips (TPU v4) across 2 clusters (Pods)
- improvements from scaling continue in language understanding (few-shot)
- disproportionate gains from certain scale e.g. reasoning: 62B to 540B vs 8B to 62B
- breakthrough performance:
  - outperforming average human on a grade school logic and math (BIG-bench)
  - outperforms specialized and fine-tuned models on multistep reasoning
  - chain-of-thought prompting simulates inner monologue

## PaLM's Size
- [transformer](/ml/transformers-self-attention-mechanism-simplified) architecture similar to [GPT-3](https://arxiv.org/pdf/2005.14165.pdf)
- PaLM has 540B parameters
- 3x bigger than GPT-3 175B parameters
- 2x smaller than sparse [Switch Transformer](https://arxiv.org/pdf/2101.03961.pdf) 1T
  - only parts of the model is activated at each time.
- human brain 100T connections
- likely the most expensive model [~$10M](https://blog.heim.xyz/palm-training-cost/) (2.5 yottaFLOPS) vs GPT-3 [~$5M](https://lambdalabs.com/blog/demystifying-gpt-3/#1)
- PaLM and GPT-3 fascinating, but likely not economical now

![PaLM vs GPT vs MT-NLG computation cost FLOPs AI training](/images/palm-chart-computation-used-in-training.png)


## Zero-Shot vs Few-Shot Prompting vs Fine-Tuning
- prompting: instructing via addition of textual context
- zero-shot: task described, but demonstrations not given
- few-shot: task described and random demonstrations provided
- fine-tuning: model parameters are updated with correct answers

![zero-shot vs one-shot vs fine-tuning (GPT-3 paper)](/images/gpt-3-zero-shot-one-shot-fine-tuning.png)


## PaLM's Breakthrough Capabilities on BIG-bench
- BIG-bench: 150+ tasks (a task contains samples) like reasoning, math, QA, translation, programming
- 58 tasks available results on other models, often multiple choice questions
- PaLM is SOTA: outperforming human average and other models GPT-3, Gopher, Chinchilla
  - still underperforms average human on many tasks
- funny footnote: they scan for the dataset in the training set using GUID
- certain capabilities emerge when a scale is reached (not log-linear)
  - english proverbs and logical sequence at 62B to 540B vs 8B to 62B

![PaLM discontinuous improvements with scale](/images/palm-discontinuous-improvement-with-scale.png)


## Chain-of-Thought Prompting
- inserts reasoning steps between for each demonstration in the prompt
- multi-step arithmetic
  - grade-school level math problems
  - difficult is to convert to equations
- commonsense logical reasoning
  - strong world knowledge
  - chaining logical inferences
- thoughts are useful for interpretation

![Chain of Thought Prompting](/images/palm-chain-of-though-prompting.png)
 

## PaLM Chain-of-Thought Prompting Results
- reasoning tasks datasets: GSM8K, SVAMP, MAWPS, AQuA, CommonsenseQA, StrategyQA
- humans allowed calculators and search engines too
- the model triggers [a calculator by generating special annotation text](https://arxiv.org/pdf/2110.14168.pdf) (+~5% acc)
- on GSM8K: PaLM+chain-of-thought competitive with GPT-3+finetuning+calculator+verifier,
  - outperforms with a calculator, but GPT-3+chain-of-thought?
- generating explicit inference chains drastically increase the quality of the predictions

![PaLM chain of thought prompting new SOTA on GSM8K, MAWPS, SVAMP, and StrategyQA](/images/palm-chain-of-though-prompting-results.png)


## Explanation Using Chain-of-Thought Prompting
- right reasons for the right answer?
- interpretability may be desired output
- 2-shot prompting with greedy decoding (deterministic)
- not in paper: I added GPT-3, results with zero-temperature
- average airplane speed 460 – 575 mph

<i style="color: blue">
Input: _Jennifer looked out her window and sees a really cool cloud below her. She unbuckles her seatbelt and heads to the bathroom. Is Jennifer probably traveling more than 300 miles per hour relative to the earth?_
</i>

<b style="color: orange">
PaLM: __300 miles per hour is about 480 km/h. This is about the speed of a commercial airplane. Clouds are usually below airplanes, so Jennifer is probably on an airplane. The answer is "yes"__
</b>

<b style="color: purple">
GPT-3: __No, because an airplane typically travels around 500-600 miles per hour, and the bathroom is usually located in the back of the plane.__
</b>


## PaLM on Code Tasks
- achieves similar results to specialized OpenAI's Codex 12B with 3% of the code training data
- after fine-tuning outperforms OpenAI's Davinci Codex

![PaLM and PaLM-Coder models scales 8B, 62B and 540B](/images/palm-coding-tasks-results.png)


## PaLM on Other Tasks
- generally SOTA on a few-shot competitions
- few-shot is not competitive with fine-tuned model
- fine-tuned only competitive with specialized fine-tuned variants
- translation: without fine-tuning outperforms GPT-3, outperforms some supervised baselines de-en, ro-en
- summarization: fine-tuned results competitive, few-shot largely underperforms the fine-tuned
- multilingual question answering: fine-tuned results competitive, few-shot largely underperformed of fine-tuned 

![palm multilingual question answering results](/images/palm-multilingual-question-answering-results.png)


## PaLM Architecture:
- decoder-only transformer (attending only to the past) like GPT-3
- modified Feed-forward layer (MLP):
  - instead of RELU \\( max(0, xW_1 + b_1)W_2 + b_2 \\) use [SwiGLU feed-foward](https://arxiv.org/pdf/2002.05202.pdf)
  - ~1% better in compute equivalent setup
  - uses GLU: gated linear unit - a sigmoid controlled output
  - SwiGLU: \\( \mathrm{FFN}_{\mathrm{SwiGLU}} := (\mathrm{Swish}(xW_1) \otimes xV ) W_2 \\)
  - uses [swish activation](https://arxiv.org/pdf/1710.05941v1.pdf?source=post_page): \\( x (1 + exp(−x))^{−1} \\)
- parallel Attention and Feed-forward layer (MLP) from [GPT-J](https://github.com/kingoflolz/mesh-transformer-jax):
  - instead of sequential is additive:
  - \\( y = x + MLP(LayerNorm(x)) + Attention(LayerNorm(x)) \\)
  - 15% speedup for small degradation
- [multi-query attention](https://arxiv.org/pdf/1911.02150.pdf):
  - block-shared key and value projections, different query projections
  - speeds up autoregressive decoding where queries 
- [RoPE Embeddings](https://arxiv.org/pdf/2104.09864.pdf):
  - want relative position info in query-value dot-product
  - use multiplicative rotational matrix mixing pairwise neighboring dimensions
  - improves performance on long sequences

## PaLM Training Dataset
- 780B tokens of high-quality text, ([5T token MassiveText](/ml/massivetext-dataset-pretraining-deepminds-gopher), GPT-3 300B tokens, MT-NLG 339B)
- social media 50%, webpages 27%, books 13%, wikipedia 4%, code 5%, news 1%
- based on dataset used for LaMBDA, GLaM
- private non-reproducible dataset, while MT-NLG 339B is reproducible but non-hosted

![PaLM dataset hierarchical topics](/images/PaLM-dataset-hierarchical-topics.png)


## PaLM Training Requirements
- ~17 TB of RAM, 2.5 yottaFLOPS (\\( 10^{24} \\)) needed for training
- 2 TPU v4 Pod clusters connected via data center network
- mind of PalM is shattered across many chips (cheaper, replaceable, cooling)
- each Pod ~1 exaflop/s: 768 hosts, 3072 TPU v4 chips
- but how to split the work and communicate?

![Pathways system datacenter network, tpu ](/images/palm-pathways-system-datacenter-pods-hosts-TPU-chips.png)


## Parallel Training of Large Scale Models
- parallel computing trades off compute ("time"), memory ("space"), communication throughput (no cool name)
- data parallelism - batches are divided between workers
- tensor model parallelism
  - splits model layers i.e. transformer block into attention heads and feedforward
- pipeline mechanism ([Megatron-Turing (MT-LNG) Microsoft and NVidia](https://arxiv.org/pdf/2201.11990.pdf))
  - computation DAG into stages e.g. layers
  - stages exchange forward and backward propagation information (micro-batches)
  - step by step passing causes "bubbles" - idling

![NVIDIA data center DGX AI](/images/nvidia-data-center-dgx-ai.jpg)

## PaLM Training Infrastructure
- PaLM uses pipeline-free 2D parallelism
- data parallel across 2 clusters (2 TPU v4 Pods)
- each cluster (Pod) has full model copy
  - model partitioned into 12 parts
  - data partitioned into 256 parts
  - 768 hosts connected to 3k chips which are interconnected
- each batch triggers update between clusters to identical models
  - each host exchanges 1.3GB with its counterpart

![Pathways system datacenter network, tpu ](/images/palm-pathways-system-datacenter-pods-hosts-TPU-chips.png)


## Training Efficiency
- observed throughput relative to the theoretical maximum of a system
- price for parallelization of PaLM is 50%
- in case of PaLM throughput is tokens-per-second

![Model FLOPs utilization of PaLM vs Megatron-Turing NLG vs Gopher vs GPT-3](/images/PaLM-model-flop-utilization-vs-megatron-vs-gopher-gpt-3.png)


## More Posts Like This 
- [SRU++ Model Speeds Up Transformer with Simple Recurrent Unit](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN)
- [DeepMind's RETRO Transformer Model](/ml/DeepMinds-RETRO-Transformer-Model)

<br>
{% include subscribe.html %}
<br>


## Appendix

### GPT-3 Explanations Full Prompts

#### Logical Inference 1
```
I will explain how to make logical inferences:
(1) John wakes to the sound of his children giggling outside the door. They bust in and say "Happy Father's Day!" with a plate full of food. 2022 has been a great year. Can we infer that John was born before the inauguration of Barack Obama?
Answer: We can infer that John is a father because of "his children". We can infer that the current year is 2022. Barack Obama was inaugurated in 2009, so it has been about 13 years since Obama was inaugurated. John's children are old enough to speak, so if John were born after Obama's inauguration, he would have been younger than 10 when he had children. So, we can infer that John was born before Obama's inauguration. The answer is "yes".
(2) Sam sees a piano in the subway stations. Laughing, his friends prod him to play, saying "Remember how amazing your rendition of Chopsticks was at the Christmas party?" Can we infer that John majored in piano at Juilliard?
Answer: Juilliard is a top school for music, so someone who majored in piano at Juilliard would be an expert pianist. "Chopsticks" is a very simple song to play on the piano. His friends were therefore likely being sarcastic when they told him to play, which would imply that Sam was not an expert piano player. So it is unlikely that Sam majored in piano at Juilliard. The answer is "no".
(3) Jennifer looked out her window and sees a really cool cloud below her. She unbuckles her seatbelt and heads to the bathroom. Is Jennifer probably traveling more than 300 miles per hour relative to the earth?
Answer:
```

Best of 2 temperature 0.7 otherwise defaults:
- We can infer that Jennifer is on an airplane because she is looking out a window and sees a cloud below her. We can also infer that she is traveling at a high speed because she is on an airplane. The average cruising speed of an airplane is about 550 miles per hour, so Jennifer is probably traveling more than 300 miles per hour relative to the earth. The answer is "yes".
- We can infer that Jennifer is in an airplane because she is looking out a window. We can also infer that she is high up in the sky because she can see a cloud "below" her. Clouds are usually found at altitudes above 3,000 feet. Finally, we know that airplanes typically travel around 500 miles per hour. So, Jennifer is probably traveling more than 300 miles per hour, but we cannot be certain. The answer is "yes".

Greedy:
- No, because an airplane typically travels around 500-600 miles per hour, and the bathroom is usually located in the back of the plane.


#### Logical Inference 2
```
I will explain how to make logical inferences:
(1) John wakes to the sound of his children giggling outside the door. They bust in and say "Happy Father's Day!" with a plate full of food. 2022 has been a great year. Can we infer that John was born before the inauguration of Barack Obama?
Answer: We can infer that John is a father because of "his children". We can infer that the current year is 2022. Barack Obama was inaugurated in 2009, so it has been about 13 years since Obama was inaugurated. John's children are old enough to speak, so if John were born after Obama's inauguration, he would have been younger than 10 when he had children. So, we can infer that John was born before Obama's inauguration. The answer is "yes".
(2) Sam sees a piano in the subway stations. Laughing, his friends prod him to play, saying "Remember how amazing your rendition of Chopsticks was at the Christmas party?" Can we infer that John majored in piano at Juilliard?
Answer: Juilliard is a top school for music, so someone who majored in piano at Juilliard would be an expert pianist. "Chopsticks" is a very simple song to play on the piano. His friends were therefore likely being sarcastic when they told him to play, which would imply that Sam was not an expert piano player. So it is unlikely that Sam majored in piano at Juilliard. The answer is "no".
(3) Shelley is from Virginia, but is visiting that city with that famous market where they throw the fish. Going home next Tuesday!
Question: Is it likely that Shelley will be near the Pacific Ocean this weekend?
Answer: 
```

Best of 2, temperature 0.7 otherwise defaults:
- It is not likely that Shelley will be near the Pacific Ocean this weekend. Shelley is from Virginia, which is on the East Coast of the United States. The city with the famous fish market is most likely Seattle, which is also on the West Coast. Shelley is visiting, so she is not from there. She is going home next Tuesday, so she will likely be going back to Virginia this weekend.
- It is not likely that Shelley will be near the Pacific Ocean this weekend. Shelley is from Virginia, which is on the East Coast of the United States. The city with the famous fish market is most likely Seattle, which is also on the West Coast. Shelley is visiting, so she is not from there. She is going home next Tuesday, so she will likely be going back to Virginia this weekend.

Greedy:
- It is not likely that Shelley will be near the Pacific Ocean this weekend. Shelley is from Virginia, which is on the East Coast of the United States. The city with the famous fish market is most likely Seattle, which is also on the West Coast. Shelley is visiting, so she is not from there. She is going home next Tuesday, so she will likely be going back to Virginia this weekend.


#### Jokes
```
I will explain these jokes:
(1) The problem with kleptomaniacs is that they always take things literally.
Explanation: This joke is wordplay. Someone who "takes things literally" is someone who doesn't fully understand social cues and context, which is a negative trait.
But the definition of kleptomania is someone who literally takes things.
(2) Always borrow money from a pessimist. They’ll never expect it back.
Explanation: Most people expect you to pay them back when you borrow money, however a pessimist is someone who always assumes the worst, so if you borrow money from them, they will expect that you won't pay them back anyways.
(3) I was going to fly to visit my family on April 6th. My mom said "Oh great, your step dad's poetry reading is that night!" So now I'm flying in on April 7th.
Explanation:
```

Best of 2 temperature 0.7 otherwise defaults:
- This joke is about how annoying mothers can be. The speaker is trying to visit their family, but their mother has just informed them that their step-dad's poetry reading is on the same night. So now the speaker has to fly in on the next day.
- This joke is about how annoying it can be to have to deal with family obligations. The person telling the joke is trying to visit their family on April 6th, but their mom tells them that their step dad's poetry reading is that night. So the person has to fly in on April 7th instead.
- This joke is about how annoying and inconsiderate step-parents can be. The punchline is that the person is flying in a day later just to avoid their step-dad's poetry reading.

Greedy:
- This joke is about how annoying and intrusive in-laws can be. The person is trying to visit their family, but their mother says that their step-dad's poetry reading is that night. So the person is now flying in the next day to avoid it.