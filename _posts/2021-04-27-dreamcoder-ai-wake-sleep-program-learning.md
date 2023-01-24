---
layout: post
title: 'DreamCoder: Wake & Sleep Program Learning'
date: 2021-04-27
categories: ml
video: I7e6vR6-yiQ
image: /images/dreamcoder-thumb.png
description: Learning to code by growing function library, fantasising coding tasks, and training neural search.
permalink: /:categories/:title
my_related_post_paths:
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2022-10-23-Neural-Network-Pruning-Explained.md
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
---



{% include load_video.html %}
{% include mathjax.html %}

## Why Code with Neural Networks?
- Regression is not enough. Neural Networks are missing [System 2](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow):
- humans can
  - think algorithmically using symbols
  - accumulate "knowledge" from small amount of samples
- GAI via symbolic + neural? ([Francois Chollet](https://youtu.be/J0p_thJJnoo))


<img
    class="figure-img img-fluid rounded lazyload"
    alt="Wiki disambiguation problem and submodularity"
    data-src="https://upload.wikimedia.org/wikipedia/en/c/c1/Thinking%2C_Fast_and_Slow.jpg"
    style="max-width: 200px">


## How DreamCoder Works?
- [DreamCoder](https://www.cs.cornell.edu/~ellisk/documents/dreamcoder_with_supplement.pdf) uses:
  - learned library of functions
  - learned neural search on the program space
- Such that:
  - given inputs-output examples
  - produces the best solution
  - and learns from that


### Why DreamCoder?
- builds on RobustFill and DeepCoder
- DeepCoder does not predict the probability of a program
- DeepCoder predicts DSL primitive will be used in the program at least once
- DeepCoder & DreamCoder libraries are
  - modestly-sized set
  - generally useful routines
  - interpretable routines
 

## DreamCoder's The Best Program Definition
- program search space is too large
- short program given previously useful functions is the best
- So, DreamCoder
  - growths library of functions that _compress_ valid solutions
  - learns neural guided search
 

## DreamCoder vs AlphaZero
Similarities to [AlphaZero](https://arxiv.org/pdf/1712.01815.pdf):
- also trains a neural search
- also does "self-play" (Dream phase)

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Solved domains from the DreamCoder paper "
        data-src="/images/dreamcoder-tasks.png"
        style="max-width: 500px">
    <figcaption class="figure-caption">
        Solved domains (sourced from the paper)
    </figcaption>
</figure>


## How is DreamCoder Trained?
1. provide program primitives (map, fold, if, cons, >)
2. wake phase:
    1. search for the best solution given the library
    1. store successful solutions
3. sleep phase
    1. abstract
        1. replay successful solutions
        1. compress them by adding to library
    1. dream:
        1. generate & replay programs
        2. train neural search
4. Loop to wake phase


## Visualization of DreamCoder Training
<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="DreamCoder Training phases"
        data-src="/images/dreamcoder-phases.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Training phases (sourced from the paper)
    </figcaption>
</figure>


### Wake Phase
- neural network \\( Q \\) ranks potential solutions
  - given input-outputs and programs returns probability
  - called recognition model
- the best solution:
    - many programs solve
    - select 5 smallest programs
    - use for next sleep
    

#### Abstraction phase:
- propose new library functions 
- minimizing the new functions
- minimizing the length of solutions
- reduce number of refactorings \\( \sim 10^{14} \\)
    - ideas from:
        - version space algebras
        - equivalence graphs
    - plus limit to small programs
    - lead to improvement \\( \sim 10^6 \\)
    
    
### Dream Phase:
- replay programs ~100s
- 50/50 mixing generated and replay programs
- to augment data but stay representative
- train Q function for search

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="DreamCoder logo task"
        data-src="/images/dreamcoder-logo-task.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
         DreamCoder LOGO task (A: tasks, B & C: learned functions, D & E: dreams. (sourced from the paper)
    </figcaption>
</figure>


## DreamCoder's Results
- list processing
    - primitives: map, fold, cons (pre-pend), ...
    - 109 training tasks
    - created library of 20 routines
        - filter, max, n-th largest
    - learned to sort
- text editing
    - e.g. "Alan Turing" -> "A.T."
    - train set: 128 auto-generated text editing task  
    - test set: 2017 SyGuS program synth  
    - prior-train solved 3.7%
    - post-training solved 84.3% vs 82.4% prior art
        - CVC4 competition
        - others used handpicked library from SysGuS
        - DreamCoder used only primitives + training samples
        - but is that really better?
- Ablations:
    - abstraction & dreaming are important
    


## Bonus Paper: Regex Generator++
- [Inference of Regular Expressions for Text Extraction from Examples (2016)](https://www.human-competitive.org/sites/default/files/bartoli-delorenzo-medvet-tarlao-tkde-paper.pdf)
- given texts and extractions
- Genetic Programming search for regular expressions
- [try demo](http://regex.inginf.units.it/)


### Regex Generator++ Solution search
- regex is represented by a tree
- nodes are
  - sub-node placeholder `*`
  - primitives (`\d`, `\w`, `[*]`, `[^*]`, look-around, ...)
- tree structure is DNA of the candidates
- keep only performing candidates ~ library in DreamCoder
- genetic crossover via swap of candidates' sub-trees
- genetic mutation via replacement of a subtree with random subtree
- fitness is "Character Precision", "Character Accuracy", length of the expression (~ DreamCoder's code length)


### Regex Generator++ vs GP-Regex and Others
- the method outperforms, but not on all datasets
- solution time is human comparable ~10 minutes


## Continue
- [DreamCoder's author video](https://youtu.be/NYIeP1hns6A)
- [Expire-Span solves reinforcement-learning-like problems with a transformer memory](/ml/expire-span-scaling-transformer-by-forgetting)
