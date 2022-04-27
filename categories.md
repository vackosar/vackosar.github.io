---
layout: default
permalink: /categories/
title: Categories
description: By category.
---

# Categories

<div id="archives">
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>

    <h3 class="category-head">{{ category_name }}</h3>
    <a name="{{ category_name | slugize }}"></a>

    {% for post in site.categories[category_name] %}
      <article class="row">
        <div style="width: 80%; min-width: 300px; margin-top: 15px;">
            <a href="{{ post.url }}" title="{{ post.title }}" style="text-decoration: none">
                <div class="lead">{{ post.title }}</div>
                <small>{{ post.description }}</small>
            </a>
        </div>
        <div class="">
            <a href="{{ post.url }}" title="{{ post.title }}" style="text-decoration: none">
                <div class="index-post-image lazyload" data-bg="{{ post.image | default: '/images/white-noise.jpeg' }}"></div>
            </a>
        </div>
      </article>

    {% endfor %}
  </div>
{% endfor %}
</div>

<a class="small" href="/">Sort by date</a>
