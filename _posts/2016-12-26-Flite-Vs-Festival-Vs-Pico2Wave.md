---
layout: post
title: "Linux Text To Speech Comparison: Flite Vs Pico2Wave Vs Festival"
date: 2016-12-26
categories: software
description: Comparison of open-source text to speech software in terms of pleasantness, comprehensibility, and modularity.
permalink: /:categories/:title
redirect_from:
- /2016/12/26/Flite-Vs-Festival
---

[Flite](http://www.festvox.org/flite/) in comparison to [Festival](http://www.festvox.org/festival/) has:

- pleasant voices
- samely comprehensible voices
- big problems when combination with ffmpeg streaming encoding over bash pipes (This is why I don't use it for [audiobook generation](https://vackosar.github.io/2016/07/11/Audiobook-Generation.html).)
- designed for embedded devices ([see docs](http://www.festvox.org/flite/) )


[pico2wave](http://manpages.ubuntu.com/manpages/xenial/man1/pico2wave.1.html) in comparison to [Festival](http://www.festvox.org/festival/) has:

- similarly pleasant voice
- less comprehensible voice
- problems when one needs to be piping text into it and resolvable problems when one needs to be piping from it:
```ln -sf /dev/fd/1 /tmp/stdout.wav; while IFS= read -r line; do pico2wave -w /tmp/stdout.wav "$line"; done | ...```
- designed for embedded devices