---
layout: default
title: Vaclav Kosar's Blog
---
<h1>{{ page.title }}</h1>
<ul class="posts">
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}" title="{{ post.title }}"><h2>{{ post.date | date_to_string }} - {{ post.title }}</h2></a>
      <div class="postpreview">
        {{ post.content }}
      </div>
      <br>
      <div class="subscribe-page">
        Subscribe:
        <a href="https://twitter.com/intent/follow?screen_name=vackosar" rel="nofollow" target="_blank" title="Follow on Twitter">Twitter</a>
        , <a href="https://www.facebook.com/vackosar" rel="nofollow" target="_blank" title="Follow on Facebook">Facebook</a>
        , <a href="https://vackosar.github.io/feed.xml" rel="nofollow" target="_blank" title="Follow on RSS">RSS</a>
        <!--, <a href="https://plus.google.com/share?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Google+">Google+</a>-->
        <!--, <a href="https://www.linkedin.com/shareArticle?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on LinkedIn">LinkedIn</a>-->
        <!--, <a href="http://www.reddit.com/submit?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Reddit">Reddit</a>-->
        <!--.-->
      </div>
      <div class="share-page">
        Share:
            <a href="https://twitter.com/intent/tweet?text={{ post.title }}&url={{ site.url }}{{ post.url }}&via={{ site.twitter_username }}&related={{ site.twitter_username }}" rel="nofollow" target="_blank" title="Share on Twitter">Twitter</a>
          , <a href="https://facebook.com/sharer.php?u={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Facebook">Facebook</a>
          , <a href="https://plus.google.com/share?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Google+">Google+</a>
          , <a href="https://www.linkedin.com/shareArticle?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on LinkedIn">LinkedIn</a>
          , <a href="http://www.reddit.com/submit?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Reddit">Reddit</a>
          .
      </div>
      <br>
    </li>
  {% endfor %}
</ul>