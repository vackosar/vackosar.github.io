---
layout: post
title: "Linux Text To Speech Comparison: Flite Vs Pico2Wave Vs Festival"
categories: software
description: Comparison of open-source text to speech (TTS) software in terms of pleasantness, comprehensibility, and modularity.
date: 2016-12-26
permalink: /:categories/:title
redirect_from:
- /2016/12/26/Flite-Vs-Festival
---

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
 

## Audio Book Generation

I love audiobooks, because they can utilize brain-time, which would otherwise be lost e.g. time when walking, running or hiking. Problem of audiobooks however is their scarcity, which I always struggled with especially in case of technical books.

Guess what? I've finally put together [a simplistic tool for generating audiobooks from plain text](https://github.com/vackosar/text2gsm) that works! I call it [text2gsm](https://github.com/vackosar/text2gsm) as it converts plain text file into GSM WAV compression format optimal for voice.

So next time I want to read book, but have no time to do it, I'll generate myself a audiobook and listen to it during otherwise lost time. Neat!


## Text 2 Speach on Android (Update)

While I used to use above software now, I mostly play text I need either via:
- [Voice Aloud Android app can read any text shared to it even emails](https://play.google.com/store/apps/details?id=com.hyperionics.avar&hl=en&gl=US)
- [Talkify Website read any other website or document aloud](https://talkify.net/web-reader-read-any-website-aloud)
