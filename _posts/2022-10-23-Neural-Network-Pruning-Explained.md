---
title: Neural Network Pruning Explained
description: Reduce on-CPU prediction and model storage costs by zeroing-out weights while minimally increasing the loss.
layout: post
categories: ml
image: /images/neural-network-pruning-thumb.png
date: 2022-10-23
last_modified_at: 2022-10-24
permalink: /:categories/:title
---

Pruning performs **lossy compression** of the model during repeated training steps to **reduce prediction costs, and model size**.
In decision trees, pruning **at first improves test accuracy (generalization)**, until a maximum is reached, after which it decreases accuracy, which corresponds to [bias-variance trade-off](/ml/double-descent-contrary-to-bias-variance-trade-off).
Neural networks use various regularization **allowing [high over-parametrization without overfitting](/ml/double-descent-contrary-to-bias-variance-trade-off)**, but we can still cut computation cost with pruning.


![neural network pruning](/images/neural-network-pruning-thumb.png)


## General Pruning Steps
In the first step we find or pre-select some initial network.
Then we iteratively **train, prune, and repeat**.
We **end after the training step**, as the weights are optimized for the pruned network, which has **a different architecture** in which pruned weight are **fixed to zero**.

![pruning steps](/images/pruning_steps__han_2015.png)

## Decision Trees
Decision trees are composed of **a tree of if-else statements of the input variables** only without use of any [internal representations (embeddings)](/ml/Embeddings-in-Machine-Learning-Explained), and consequently they are highly **interpretable**.
The if-else condition are of type: **input variable x is greater than value z**.
They **overfit without regularization** is applied by encoding entire dataset.
Commonly **regularization methods are pruning, minimum samples per leaf node, or maximum tree depth**.
Popular algorithms available:
- [C4.5](https://www.amazon.com/C4-5-Programs-Machine-Learning-Kaufmann/dp/1558602380) and its predesor [ID3](https://link.springer.com/content/pdf/10.1007/BF00116251.pdf), extension C5.0. C4.5 is one of the [top 10 algorithms listed in ML in 2008 survey paper](http://www.cs.umd.edu/~samir/498/10Algorithms-08.pdf).
- [CART](https://www.amazon.com/Classification-Regression-Wadsworth-Statistics-Probability/dp/0412048418/) another popular similar approach. Used by [Scikit-learn](https://scikit-learn.org/stable/modules/tree.html#classification).

[//]: # (![decision tree Iris dataset, Scikit documentation]&#40;/images/decision_tree_iris_dataset__scikit_docs.png&#41;)
![decision tree regression with data points and two maximum depths](/images/decision_tree_regression_with_data_points_and_two_maximum_depths.png)


### Minimal Cost-Complexity Pruning in CART Decision Trees
Minimal Cost-Complexity Pruning is **a greedy algorithm, which iteratively removes the best to prune subtrees** until reaching a specified limit `alpha`.
Increasing the pruning intensity by increasing alpha, improves generalization up to a point and then leads to decrease in generalization.

![decision tree cost complexity pruning improves test accuracy until a maximum, scikit docs](/images/decision_tree_cost_complexity_pruning__improves_test_accuracy_until_a_maximum__scikit_docs.png) 

#### Minimal Cost-Complexity Pruning Algorithm
For each non-terminal node `t` and we can calculate cost complexity of its subtree:
`def cost_complexity(t): misclassification_rate(t) + alpha * n_terminal_nodes(t)`

We start with `alpha_j` of `0` and increase it until we find a node, **for which `cost_complexity(t)` would be lower if pruned**, and so we prune the node's subtree.
We repeat this until we reach a specified limit `alpha`.
Note that `cost_complexity` above has similarities to [lasso regularization](https://en.wikipedia.org/wiki/Lasso_(statistics)).

![decision tree pruning example (Kijsirikul 2001)](/images/decision_tree_pruning__kijsirikul_2001.png)


## Decision Tree vs Neural Network
- Vanilla **decision trees split on the input variables only** and have no embeddings, while neural networks also train linear transformations of the values and thus create embeddings.
- [Neural networks with piecewise activation functions (e.g. ReLU) are equivalent to extension of a decision tree](https://arxiv.org/pdf/2210.05189.pdf) with linear manifold decision boundaries called [Multivariate Decision Trees](https://link.springer.com/content/pdf/10.1023/A:1022607123649.pdf).

![neural network as a multivariate decision tree for a parabola dataset](/images/neural_networks_are_decision_trees__aytekin_2022.png)


## Pruning in Neural Networks
In general, we start with a random initialization or a pretrained model of a certain architecture and then prune the model, producing sparser architecture, and train again. Various methods exists:
- **Unstructured Pruning** prunes individual weights. **Structured Pruning** prunes entire architectural blocs (layers, heads). **Semi-structured Pruning** prunes square blocks of weights.
- **[Magnitude Pruning](https://arxiv.org/pdf/1506.02626.pdf) prunes the smallest weights**, the most obvious idea.
- Pruning based on estimating change of loss corrensponding to a task are detailed below.

### Pruning Neural Networks by Estimating Loss Change
Similar to decision trees, we can zero-out weights that don't change the loss based on [Taylor series](https://en.wikipedia.org/wiki/Taylor_series) approximation.
**First-order Pruning prunes based on training loss gradients**.
For example [Movement Pruning](https://arxiv.org/pdf/2005.07683.pdf) removes those weights with gradient pointing towards zero during fine-tuning on a downstream task.

If the network weights are optimized and the first order gradient is zero, we need to use the second order derivative.
**Second-order Pruning prunes based on Hessian** prunes by minimization of the second-order loss change approximation e.g., [M-FAC method](https://arxiv.org/pdf/2107.03356.pdf). 

### Pruning Methods in Neural Networks
- [Learning both Weights and Connections for Efficient Neural Networks paper](https://arxiv.org/pdf/1506.02626.pdf), starts with random initialization, trains, prunes the smallest weights (small magnitude), and then crucially trains again the new network, and repeat. [Tensorflow pruning API](https://blog.tensorflow.org/2019/05/tf-model-optimization-toolkit-pruning-API.html) uses this method and sparsifies the layer's weights during training.
- [The Lottery Ticket Hypothesis paper](https://arxiv.org/pdf/1803.03635.pdf) prunes 90% its [smallest weights](https://arxiv.org/pdf/1506.02626.pdf), and **finds a subnetworks in the random initialization**, that trains to near optima.
- A notable oBERT method of 2022 is described below.


![pruning synapses, neurons, layers](/images/pruning_both_synapses_and_neuron_nodes_han_2015.png)


### Optimal BERT Surgeon Pruning Method
[oBERT paper](https://arxiv.org/pdf/2203.07259.pdf) from [Neural Magic](https://neuralmagic.com/blog/obert/) achieves **the same latency on [4-Core CPU as on A100 GPU](https://neuralmagic.com/wp-content/uploads/2022/09/Conference-Slides-Graphs-18.png)** with batch size 1, metrics within 1% difference, and 10x smaller [BERT model](/ml/transformers-self-attention-mechanism-simplified).
oBERT extends **Second-order to Structured Pruning**, reusing Fisher Information Matrix **approximation of the Hessian**, speeds ups inversion with WSM inversion formula and block-wise approximation, and fine-tunes with **Knowledge Distillation**.
**Fine-tuning for another task on pruned models is possible**, but requires distillation to preserve the accuracy.
**Initial training stays dense** and there is additional step of pruning fine-tune, so pruning helps only with **prediction and not training**.
oBERT optimized for CPU achieves 8.4x speed up, while when tuned for GPU only 2.3x speed up.

![optimal bert surgeon evaluation  comparission of compression methods  obert paper](/images/optimal-bert-surgeon-evaluation--comparission-of-compression-methods--obert-paper.png)


### Neural Magic Engine
Neural Magic Engine is a closed source inference software for sparse models optimized for CPU.
Popular models like BERT and Resnet50 in vision and text available for experimentation on their [website](https://sparsezoo.neuralmagic.com/).

<blockquote class="blockquote text-right">
  <i class="mb-0">
    But once FLOPs are reduced, the computation becomes more “memory bound”, that is, there is less compute per data item, so the cost of data movement in and out of memory becomes crucially important. ...
    rather than execute the network layer after layer, we are able to execute the neural network in depth-wise stripes we call Tensor Columns. ... Each Tensor Column stays completely in the CPU’s large fast caches along the full execution length of the neural network, ... In this way, we almost completely avoid moving data in and out of memory.
  </i>
  <footer class="blockquote-footer">
	  <a href="https://neuralmagic.com/technology/">A Software Architecture for the Future of ML - Neural Magic</a>
  </footer>
</blockquote>

![From Nvidia: GPU vs CPU in CUDA documentation](/images/sru-cpu-vs-gpu.png)



#### Neural Magic Engine CPU vs GPU Costs Estimate
**In my experiment**, oBERT outperformed Distilbert latency 2.3x on my CPU with 12 cores with batch size 1, while oBERT should have higher accuracy.
**Predicting on 4-Core CPU should save 2x to 4x costs** with more device availability in contrast to T4 GPU on Ohio.
See below table for AWS Ohio pricing.

| Instance name | On-Demand hourly rate | vCPU  |  Memory  | 
| g4dn.xlarge (T4 GPU)  |   $0.526  |   4  |   16 GiB  |   
| t4g.xlarge  (4 core CPU) |   $0.1344  |   4  |   16 GiB  |  


#### Licence and Patents
Sparsification libraries SparseML are Apache 2 licenced.
The inference engine is
- patented technology (["to execute in parallel involve computations from multiple layers"](https://patents.justia.com/assignee/neuralmagic-inc))
- restrictive licence not for production use (["solely for evaluation  use in development and testing environments, and not for production use."](https://github.com/neuralmagic/deepsparse/blob/main/LICENSE-NEURALMAGIC))


#### Neural Magic Management
**Nir Shavit won Dijkstra price and Godel price** for research in computer science, mainly in memory and parallel computation.
Other [ML Performance Research Papers on Neural Magic](https://neuralmagic.com/resources/technical-papers/)


#### Neural Magic Solution Summary
- could save 2x money minus pricing of NeuralMagic by inferring on commodity CPU with similar time cost as on GPU.
  - the next best thing would be just use similar methods without their specific technology
  - How much they charge?
- training still requires GPU (often not important)
- vendor lock in - probably want to avoid or be ready to switch.
- no clear alternative (maybe [Vertigo Applied Intelligence - Vertigo.ai](https://vertigo.ai/) ?)
- not sure what their patent means in practice as the wording seems overly broad
 
