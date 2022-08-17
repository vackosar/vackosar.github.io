---
layout: post
title: "Strong Static Typing"
date: 2022-08-17
last_modified_at: 2022-08-17
categories: software
description: Master programmers Carmack, Fowler, and Blow on strong static typing.
permalink: /:categories/:title
---

- John Carmack: "[strong static typing has really significant benefits](https://youtu.be/1PhArSujR_A?t=808)"
- Jonathan Blow's [Jai is static/strongly typed C-style language](https://github.com/BSVino/JaiPrimer/blob/master/JaiPrimer.md)
- Martin Flower:  "[the lack of type information on parameters made life difficult](https://martinfowler.com/bliki/DynamicTyping.html)"


## Clarity Of Typed Code

<blockquote style="font-style: italic" class="blockquote">
I found the lack of type information on parameters made life difficult - I kept saying to myself 'what exactly do I have here?' I didn't find this so much of an issue in Smalltalk for two reasons: the excellent environment makes it easy to fire up a debugger and see what you have, and secondly the common convention is to name the arguments after the type.

<footer class="blockquote-footer"><a href="https://martinfowler.com/bliki/DynamicTyping.html">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Anything that isn’t crystal clear to a static analysis tool probably isn’t clear to your fellow programmers, either. The classic hacker disdain for “bondage and discipline languages” is short-sighted – the needs of large, long-lived, multi-programmer projects are just different than the quick work you do for yourself.
<footer class="blockquote-footer"><a href="https://web.archive.org/web/20140713032309/http://www.altdev.co/2011/12/24/static-code-analysis/">John Carmack's Static Code Analysis post</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Everything that is syntactically legal that the compiler will accept will eventually wind up in your codebase. And that's why I think that static typing is so valuable because it cuts down on what can kind of make it past those.
<footer class="blockquote-footer"><a href="https://youtu.be/1PhArSujR_A?t=808">John Carmack's keynote at Quakecon 2013</a></footer>
</blockquote>


## Type Linting vs Tests

<blockquote style="font-style: italic" class="blockquote">
the success that we have had with code analysis has been clear enough that I will say plainly it is irresponsible to not use it.
<footer class="blockquote-footer"><a href="https://web.archive.org/web/20140713032309/http://www.altdev.co/2011/12/24/static-code-analysis/">John Carmack's Static Code Analysis post</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
But I discovered that in the presence of SelfTestingCode, most bugs that static types would have were found just as easily by the tests. Since the tests found much more than type errors, you needed them in either a static or dynamically typed language, so having the static typing gave you little gain.
<footer class="blockquote-footer"><a href="`https://martinfowler.com/bliki/DynamicTyping.html`">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>


## IDE Completion with Static Typing

<blockquote style="font-style: italic" class="blockquote">
Another area where static typing is useful is that it allows programming environments to be much more helpful. The revelation here (as in so many things) was IntelliJ. With an IDE like this I really felt the type system was helping me. Even simple things like auto-completion are greatly helped by static types, and leading IDEs can do much more than that.
<footer class="blockquote-footer"><a href="`https://martinfowler.com/bliki/DynamicTyping.html`">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>


## Is Strong Static Typing Fun?

<blockquote style="font-style: italic" class="blockquote">
I see the lure the enticement of having just throw random types onto anything about not having to you know have sort of template typing arrangements and things you're there's a there's an appeal to that, but I think that it bites you in the end. If the code lives a long time, and it grows enough. I think that the value of types is just super, super important and that's something that's good. 
<footer class="blockquote-footer"><a href="https://youtu.be/1PhArSujR_A?t=808">John Carmack's keynote at Quakecon 2013</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Whatever the reason, this better flow leads to more fun programming - even with an inferior environment. This may not seem to matter much, who cares if programmers have fun?
<footer class="blockquote-footer"><a href="`https://martinfowler.com/bliki/DynamicTyping.html`">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>
