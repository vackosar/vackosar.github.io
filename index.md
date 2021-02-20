---
layout: default
title: Blog
---
<h2>{{ page.title }}</h2>

{% include subscribe.html %}

<div class="container posts">
  {% for post in site.posts %}
      <div class="row">
        <div style="width: 80%; min-width: 300px; margin-top: 15px;">
            <a href="{{ post.url }}" title="{{ post.title }}" style="text-decoration: none">
                <div class="lead">{{ post.title }}</div>
                <small>{{ post.description }}</small>
            </a>
        </div>
        <div class="">
            <a href="{{ post.url }}" title="{{ post.title }}" style="text-decoration: none">
                <div style="background-image: url('{{ post.image | default: '/images/white-noise.jpeg' }}');" class="index-post-image"></div>
            </a>
        </div>
      </div>
     <!-- ({{ post.date | date_to_string }}) -->
  {% endfor %}
</div>

<br>
<small>
    <a href="/privacy-policy">Privacy Policy</a>
</small>