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
                <div>
                    <div class="clear">
                        <button type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="btn btn-secondary">Subscribe</button>
                    </div>
                </div>
                
                <span>
                    <a href="https://twitter.com/intent/follow?screen_name=vackosar" rel="nofollow" target="_blank" title="Follow on Twitter" class="m-1"><i class="fab fa-twitter"></i></a>
                    <a href="https://www.facebook.com/vackosar" rel="nofollow" target="_blank" title="Follow on Facebook" class="m-1"><i class="fab fa-facebook"></i></a>
                    <a href="https://vackosar.github.io/feed.xml" rel="nofollow" target="_blank" title="Follow on RSS" class="m-1"><i class="fas fa-rss"></i></a>
                </span>
            </div>
        </form>
    </div>
    <!--End mc_embed_signup-->
    
</div>

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