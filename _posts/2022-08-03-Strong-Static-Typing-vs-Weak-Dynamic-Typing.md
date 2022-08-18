---
layout: post
title: "Strong Static Typing vs Weak Dynamic Typing"
date: 2022-08-17
last_modified_at: 2022-08-17
categories: software
description: Master programmers Carmack, Fowler, and Blow on strong static typing in contrast to dynamic typing.
image: /images/strong-static-vs-weak-dynamic-typing-table.png
permalink: /:categories/:title
---

- John Carmack: "[strong static typing has really significant benefits](https://youtu.be/1PhArSujR_A?t=808)"
- Jonathan Blow: ["The type safety part of Python or the lack thereof is huge."](https://youtu.be/2J-HIh3kXCQ?t=287)
- Jonathan Blow's [Jai is static/strongly typed C-style language](https://github.com/BSVino/JaiPrimer/blob/master/JaiPrimer.md)
- Martin Fowler:  "[the lack of type information on parameters made life difficult](https://martinfowler.com/bliki/DynamicTyping.html)"


## Summary
Highly productive game developers Blow and Carmack, as opposed to more enterprise developers like Fowler and Bob, favor strong static typing for bug prevention and increasing quality.
All recognize the cost of typing, which can be reduced with type inference.
While unit testing can replace static typing, Blow mentions that it brings the additional cost of extra code, which make refactoring harder, while with static typing and larger granularity test this is less of a problem.


## Strong, Weak, Static, Dynamic Definitions
Strongly typed languages apply strict type checking at compile time, while weak typing does not.
Static typed language apply type checking at compile time, while dynamic typing languages apply them at runtime and use automatic type conversion.

<table class="table table-striped">
    <thead>
        <tr>
            <th scope="col">
            </th>
            <th scope="col">
                Dynamic
            </th>
            <th scope="col">
                Static
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>Strong</td>
          <td>Python, Ruby, Closure, Erlang</td>
          <td>Java, C#, C++, Haskell, Scala</td>
        </tr>
        <tr>
          <td>Weak</td>
          <td>JavaScript, PHP, Visual Basic, Perl</td>
          <td>C</td>
        </tr>
</tbody>
</table>
          


## Clarity Of Typed Code
Most agree that strong static typing increases code readability and clarity.

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

<blockquote style="font-style: italic" class="blockquote">
If you don't have like serious static type checking like you have in a language like C++ then once you start doing a non-trivial amount of stuff it becomes very easy to make mistakes. And it becomes very hard to find the mistakes easy to make mistakes.
<footer class="blockquote-footer"><a href="https://youtu.be/y2Wmz15aXk0?t=139">Jonathan Blow on scripting languages</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Another area where static typing is useful is that it allows programming environments to be much more helpful. The revelation here (as in so many things) was IntelliJ. With an IDE like this I really felt the type system was helping me. Even simple things like auto-completion are greatly helped by static types, and leading IDEs can do much more than that.
<footer class="blockquote-footer"><a href="`https://martinfowler.com/bliki/DynamicTyping.html`">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>



## Type Checks: Compilation, Type Linting, versus Tests
There is a disagreement, about the cost of unit tests compared to flexibility with fewer tests with static typing.


<blockquote style="font-style: italic" class="blockquote">
the success that we have had with code analysis has been clear enough that I will say plainly it is irresponsible to not use it.
<footer class="blockquote-footer"><a href="https://web.archive.org/web/20140713032309/http://www.altdev.co/2011/12/24/static-code-analysis/">John Carmack's Static Code Analysis post</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Statically typed strongly statically typed programming languages let you do this thing, that things like Lua for example don't let you do, or you just break your program.
Very useful technique that you can't do in Python or Javascript or any of this other stuff.
...
The type safety part of Python or the lack thereof is huge.
A lot of the stuff that we did today these grunt work refactors that I'm doing would be a lot scarier in Python.
Because you'd be like: I don't know if I just broke something. We've done 10 things today at least where you'd be like yeah I don't know if that broke something. We're in c plus you're like yeah i know i didn't break something.
<footer class="blockquote-footer"><a href="https://www.youtube.com/watch?v=2J-HIh3kXCQ">Jonathan Blow on strong static typing in refactoring</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
But I discovered that in the presence of SelfTestingCode, most bugs that static types would have were found just as easily by the tests. Since the tests found much more than type errors, you needed them in either a static or dynamically typed language, so having the static typing gave you little gain.
<footer class="blockquote-footer"><a href="https://martinfowler.com/bliki/DynamicTyping.html">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Whether you use static, or dynamic typing, you must still demonstrate correctness by executing tests.  Static typing does not reduce that number of tests, because those tests are behavioral and empirical.
<footer class="blockquote-footer"><a href="https://blog.cleancoder.com/uncle-bob/2019/06/08/TestsAndTypes.html">Martin's Types and Tests</a></footer>
</blockquote>


<blockquote style="font-style: italic" class="blockquote">
this whole thing about TDD about writing the test before you write the code is nonsense because you don't exactly know what you're building yet if you're doing anything interesting
...
The more code you have, the less agile you are, and unit tests add a great deal of code. So changing things it's like tar. It's keeping you stuck and keeping you from changing things.
...
if you can test the thing not as a unit for example as an entire game that might be a much more efficient way of testing in terms of the number of hours you put into programming
...
testing is very important right if you don't test your software then your software doesn't work what I'm saying is I don't think that this obsessive unit testing
<footer class="blockquote-footer"><a href="https://www.youtube.com/watch?v=21JlBOxgGwY">Jonathan Blow on unit testing and TDD</a></footer>
</blockquote>



## Is Strong Static Typing Fun?
Most note that static typing is less fun.


<blockquote style="font-style: italic" class="blockquote">
I see the lure the enticement of having just throw random types onto anything about not having to you know have sort of template typing arrangements and things you're there's a there's an appeal to that, but I think that it bites you in the end. If the code lives a long time, and it grows enough. I think that the value of types is just super, super important and that's something that's good. 
<footer class="blockquote-footer"><a href="https://youtu.be/1PhArSujR_A?t=808">John Carmack's keynote at Quakecon 2013</a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
Whatever the reason, this better flow leads to more fun programming - even with an inferior environment. This may not seem to matter much, who cares if programmers have fun?
<footer class="blockquote-footer"><a href="https://martinfowler.com/bliki/DynamicTyping.html">Martin Fowler's Dynamic Typing </a></footer>
</blockquote>

<blockquote style="font-style: italic" class="blockquote">
At the beginning it seems really easy because you just type some stuff, and it works.
<footer class="blockquote-footer"><a href="https://youtu.be/y2Wmz15aXk0?t=139">Jonathan Blow on scripting languages</a></footer>
</blockquote>
