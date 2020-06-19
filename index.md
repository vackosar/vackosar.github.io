---
layout: default
title: Blog
---
<h2>{{ page.title }}</h2>

<div class="subscribe-page">
    
    <!-- Begin Mailchimp Signup Form -->
    <div id="mc_embed_signup" class="m-2">
        <form action="https://vaclavkosar.us3.list-manage.com/subscribe/post?u=289873d7958b1bdc1c6dc93b7&amp;id=4b8172df11" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
            <div id="mc_embed_signup_scroll" class="d-flex flex-column flex-md-row ">
                <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" style="width: 200px" required>
                <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
                <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_289873d7958b1bdc1c6dc93b7_4b8172df11" tabindex="-1" value=""></div>
                <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="btn btn-secondary"></div>
                
                <span>
                    <a href="https://twitter.com/intent/follow?screen_name=vackosar" rel="nofollow" target="_blank" title="Follow on Twitter" class="m-1"><i class="fab fa-twitter"></i></a>
                    <a href="https://www.facebook.com/vackosar" rel="nofollow" target="_blank" title="Follow on Facebook" class="m-1"><i class="fab fa-facebook"></i></a>
                    <a href="https://vackosar.github.io/feed.xml" rel="nofollow" target="_blank" title="Follow on RSS" class="m-1"><i class="fas fa-rss"></i></a>
                </span>
            </div>
        </form>
    </div>
    <!--End mc_embed_signup-->
    
    <!--, <a href="https://plus.google.com/share?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Google+">Google+</a>-->
    <!--, <a href="https://www.linkedin.com/shareArticle?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on LinkedIn">LinkedIn</a>-->
    <!--, <a href="http://www.reddit.com/submit?url={{ site.url }}{{ post.url }}" rel="nofollow" target="_blank" title="Share on Reddit">Reddit</a>-->
    <!--.-->
</div>

<div class="posts">
  {% for post in site.posts %}
    <a href="{{ post.url }}" title="{{ post.title }}"><h4>{{ post.title }}</h4></a>
     <!-- ({{ post.date | date_to_string }}) -->
  {% endfor %}
</div>
