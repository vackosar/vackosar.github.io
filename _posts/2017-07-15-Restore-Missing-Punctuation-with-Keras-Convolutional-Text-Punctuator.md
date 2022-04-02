---
layout: post
title: "Restore Missing Punctuation with Keras Convolutional Text Punctuator"
date: 2017-07-15
description: Simple deep neural network machine learning project for restoring punctuation in a text.
categories: software
permalink: /:categories/:title
redirect_from:
- /2017/07/15/Keras-Convolutional-Text-Punctuator-Presentation.html
- /2017/05/28/Youtube-Reader-Neural-Network-Android-App.html
video: w-w3QamQIKY
image: http://i3.ytimg.com/vi/w-w3QamQIKY/hqdefault.jpg
---

{% include load_video.html %}

The project uses GloVe embeddings and has simple convolutional architecture implemented in Keras framework.
It achieved reasonable performance, such that I could use it in [an Android application for downloading and punctuating Youtube subtitles](http://vaclavkosar.com/2017/05/28/Youtube-Reader-Neural-Network-Android-App.html).

### Code
The source code in on Github: https://github.com/vackosar/keras-punctuator


# YouTube Reader: Save Data Using Only Punctuated Captions
![Youtube reader](https://raw.githubusercontent.com/vackosar/youtube-reader/master/store/featured.png)

Using the punctuator above I build this little Android app.
Android app that uses neural network to punctuate YouTube video captions to be used with any text to speech software.

I am publishing my Android app called Youtube Reader. It saves your mobile data, when you are interested only in what is being said in a YouTube video.
[Source code](https://github.com/vackosar/youtube-reader)

