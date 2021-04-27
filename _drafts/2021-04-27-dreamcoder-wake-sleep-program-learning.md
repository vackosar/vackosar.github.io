---
layout: post
title: "DreamCoder AI: TODO"
date: 2021-04-27
categories: ml
description: Learning to code by growing library and training neural search.
permalink: /:categories/:title
---

{% include mathjax.html %}

### Why coding?

Missing System 2:
- interpolation not enough
- humans can
  - think algorithmically ([system 2](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow))
  - accumulate "knowledge"
  - from small amount of samples
- symbolic + neural?


<img
    class="figure-img img-fluid rounded lazyload"
    alt="Wiki disambiguation problem and submodularity"
    data-src="https://upload.wikimedia.org/wikipedia/en/c/c1/Thinking%2C_Fast_and_Slow.jpg"
    style="max-width: 100px">


### How DreamCoder works?

- DreamCoder uses:
  - learned library of functions
  - learned neural search on program space
- To:
  - given inputs-output examples
  - produce a "reasonable" solution  
    
    
Reasonable program:
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
        Solved domains from the DreamCoder paper 
    </figcaption>
</figure>


### How DreamCoder learns?

Training:
1. provide program primitives (map, fold, if, cons, >)
1. iterate
    1. wake phase:
        1. search for the best solution with the library
        1. store successful solutions
    1. sleep phase
        1. abstract
            1. replay successful solutions
            1. rewrite and grow library to compress
        1. dream:
            1. generate & replay programs
            1. train neural search

The best solution:
- many programs solve
- select 5 smallest programs
- use for next sleep

Notation in the paper:
- library: \\( L \\)
- program:
    \\( \rho \\)  
- length:
    \\( P( \rho | L) \\)
- is solution:
    \\( P(x | \rho) \in \lbrace 0, 1 \rbrace \\)

  