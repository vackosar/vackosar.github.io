---
layout: default
title: Vaclav Kosar's Software & Machine Learning Blog
---
<h1 class="h2">{{ page.title }}</h1>

<br>
{% include subscribe.html %}
<br>


<div class="container posts">
  {% for post in site.posts %}

      <div class="row">
        <div style="width: 80%; min-width: 300px; margin-top: 15px;">
        <a href="{{ post.url | relative_url }}" title="{{ post.title }}" style="text-decoration: none">
                  <div class="lead">{{ post.title }}</div>
                  <small>{{ post.description }}</small>
            </a>
          </div>
          <div class="">
              <a href="{{ post.url | relative_url }}" title="{{ post.title }}" style="text-decoration: none">
                  <div class="index-post-image lazyload" data-bg="{{ post.image | default: '/images/white-noise.jpeg' }}"></div>
              </a>
          </div>
      </div>
      <br>
     <!-- ({{ post.date | date_to_string }}) -->
  {% endfor %}
</div>

<a class="small" href="/categories">Sort by category</a>

