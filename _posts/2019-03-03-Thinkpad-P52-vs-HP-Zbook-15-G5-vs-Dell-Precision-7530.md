---
layout: post
title: "Thinkpad P52 vs ZBook 15 G5 vs Precision 7530"
date: 2019-03-03
categories: electronics
description: This is my experience working on the best mobile workstation of 2019 with specs matching Thinkpad P52 and ZBook 15 G5.
image: /images/2019-03-thinkpad-p52-vs-zbook-15-G5.png
video: sRnKbLtE21k
permalink: /:categories/:title
redirect_from:
  - /2019/03/03/Thinkpad-P52-vs-HP-Zbook-15-G5-vs-Dell-Precision-7530.html 
  - /review/Thinkpad-P52-vs-HP-Zbook-15-G5-vs-Dell-Precision-7530
---

I wanted at least __15inch display__ processor __i7-8750H__, reasonable graphics __P1000__, at least __max 64GB RAM__, __RJ45__, __trackpoint__, physical __resilience__. I first decided to buy ZBook 15 G5 over Thinkpad P52 and Precision 7530, but ended up using Thinkpad P52.

I also shortly considered a wild card _14inch Latitude 5491_ as it had attractive price, but it missed too many of the requirements (poor cooling, low max ram, poor physical resilience, low graphics).
With P52 graphics card I can [train neural networks like DistilBERT](/ml/transformers-self-attention-mechanism-simplified) on my local machine.

{% include load_video.html %}


### ZBook 15 G5

#### Specs
- max RAM only 64GB
- medium trackpoint
- very good [cooling](https://f1.media.brightcove.com/8/1160438711001/1160438711001_5763673639001_5763663561001-vs.jpg?pubId=4119874066001&videoId=5763349495001) but [after repaste](http://forum.notebookreview.com/threads/dell-precision-7530-hp-zbook-15-g5-or-lenovo-thinkpad-p52.820474/page-26#post-10817321)
- replaceable battery ([tooless access also to RAM, HDD](https://i.ytimg.com/vi/4jW1loaLgyI/maxresdefault.jpg))
- best physical resilience (aluminium)
- simpler disassembly than P52
- dedicated graphics card ([can train small neural networks like DistilBERT](/ml/transformers-self-attention-mechanism-simplified))
    
#### Experience
I bought ZBook 15 G5, but ended up replacing it with Thinkpad P52.

- Charging port is too thin and probably will be damaged soon
- Page Up, Page Down keys are not as conveniently placed as on Thinkpads
- Home, End, Insert keys were replaced by useless keys Desktop, Call, Hang Up contrary to Thinkpad
- Home, End moved to the top right
- Insert key completely removed!
- Up and Down keys are stupidly thin!
- While the notebook should have passed MIL tests it doesnt really seem resilient as Thinkpad
- Without repaste the performance on Cinebench R15 drops to [1030 the same as on Thinkpad P52](https://www.notebookcheck.net/Lenovo-ThinkPad-P52-i7-P1000-FHD-Workstation-Review.322974.0.html)
- Linux (Ubuntu) runs ok, except for trackpoint which doesn't work on Ubuntu 18.04
- Overall, I think I will be replacing the notebook with P52
    
    
### Thinkpad P52

#### spec:
- max RAM 128GB
- best trackpoint
- worst cooling ([single heatpipe](http://forum.notebookreview.com/attachments/cooling_comparison-png.160125/), [prolonged cinebench performance dropoff](https://www.notebookcheck.net/Lenovo-ThinkPad-P52-i7-P1000-FHD-Workstation-Review.322974.0.html))
- replaceable battery
- medium physical resilience
- [slightly more complicated disassembly](/2020/05/03/P52-disassembly.html).

#### Experience
Thinkpad P52 is my main machine now.

##### Update 2019-05-07
So far minor issues with P52
- Refuses to charge sometimes even with 170W charger. Seems to be getting worse.
    - Battery issues were resolved during on-site support from Lenovo. Most probable cause was faulty power source, but the mainboard was fully removed during inspection (for no reason), so I cannot confirm the issue wasn't incorrectly attached connector or needed hard reset.
- Display cover seems too easy to bend
- LTE modem supported but not yet installed in my version
- I will be ordering LTE modem and will attempt to install it either with on-site support or manually.

##### Update 2019-11-02
- Linux dmesg messages about "temperature above threshold" are gone after repaste. The service guy haven't returned some of the screws.
- I had to [disassemble](/2020/05/03/P52-disassembly.html) the whole notebook due to pouring almond butter all over it - faulty jar in my backpack.
- [I posted about thermals P52 vs P53 here](https://vaclavkosar.com/2019/11/02/Thinkpad-P53-vs-P52-Thermals.html).

##### Update 2020-04-26
- Message "temperature above threshold" returned into dmesg log, so it seem that the improvement after repaste is only temporary.
- I posted [a video comparison of P52 vs G5](https://youtu.be/sRnKbLtE21k).

#### Quiz

Retain your memory of basic characteristics of Thinkpad P52 by taking following auto-generated quiz.
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=71f196f0-b4b7-43aa-87e0-2b8f42a65293">Thinkpad P52 Quiz</a>


### Precision 7530 
I only evaluated precision, but haven't bought it.

#### Specs
- max RAM 128GB
- worst trackpoint
- [medium cooling](https://scene7-cdn.dell.com/is/image//DellComputer/workstation-precision-7530-html5-thumb-image-set?wid=1110&fmt=png-alpha)
- no replaceable battery
- less physical resilience
- extra M.2 drive slot


### My Previous Thinkpad Yoga X260 Fix
I fixed [Touchpad Lost Sync on Lenovo Yoga X260 using a bash script](/software/Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync).