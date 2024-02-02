---
layout: post
title: Learn faster with a generated quiz
date: 2019-11-02
categories: productivity
description: Reduce your effort of creating and revising learning material using a free AI-powered tool.
image: https://quizrecall.com/static/quiz-recall-logo.webp
video: LaJqH0GE_cQ
permalink: /:categories/:title
redirect_from:
- /2019/11/02/Quizrecall-Learn-any-text-with-automatically-generated-quiz.html
- /2020/04/19/Converting-knowledge-base-to-training.html
my_related_post_paths:
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2020-02-25-I-read-papers-on-a-podcast.md
- _posts/2020-05-08-starspace-embedding.md
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
- _posts/2023-06-08-Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
---



### Update 2021-03-07

__The service is deprecated and is not accepting new users at the moment.__

### Anki

I used [Anki](https://apps.ankiweb.net/) to learn various Math, Stats, and Software Dev definitions.
But it was time consuming and had broken [testing effect](https://en.wikipedia.org/wiki/Testing_effect).
I resolved these problems by developing [a web app Quizrecall - an automated quiz generator with spaced repetition](https://quizrecall.com/personal).
Read on as the app may be something for you as well.

### Anki Issues

1. *Time to create*: But I always had a problem with *having to spend a lot of time creating my flashcards*. Over time I moved from creating a front-back card to just fill-in-the-blank questions to reduce effort. But that still felt too slow. I knew it must be possible to generate the cloze questions automatically. And over time, I developed an algorithm to do that for me.

2. *Self-assessment breaks [testing effect](https://en.wikipedia.org/wiki/Testing_effect)*: Another issue I had with Anki was that I was *losing attention during the reviews*. I kept zoning out and self-assessing my self as "Good" without actually recalling anything. The issue here is that Anki allows you to keep pushing one green button.

3. *Time to review*: The last problem for me with Anki was that spending *too much time during card review*. I tried configuring a time limit to answer, but it only increased the focus problem in point 2 above.


### Quizrecall as a solution

I solved all of these problems for myself by developing the app, and I switched entirely recently. It is leveraging the latest Machine Learning (AI) technology. It works only with text, but right now, it is enough.
1. Generates fill-in-the-blank (cloze) _questions_ and _alternative answers_
3. Pushes me to select the correct answer from 3 options
3. The answer correctness also decreases with the elapsed time needed to answer

{% include load_video.html %}

### Conclusion

I am happy with finding a solution to my issues with Anki. I am committed to using and improving the app over time, because it is genuinely reducing my effort to memorize and learn.


## Enterprise Follow Up

It started by solving my pains with personal training app Anki by building an AI powered tool.
Now I finished baseline features for the applience's use in the enterprise.


### Without Training Automation

The problem of creating training is that it takes so much effort to rewrite the source text into a training system, that it ends up not being done at all. Companies usually end up reverting to "learning on-the-go" which means learning inefficiently or not at all.

Training also becomes outdated fast, so even if somebody does amount the effort, it ends up being misleading after year or two.

The companies end up with employees having only a patchy understanding of the core business and domain knowledge leading to a loss in revenue.


### The AI solution

Natural language processing progressed so much recently, such that AI-assisted training generation is now possible. Quizrecall can now help you extract essential sentences from your textual resource, hide suitable parts, and generate alternative answers.

After the training is generated, it is saved into the system, and the period of two weeks starts during which all submitted employees will be repeatedly tested. Retry count each training question is determined by their individual performance.

