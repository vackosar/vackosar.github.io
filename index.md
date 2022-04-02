---
layout: default
title: Software, Machine Learning, & Business Blog
---
<h2>{{ page.title }}</h2>

<br>
{% include subscribe.html %}
<br>


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
                <div class="index-post-image lazyload" data-bg="{{ post.image | default: '/images/white-noise.jpeg' }}"></div>
            </a>
        </div>
      </div>
     <!-- ({{ post.date | date_to_string }}) -->
  {% endfor %}
</div>

<a class="small" href="/categories">Sort by category</a>

<script src="/js/lazysizes.min.js" async></script>
<script defer>
    document.addEventListener('lazybeforeunveil', function(e){
        var bg = e.target.getAttribute('data-bg');
        if(bg){
            e.target.style.backgroundImage = 'url(' + bg + ')';
        }
    });
</script>
