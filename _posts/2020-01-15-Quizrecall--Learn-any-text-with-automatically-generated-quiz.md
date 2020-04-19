---
layout: post
title: "Learn faster with a generated quiz"
date: 2019-11-02
---

I used [Anki](https://apps.ankiweb.net/) to learn various Math, Stats, and Software Dev definitions. But I kept having three problems with it. I resolved them by developing [a web app Quizrecall - an automated quiz generator with spaced repetition](https://quizrecall.com/personal). Read on as the app may be something for you as well.

### Anki Issues

1. *Time to create*: But I always had a problem with *having to spend a lot of time creating my flashcards*. Over time I moved from creating a front-back card to just fill-in-the-blank questions to reduce effort. But that still felt too slow. I knew it must be possible to generate the cloze questions automatically. And over time, I developed an algorithm to do that for me.

2. *Self-assessment breaks [testing effect](https://en.wikipedia.org/wiki/Testing_effect)*: Another issue I had with Anki was that I was *losing attention during the reviews*. I kept zoning out and self-assessing my self as "Good" without actually recalling anything. The issue here is that Anki allows you to keep pushing one green button.

3. *Time to review*: The last problem for me with Anki was that spending *too much time during card review*. I tried configuring a time limit to answer, but it only increased the focus problem in point 2 above.


### Quizrecall as a solution

I solved all of these problems for myself by developing the app, and I switched entirely recently. It is leveraging the latest Machine Learning (AI) technology. It works only with text, but right now, it is enough.
1. Generates fill-in-the-blank (cloze) _questions_ and _alternative answers_
3. Pushes me to select the correct answer from 3 options
3. The answer correctness also decreases with the elapsed time needed to answer

<iframe style="width: calc(200px + 30vw); max-width: 500px; height: calc((200px + 30vw)* 9/16); max-height: 273px"  src="https://www.youtube.com/embed/LaJqH0GE_cQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Conclusion

I am happy with finding a solution to my issues with Anki. I am committed to using and improving the app over time, because it is genuinely reducing my effort to memorize and learn.

I think you may very well like it as well. You can [try it with your favorite Wikipedia article summary](https://quizrecall.com/personal).
