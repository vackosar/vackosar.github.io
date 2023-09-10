---
title: Result Diversification in Web Search and Recommenders
description: Increase coverage in web search and recommendation via re-ranking diversification factor
layout: post
categories: ml
date: 2020-03-05
image: /images/long-tail-popularity-rank.drawio.svg
video: 35-xa9IOsnw
last_modified_at: 2022-06-11
permalink: /:categories/:title
my_related_post_paths:
- _posts/2021-02-07-submodularity-in-ranking-summarization-and-self-attention.md
- _posts/2023-08-19-Validate-Reliability-of-Research-Paper.md
- _posts/2021-03-22-Automatically-Expanding-Taxonomy.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2021-08-24-expire-span-scaling-transformer-by-forgetting.md
- _posts/2020-05-08-starspace-embedding.md
---



- Since user already seen results above, and they haven't clicked and continue reading
- What next the results should be?
- Increase diversity to satisfy all users for reduction of global relevance

{% include load_video.html %}


## Diverse Results Example
- word apple can mean a company or a fruit
- web search should cover both of these meanings (aspects)

![diverse web results for word apple - a company and a fruit](/images/diverse-web-search-results-apple.png)


## Query Reformulations for Web Search Diversification
- [xQuAD: Exploiting Query Reformulations for Web Search Result Diversification (2010, Uni of Glasgow)](https://www.ra.ethz.ch/cdstore/www2010/www/p881.pdf)
- Diversify results and hope that at least one will satisfy the user
- query is underspecified, we can find more specific query reformulation
- Various aspects are covered by more query reformulations
- Estimate of coverage of aspects and redundancy of documents


## How to Query Reformulations Work?
- How relevant the document to the user, given already seen higher results?
- Each document added to results should cover different aspect
- Previous methods: similarity between docs using [maximal marginal relevance](/ml/submodularity-in-ranking-summarization-and-self-attention)
- Paper contribution: similarity between sub-queries


## Sub-Query Generation
- query reformulations provided by three major Web search engines
- Created probably via query log mining 
- related sub-queries + suggested sub-queries
- relative importance generated sub-queries from centralized ranking of documents covering them


## Personalized Re-Ranking
- [Managing Popularity Bias in Recommender Systems with Personalized Re-ranking (2019, Uni of Colorado Boulder)](https://arxiv.org/pdf/1901.07555.pdf)
- Document → Item, Query → User, Aspect → long-tail vs short-head
- Goal: Relevant but cover both long-tail (rare) and short-head (popular)
- Use "Smooth" xQuAD - maintain some ratio of long tail items
- personalize based on how much user interacted with long-tail vs short-head items (ratio)
- Vaclav's opinion: why not make item popularity more continuous instead of using 2 categories?
- Adding small diversification can improve NDCG


## Coverage and Submodularity
Coverage is [a submodularity and diminishing returns problem - read more here](/ml/submodularity-in-ranking-summarization-and-self-attention)
