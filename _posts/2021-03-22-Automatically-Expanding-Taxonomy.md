---
layout: post
title: Automatically Expanding Taxonomy
date: 2021-03-22
categories: ml
description: Pinterest's Arborist model finds parents for unseen textual nodes using triplet-loss, StarSpace embeddings, & shortest path.
permalink: /:categories/:title
image: /images/automatic-taxonomy.png
video: jve806iUHVo
redirect_from:
- /ml/Automatically-Expanding-Taxanomy
last_modified_at: 2022-05-21
my_related_post_paths:
- _posts/2021-03-22-google-product-taxonomy-viewer.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2022-10-23-Neural-Network-Pruning-Explained.md
- _posts/2022-05-14-neural-data-compression.md
---



{% include load_video.html %}
{% include mathjax.html %}

### Why Taxonomies?
- map concepts into a hierarchy, usually tree
- parents are related but more general or more abstract
- multiple relation types possible
- abstraction is information [compression](/ml/neural-data-compression)
- simplifies user navigation via categorization


#### [Google Product Taxonomy (Viewer)](/software/google-product-taxonomy-viewer)

Click on the __green nodes__ below to Google Product Taxonomy interactively. The second click collapses the children.

<script src="/js/d3.v6.min.js" type="text/javascript"></script>
<script src="/js/google-shopping-taxonomy.js" type="text/javascript"></script>

<small id="d3noScript">
    Loading taxonomy viewer...
</small>
<svg id="d3view" style="width: 90%; height: auto; overflow: scroll;"></svg>

Examples:
- Animals & Pet Supplies > Pet Supplies > Bird Supplies > Bird Cage Accessories > Bird Cage Bird Baths
- Home & Garden > Kitchen & Dining > Tableware > Serveware Accessories > Punch Bowl Stands
- Sporting Goods > Outdoor Recreation > Outdoor Games > Platform & Paddle Tennis > Platform & Paddle Tennis Paddles

#### Shopify Taxonomy
- [uses Google Product Taxonomy](https://shopify.engineering/categorizing-products-at-scale)
- published scalable product categorization

#### [Pinterest Taxonomy](https://arxiv.org/pdf/1907.02106.pdf)
- Interests are organized into Pinterest taxonomy
- Advertizeres use taxonomy to target ad campaigns
- In 2020:
  - 11000 nodes/edges
  - 7 levels deep
  - 100% expert curated
  - [nodes have 300dim feature embedding](https://labs.pinterest.com/user/themes/pin_labs/assets/paper/pintext-kdd2019.pdf)
    - trained [StarSpace](/ml/starspace-embedding)-like
- Examples:
  - Food & Drink > Drinks > Wines
- Use custom software for curation
- Pins and Pinners are categorized into the taxonomy to allow recommendation.
  - together called Taste Graph

## Other papers on use of taxonomies

#### [Sherlock recommender](https://cseweb.ucsd.edu/~csjgwang/pubs/IJCAI16_Sherlock.pdf)
- "Casualness" of skirts has different visuals to casualness of "flip-flops"
- taxonomy sub-trees use different projections of visual embeddings
- Visual projections are shared from parents to children via stacking

#### [Taxonomy-Aware Multi-Hop Reasoning Networks for Sequential Recommendation](https://dl.acm.org/doi/10.1145/3289600.3290972)
- taxonomy data as structural knowledge to instruct the learning of our model
- learn a unique preference representation corresponding to each level in the taxonomy based on her/his overall sequential preference


## Pininterest's automatic taxonomy expansion

- Pinterest motivation:
  - 8 curators added 6000 new taxonomy nodes in a month
  - compared to 100M of new pins every month
  - Interests = textual phrases describing concepts (mid-century architecture)
  - textual [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) available
- automatically find new node parent
- handles multiple relationships: is-type-of, is-in
- construct embeddings for unseen nodes
- minimizes an upper-bound on the shortest-path distances between the predicted and actual taxonomy parents
- SoTA and ablation study
- Code: available
- Data: no new published
- Name: Arborist

## Building Taxonomy
- is parent retrieval problem
- Given taxonomy and a query node 
- Rank true parents high
- Rank short-path to true parent high as well

## Parental Retrieval Examples
- luxor: **africa travel**, european travel, asia travel, greece
- 2nd month baby: **baby stage**, baby, baby names, preparing for baby
- depression: mental illness, **stress**, mental wellbeing, disease
- ramadan: hosting occasions, **holiday**, sukkot, middle east and african cuisine
- minion humor: humor, people humor, **character humor**, funny

## Modeling

Setup
- each node \\( u \\) of the dataset has a feature vector \\( e_u \in \mathbb{R}^{d} \\)
- choose natural number for hyper-param \\( k \in \mathbb{N} \\)
- \\( k \\) linear relatedness matricies \\( M_i \in \mathbb{R}^{d \times d} \\)
- to each node \\( u \\) assign \\( k \\) learnable weights \\( w_{i, u} \in \mathbb{R} \\) 
- define relatedness score from child \\( u \\) to candidate parent \\( v \\):

\\( s(u, v) = e_u^\intercal \sum_{i = 0}^{k} w_{i, v} M_i e_v \\)

## Training

Loss
- similar to triplet loss
- we want \\( s(child, parent) > s(child, nonparent) + \gamma \\)
- loss \\( \sum max(0, s(child, nonparent) + \gamma \\) \\( -  s(child, parent) ) \\)
- How to choose margin \\( \gamma \\) and scalable sum?

Dynamic Margin
- set \\( \gamma \\) to [shortest path to the true parent](https://github.com/cmuarborist/cmuarborist-core/blob/aff80ff85121d4f6a758e1e386bcffc6d03ccb7f/large_margin_taxonomic_role_model/model.py#L212)
  - [the distance is normalized to fit between 0 and 1 (see code)](https://github.com/cmuarborist/cmuarborist-core/blob/aff80ff85121d4f6a758e1e386bcffc6d03ccb7f/large_margin_taxonomic_role_model/model.py#L111)
- minimizing leads to upper-bounding of the path from predicted to parents
- curator needs to only move node in the neighborhood

Negative sampling
- cannot sum over all
- easy samples slow convergence
- use embedding-similarity-weighted negative-sampling

\\( \mathrm{Pr}(v', (u, v)) \propto e_u^\intercal e_{v'} \\)


## Evaluation

Datasets:
- Public: Mammal & SemEval
  - FastText embeddings
- Pinterest
  - Custom [300dim text embedding](https://labs.pinterest.com/user/themes/pin_labs/assets/paper/pintext-kdd2019.pdf) - [StarSpace](/ml/starspace-embedding)-like

Metrics:
- mean reciprocal rank (MRR)
  - = the multiplicative inverse of its rank in the predicted parents list
  - if multiple parents => the reciprocal of the highest ranked true parent
  - 0% (worst) to 100% (best)
- Recall@15
- SPDist = shortest-path distance in the taxonomy

<div class="table-responsive" id="tab4"> 
      <div class="table-caption"> 
       <span class="table-number">Results - (<a href="https://dl.acm.org/doi/fullHtml/10.1145/3366423.3380271#BibPLXBIB0014">Source: Table 4 of the paper</a>)</span> 
      </div> 
      <table class="table"> 
       <thead> 
        <tr> 
         <th></th> 
         <th colspan="3">Pinterest</th> 
         <th colspan="3">SemEval</th> 
         <th colspan="3">Mammal</th> 
        </tr> 
        <tr> 
         <th></th> 
         <th>MRR (%)</th> 
         <th>Recall@15 (%)</th> 
         <th>SPDist</th> 
         <th>MRR (%)</th> 
         <th>Recall@15 (%)</th> 
         <th>SPDist</th> 
         <th>MRR (%)</th> 
         <th>Recall@15 (%)</th> 
         <th>SPDist</th> 
        </tr> 
       </thead> 
       <tbody> 
        <tr> 
         <td>Vec-Concat</td> 
         <td>41.831</td> 
         <td>64.671</td> 
         <td>3.816</td> 
         <td>20.992</td> 
         <td>33.155</td> 
         <td>3.474</td> 
         <td>14.995</td> 
         <td>30.726</td> 
         <td>4.274</td> 
        </tr> 
        <tr> 
         <td>Vec-Sum</td> 
         <td>33.891</td> 
         <td>62.548</td> 
         <td>4.124</td> 
         <td>17.803</td> 
         <td>27.607</td> 
         <td>4.047</td> 
         <td>19.611</td> 
         <td>38.175</td> 
         <td>4.186</td> 
        </tr> 
        <tr> 
         <td>Vec-Diff</td> 
         <td>41.185</td> 
         <td>67.699</td> 
         <td>3.494</td> 
         <td>18.514</td> 
         <td>30.949</td> 
         <td>4.163</td> 
         <td>31.386</td> 
         <td>46.182</td> 
         <td>3.674</td> 
        </tr> 
        <tr> 
         <td>Vec-Prod</td> 
         <td>42.233</td> 
         <td>68.743</td> 
         <td>3.144</td> 
         <td>17.483</td> 
         <td>31.083</td> 
         <td>4.178</td> 
         <td><strong>32.177</strong></td> 
         <td>48.976</td> 
         <td>3.665</td> 
        </tr> 
        <tr> 
         <td>CRIM</td> 
         <td>53.223</td> 
         <td>79.325</td> 
         <td>2.393</td> 
         <td>41.691</td> 
         <td>62.064</td> 
         <td><strong>2.743</strong></td> 
         <td>21.345</td> 
         <td>52.700</td> 
         <td>4.080</td> 
        </tr> 
        <tr> 
         <td>Arborist</td> 
         <td><strong>59.044</strong></td> 
         <td><strong>83.606</strong></td> 
         <td><strong>2.220</strong></td> 
         <td><strong>43.373</strong></td> 
         <td><strong>67.694</strong></td> 
         <td>2.864</td> 
         <td>29.354</td> 
         <td><strong>61.639</strong></td> 
         <td><strong>3.225</strong></td> 
        </tr> 
       </tbody> 
      </table> 
     </div>

### Sources
- [Arborist - Expanding Taxonomies with Implicit Edge Semantics](https://cmuarborist.github.io/)


## Meet Other ML Enthusiasts One-on-One Online

Video-call each week an interesting person in the machine learning field and break out of your remote isolation.
Network One-on-One Around Your Online Village with RandomMeets.<br>
Or create a room of your own for you company or friend group and invite them to meet each other!

<a class="btn btn-info" style="text-decoration: none;" href="https://randommeets.com/invite/eyJncm91cF9pZCI6IjZhMzNkMTVjLTc0NjItNGFhMS1hNTc0LWM1NTUwMWQ4NWNkZiJ9.X76oug.2563ghpMTzbST9KPHerGeDqhXRY">
    Join Machine Learning @ RandomMeets
</a>
