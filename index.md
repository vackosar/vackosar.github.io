---
layout: default
title: Blog
---
<h1>{{ page.title }}</h1>

<div class="subscribe-page">
    Subscribe:
    <a href="httfsaps://twitter.com/intent/follow?screen_name=vackosar" rel="nofollow" target="_blank" title="Follow on Twitter">Twitter</a>
    , <a href="https://www.facebook.com/vackosar" rel="nofollow" target="_blank" title="Follow on Facebook">Facebook</a>
    , <a href="https://vackosar.github.io/feed.xml" rel="nofollow" target="_blank" title="Follow on RSS">RSS</a>
    <!--, <a href="https://plus.google.com/share?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Google+">Google+</a>-->
    <!--, <a href="https://www.linkedin.com/shareArticle?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on LinkedIn">LinkedIn</a>-->
    <!--, <a href="http://www.reddit.com/submit?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Reddit">Reddit</a>-->
    <!--.-->
</div>

<div class="posts">
  {% for post in site.posts %}
    <a href="{{ post.url }}" title="{{ post.title }}"><h3>{{ post.date | date_to_string }} - {{ post.title }}</h3></a>
  {% endfor %}
</div>
