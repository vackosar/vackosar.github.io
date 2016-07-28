---
layout: post
title: "Functional ForEach In Bash"
date: 2016-07-28
---

Don't you hate verbosity of Bash's while-do statements when writing in-line scripts? No worries, you can improve on that!

Instead of writing long-winded

    while IFS= read l; do <<<command>>>; done

you can save space and time using a function. But how to allow flexible use of the line that was read? Functional programmers will recognize familiar ```foreach``` command in below:

    foreach () { while IFS= read -r l; do eval "$@"; done; }

Notice usage of the evil "eval" function. The eval function is important here to allow flexible usage of the variable "l". To stay secure always use parenthesis around the variable reference e.g.:

    cat files.txt | foreach 'mv "$l" "${l/.txt/.md}"';

Above should keep all evils at bay.

Try it out and let me know below!