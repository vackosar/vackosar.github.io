---
layout: post
title: "DreamCoder AI: Wake & Sleep Program Learning"
date: 2021-04-27
categories: ml
description: Learning to code by growing library, training neural search, and fantasising code.
permalink: /:categories/:title
---

{% include mathjax.html %}

### Why coding?

Missing [System 2](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)):
- regression is not enough
- humans can also:
  - think algorithmically (
  - accumulate "knowledge"
  - from small amount of samples
- symbolic + neural?


<img
    class="figure-img img-fluid rounded lazyload"
    alt="Wiki disambiguation problem and submodularity"
    data-src="https://upload.wikimedia.org/wikipedia/en/c/c1/Thinking%2C_Fast_and_Slow.jpg"
    style="max-width: 200px">


### How DreamCoder works?

- [DreamCoder](https://web.mit.edu/ellisk/www/documents/dreamcoder_with_supplement.pdf) uses:
  - learned library of functions
  - learned neural search on program space
- To:
  - given inputs-output examples
  - produce a the best solution  
    
    
The best program:
- in based on experience
- too large program search space
- DreamCoder  
  - learn functions that _compress_ solved examples
  - learn neural guided search
    

Example solved tasks:

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


### How DreamCoder learns?

Training:
1. provide program primitives (map, fold, if, cons, >)
1. loop
    1. wake phase:
        1. search for the best solution given the library
        1. store successful solutions
    1. sleep phase
        1. abstract
            1. replay successful solutions
            1. compress them by adding to library
        1. dream:
            1. generate & replay programs
            1. train neural search

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        alt="Training phases"
        data-src="/images/dreamcoder-phases.png"
        style="max-width: 900px">
    <figcaption class="figure-caption">
        Training phases (sourced from the paper)
    </figcaption>
</figure>


#### Wake Phase
- neural network \\( Q \\) ranks potential solutions
  - given input-outputs and programs returns probability
  - called recognition model
- the best solution:
    - many programs solve
    - select 5 smallest programs
    - use for next sleep
    

##### Abstraction phase:
- propose new library functions 
- minizing the new functions
- minimizing the length of solutions
- reduce number of refactorings \\( \sim 10^{14} \\)
    - ideas from:
        - version space algebras
        - equivalence graphs
    - plus limit to small programs
    - lead to improvement \\( \sim 10^6 \\)
    
    
#### Dream phase:
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


### Results
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
    
    
### Why DreamCoder?
- builds on RobustFill and DeepCoder
- DeepCoder does not predict the probability of a program
- DeepCoder predicts DSL primitive will be used in the program at least once
- DeepCoder & DreamCoder libraries are 
  - modestly-sized set
  - generally useful routines
  - interpretable routines  


#### Sources & Details
- [DreamCoder Paper with Supplement](https://web.mit.edu/ellisk/www/documents/dreamcoder_with_supplement.pdf)
- [DreamCoder Video](https://youtu.be/NYIeP1hns6A)

Paper Notation
- library: \\( L \\)
- program:
  \\( \rho \\)
- length:
  \\( P( \rho | L) \\)
- is solution:
  \\( P(x | \rho) \in \lbrace 0, 1 \rbrace \\)
- search: approximate posterior of recognition model
  \\( Q( \rho | x) \\)


