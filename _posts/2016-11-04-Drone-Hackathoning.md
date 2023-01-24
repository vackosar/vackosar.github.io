---
layout: post
title: Drone Detecting White Marker for Stabilization
date: 2016-11-04
description: On a hackathon I implemented trivial image processing algorithm to locate white piece of paper on grey carpet floor to be used for drone horizontal stabilization.
image: https://raw.githubusercontent.com/vackosar/triv-white-spot-locator/master/output/androidTest/marked.jpg
categories: ml
permalink: /:categories/:title
redirect_from:
- /2016/11/04/Drone-Hackathoning.html
my_related_post_paths:
- _posts/2020-08-09-Word-Movers-Embedding--Cheap-WMD-For-Documents.md
- _posts/2021-12-28-cross-attention-in-transformer-architecture.md
- _posts/2021-05-21-PID-controller-control-loop-mechanism.md
- _posts/2022-06-04-transformer-positional-embeddings-and-encodings.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
---



Yesterday I attended a hackathon choosing to join up with colleagues to develop an android app for DJI Phantom 3. We aimed to stabilize the drone horizontally to be able to screw a light bulb into a socket mounted on the ceiling. Ultimately we didn't succeed, although the journey was very interesting.

## White Spot Locator

I mainly focused on locating white piece of paper on grey carpet floor in a picture. I succeeded in that, but lost lots of time setting up my system and using computer of others to implement my code.

I simply blurred the image using gaussian resizing to reduce noise and then implemented threshold for brightness to filter in sufficiently white pixels. After that I located the center of white spot averaging over coordinates of white pixels.

The algorithm suffered from being quite slow as processing took 20 seconds, until I had another look post-hackathon and improved that to 40 miliseconds. Interestingly the algorithm doesn't require any libraries.

### Source

[Revised source in my repo](https://github.com/vackosar/triv-white-spot-locator/blob/master/src/androidTest/java/com/vackosar/trivwhitespotlocator/LocateWhiteSpotTest.java), [Original hackathon source](https://github.com/pechovic/barcode-dji/blob/master/app/src/androidTest/java/barcode/barclays/com/drone/ExampleInstrumentedTest.java)

### Example

Source Image:

![Source Image](https://raw.githubusercontent.com/vackosar/triv-white-spot-locator/master/src/main/res/drawable/testimg2.jpg)

Blurred:

![Blurred](https://raw.githubusercontent.com/vackosar/triv-white-spot-locator/master/output/androidTest/blured.jpg)

Treshholded:

![Treshholded](https://raw.githubusercontent.com/vackosar/triv-white-spot-locator/master/output/androidTest/treshholded.jpg)

Marked:

![Marked](https://raw.githubusercontent.com/vackosar/triv-white-spot-locator/master/output/androidTest/marked.jpg)

## Lessons Learned
Lesson for me is that whenever speed is needed addressing potential risk is critical. Single small thing off will result in failure. Periodical reevaluation of risk and possible investment is needed.

### Preps
Having a little time evening before, I underestimated importance of environmental preparation. Crippled by strange internet connection provided, I was ultimately not able to  set my Android Studio straight and had to use computer stations of others.

### Morale
Abundance of food is not a good thing as it breaks focus and leads to overeating. As night progresses, sleep deficit will also take its toll on morale and attention.

### Micro Iterations
Perhaps strictly periodical stand-ups, risk and investment reviews would improve the implementation.

### Sticking To Plan
Sticking to single plan until proven completely impossible is better than experimenting around when severely time constrained.