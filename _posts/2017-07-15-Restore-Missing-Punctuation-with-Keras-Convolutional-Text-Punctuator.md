---
layout: post
title: Restore Missing Punctuation with Keras Convolutional Text Punctuator
date: 2017-07-15
description: Simple neural network android app for restoring punctuation in text e.g. YouTube subtitles.
categories: software
permalink: /:categories/:title
redirect_from:
- /2017/07/15/Keras-Convolutional-Text-Punctuator-Presentation.html
- /2017/05/28/Youtube-Reader-Neural-Network-Android-App.html
video: w-w3QamQIKY
image: http://i3.ytimg.com/vi/w-w3QamQIKY/hqdefault.jpg
my_related_post_paths:
- _posts/2016-12-26-Flite-Vs-Festival-Vs-Pico2Wave.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2021-03-22-google-product-taxonomy-viewer.md
---



{% include load_video.html %}

The project uses GloVe embeddings and has simple convolutional architecture implemented in Keras framework on Tensorflow.
It achieved reasonable performance, such that I could use it in an Android application for downloading and punctuating YouTube subtitles described below.
The [source code for Keras Punctuator is on GitHub](https://github.com/vackosar/keras-punctuator). 


## YouTube Reader
![Youtube reader](https://raw.githubusercontent.com/vackosar/youtube-reader/master/store/featured.png)

Using the punctuator above I build this machine learning Android app "YouTube Reader" to save data by only downloading captions and adding punctuation.
The android app uses neural network to punctuate YouTube video captions such that they can be used with a text to speech software.
It saves your mobile data, when you are interested only in what is being said in a YouTube video.
The app uses Tensorflow native libraries for Android packaged as a binary blob into the app.
The app is available as [an APK here](https://github.com/vackosar/youtube-reader).
I couldn't publish it to Google Play as it was not up to guidelines.
Then I wanted to publish it to F-Droid, but the build process was complicated to reproduce for others than to the Tensorflow binary libraries, so focused on other ventures.
[Source code for YouTube Reader is here](https://github.com/vackosar/youtube-reader).

![Youtube reader Screen shot](/images/youtube-reader-screenshot.png)
