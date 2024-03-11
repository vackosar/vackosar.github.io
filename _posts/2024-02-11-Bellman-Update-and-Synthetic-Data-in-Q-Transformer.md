---
title: Bellman Update and Synthetic Data in Q-Transformer
description: Notes on Q-learning, temporal difference, Monte Carlo, and others methods related to Q-Transformer.
categories: ml
date: 2024-02-11
last_modified_at: 2024-03-05
image: /images/bellman-update-q-transformer-thumb.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2024-02-20-Synthetic-Data-for-LLM-Training.md
- _posts/2019-08-28-1D-Kalman-Is-Exponential-Or-Cumulative-Average.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2021-02-07-submodularity-in-ranking-summarization-and-self-attention.md
- _posts/2023-03-24-Symbolic-vs-Connectionist-Machine-Learning.md
---

{% include mermaidjs.html %}
{% include highlight-rouge-friendly.css.html %}

{% include image.html alt="Bellman Update and Synthetic Data in Q-Transformer" src="/images/bellman-update-q-transformer-thumb.png" %}



Here are my notes on Q-learning and Q-transformer. Take it with grain of salt, as I am new in this area.

The [Q-transformer](https://qtransformer.github.io/assets/qtransformer.pdf) is important paper, because it describes successful application of **suboptimal [synthetic (autonomously collected) data](/ml/Synthetic-Data-for-LLM-Training)** and [**transformer architecture**](/ml/transformers-self-attention-mechanism-simplified) in a robotic reinforcement learning problem.

Before Q-transformer let's first talk about a bigger topic: Bellman Update in Reinforcement Learning.

## States, Actions, and Rewards
Let's suppose we have a game with game states and actions we can take (a finite-state Markov decision process (MDP)). For example, in chess this is a state of the chessboard and actions are allowed moves we can make. Or even simpler example is below, where we have just a single state, single possible action, and single reward for that action.

<div class="mermaid">
    flowchart TD
    State1 -- "Action1 with reward=1" --> State1
</div>

In this diagram if we keep looping, we will keep stacking rewards.
If we discount future rewards with 0.5 discount factor the total reward will be 2,
so value of the state is 2.

More interesting examples is where we have 2 possible actions:

<div class="mermaid">
    flowchart TD
    State1 -- reward=1 --> State1
    State1 -- reward=0.1 --> State1
</div>

In this case, we if we're making the right decision, 
we still get reward 2, so the value of the state is still 2.


## Bellman Equation

Optimal decision maker is always able to get the best in each situation in the total.
Because the rewards are added to the total value, we can decompose the value of the state into the best reward and the value of the next state.

The Principle of Optimality simply says that for the best decision maker (policy), no matter where you start or what your first step is, the next steps should always form the best plan for the situation after that first step.
Where the best plan is the highest total reward.
This principle is captured by the Bellman Equation, which is a necessary condition for optimality.

```
# Bellman Equation
value(current_state) == (
  reward(current_state, the_best_action)
  + discount * value(the_best_next_state)
)
```

## Bellman Update and Q-function
If we can explore which actions gives us the highest rewards, and remember the best rewards,
then every time we find out better path, we can use the Bellman equation above to update the state value.
This was we iterate until we reach the best solution.
So we can apply the principle of optimality above to refine our decision-making,
and this we do with Bellman Update in Value Iteration method.

To do this we can brute-force exhaustively explore all actions at all states across paths.
We would always update corresponding value function values with the action that leads along the path that leads to the highest reward.

Since we are brute-forcing the solution evaluating everything without a model of the environment, we can describe the value function as an array or python dictionary:

```
# Bellman Equation
value[current_state] == (
  reward[current_state, the_best_action]
  + discount * value[the_best_next_state]
)
```

Instead of a value function, it is easier to work with a Q-function:
```
# Bellman Equation with q_function
q_function[current_state, the_best_action] = (
  reward[current_state, the_best_action]
  + discount * max(
    q_function[the_best_next_state, the_next_action]
    for the_next_action actions[the_best_next_state]
  )
)
```

With that we can describe the Bellman update rule in more detail:

```
states = [...] # list of all states
actions = [...] # list of all actions
gamma = 0.9 # discount factor

# The Q-table is initially filled with zeros
q_function = { (state, action): 0 for state in actions for action in actions }


def bellman_optimal_operator_update(q_function, state, action):
	# this defined by the environment
	next_state = get_next_state(state, action)
	# the next action of in the next step as defined by the optiomal policy maximizing the q_function
	# we directly update the q_function
	q_function[state, action] = reward(state, action) + gamma * max(q_function[next_state, next_action] for next_action in actions)
	return q_function
	
def optimal_policy(q_function, state):
    # optimal policy is defined by action maximizing the q_function
    return argmax(lambda a: q_function[a, state], all_actions(state))
```


## Modelling Q-Function and Training It
Instead of model-free tabulation, that is very data-intensive, we can model the Q-function to interpolate the table using less than full data.

Temporal difference learning (TD-learning) is related to Q-learning, but instead of just updating the Q-value of a single state, we also update the previous ancestral states.
The method is called temporal difference because of the difference between current estimate, and one-lookahead estimate based on future state Q-function values.

For example, in the Q-transformer a multi-modal neural network with [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) is used for modeling the Q-function and TD-learning is used for offline training.

More specifically the input camera image goes to instruction-conditioned convolutional network for images. The text instruction is converted into text and the text goes to condition [FiLM-conditioned](/ml/Feature-wise-Linear-Modulation-Layer) visual-modality EfficientNet convolutional network. The conditioned network outputs then combined information into a [transformer](/ml/transformers-self-attention-mechanism-simplified), which then outputs Q-function value predictions. 

{% include image.html src="/images/q-transformer-universal-sentence-encoder-film-efficientnet-transformer.png" alt="Q-transformer encodes camera image Film EfficientNet, text instruction with Universal Sentence Encoder both are combined into a Transformer (from the paper)" %}


## Q-Function Learning Speedup by Monte Carlo Return
At initialization, the neural model has a **cold-start** problem and is very bad at estimating the state values. But if we **tabulate (memoize) rewards for successful trajectories**, we can immediately provide **a minimal reward** for any point on the successful pathway. This speeds up learning of the Q-function neural network. This tabulation method is called **Monte Carlo return**. In a way, we are combing brute-force with neural network interpolation.


## Other Tricks used in Q-Transformer

The most foundational ideas applied in Q-transformer paper were described above. Here is a summary of other contributions in this paper:

1. **Autoregressive Discretization of Actions**: To accommodate the high-capacity Transformer architecture, the Q-Transformer discretizes each dimension of the continuous action space separately and treats each dimension as a different timestep in the learning process. This allows the model to learn Q-values for each action dimension separately, enabling efficient scaling of the method to high-dimensional action spaces without encountering the curse of dimensionality.

2. **Conservative Q-Function Regularization**: The Q-Transformer uses a modified version of Conservative Q-learning (CQL) that introduces a **regularizer to minimize Q-values for actions not present in the dataset explicitly**. This conservative approach **biases the model towards in-distribution actions**, i.e., those seen during training, and serves to mitigate overestimation of Q-values for unseen or suboptimal actions. This approach ensures that during training, the estimated Q-values are kept closer to the minimal possible cumulative reward, which is consistent with the non-negative nature of the rewards in the tasks targeted by the Q-Transformer. This method **differs from softmax method** of pushing Q-values down for unobserved actions and up for the observed actions, which may prevent keeping Q-values low for suboptimal in-distribution actions that fail to achieve high reward.

3. **Loss Function**: The loss function for the Q-Transformer combines both the temporal difference error (between the current and target Q-values) and the **conservative regularization term**. In practice, the action space dimensionality is expanded to include the discrete bins of action values, and the update rule is applied separately for each action dimension.


## Q-Transformer Results

Q-Transformer outperforms QT-OPT and Decision Transformer in a reinforcement learning task, where [suboptimal synthetic data](/ml/Synthetic-Data-for-LLM-Training) is available for offline training.
QT-OPT, also performs TD-learning in contrast to Decision Transformer, which seems to be the biggest factor here for good performance with suboptimal data.

{% include image.html alt="Performance on picking task q-transformer, qt-opt-cql, decision-transformer, aw-opt, iql, rt-1-bc.png" src="/images/performance-on-picking-task--q-transformer--qt-opt-cql--decision-transformer--aw-opt--iql--rt-1-bc.png" %}

