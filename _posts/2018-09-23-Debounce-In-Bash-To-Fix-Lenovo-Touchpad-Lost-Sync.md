---
layout: post
title: "Debounce In Bash To Fix Lenovo Touchpad Lost Sync"
date: 2018-09-23
---

## Functional Debounce In Bash

Debounce is commonly used name for rate limiting function used in functional programming. For example it exists both in React and JavaScript. In Bash it can be implemented as follows:

    debounce() {
      intervalInSeconds="$1";
      unixtime() {
        date +%s;
      }
      nextTimeLimit() {
        echo $(($(unixtime) + $intervalInSeconds));
      }
      limit=$(nextTimeLimit);
      while read line; do
        if test $limit -lt $(unixtime); then
          limit=$(nextTimeLimit);
          echo "$line";
        fi
      done;
    }

Similarly useful function is foreach which I wrote [post about as well](https://vaclavkosar.com/2016/07/28/Functional-Foreach-In-Bash.html).


## Workaround For Lenovo Touchpad Lost Sync

I am having issues on my Lenovo Yoga X260 with freezing trackpoint and touchpad. I failed to find proper solution but at least I have following reasonable workaround which uses above debounce implementation.

The issue can be detected by Linux kernel logging following line:

    [ 5416.628532] psmouse serio1: Touchpad at isa0060/serio1/input0 lost sync at byte 6


And can be immediately fixed by restarting psmouse module:

    modprobe -r psmouse; modprobe psmouse

Using debounce function above I implemented a script to do just that automagically.  I placed below script to be executed on startup with root privilages:

    #!/bin/bash
    #set -ue
    # -o pipefail
    
    foreach () {
      while IFS= read -r l; do
        eval "$@";
      done;
    }
    
    debounce() {
      intervalInSeconds="$1";
      unixtime() {
        date +%s;
      }
      nextTimeLimit() {
        echo $(($(unixtime) + $intervalInSeconds));
      }
      limit=$(nextTimeLimit);
      while read line; do
        if test $limit -lt $(unixtime); then
          limit=$(nextTimeLimit);
          echo "$line";
        fi
      done;
    }
    
    dmesg -w|
      grep "lost sync"|
      debounce 3|
      foreach 'echo restarting mouse; modprobe -r psmouse; modprobe psmouse;' &


