---
layout: post
title: 'Linux Text To Speech Comparison: Flite Vs Pico2Wave Vs Festival'
categories: software
description: Comparison of open-source text to speech (TTS) software in terms of pleasantness, comprehensibility, and modularity.
date: 2016-12-26
permalink: /:categories/:title
redirect_from:
- /2016/12/26/Flite-Vs-Festival
my_related_post_paths:
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
- _posts/2017-07-15-Restore-Missing-Punctuation-with-Keras-Convolutional-Text-Punctuator.md
- _posts/2018-09-23-Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync.md
---





## Text 2 Speech on Android and Web (Update)

I love audiobooks, because they can utilize brain-time, which would otherwise be lost e.g. time when walking, running or hiking.
Problem of audiobooks however used to be their scarcity, which I always struggled with especially in case of technical books.
I used to generate the books to audio files.
Since then may real-time text-to-speech software is available, especially on my mobile device where it matters the most:

I mostly play text I need either via:
- [Voice Aloud Android app can read any text shared to it even emails](https://play.google.com/store/apps/details?id=com.hyperionics.avar&hl=en&gl=US)
- [Talkify Website read any other website or document aloud](https://talkify.net/web-reader-read-any-website-aloud)


## Linux Tools for Text-to-Speech

[Flite](http://www.festvox.org/flite/) in comparison to [Festival](http://www.festvox.org/festival/) has:

- pleasant voices
- samely comprehensible voices
- big problems when combination with ffmpeg streaming encoding over bash pipes (This is why I don't use it for [audiobook generation](#audio-book-generation).)
- designed for embedded devices ([see docs](http://www.festvox.org/flite/) )

[pico2wave](http://manpages.ubuntu.com/manpages/xenial/man1/pico2wave.1.html) in comparison to [Festival](http://www.festvox.org/festival/) has:

- similarly pleasant voice
- less comprehensible voice
- problems when one needs to be piping text into it and resolvable problems when one needs to be piping from it:
```ln -sf /dev/fd/1 /tmp/stdout.wav; while IFS= read -r line; do pico2wave -w /tmp/stdout.wav "$line"; done | ...```
- designed for embedded devices
 

### Audiobook Generation
I've put together [a simplistic tool for generating audiobooks from plain text](https://github.com/vackosar/text2gsm) that works!
I call it [text2gsm](https://github.com/vackosar/text2gsm) as it converts plain text file into GSM WAV compression format optimal for voice.

I used above scripts to compress [Hammings lectures for download - read more here](/software/Highly-Compressed-Richard-Hamming-Lectures).

