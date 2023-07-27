---
layout: default
title: Google Product Taxonomy Viewer
date: 2021-04-16
description: Interactively explore Google Shopping's and Shopify's categories to configure products in your feed.
image: /images/google-shopping-taxonomy-viewer-graphic.png
permalink: /:categories/:title
categories: software
redirect_from:
- /google-product-taxonomy-viewer.html
last_modified_at: 2023-07-27
my_related_post_paths:
- _posts/2021-03-22-Automatically-Expanding-Taxonomy.md
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2021-10-25-manipulate-item-attributes-via-disentangled-representation.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2020-04-22-result-diversification-in-web-search-and-recommenders.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2020-05-08-starspace-embedding.md
---



# {{ page.title }}

<i>{{ page.description }}</i>

![Google Product Taxonomy Interactive Viewer ](/images/google-shopping-taxonomy-viewer-graphic.png)

Explore Google Product Taxonomy below to understand where to place products in your feed.
<span style="color: green">Click on the green nodes</span> to expand product category tree. The second click collapses the children in the diagram.

<script src="/js/d3.v6.min.js" type="text/javascript"></script>
<script src="/js/google-shopping-taxonomy.js" type="text/javascript"></script>

<small id="d3noScript">
    Loading taxonomy viewer...
</small>

<svg id="d3view" style="width: 90%; height: auto; overflow: auto !important;"></svg>


## What is Google Product Taxonomy?

Google Product Taxonomy is a product categorization tree for e-commerce.
Google and [Shopify classify e-shop articles into this structure](https://help.shopify.com/en/manual/online-sales-channels/facebook/checkout-on-instagram-and-facebook/product-categories).
The taxonomy purpose to departmentalize products from the merchant feed into 5583 sections.
This partitioning of the shopping feed improves article discovery for customers.
The automatic categorization is performed [based on product input fields](https://support.google.com/merchants/answer/6324436?hl=en) provided by the merchant.
The merchants have an option to override categorization using _google_product_category_ attribute.
Only one category per product is allowed.

## Download Google Taxonomy
[Download](http://google.com/basepages/producttype/taxonomy.en-US.txt) the Google product category tree directly from the Google. The taxonomy list file has the following format:

{% include highlight-rouge-friendly.css.html %}

```text
Animals & Pet Supplies > Pet Supplies > Bird Supplies > Bird Cage Accessories > Bird Cage Bird Baths
Home & Garden > Kitchen & Dining > Tableware > Serveware Accessories > Punch Bowl Stands
Sporting Goods > Outdoor Recreation > Outdoor Games > Platform & Paddle Tennis > Platform & Paddle Tennis Paddles
...
```

## Google Guidelines
Read more in [official guidelines](https://support.google.com/merchants/answer/6324436?hl=en#zippy=%2Cshopping-ads-campaigns%2Capparel-products).


## How to Automatically Classify Products Into Taxonomies?
Product information usually includes image and text. Both of these need to be utilized to correctly place the product into the taxonomy.
Automatized classficiation can substatially reduce costs of catalogue maintanance and curation.
Read more about automation of [image-text product classification using machine learning here](/ml/Multimodal-Image-Text-Classification).


## Pinterest's Auto Expanding Taxonomy
Pinterest's [Arborist model](/ml/Automatically-Expanding-Taxonomy) finds parents for unseen textual nodes using triplet-loss, StarSpace embeddings, & shortest path.


<br>
{% include lets-connect.html %}