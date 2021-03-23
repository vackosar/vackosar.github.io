---
layout: post
title: "Expanding Taxonomies"
date: 2021-03-22
categories: ml
description: TODO
permalink: /:categories/:title
image: /images/submodularity-main.png
video: fLAYeDYqhag
---

{% include mathjax.html %}

[comment]: <> ({% include load_video.html %})


### Why taxanomies?

Concepts into hierarchy where parents are:
- related to
- more general

Usually a tree
Usually 

#### [Google Shopping Taxanomy](http://google.com/basepages/producttype/taxonomy.en-US.txt)
Examples:
- Animals & Pet Supplies > Pet Supplies > Bird Supplies > Bird Cage Accessories > Bird Cage Bird Baths
- Home & Garden > Kitchen & Dining > Tableware > Serveware Accessories > Punch Bowl Stands
- Sporting Goods > Outdoor Recreation > Outdoor Games > Platform & Paddle Tennis > Platform & Paddle Tennis Paddles


#### [Mozilla Web Dmoztools](http://dmoztools.net/)

#### [Pinterest Taxonomy](https://arxiv.org/pdf/1907.02106.pdf)
- Interests are organized into Pinterest taxanomy
- Advertizeres use taxonomy to target ad campaigns
- In 2020:
  - 11000 nodes/edges
  - 7 levels deep
  - 100% expert curated
- Examples:
  - Food & Drink > Drinks > Wines
- Pins and Pinners are categorized into the taxonomy to allow recommendation.
  - together called Taste Graph

## Uses of Taxonomies

#### [Sherlock recommender](https://cseweb.ucsd.edu/~csjgwang/pubs/IJCAI16_Sherlock.pdf)
- "Casualness" of skirts has different visuals to casualness of "flip-flops"
- taxonomy sub-trees use different projections of visual embeddings
- Visual projections are shared from parents to children via stacking

#### [Taxonomy-Aware Multi-Hop Reasoning Networks for Sequential RecommendatioTaxonomy-Aware Multi-Hop Reasoning Networks for Sequential Recommendation](https://dl.acm.org/doi/10.1145/3289600.3290972)
- taxonomy data as structural knowledge to instruct the learning of our model
- learn a unique preference representation corresponding to each level in the taxonomy based on her/his overall sequential preference


## Pininterest's Arborist

Basics
- automatic taxonomy expansion
- handles multiple relationships: is-type-of, is-in
- construct embeddings for unseen nodes
- minimizes an upper-bound on the shortest-path distances between the predicted and actual taxonomy parents
- SoTA and ablation study
- Code: available
- Data: no new published

Problem = parent retrieval
- Given taxanomy & query node 
- Rank true parents high
- Rank short-path to true high as well

## Modeling

Setup
- each node \\( u \\) of the dataset has a feature vector \\( e_u \\)
- choose natural number for hyper-param \\( k \\)
- \\( k \\) linear relatedness matricies \\( M_i \\)
- to each node \\( u \\) assign \\( k \\) learnable weights \\( w_{i, u} \\) 
- define relatedness score:

\\( s(u, v) = e_u^\intercal \sum_{i = 0}^{k} w_{i, v} M_i e_v \\)



### Sources
- [Expanding Taxonomies with Implicit Edge Semantics - Paper](https://dl.acm.org/doi/fullHtml/10.1145/3366423.3380271#BibPLXBIB0014)
- [Expanding Taxonomies with Implicit Edge Semantics - Video](https://youtu.be/vuKKubFaOjs)