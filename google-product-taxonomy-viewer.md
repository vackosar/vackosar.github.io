---
layout: default
title: "Google Product Taxonomy Viewer"
date: 2021-04-16
description: Explore with an interactively Google's shopping category structure.
image: /images/automatic-taxonomy.png
---

# {{ page.title }}

<i>{{ page.description }}</i>

![Google Product Taxonomy Interactive Viewer ](/images/google-shopping-taxonomy-viewer-graphic.png)

Explore Google Product Taxonomy below.
<span style="color: green">Click on the green nodes</span> to expand product category tree. The second click collapses the children in the diagram.

<script src="/js/d3.v6.min.js" type="text/javascript"></script>
<script src="/js/google-shopping-taxonomy.js" type="text/javascript"></script>

<small id="d3noScript">
    Loading taxonomy viewer...
</small>

<svg id="d3view" style="width: 90%; height: auto; overflow: auto !important;"></svg>


Google Product Taxonomy is a product categorization tree for e-commerce.
Google classifies e-shop articles into this structure.
The goal is to departmentalize products from the merchant feed into 5583 sections.
This partitioning improves article discovery for customers.
The automatic categorization is performed [based on product input fields](https://support.google.com/merchants/answer/6324436?hl=en) provided by the merchant.
The merchants have an option to override categorization using _google_product_category_ attribute.
Only one category per product is allowed.

## Download Full Google Taxanomy
Open and download [full taxonomy directly from Google](http://google.com/basepages/producttype/taxonomy.en-US.txt)
- Animals & Pet Supplies > Pet Supplies > Bird Supplies > Bird Cage Accessories > Bird Cage Bird Baths
- Home & Garden > Kitchen & Dining > Tableware > Serveware Accessories > Punch Bowl Stands
- Sporting Goods > Outdoor Recreation > Outdoor Games > Platform & Paddle Tennis > Platform & Paddle Tennis Paddles

## Google Guidelines
Read more in [official guidelines](https://support.google.com/merchants/answer/6324436?hl=en#zippy=%2Cshopping-ads-campaigns%2Capparel-products).

<br>
{% include subscribe.html %}