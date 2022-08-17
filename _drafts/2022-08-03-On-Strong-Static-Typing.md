---
layout: post
title: "Strong Static Typing Field Experts"
date: 2022-08-03
last_modified_at: 2022-08-03
categories: software
description: Carmack, Fowler, and Blow on strong static typing
permalink: /:categories/:title
---

- John Carmack: "[strong static typing has really significant benefits](https://youtu.be/1PhArSujR_A?t=808)"
- Jonathan Blow's [Jai is static/strongly typed C-style language](https://github.com/BSVino/JaiPrimer/blob/master/JaiPrimer.md)
- Martin Flower:  "[the lack of type information on parameters made life difficult](https://martinfowler.com/bliki/DynamicTyping.html)"


## Clarity Of Object Type 

<blockquote style="font-style: italic" class="blockquote">
I found the lack of type information on parameters made life difficult - I kept saying to myself 'what exactly do I have here?' I didn't find this so much of an issue in Smalltalk for two reasons: the excellent environment makes it easy to fire up a debugger and see what you have, and secondly the common convention is to name the arguments after the type.
</blockquote>


## IDE Completion

<blockquote style="font-style: italic" class="blockquote">
Another area where static typing is useful is that it allows programming environments to be much more helpful. The revelation here (as in so many things) was IntelliJ. With an IDE like this I really felt the type system was helping me. Even simple things like auto-completion are greatly helped by static types, and leading IDEs can do much more than that.
</blockquote>


<blockquote style="font-style: italic" class="blockquote">
Everything that is syntactically legal that the compiler will accept will eventually wind up in your codebase. And that's why I think that static typing is so valuable because it cuts down on what can kind of make it past those.
<footer class="blockquote-footer"><a href="https://youtu.be/1PhArSujR_A?t=808">John Carmack</a></footer>
</blockquote>

https://web.archive.org/web/20140713032309/http://www.altdev.co/2011/12/24/static-code-analysis/


## Is Strong Static Typing Slow?

Martin Flower 
https://martinfowler.com/bliki/DynamicTyping.html
