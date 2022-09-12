---
layout: post
title: Functional ForEach In Bash
date: 2016-07-28
description: Don't you hate verbosity of Bash's while-do statements when writing in-line scripts? No worries, you can improve on that!
categories: software
permalink: /:categories/:title
redirect_from:
- /2016/07/28/Functional-Foreach-In-Bash.html
my_related_post_paths:
- _posts/2018-09-23-Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
- _posts/2022-08-03-Python-functools.cmp_to_key-explained.md
- _posts/2018-10-04-Spline-Data-Lineage-Spark-Structured-Streaming-Spark-AI-Summit-2018.md
---



Instead of writing long-winded

    while IFS= read l; do <<<command>>>; done

you can save space and time using a function. But how to allow flexible use of the line that was read? Functional programmers will recognize familiar ```foreach``` command in below:

    foreach () { while IFS= read -r l; do eval "$@"; done; }

Notice usage of the evil "eval" function. The eval function is important here to allow flexible usage of the variable "l". To stay secure always use parenthesis around the variable reference e.g.:

    cat files.txt | foreach 'mv "$l" "${l/.txt/.md}"';

Above should keep all evils at bay.

Try it out and let me know below!

I used above foreach method together with [functional debounce method in Bash to fix my Lenovo Yoga X260](/software/Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync).
