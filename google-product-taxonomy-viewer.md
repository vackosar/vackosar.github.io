---
layout: default
title: "Google Product Taxonomy Viewer"
date: 2021-04-16
description: Interactive viewer for Google Product categorization tree. 
image: /images/automatic-taxonomy.png
---

Google Product Taxonomy is a product categorization tree into which merchants products are automatically categorized.
The automatic categorization is performed [automaticaly based on product input fields](https://support.google.com/merchants/answer/6324436?hl=en) provided by the merchant.

You can explore product category below.
Click on the __green nodes__ below to Google Product Taxonomy interactively. The second click collapses the children.

<script src="/js/d3.v6.min.js" type="text/javascript"></script>
<script src="/js/google-shopping-taxonomy.js" type="text/javascript"></script>

<small id="d3noScript">
    Loading taxonomy viewer...
</small>
<svg id="d3view" style="width: 90%; height: auto; overflow: scroll;"></svg>


[Full taxonomy](http://google.com/basepages/producttype/taxonomy.en-US.txt)

Examples:
- Animals & Pet Supplies > Pet Supplies > Bird Supplies > Bird Cage Accessories > Bird Cage Bird Baths
- Home & Garden > Kitchen & Dining > Tableware > Serveware Accessories > Punch Bowl Stands
- Sporting Goods > Outdoor Recreation > Outdoor Games > Platform & Paddle Tennis > Platform & Paddle Tennis Paddles
